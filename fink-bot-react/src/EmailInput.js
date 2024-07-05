import React, { useState } from 'react';
import './styles/chatbot.css';
const EmailInput = ({ onEmailSubmit }) => {
    const [email, setEmail] = useState('');

    const handleEmailSubmit = (e) => {
        e.preventDefault();
        if (email.trim() !== '') {
            onEmailSubmit(email);
            setEmail('');
        }
    };

    return (
        <div className="login-container">
            <div className="welcome-message">WELCOME TO FINK CHATBOT</div>
            <h2 className="login-header">Login</h2>
            <form onSubmit={handleEmailSubmit}>
                <input
                    type="email"
                    placeholder="Enter your email..."
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <button type="submit">Login</button>
            </form>
        </div>
    );
};

export default EmailInput;
