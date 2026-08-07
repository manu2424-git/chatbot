import React, { useState } from "react";
import axios from "axios";

function ChatWindow() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input) return;
    const userMessage = { sender: "user", text: input };
    setMessages([...messages, userMessage]);
    setInput("");

    const response = await axios.post("https://chatbot-6-ynkb.onrender.com/chat", {
      message: input,
      user_profile: {}
    });

    const botMessage = { sender: "bot", text: response.data.reply };
    setMessages([...messages, userMessage, botMessage]);
  };

  return (
    <div>
      <input value={input} onChange={(e) => setInput(e.target.value)} />
      <button onClick={sendMessage}>Send</button>
      <div>
        {messages.map((msg, i) => <p key={i}>{msg.sender}: {msg.text}</p>)}
      </div>
    </div>
  );
}

function App() {
  return (
    <div>
      <h1>Career Guidance Chatbot</h1>
      <ChatWindow />
    </div>
  );
}

export default App;