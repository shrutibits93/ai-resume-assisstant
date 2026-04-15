# ai-resume-assisstant
LLM powered tool to help improve resumes based on job description

PRD

Product Name: Resume Assistant
Problem: When applying for new jobs, people need to keep tweaking their resume and
cover letter based on the company they are applying for and it’s hard to know for sure if their
final output meets the requirements. It’s a long and tedious process.
Users:
  1. New college graduates
  2. Working people looking for new job
  3. Unemployed folks looking for a new job

Jobs to be done:
  1. When I am applying for a role at a company, I want my resume to have the right keywords for that role and company
  2. When I am applying for a job, I want a tailored cover letter when needed.

Why AI:
  AI helps increase the chances of users getting a job by ensuring important keywords
  are included which user might miss while creating multiple resumes. Many times
  users may not know which words would be needed for ATS &gt; 90%, but here models
  learning can help.
  
North Star Metrics
  Number of resumes converted to interview process
  Initially let the north star metrics be 80% - an iterative development and eval cycle should
  help improve this and achieve the goal of 95%
  
Success Criteria
  Number of resumes converted to interview process &gt; 95%
  Hallucinations &lt; 5%
  Changes done to final resume by user &lt; 5%
  
Counter metrics
1. Hallucinations &lt; 5% (incorrect company or resume points)
2. Bias
3. Verbose resume
4. Tone – is it formal
   
Human Evaluation + LLM as judge
Have humans evaluate resumes that are output by the LLM and mark it as good or bad.
Prompt a powerful LLM to do the same and improve LLM prompt so that human evaluation
matches LLM evaluations. Once this LLM as judge is built, this can be a powerful evaluation
system to monitor any resumes output by the model before it is handed to users and help
improve the model and fix any model issues.

Post-launch

1. A/B testing – once the model is mature
2. View user responses to resumes (provide like, unlike buttons)
3. View how many times user changes resume output (ideally this should be &lt;5%)
   
Ongoing or development evaluation
1. Unit/regression tests (constant improvement needed here for new data)
2. While model is being built or fine-tuned, ensure 75% are training data and 25% test
data – model should not overfit the training data, the 25% data should help guarantee
this.

Risks
1. Model may make up resume points (hallucination)
2. Incorrect data/ points
3. May generate same resume for people applying for similar jobs
4. Low adoption due to trust on AI output

Safety/guardrails
1. Resume should not interpret data outside of resume provided
2. Initially can keep guardrails such as should not tweak resume more than 30%
3. Should not apply on behalf of the user, only provide resume sample
4. Use formal and polished language
UI/UX flow

Functional Requirements:
1. Provide users the ability to tweak their resume to reflect a certain job description so
that users don’t have to tweak for every role they apply.
2. Create a cover letter for the job description and resume provided by the user so that
users get a tailored cover letter for that role.

Data Requirements:
Input Data for AI model: Resume and job description provided by user
Context Data for AI model:
1. Past job description and resumes used by people that got selected
2. Data across multiple companies and roles
Feedback data: User gives feedback in text or reaction form

AI Feasibility
Model options:
1. LLM
2. RAG
3. Fine Tuning
Since this is an output based on input triggers a basic LLM can be used as MVP. There is
not company specific data required here so no need of RAG. LLM with prompting is the
MVP.

Data feasibility

1. How can we get data regarding company roles and resumes hired?
Latency is not a constraint here, so cost can be optimised accordingly by finetuning model in
future iterations.
No PII data involved hence no privacy constraints.

Iterations
MVP:
1. User can upload a resume and job description
2. Output a 30% tweaked resume in output
V2:
1. Allow users to input feedback
2. Model can incorporate feedback
3. Final resume in PDF
V3:
1. Ask user if they want cover letter
2. Based on adoption and learning of model, resume tweak can be increased to 50%
