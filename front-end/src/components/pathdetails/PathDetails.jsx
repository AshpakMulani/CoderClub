import React from 'react'
import './pathdetails.css'
import pathline from '../../assets/pathline.png'


const PathDetails = () => {
  return (
   <div className='coder_club_path_details coder_club_slide_from_right'>
       <div className='coder_club_slide_from_left'>
       <img  src={pathline} alt="path line"/>
       </div>
        <div className='coder_club_path_step_one'>
           <div className='coder_club_path_step_one_block'>
           <div className='coder_club_path_step_sub'/>
           </div>
           <div className='coder_club_path_step_one_details'>
                <div className='coder_club_path_step_one_number'>1</div>
                <div className='coder_club_path_step_one_text'>
                    <div className='coder_club_path_step_one_title'>Blogs & Primer</div>
                    <div className='coder_club_path_step_one_subtitle'>
                        Read blogs and Primer cources to understand basics of pre-reuisits
                    </div>
                </div>
            </div>           
        </div>

        <div className='coder_club_path_step_two'>
            <div className='coder_club_path_step_two_block'>
            <div className='coder_club_path_step_sub'/>
            </div>
            <div className='coder_club_path_step_two_details'>
                    <div className='coder_club_path_step_two_number'>2</div>
                    <div className='coder_club_path_step_two_text'>
                        <div className='coder_club_path_step_two_title'>Mini Project</div>
                        <div className='coder_club_path_step_two_subtitle'>
                        Build mini project with step-by-step instructions to understand nits
                        and grits of the development process
                        </div>
                    </div>
            </div>  
        </div>    

        <div className='coder_club_path_step_three'>    
        <div className='coder_club_path_step_three_block'>
            <div className='coder_club_path_step_sub'/>
            </div>
            <div className='coder_club_path_step_three_details'>
                    <div className='coder_club_path_step_three_number'>3</div>
                    <div className='coder_club_path_step_three_text'>
                        <div className='coder_club_path_step_three_title'>Practice</div>
                        <div className='coder_club_path_step_three_subtitle'>
                        Build upon learnings by adding new features to exiting mini projects
                        or create new project to practice
                        </div>
                    </div>
            </div>  
        </div>    
    </div>
 
  )
}


export default PathDetails