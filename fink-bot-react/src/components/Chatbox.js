
// import React, { useState } from 'react';
// import axios from 'axios';
// import './Chatbox.css';
// import sendIcon from '../assets/sendmessage.png';
// import chaticon from '../assets/message.jpg';

// const Chatbox = () => {
//     const [messages, setMessages] = useState([]);
//     const [userInput, setUserInput] = useState('');
//     const sessionId = 'unique_session_id'; // Generate or retrieve a unique session ID

//     const toggleChatbox = () => {
//         const chatbox = document.querySelector('.chatbox__support');
//         chatbox.classList.toggle('chatbox--active');
//     };

//     const sendMessage = async () => {
//         if (userInput === '') return;

//         const userMessage = { name: 'User', message: userInput };
//         setMessages([...messages, userMessage]);

//         try {
//             const response = await axios.post('http://127.0.0.1:5000/api/chat', { message: userInput, email: 'user@example.com', session_id: sessionId });
//             const botMessage = { name: 'Bot', message: response.data.response };
//             setMessages([...messages, userMessage, botMessage]);
//         } catch (error) {
//             console.error('Error:', error);
//             const errorMessage = { name: 'Bot', message: 'Sorry, something went wrong.' };
//             setMessages([...messages, userMessage, errorMessage]);
//         }

//         setUserInput('');
//     };

//     const handleKeyPress = (event) => {
//         if (event.key === 'Enter') {
//             sendMessage();
//         }
//     };

//     return (
//         <div className="chatbox">
//             <div className="chatbox__button" onClick={toggleChatbox}>
//                 <button><img src={chaticon} alt="Chat Icon" height="10px" width={"20px"} /></button>
//             </div>
//             <div className="chatbox__support">
//                 <div className="chatbox__header">
//                     <div className="chatbox__image--header">
//                         <img src="https://img.icons8.com/color/48/000000/circled-user-female-skin-type-5--v1.png" alt="Support" />
//                     </div>
//                     <div className="chatbox__content--header">
//                         <h4 className="chatbox__heading--header">Finkraft</h4>
//                         <p className="chatbox__description--header">Greetings! I'm Fink. What assistance can I provide you with today?</p>
//                     </div>
//                 </div>
//                 <div className="chatbox__messages">
//                     {messages.map((msg, index) => (
//                         <div key={index} className={`messages__item messages__item--${msg.name === 'User' ? 'operator' : 'visitor'}`}>
//                             {msg.message}
//                         </div>
//                     )).reverse()}
//                 </div>
//                 <div className="chatbox__footer">
//                     <input
//                         type="text"
//                         placeholder="Write a message..."
//                         value={userInput}
//                         onChange={(e) => setUserInput(e.target.value)}
//                         onKeyPress={handleKeyPress}
//                     />
//                     <button className="chatbox__send--footer" onClick={sendMessage}>
//                         <img src={sendIcon} alt="Send" />
//                     </button>
//                 </div>
//             </div>
//         </div>
//     );
// };

// export default Chatbox;


//////////////

// import React, { useState, useEffect } from 'react';
// import axios from 'axios';
// import './Chatbox.css';
// import sendIcon from '../assets/sendmessage.png';
// import chaticon from '../assets/message.jpg';

// const Chatbox = () => {
//     const [messages, setMessages] = useState([]);
//     const [userInput, setUserInput] = useState('');
//     const [email, setEmail] = useState('');
//     const [sessionId, setSessionId] = useState(null);

//     const toggleChatbox = () => {
//         const chatbox = document.querySelector('.chatbox__support');
//         chatbox.classList.toggle('chatbox--active');
//     };

//     const startSession = async () => {
//         if (email === '') return;
//         try {
//             const response = await axios.post('http://127.0.0.1:5000/api/start_session', { email });
//             setSessionId(response.data.session_id);
//         } catch (error) {
//             console.error('Error starting session:', error);
//         }
//     };

//     const sendMessage = async () => {
//         if (userInput === '' || sessionId === null) return;

//         const userMessage = { name: 'User', message: userInput };
//         setMessages([...messages, userMessage]);

//         try {
//             const response = await axios.post('http://127.0.0.1:5000/api/chat', { message: userInput, email, session_id: sessionId });
//             const botMessage = { name: 'Bot', message: response.data.response };
//             setMessages([...messages, userMessage, botMessage]);
//         } catch (error) {
//             console.error('Error:', error);
//             const errorMessage = { name: 'Bot', message: 'Sorry, something went wrong.' };
//             setMessages([...messages, userMessage, errorMessage]);
//         }

//         setUserInput('');
//     };

//     const handleKeyPress = (event) => {
//         if (event.key === 'Enter') {
//             sendMessage();
//         }
//     };

//     return (
//         <div className="chatbox">
//             <div className="chatbox__button" onClick={toggleChatbox}>
//                 <button><img src={chaticon} alt="Chat Icon" height="10px" width={"20px"} /></button>
//             </div>
//             <div className="chatbox__support">
//                 <div className="chatbox__header">
//                     <div className="chatbox__image--header">
//                         <img src="https://img.icons8.com/color/48/000000/circled-user-female-skin-type-5--v1.png" alt="Support" />
//                     </div>
//                     <div className="chatbox__content--header">
//                         <h4 className="chatbox__heading--header">Finkraft</h4>
//                         <p className="chatbox__description--header">Greetings! I'm Fink. What assistance can I provide you with today?</p>
//                     </div>
//                 </div>
//                 <div className="chatbox__messages">
//                     {messages.map((msg, index) => (
//                         <div key={index} className={`messages__item messages__item--${msg.name === 'User' ? 'operator' : 'visitor'}`}>
//                             {msg.message}
//                         </div>
//                     )).reverse()}
//                 </div>
//                 <div className="chatbox__footer">
//                     {sessionId === null ? (
//                         <>
//                             <input
//                                 type="email"
//                                 placeholder="Enter your email..."
//                                 value={email}
//                                 onChange={(e) => setEmail(e.target.value)}
//                             />
//                             <button onClick={startSession}>Start Chat</button>
//                         </>
//                     ) : (
//                         <>
//                             <input
//                                 type="text"
//                                 placeholder="Write a message..."
//                                 value={userInput}
//                                 onChange={(e) => setUserInput(e.target.value)}
//                                 onKeyPress={handleKeyPress}
//                             />
//                             <button className="chatbox__send--footer" onClick={sendMessage}>
//                                 <img src={sendIcon} alt="Send" />
//                             </button>
//                         </>
//                     )}
//                 </div>
//             </div>
//         </div>
//     );
// };

// export default Chatbox;
import React, { useState } from 'react';
import axios from 'axios';
import './Chatbox.css';
import sendIcon from '../assets/sendmessage.png';
import chaticon from '../assets/message.jpg';
// import './styles/chatbot.css';
const Chatbox = ({ sessionId, email }) => {
    const [messages, setMessages] = useState([]);
    const [userInput, setUserInput] = useState('');

    const toggleChatbox = () => {
        const chatbox = document.querySelector('.chatbox__support');
        chatbox.classList.toggle('chatbox--active');
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
            setMessages([...messages, botMessage]);
        } catch (error) {
            console.error('Error:', error);
            const errorMessage = { name: 'Bot', message: 'Sorry, something went wrong.' };
            setMessages([...messages, errorMessage]);
        } finally {
            setUserInput('');
        }
    };

    const handleInputChange = (e) => {
        setUserInput(e.target.value);
    };

    return (
        <div>
            <div className="chatbox__button" onClick={toggleChatbox}>
                <button><img src={chaticon} alt="Chat Icon" width='10px' height='10px' /></button>
            </div>
            <div className="chatbox__support">
                <div className="chatbox__header">
                <div className="chatbox__header">
                     <div className="chatbox__image--header">
                         <img src="https://img.icons8.com/color/48/000000/circled-user-female-skin-type-5--v1.png" alt="Support" />
                     </div>
                     <div className="chatbox__content--header">
                         <h4 className="chatbox__heading--header">Finkraft</h4>
                         <p className="chatbox__description--header">Greetings! I'm Fink. What assistance can I provide you with today?</p>
                    </div>
                 </div>
                </div>
                <div className="chatbox__messages">
                    {messages.map((msg, index) => (
                        <div key={index} className={`message ${msg.name === 'User' ? 'user-message' : 'bot-message'}`}>
                            <div className="message__content">{msg.message}</div>
                        </div>
                    ))}
                </div>
                <div className="chatbox__footer">
                    <input 
                        type="text" 
                        value={userInput} 
                        onChange={handleInputChange} 
                        placeholder="Type a message..." 
                    />
                    <button onClick={sendMessage}>
                        <img src={sendIcon} alt="Send" width='20px' height='20px'/>
                    </button>
                </div>
            </div>
        </div>
    );
};

export default Chatbox;
