import '../Style/globals.scss'
import { Nunito, Poppins } from 'next/font/google'

const nunito = Nunito({
  subsets: ['latin'],
  variable: '--font-nunito',
  display: 'swap',
  weight: ['400', '700'],
})
 
const poppins = Poppins({
  subsets: ['latin'],
  variable: '--font-poppins',
  display: 'swap',
  weight: ['400', '700'],
})

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={`${poppins.variable} ${nunito.variable}`}>
      <body>{children}</body>
    </html>
  )
}
