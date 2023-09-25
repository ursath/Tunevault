"use client"
import Menu from '../../Components/Menu';
import '../../Style/globals.scss';
import '../../Style/Home.scss';
import Image from 'next/image';
import home from '../../Resources/home.png';
import RegisterModal from '../../Components/RegisterModal';
import { useState } from 'react';

export default function Init() {
  const[showModal, setShowModal] = useState(false);
  
  return (
<div className='all'>
  <div className='Basics'>
      <Menu />
      <RegisterModal isvisible={showModal} onclose={() => setShowModal(false)} /> 
      <div className='container'>
        <div className='homeBox'> 
          <div className='Header'>
            <h1>Join our music <span style={{ color: '#FF00FF' }}>lover</span> community</h1>
            <div>
              <button className="createAccount" onClick={() => setShowModal(true)} >
                    <p className="createAccount">Create an account</p> 
              </button>
            </div>
          </div>
            <Image src={home} className="homeImage" alt="home"></Image>
        </div>
    </div>
      <div className='Black'> 
        <div className='container'>
        <h2> Discover new albums & artists</h2>
        </div>
      </div>
      
    </div>
    </div>
  )
}