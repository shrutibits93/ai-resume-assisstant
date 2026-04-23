# ai-resume-assisstant
LLM powered tool to help improve resumes based on job description

**Product Name: Resume Assistant**

  Do you ever go through multiple jobs reading through the job description and feel like, I am a viable candidate. You update your resume to show relevant experience, expecting to atleast
  hear back from the hiring team but instead you get a rejection!
  This happens due to low keyword match which creates a low ATS ranking and not having a resume aligned to the right job. 
  

1. **Problem:** Job seekers struggle to understand whether they are a strong fit for a role and how to tailor their resume for Applicant Tracking Systems (ATS). As a result, qualified candidates are often filtered out due to poor keyword alignment.

2. **Solution**

    The problem is that users want to know what keywords should be included and where in the resume. They are not always aware what helps increase the ATS match.
    The resume assistant helps makes applying for jobs easier by providing the following features
       Job Match Score – Estimates alignment between resume and job description
       Keyword Gap Analysis – Identifies missing or weak signals
       Resume Rewrite – Generates a tailored version while preserving factual accuracy
       User Feedback Loop – Like/dislike signals to guide future improvements
    The reason we use AI here is because there is no single template that fits every job and every candidate is different. AI can help here by using semantic similarities to understand        differences between a resume and job description and bridge that gap. The right prompts can also help monitor the tone and format. AI also has the ability to personalise overtime as       it understands the users preferences.

    For MVP, I have decided to just provide a basic output in the same format of the resume the user provides. User can like or dislike the resume which will help decide if it is serving 
    user's purpose or not. Eventually the idea is to get more user inputs and feedback to enhance the output dynamically, but thats for future iterations.
    
    MVP: Assist user to apply for jobs where they have highest match and where applicable improved Keyword coverage and align resume to the job 
    1. User will provide resume and description in UI
    2. LLM will provide match percentage of job and resume and key gaps
    3. User can decide to proceed by clicking yes or no
    4. When user clicks yes, then LLM will list key areas where resume needs changes and furnish a rewritten resume.
    5. User can click "Use for job" or "Rewrite to get a better output"

4. **Approach**

    Based on the solution, the model I decided to use initially was a pre-trained model with prompting. I did not go with RAG or fine-tuning for MVP as the model has to only consider the
    data shared by the user and rewrite it. The context is also small and there are no history to be considered for MVP. Prompting provides quick results as well.
    
    Since the model should rewrite based on facts only and not show too much creativity, I have kept the temperature on the lower end. This will also help reduce hallucinations and be more
    deterministic. 

    Every input and output combination will be stored and logged (I have not captured this in code as I dont have a big data base, but thats the idea). This helps monitor usage and helps 
    in future iterations.

    I have also chosen streamlit to run the app as its only a few lines of code for MVP and need to quickly run the app with less complexity.
      
5. **Architecture**

    User Input -> Prompt Engine -> LLM -> Output formatter -> UI

    Code structure
    app.py - runs the UI and takes user input and internally calls ResumeJD_Compare.py
    ResumeJD_Comapre - runs the prompts that actually compare the resume and JD to output the final result

    UI flow
    1. User enters data and submits which triggers the model
    2. Prompts and LLM process the input and based on the job tailore the resume
    3. User provided with where the resume was weak and what keywords need to be included for better alignement and also provided with a final tailored resume
    4. User can react by liking or unliking the output. 
    5. User can choose to re-input the aligned version and LLM can further improve this.

    The UI ensures that users have control on what resume they like and want to use and how much they want to rely on AI. The AI only provide suggestions.
   
6. **Prompt Design**

    The prompt structure for MVP is-
    system - to define the initial instructions/foundation rules for the LLM. Controls are put in place to prevent data leakage, maintain tone and format.
    user - to provide the user entered job description and resume and query for what generically a user may want, which is ATS match of 90%+

    For future iterations, assistant can be put in place when context needs to be preserved and LLM is also considering continuous user feedback and using that to improve a resume further.
    
7. **Evaluation**

   North-star metric

      1. Number of resumes requested by user for rewrite - this captures engagement and usage
      2. Number of resumes used for job application
   
   Success metrics

     1. Number of rewrites requested (this should be low)
     2. % JD coverage by keywords

   Counter metrics

     1. % Incorrect matches shown
     2. Resume accuracy and tone
     3. Keyword stuffing %
     4. Model should not overcompensate for gaps in resume

   Kill criteria

     1. If a user clicks on rewrite more than 5 times then there is less value for them
     2. Overall rewrites % exceeds 20% then kill
  
9. **Example Output**

    Model Running
    
   <img width="1219" height="541" alt="Screenshot 2026-04-17 at 11 24 50 AM" src="https://github.com/user-attachments/assets/e71cd365-7a1c-4e9f-bc26-5cf8dbb652a9" />

    Output

    <img width="785" height="725" alt="Screenshot 2026-04-17 at 11 27 47 AM" src="https://github.com/user-attachments/assets/d6bdbbcb-725e-4f12-b983-5ddec30415b1" />

    <img width="798" height="857" alt="Screenshot 2026-04-17 at 11 28 11 AM" src="https://github.com/user-attachments/assets/13241ff7-0abc-43f5-a825-5b260efcdba5" />

    
11. **Challenges**

    AI specific risks to consider:
     1. Bias - model may decide to use certain keywords based on job role/user 
     2. Hallucinations - model may create its own facts for a job role and try to reach ATS 90%
     
12. **Future Work**

    V1: Improvements based on user input and feedback - more dynamic feedback loop
    V2: Downloadable pdf version of resume based on template selection by user
