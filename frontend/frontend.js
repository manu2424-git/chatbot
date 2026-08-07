import React, { useState } from "react";
import ChatWindow from "./components/ChatWindow";

function App() {
  return (
    <div>
      <h1>Career Guidance Chatbot</h1>
      <ChatWindow />
    </div>
  );
}

export default App;
import React, { useState } from "react";
import axios from "axios";

function ChatWindow() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    const userMessage = { sender: "user", text: input };
    setMessages([...messages, userMessage]);

    const response = await axios.post("http://127.0.0.1:8000/chat", {
      message: input,
      user_profile: {}
    });

    const botMessage = { sender: "bot", text: response.data.reply };
    setMessages([...messages, userMessage, botMessage]);
    setInput("");
  };

  return (
    <div>
      <div style={{ border: "1px solid #ccc", padding: "10px", height: "300px", overflowY: "scroll" }}>
        {messages.map((msg, i) => (
          <div key={i} style={{ textAlign: msg.sender === "user" ? "right" : "left" }}>
            <b>{msg.sender}:</b> {msg.text}
          </div>
        ))}
      </div>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type your message..."
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

export default ChatWindow;
