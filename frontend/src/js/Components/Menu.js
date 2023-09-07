import React from 'react';
import '../../css/Components/Menu.css';
import logo from '../../Resources/logo.png';
/*import { Link } from "react-router-dom";*/

export default function Menu() {
  return (
    <header>
      <div className='Menu'>
        <img className='logo' src={logo} alt="logo" />
        <nav>
          <ul>
            <li className='item'><a href="/Music">Music</a></li>
            <li className='item'><a href="/Podcsats">Podcasts</a></li>
            <li className='item'><a href="/LogIn">Log in</a></li>
          </ul>
        </nav>
      </div>
    </header>
  );
}

/* <li><Link to="/">Home</Link></li>
            <li><Link to="/Music">Music</Link></li>
            <li><Link to="/Podcsats">Podcasts</Link></li>
            <li><Link to="/LogIn">Log in</Link></li>
            */
