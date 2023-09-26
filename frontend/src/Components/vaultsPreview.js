import '@/Style/globals.scss';
import '@/Style/boxVaults.scss'
import Image from 'next/image';
import album from '@/Resources/albumEj.png'

export function VaultPreview(){
    <div classname="box">
        <Image src={album} className="imgVault" alt="home"></Image>
    </div>
    
}

export default function BoxVaults () {
    return (
        <div>
    
    <div classname="box">
        <Image src={album} className="imgVault" alt="home"></Image>
    </div>
    
    
            <VaultPreview/>
            <VaultPreview/>
            <VaultPreview/>
        </div>
    );
}

