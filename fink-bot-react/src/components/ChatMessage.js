import React from 'react';
import './styles/chatbot.css';
import './ChatMessage.css';

const ChatMessage = ({ message }) => {
    return (
        <div className={`chat-message ${message.sender}`}>
            {message.text}
        </div>
    );
};

export default ChatMessage;
