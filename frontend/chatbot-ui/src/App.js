import React, { useState } from "react";
import axios from "axios";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input) return;
    const newMessages = [...messages, { sender: "user", text: input }];
    setMessages(newMessages);
    setInput("");

    try {
      const response = await axios.post("https://chatbot-6-ynkb.onrender.com/chat", {
        message: input,
        user_profile: {}
      });

      setMessages([...newMessages, { sender: "bot", text: response.data.reply }]);
    } catch (error) {
      setMessages([...newMessages, { sender: "bot", text: "Error: Server ki connect avvatledu" }]);
    }
  };

  return (
    <div style={{padding: 20, maxWidth: 600, margin: "auto"}}>
      <h1>Career Guidance Chatbot</h1>
      
      <div style={{border: "1px solid gray", height: 400, overflowY: "scroll", padding: 10, marginBottom: 10}}>
        {messages.map((msg, i) => (
          <p key={i}><b>{msg.sender}:</b> {msg.text}</p>
        ))}
      </div>

      <input 
        value={input} 
        onChange={(e) => setInput(e.target.value)} 
        onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
        placeholder="Ask me anything about careers..."
        style={{width: "70%", padding: 8}}
      />
      <button onClick={sendMessage} style={{padding: 8, marginLeft: 5}}>Send</button>
    </div>
  );
}

export default App;