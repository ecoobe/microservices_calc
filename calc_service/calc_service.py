from flask import Flask, request, jsonify
import requests
from prometheus_client import make_wsgi_app, Counter, generate_latest
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)
AUTH_URL = "http://auth_service:5002/login"
HISTORY_URL = "http://history_service:5003/history"

# Создаем метрики
CALC_REQUESTS = Counter('calc_requests_total', 'Total calculation requests')
CALC_ERRORS = Counter('calc_errors_total', 'Total calculation errors', ['type'])

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/calc/<operation>", methods=["POST"])
def calculate(operation):
    CALC_REQUESTS.inc()
    data = request.json
    
    try:
        auth_response = requests.post(AUTH_URL, json={"username": data["username"], "password": data["password"]})
        if auth_response.json().get("status") != "success":
            CALC_ERRORS.labels(type='auth').inc()
            return jsonify({"error": "Unauthorized"}), 401
        
        a = data["a"]
        b = data["b"]
        
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            if b == 0:
                CALC_ERRORS.labels(type='division_by_zero').inc()
                return jsonify({"error": "Division by zero"}), 400
            result = a / b
        else:
            CALC_ERRORS.labels(type='invalid_operation').inc()
            return jsonify({"error": "Invalid operation"}), 400
        
        requests.post(HISTORY_URL, json={"operation": operation, "result": result})
        return jsonify({"result": result})
    
    except Exception as e:
        CALC_ERRORS.labels(type='unexpected').inc()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)