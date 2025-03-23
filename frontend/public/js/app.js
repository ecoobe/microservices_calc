document.getElementById('calcForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const a = parseFloat(document.getElementById('a').value);
    const b = parseFloat(document.getElementById('b').value);
    const operation = document.getElementById('operation').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch(`/calc/${operation}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password, a, b })
        });

        const data = await response.json();
        const resultDiv = document.getElementById('result');
        
        if (response.ok) {
            resultDiv.style.color = '#4CAF50';
            resultDiv.textContent = `Результат: ${data.result}`;
        } else {
            resultDiv.style.color = '#ff4444';
            resultDiv.textContent = `Ошибка: ${data.error}`;
        }
    } catch (error) {
        document.getElementById('result').textContent = 'Ошибка подключения';
    }
});