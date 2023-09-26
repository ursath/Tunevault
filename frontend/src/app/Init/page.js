"use client"
import Menu from '../../Components/Menu';
import '../../Style/globals.scss';
import '../../Style/Home.scss';
import Image from 'next/image';
import home from '../../Resources/home.png';
import RegisterModal from '../../Components/RegisterModal';
import LogInModal from '../../Components/LogInModal';
import { useState } from 'react';
import Cilindro from '@/Resources/figures/cilindroHome';
import BoxVaults from '@/Components/vaultsPreview';
import Lupa from '@/Resources/search.js'

export default function Init() {
  const [showRegisterModal, setShowRegisterModal] = useState(false);
  const [showLogInModal, setShowLogInModal] = useState(false);

  const toggleModal = (modal) => {
    if (modal === 'register') {
      setShowRegisterModal(true);
      setShowLogInModal(false);
    } else if (modal === 'login') {
      setShowLogInModal(true);
      setShowRegisterModal(false);
    }
    else if (modal == 'close') {
      setShowRegisterModal(false);
      setShowLogInModal(false);
    }
  };
  
  return (
  <div className='all'>
    <div className='Basics'>
      <Menu/>
      <RegisterModal isvisible={showRegisterModal} onclose={() => toggleModal('close')} onchange={() => toggleModal('login')} />
      <LogInModal isvisible={showLogInModal} onclose={() => toggleModal('close')} onchange={() => toggleModal('register')} /> 
      <div className='container'>
        <div className='homeBox'> 
          <div className='Header'>
            <h1>Join our music <span style={{ color: '#FF00FF' }}>lover</span> community</h1>
            <div>
              <button className="createAccount" onClick={() => toggleModal('register')} >
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
        <div className='container'>
          <BoxVaults/>
        </div>
        <div>
          <div className="SearchHome">
            <input className="InputSearch" placeholder='What do you want to talk about?' type="text" id="searcher" />
            <Lupa size="20" color="white" />
          </div>
          <div className='container'>
        <Cilindro className="figure"/>
        </div>
        </div>
      </div>
    </div>
  </div>
  )
}