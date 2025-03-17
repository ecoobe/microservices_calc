from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Конфигурация БД
DB_HOST = os.getenv("POSTGRES_HOST", "postgres")
DB_USER = os.getenv("POSTGRES_USER", "admin")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "secret")
DB_NAME = os.getenv("POSTGRES_DB", "calculator")

def get_db():
    return psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME
    )

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/history", methods=["GET", "POST"])
def handle_history():
    if request.method == "POST":
        data = request.json
        try:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO operations (operation, result) VALUES (%s, %s)",
                (data["operation"], data["result"])
            )
            conn.commit()
            return jsonify({"status": "success"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            conn.close()
    else:
        try:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute("SELECT operation, result FROM operations")
            history = [{"operation": op, "result": res} for (op, res) in cursor.fetchall()]
            return jsonify({"history": history})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    # Создаём таблицу при первом запуске
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS operations (
            id SERIAL PRIMARY KEY,
            operation VARCHAR(50) NOT NULL,
            result FLOAT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    
    app.run(host='0.0.0.0', port=5003, debug=True)