import React, { useState, useEffect } from 'react';
function App() {
  const [texts, setTexts] = useState([]);
  const [input, setInput] = useState('');

  const fetchTexts = async () => {
    const res = await fetch('http://flask-service:5000/texts');
    const data = await res.json();
    setTexts(data);
  };

  const addText = async () => {
    await fetch('http://flask-service:5000/add', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: input })
    });
    setInput('');
    fetchTexts();
  };

  const deleteTexts = async () => {
    await fetch('http://flask-service:5000/delete', { method: 'DELETE' });
    fetchTexts();
  };

  useEffect(() => { fetchTexts(); }, []);

  return (
    <div>
      <h1>Text Saver</h1>
      <input value={input} onChange={e => setInput(e.target.value)} />
      <button onClick={addText}>Add</button>
      <button onClick={deleteTexts}>Delete All</button>
      <ul>{texts.map(t => <li key={t.id}>{t.text}</li>)}</ul>
    </div>
  );
}
export default App;