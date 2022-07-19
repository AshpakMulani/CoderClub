import React, {useRef, useEffect, useState} from 'react'
import './pathtitle.css'


const PathTitle = () => {  
  const options = {root:null, rootMargin: "-150px", threshold:0};
  const slideupsection =  document.querySelectorAll(".slide_up_section");
  const [isElementOnScreen,setIsElementOnScreen] = useState();

  let myArray = Array.from(slideupsection)

  useEffect(()=>{
    const observer =  new IntersectionObserver((entries)=>{    
      entries.forEach(entry => {
            console.log(entry);
            setIsElementOnScreen(entry.isIntersecting);
          }
        );
  },options);


  myArray.forEach(
    (element) => {
      observer.observe(element);
      console.log(element);
    }
  );

  },[])
  
  
  
  /*
  useEffect(() => {    
    const observer =  new IntersectionObserver((entries)=>{    
        
        entries.forEach(
          entry => {
            
            console.log(entry)
            if(entry.isIntersecting){
              entry.target.classList.add('appear')     
           
            
            else{
              entry.target.classList.remove('appear')
              console.log('removing....')
            }
          }
        )    
  
      },[options])

      slideupsection.forEach(element => {
      observer.observe(element);
    })  
    
  },[])
  */

  return (
   <div>
       <div className='coder_club_path_title slide_up_section appear'>
           PATH
       </div>
       <div className='coder_club_path_subtitle slide_up_section appear'>
       Learning path needs to be followed starting with understanding basics
        of all required pre-requisits followed with developing mini-projects
         with step by step instructions to understand different aspects around
         end to end delivery 
       </div>       
    </div> 
  )
}


export default PathTitle
