# ai-resume-assisstant
LLM powered tool to help improve resumes based on job description

PRD

Product Name: Resume Assistant

Do you ever go through multiple jobs reading through the job description and feel like, I am a viable candidate. You update your to show relevant experience, expecting to atleast hear back from the hiring team but instead you get a rejection!
Well you are not doing anything wrong, but companies thes days only pick resumes that have ATS matches of 90%+ and this is where you are losing out. 
The resume assistant helps you bridge this gap and make your resume have an ATS match of 90%+, thus helping to elevate your resume.

1. Problem: When applying for new jobs, candidates are not sure what keywords to use to get an ATS match of 90%+

2. Solution

  AI can help bridge the gap by providing candidates with the right keywords based on the job description for which they are applying. Based on these keywords, AI can rewrite a polished 
  resume for users in the exact same format which users can directly use for the relevant job.
  MVP:
  1. User will provide resume and description in UI
  3. LLM will output a polished resume containing all ATS relevant keywords in all the right places.
  4. LLM will also list keywords that it included and why

3. Approach
  Based on the 
      
4. Architecture

    User Input -> Prompt Engine -> LLM -> Output formatter -> UI

   Code structure
   app.py - runs the UI and takes user input and internally calls ResumeJD_Compare.py
   ResumeJD_Comapre - runs the prompts that actually compare the resume and JD to output the final result
   
5. Prompt Design
6. Evaluation
7. Example Output
8. Challenges
9. Future Work
