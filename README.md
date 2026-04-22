# ai-resume-assisstant
LLM powered tool to help improve resumes based on job description

**Product Name: Resume Assistant**

  Do you ever go through multiple jobs reading through the job description and feel like, I am a viable candidate. You update your resume to show relevant experience, expecting to atleast
  hear back from the hiring team but instead you get a rejection!
  Well you are not doing anything wrong, low keyword match creates a low ATS ranking and this is where you are losing out. 
  The resume assistant helps you bridge this gap and make your resume have an ATS match of 90%+, thus helping to elevate your resume.

1. **Problem:** When applying for new jobs, candidates are not sure what keywords to use to get an ATS match of 90%+ and hence do not clearly articulate their experience to match the job. 
                Resume tailoring is a real problem!

2. **Solution**

    The problem is that users want to know what keywords should be included and where in the resume. They are not always aware what helps increase the ATS match. 
    AI can help bridge the gap by providing candidates with the right keywords based on the job description for which they are applying. It will help increase keyword coverage for each 
    resume and provide a more tailored, aligned resume per job and word the the skills towards the job without assuming data and solely relying on data provided by user. The original
    format of users resume will also be maintained.

    For MVP, I have decided to just provide a basic output in the same format of the resume the user provides. User can like or dislike the resume which will help decide if it is serving 
    user's purpose or not. Eventually the idea is to get more user inputs to enhance model, but thats for future iterations.
    
    MVP: Improved Keyword coverage and match to the job for users
    1. User will provide resume and description in UI
    2. LLM will output a polished resume containing all ATS relevant keywords in all the right places.
    3. LLM will also list keywords that it included and to which section to get the best match without keyword stuffing
    4. User can like or dislike the solution

3. **Approach**

    Based on the solution, the model I decided to use initially was a pre-trained model with prompting. I did not go with RAG or fine-tuning for MVP as the model has to only consider the
    data shared by the user and rewrite it. The context is also small and there are no history to be considered for MVP.
    Cost and Latency considerations: 
    Between RAG and LLM prompting, LLM prompting would have a lower cost. To consider user adoption, I have decided to take lower cost for MVP, based on user reations, the model can be 
    built with more sofistication. Prompt LLMs will be faster as well
    
    Since the model should rewrite based on facts only and show too much creativity, I have kept the temperature on the lower end. This will also help reduce hallucinations and be more
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
    5. Use can choose to re-input the aligned version and LLM can further improve this.

    The UI ensures that users have control on what resume they like and want to use and how much they want to rely on AI. The AI only provide suggestions.
   
6. **Prompt Design**

    The prompt structure for MVP is-
    system - to define the initial instructions/foundation rules for the LLM. Controls are put in place to prevent data leakage, maintain tone and format.
    user - to provide the user entered job description and resume and query for what generically a user may want, which is ATS match of 90%+

    For future iterations, assistant can be put in place when context needs to be preserved and LLM is also considering continuous user feedback and using that to improve a resume further.
    
7. **Evaluation**

   North-star metric

      Number of users happy with the ATS matched resume provided by the app
   
   Success metrics

     1. Resume accuracy > 95%
     2. Less edit rate post resume generation
     3. % JD coverage by keywords

   Counter metrics

     1. Hallucinations < 5%
     2. Dislikes by user < 10%

   Kill criteria

     1. Dislikes by user exceeding 15%
  
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
