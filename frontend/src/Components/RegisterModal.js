"use client";
import React, {useState} from 'react';
import '@/Style/Register.scss';
import '@/Style/globals.scss'
import { postApi } from '@/Components/callApi';

const RegisterModal = ({ isvisible, onclose, onhange }) => {

    // const [username, setUsername] = useState('');
    // const [email, setEmail] = useState('');
    // const [password, setPassword] = useState('');
    // const [password2, setPassword2] = useState('');

    // const submit = async (e) => {
    //     e.preventDefault();
    //     await postApi('register/',{}, {
    //         username,
    //         email,
    //         password, 
    //         password2
    //     });
    // }

    const [formData, setFormData] = useState({
      username: '',
      email: '',
      password: '',
      password2: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
        ...formData,
        [name]: value,
    });
};

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      postApi({ path: 'register/', dataToPost: formData });
      // Redirect or display a success message
    } catch (error) {
      console.error(error.response.data);
    }
};

    if(!isvisible) return null;

    return (
      <div className="PopUp">

      <form onSubmit={handleSubmit} method="post"> 
      <button className="CrossButton" onClick={() => {onclose()}}>x</button>
      <h3 className="Title">Create an account</h3>

      <h3 className="InputItem">Username</h3> 
      <div className="InputBox">
          <input className="Input" type="text" required onChange={handleChange}/>
      </div>

      <h3 className="InputItem">Email</h3>
      <div className="InputBox">
          <input className="Input" type="email" required onChange={handleChange}/>
      </div>

      <h3 className="InputItem">Password</h3>
      <div className="InputBox">
          <input className="Input" type="password" required onChange={handleChange}/>
      </div>

      <h3 className="InputItem">Repeat password</h3>
      <div className="InputBox">
          <input className="Input" type="password" required onChange={handleChange}/>  
      </div>

      <div className="SignUpButton">
          <button type='submit' value="Submit" className="SignUp">Sign up</button>
      </div>
      </form>

      <div className="OtherOptionButton">
          <button onClick={() => onchange()}>Are you a member? <span style={{ textDecoration: 'underline' }}>Sign in</span></button>
      </div>

      </div> 
    );
};


export default RegisterModal;
