"use client";
import '../Style/Menu.scss';
import logo from '../Resources/logo.png';
import Link from "next/link";
import Image from 'next/image';
import LogInModal from './LogInModal';
import RegisterModal from './RegisterModal';
import Lupa from '../Resources/search.js';
import { useState } from 'react';

export default function Menu() {
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
    <div>
      <RegisterModal isvisible={showRegisterModal} onclose={() => toggleModal('close')} onchange={() => toggleModal('login')} />
      <LogInModal isvisible={showLogInModal} onclose={() => toggleModal('close')} onchange={() => toggleModal('register')} /> 
      <div className="Menu">
        <Link href="/">
          <button className="Logo">
            <Image src={logo} alt="logo" />
          </button>
        </Link>
        <nav className="Navigation">
          <ul className="List">
            <li className="NavItem"><Link href="/Music" className="Item">Music</Link></li>
            <li className="NavItem"><Link href="/Podcasts" className="Item">Podcasts</Link></li>
            <li className="NavItem"><Link href="/Members" className="Item">Members</Link></li>
            <li className="NavItem">
                <button className="LogIn" onClick={() => toggleModal('login')}>
                   <p className="Item">Log In</p>
                </button>
            </li>
            <li className="NavItem">
              <div className="search">
                  <input className="Item" type="text" id="searcher" />
                  <Lupa size="20" />
              </div>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  );
}
