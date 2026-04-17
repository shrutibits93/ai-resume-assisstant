# ai-resume-assisstant
LLM powered tool to help improve resumes based on job description

**Product Name: Resume Assistant**

  Do you ever go through multiple jobs reading through the job description and feel like, I am a viable candidate. You update your resume to show relevant experience, expecting to atleast
  hear back from the hiring team but instead you get a rejection!
  Well you are not doing anything wrong, but companies thes days only pick resumes that have ATS matches of 90%+ and this is where you are losing out. 
  The resume assistant helps you bridge this gap and make your resume have an ATS match of 90%+, thus helping to elevate your resume.

1. **Problem:** When applying for new jobs, candidates are not sure what keywords to use to get an ATS match of 90%+

2. **Solution**

    The problem is that users want to know what keywords should be included and where in the resume. They are not always aware what helps increase the ATS match. 
    AI can help bridge the gap by providing candidates with the right keywords based on the job description for which they are applying. Based on these keywords, AI can rewrite a polished 
    resume for users in the exact same format which users can directly use for the relevant job.

    For MVP, I have decided to just provide a basic output in the same format of the resume the user provides. User can like or dislike the resume which will help decide if it is serving 
    user's purpose or not. Eventually the idea is to get more user inputs to enhance model, but thats for future iterations.
    
    MVP:
    1. User will provide resume and description in UI
    2. LLM will output a polished resume containing all ATS relevant keywords in all the right places.
    3. LLM will also list keywords that it included and why
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
   
6. **Prompt Design**
7. **Evaluation**
8. Example Output
9. Challenges
10. Future Work
