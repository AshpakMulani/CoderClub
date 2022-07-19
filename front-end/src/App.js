import './App.css';
import { useEffect } from "react";
import { Hero, Topics, Navbar, WhatYouGet, Footer, Path, SideDraw, BackgroundResources } from './containers';




function App() {

  useEffect(() => {
    document.title = "CoderClub" ;
  }, [])
  

  return (
    <div className='App'>
      <div className='gradient_bg'>
        
      <SideDraw/>
      <BackgroundResources/>
      
        <div className='app_margin'>   
        
          <Navbar/>
          
          <Hero/>   
               
          <Path/>
          <Topics/>
        </div>    
      </div>
        
        <WhatYouGet/>
        <Footer/>
    </div>

  
  );
}

export default App;
