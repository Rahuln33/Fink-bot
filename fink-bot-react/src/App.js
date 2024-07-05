import React, { useState } from 'react';
import axios from 'axios';
import Chatbox from './components/Chatbox';
import EmailInput from './EmailInput';
import './styles/chatbot.css';
// import { Component } from '../src/components/Chatbox';
const App = () => {
    const [email, setEmail] = useState('');
    const [sessionId, setSessionId] = useState(null);

    const handleEmailSubmit = async (email) => {
        try {
            const response = await axios.post('http://127.0.0.1:5000/api/start_session', { email });
            setSessionId(response.data.session_id);
            setEmail(email);
        } catch (error) {
            console.error('Error starting session:', error);
        }
    };

    return (
        <div>
            {sessionId ? (
                <Chatbox sessionId={sessionId} email={email} />
            ) : (
                <EmailInput onEmailSubmit={handleEmailSubmit} />
            )}
        </div>
    );
};

export default App;
