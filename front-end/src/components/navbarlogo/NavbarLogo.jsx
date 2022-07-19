import React from 'react'
import './navbarlogo.css'
import icon from '../../assets/icon.png'
import logo from '../../assets/logotext.png'

const NavbarLogo = () => {
  return (
   <div  className='coderclub_navbar_logo'>
        <img className='icon' src={icon} alt='coderclub logo'/>        
        <img className='text' src={logo} alt='coderclub logo'/> 
    </div>
 
  )
}


export default NavbarLogo
