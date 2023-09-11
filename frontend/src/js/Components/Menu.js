import React from 'react';
import '../../css/Components/Menu.css';
import logo from '../../Resources/logo.png';
import { Link } from "react-router-dom";

export default function Menu() {
  return (

      <div className="Menu">
        <Link to="/">
          <button className="Logo">
            <img src={logo} alt="logo" />
          </button>
        </Link>
        <nav>
          <ul>
            <li><Link className="Item" to="/Music">Music</Link></li>
            <li><Link className="Item" to="/Podcasts">Podcasts</Link></li>
            <li><Link className="Item" to="/Members">Members</Link></li>
            <li>
              <Link className="Item" to="/LogIn">
                <button className="LogIn">
                  <p className="Item">Log In</p>
                </button>
              </Link>
            </li>
          </ul>
        </nav>
      </div>

  );
}

            
