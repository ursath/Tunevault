"use client";
import '../Style/Menu.scss';
import logo from '../Resources/logo.png';
import Link from "next/link";
import Image from 'next/image';
import LogInModal from './LogInModal';
import Lupa from '../Resources/search.js';
import { useState } from 'react';

export default function Menu() {
  const[showLogInModal, setShowLogInModal] = useState(false);

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
                <button className="LogIn" onClick={() => setShowLogInModal(true)}>
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
      <LogInModal isvisible={showLogInModal} onclose={() => setShowLogInModal(false)} />
      </div>
  );
}
