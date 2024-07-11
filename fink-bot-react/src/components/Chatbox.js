import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import './Chatbox.css';
import sendIcon from '../assets/sendmessage.png';
import chaticon from '../assets/message.jpg';

const Chatbox = ({ sessionId, email }) => {
    const [messages, setMessages] = useState([
        {
            name: 'Bot',
            message: "Hi! I'm fink.ai. I'm here to assist you. What are you looking for? Choose one of these popular topics or type your question below."
        }
    ]);
    const [userInput, setUserInput] = useState('');
    const messagesEndRef = useRef(null);

    useEffect(() => {
        const storedMessages = localStorage.getItem('chatMessages');
        if (storedMessages) {
            setMessages(JSON.parse(storedMessages));
        }
    }, []);

    useEffect(() => {
        localStorage.setItem('chatMessages', JSON.stringify(messages));
        scrollToBottom();
    }, [messages]);

    const toggleChatbox = () => {
        const chatbox = document.querySelector('.chatbox__support');
        chatbox.classList.toggle('chatbox--active');
    };

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    };

    const sendMessage = async () => {
        if (userInput === '' || sessionId === null) return;

        const userMessage = { name: 'User', message: userInput };
        setMessages([...messages, userMessage]);

        try {
            const response = await axios.post('http://127.0.0.1:5000/api/chat', {
                message: userInput,
                session_id: sessionId,
                email: email
            });
            const botMessage = { name: 'Bot', message: response.data.response };
            setMessages((prevMessages) => [...prevMessages, botMessage]);
        } catch (error) {
            console.error('Error:', error);
            const errorMessage = { name: 'Bot', message: 'Sorry, something went wrong.' };
            setMessages((prevMessages) => [...prevMessages, errorMessage]);
        } finally {
            setUserInput('');
        }
    };

    const handleInputChange = (e) => {
        setUserInput(e.target.value);
    };

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    };

    return (
        <div>
            <div className="chatbox__button" onClick={toggleChatbox}>
                <button><img src={chaticon} alt="Chat Icon" width="40px" height="40px" /></button>
            </div>
            <div className="chatbox__support">
                <div className="chatbox__header">
                    <div className="chatbox__image--header">
                        <img src="https://i.pinimg.com/564x/6c/1e/10/6c1e10e6ddfc5002662049930702c23a.jpg" alt="Support" />
                        <div className="chatbox__content--header">
                            <h4 className='fink'>Fink.ai</h4>
                            <h6 className='fink1'>face of finkraft</h6> 
                        </div>
                    </div>
                </div>
                <div className="chatbox__messages">
                    {messages.map((msg, index) => (
                        <div key={index} className={`message ${msg.name === 'User' ? 'user-message' : 'bot-message'}`}>
                            {msg.name === 'Bot' && (
                                <div className="bot-message-container">
                                     <img src="https://i.pinimg.com/564x/6c/1e/10/6c1e10e6ddfc5002662049930702c23a.jpg" alt="Bot Avatar" className="bot-avatar" />
                                    <div className="message__content">{msg.message}</div>
                                </div>
                            )}
                            {msg.name === 'User' && (
                                <div className="message__content">{msg.message}</div>
                            )}
                        </div>
                    ))}
                    <div ref={messagesEndRef}></div>
                    <div className="chatbox-buttons">
                        <button onClick={() => setUserInput('Claimable GST')}>Claimable GST</button>
                        <button onClick={() => setUserInput('Un claimable GST')}>Un claimable GST</button>
                        <button onClick={() => setUserInput('Total vendor GST')}>Total vendor GST</button>
                    </div>
                </div>

                <div className="chatbox__footer">
                <div className="input-container">
                    
                    <input 
                        type="text" 
                        value={userInput} 
                        onChange={handleInputChange} 
                        onKeyPress={handleKeyPress}
                        placeholder="Type here..." 
                        className="input-on-image"
                    />
                </div>
               
                <img onClick={sendMessage} src={sendIcon} alt="Send" width="20px" height="15px" />
            </div>

            </div>
        </div>
    );
};

export default Chatbox;


                
