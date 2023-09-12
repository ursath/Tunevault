import React from 'react';
import Menu from './Components/Menu';
import home from '../Resources/home.png';
import '../css/Components/Basics.css';
import '../css/Home.css';
export default function Home() {
  return (
    <div className='Basics'>
        <Menu />
        <div className='Header'>Join our music lover community</div>
        <div className='ImageBox'><img className="Image" src={home} alt="home"></img></div>
    </div>
  )
}