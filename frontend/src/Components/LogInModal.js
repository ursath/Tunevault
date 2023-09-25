"use client";
import React, {useState} from 'react';
import '../Style/Register.scss';
import '../Style/globals.scss'
import RegisterModal from './RegisterModal';

const LogInModal = ({ position, isvisible, onclose }) => {

    const[showRegisterModal, setShowRegisterModal] = useState(false);

    const openRegisterModal = () => {
        setShowRegisterModal(true);
      };

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const submit = async (e) => {
        e.preventDefault();
        await fetch('http://127.0.0.1:8000/api/profiles/', {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
            username,
            password
            })
        });
        window.location.href = '/';
    }

    if(!isvisible) return null;

    return (
    <div className="PopUp">
        <RegisterModal isvisible={showRegisterModal} onclose={() => setShowRegisterModal(false)} />
        <form onSubmit={submit}> 
        <button className="CrossButton" onClick={() => {setShowRegisterModal(false); onclose()}}>x</button>
        <h3 className="Title">Sign In</h3>

        <h3 className="InputItem">Username</h3> 
        <div className="InputBox">
            <input className="Input" type="text" required onChange={e => setUsername(e.target.value)}/>
        </div>

        <h3 className="InputItem">Password</h3>
        <div className="InputBox">
            <input className="Input" type="password" required onChange={e => setPassword(e.target.value)}/>
        </div>

        <div className="SignUpButton">
            <button type='submit' className="SignUp">Sign in</button>
        </div>

        <div className="OtherOptionButton">
            <button onClick={openRegisterModal}>Don't have an account? <span style={{ textDecoration: 'underline' }}>Sign up</span></button>
        </div>

        </form>
    </div>
    );
};

export default LogInModal;