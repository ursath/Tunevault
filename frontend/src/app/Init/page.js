import Menu from '../../Components/Menu';
import '../../Style/globals.css';
import '../../Style/Home.css';
import Image from 'next/image';
import home from '../../Resources/home.png';

export default function Init() {
  return (
    <div className='Basics'>
        <Menu />
        <div className='Header'><h1>Join our music <span style={{ color: '#FF00FF' }}>lover</span> community</h1></div>
        <div className='ImageBox'><Image src={home} className="Image" alt="home" width={500} height={300}></Image></div>
    </div>
  )
}