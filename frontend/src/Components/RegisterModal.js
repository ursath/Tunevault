"use client";
import React, {useState} from 'react';
import '../Style/Register.css';
import '../Style/globals.css'

const RegisterModal = ({ isvisible, onclose }) => {

    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [password2, setPassword2] = useState('');

    const submit = async (e) => {
    e.preventDefault();
    await fetch('http://localhost:8000/api/profiles', {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
        username,
        email,
        password, 
        password2
        })
    });
    }

    if(!isvisible) return null;

    return (
    <div className="PopUp">
        <form onSubmit={submit}> 
        <button className="CrossButton" onClick={() => onclose()}>x</button>
        <h2 className="Title">Create an account</h2>

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

        <button className="SingInButton">Sign up</button>
        </form>
    </div>
    );
};

export default RegisterModal;