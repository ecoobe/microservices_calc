import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [num1, setNum1] = useState('');
  const [num2, setNum2] = useState('');
  const [operation, setOperation] = useState('add');
  const [result, setResult] = useState('');
  const [history, setHistory] = useState([]);

  const calculate = async () => {
    try {
      const response = await fetch(`/api/calc/${operation}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          username: 'admin',
          password: 'password',
          a: parseFloat(num1),
          b: parseFloat(num2)
        })
      });
      
      const data = await response.json();
      if (response.ok) {
        setResult(data.result);
        loadHistory();
      }
    } catch (error) {
      console.error('Calculation error:', error);
    }
  };

  const loadHistory = async () => {
    try {
      const response = await fetch('/api/history/history');
      const data = await response.json();
      setHistory(data.history.reverse());
    } catch (error) {
      console.error('History load error:', error);
    }
  };

  useEffect(() => {
    loadHistory();
  }, []);

  return (
    <div className="App">
      <h1>Калькулятор</h1>
      
      <div>
        <input 
          type="number" 
          value={num1} 
          onChange={(e) => setNum1(e.target.value)} 
          placeholder="Первое число"
        />
        
        <select 
          value={operation} 
          onChange={(e) => setOperation(e.target.value)}
        >
          <option value="add">+</option>
          <option value="subtract">-</option>
          <option value="multiply">×</option>
          <option value="divide">÷</option>
        </select>
        
        <input 
          type="number" 
          value={num2} 
          onChange={(e) => setNum2(e.target.value)} 
          placeholder="Второе число"
        />
        
        <button onClick={calculate}>Вычислить</button>
      </div>

      {result && <div className="result">Результат: {result}</div>}
      
      <div className="history">
        <h2>История операций</h2>
        <button onClick={loadHistory}>Обновить</button>
        <ul>
          {history.map((item, index) => (
            <li key={index}>{item.operation}: {item.result}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;