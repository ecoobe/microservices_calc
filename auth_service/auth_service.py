from flask import Flask, request, jsonify
from prometheus_client import make_wsgi_app, Counter, generate_latest
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)
users = {"admin": "password"}

# Создаем метрики
LOGIN_REQUESTS = Counter('login_requests_total', 'Total login attempts')
LOGIN_FAILURES = Counter('login_failures_total', 'Total failed logins')

# Добавляем эндпоинт для метрик
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/login", methods=["POST"])
def login():
    LOGIN_REQUESTS.inc()  # Увеличиваем счетчик запросов
    data = request.json
    if users.get(data["username"]) == data["password"]:
        return jsonify({"status": "success"})
    LOGIN_FAILURES.inc()  # Увеличиваем счетчик ошибок
    return jsonify({"status": "fail"}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)