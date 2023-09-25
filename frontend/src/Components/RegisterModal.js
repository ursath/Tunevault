"use client";
import React, {useState} from 'react';
import '../Style/Register.scss';
import '../Style/globals.scss'

const RegisterModal = ({ isvisible, onclose, onchange }) => {

    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [password2, setPassword2] = useState('');

    const submit = async (e) => {
        e.preventDefault();
        await fetch('http://127.0.0.1:8000/api/profiles/', {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
            username,
            email,
            password, 
            password2
            })
        });
        window.location.href = '/';
    }

    if(!isvisible) return null;

    return (
    <div className="PopUp">

        <form onSubmit={submit}> 
        <button className="CrossButton" onClick={() => {onclose()}}>x</button>
        <h3 className="Title">Create an account</h3>

        <h3 className="InputItem">Username</h3> 
        <div className="InputBox">
            <input className="Input" type="text" required onChange={e => setUsername(e.target.value)}/>
        </div>

        <h3 className="InputItem">Email</h3>
        <div className="InputBox">
            <input className="Input" type="email" required onChange={e => setEmail(e.target.value)}/>
        </div>

        <h3 className="InputItem">Password</h3>
        <div className="InputBox">
            <input className="Input" type="password" required onChange={e => setPassword(e.target.value)}/>
        </div>

        <h3 className="InputItem">Repeat password</h3>
        <div className="InputBox">
            <input className="Input" type="password" required onChange={e => setPassword2(e.target.value)}/>  
        </div>

        <div className="SignUpButton">
            <button type='submit' className="SignUp">Sign up</button>
        </div>

        <div className="OtherOptionButton">
            <button onClick={() => onchange()}>Are you a member? <span style={{ textDecoration: 'underline' }}>Sign in</span></button>
        </div>
        </form>
    </div>
    );
};

export default RegisterModal;