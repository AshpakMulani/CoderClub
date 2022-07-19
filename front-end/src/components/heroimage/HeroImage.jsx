import React from 'react'
import './heroimage.css'
import hero_image from '../../assets/hero_image.png'

const HeroImage = () => {
  return (
    
    <div className='coder_club_hero_image_tilt_box'>
      <span className='t_over'></span>
      <span className='t_over'></span>
      <span className='t_over'></span>
      <span className='t_over'></span>
      <span className='t_over'></span>
      <span className='t_over'></span>
      <span className='t_over'></span>
      <span className='t_over'></span>
      <span className='t_over'></span>
      <img className='coder_club_hero_image' src={hero_image} alt="hero banner"/>
    </div>
    
  )
}


export default HeroImage
