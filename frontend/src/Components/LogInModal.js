"use client";
import React, {useState} from 'react';
import '../Style/Register.scss';
import '../Style/globals.scss';
import {postApi} from '@/Components/callApi.js' 
const LogInModal = ({ isvisible, onclose, onchange }) => {

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const submit = async (e) => {
        e.preventDefault();
        await postApi('api/jwt/create/',{
          username: username,
          password: password,
      });
    }
    
    if(!isvisible) return null;

    return (
    <div className="PopUp">
        <form onSubmit={submit}> 
        <button className="CrossButton" onClick={() => onclose()}>x</button>
        <h3 className="Title">Sign in</h3>

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
            <button onClick={() => onchange()}>{`Don't have an account?`} <span style={{ textDecoration: 'underline' }}>Sign up</span></button>
        </div>

        </form>
    </div>
    );
};

export default LogInModal;