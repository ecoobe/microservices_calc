from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
AUTH_URL = "http://auth_service:5002/auth"  # Имя сервиса из docker-compose.yml
HISTORY_URL = "http://history_service:5003/history"

@app.route("/calc/<operation>", methods=["POST"])
def calculate(operation):
    data = request.json
    
    # Проверяем аутентификацию через auth-service
    auth_response = requests.post(AUTH_URL, json={"username": data["username"], "password": data["password"]})
    if auth_response.json().get("status") != "success":
        return jsonify({"error": "Unauthorized"}), 401
    
    a = data["a"]
    b = data["b"]
    
    # Вычисляем результат
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return jsonify({"error": "Division by zero"}), 400
        result = a / b
    else:
        return jsonify({"error": "Invalid operation"}), 400
    
    # Сохраняем историю через history-service
    requests.post(HISTORY_URL, json={"operation": operation, "result": result})
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)   # Запускаем на порту 5001