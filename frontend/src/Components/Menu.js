import '../Style/Menu.css';
import logo from '../Resources/logo.png';
import Link from "next/link";
import Image from 'next/image';

export default function Menu() {
  return (
      <div className="Menu">
        <Link href="/">
          <button className="Logo">
            <Image src={logo} alt="logo" />
          </button>
        </Link>
        <nav>
          <ul>
            <li><Link href="/Music" className="Item">Music</Link></li>
            <li><Link href="/Podcasts" className="Item">Podcasts</Link></li>
            <li><Link href="/Members" className="Item">Members</Link></li>
            <li>
              <Link className="Item" href="/LogIn">
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
