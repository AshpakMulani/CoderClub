import * as React from 'react';
import Button from '@mui/material/Button';
import { withStyles, makeStyles } from "@material-ui/core/styles";

import './herotext.css'


const useStyles = makeStyles({
  root: {
    background: "#920E0E",
    border: 0,
    borderRadius: 3,
    boxShadow: "0 3px 5px 2px rgba(255, 105, 135, .3)",
    color: "white",
    height: 48,
    padding: "0 30px",
    marginTop: "4rem",    
  }
});


const HeroText = () => {
  const classes = useStyles();
  
  return (
  
    <div className='coder_club_hero_text'>
      {/*
      <div className='coder_club_hero_maintext_combine' >
          <div className='coder_club_hero_maintext'>  REAL  </div>
          <div className='coder_club_hero_maintext coder_club_hero_maintext_coding_span'> CODING</div> 
          <div className='coder_club_hero_maintext'> EXPOSURE WITH </div>
      </div>

      <div className='coder_club_hero_maintext'>HANDS-ON PROJECT BUILDING</div>
      */}

      <div className='coder_club_hero_maintext'>
        REAL 
        <span className='coder_club_hero_maintext_coding_span'>
          CODING
        </span>
        EXPOSURE WITH HANDS-ON PROJECT BUILDING
      </div>

      <div className='coder_club_hero_subtext'>
        CoderClub is run by coders for coders portal which is focused on do it
        yourself practicle coding approach with industry best practices around
        multiple programming laguages.
      </div>   
      
      <Button variant="contained"  sx={{background: '#920E0E', marginTop: '5rem'}}>explore more</Button>;
    </div>
   
  )
}


export default HeroText
