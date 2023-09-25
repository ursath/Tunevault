"use client";
import '../Style/Menu.scss';
import logo from '../Resources/logo.png';
import Link from "next/link";
import Image from 'next/image';
import RegisterModal from './RegisterModal';
import Lupa from '../Resources/search.js';
import { useState } from 'react';

export default function Menu() {
  const[showModal, setShowModal] = useState(false);

  return (
    <div>
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
              
                <button className="LogIn" onClick={() => setShowModal(true)}>
                   <p className="Item">Log In</p>
                </button>
            </li>
            <li className='NavItem'>
              <div className="search">
                  <input className='Item' id='searcher' >
                  </input>
                  <Lupa size="20" />
              </div>
            </li>
          </ul>
        </nav>
      </div>
      <RegisterModal isvisible={showModal} onclose={() => setShowModal(false)} />
      </div>
  );
}
