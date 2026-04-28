import os
import openai
from pathlib import Path

os.environ["OPENAI_API_KEY"] = "Your Key"

def enhance_text(resume_txt, job_description):
    client = openai.OpenAI()

    response = client.chat.completions.create(
        model="gpt-5.4",
        messages=[
            {
                "role": "system", "content": (f"""
                                                You are a resume assistant. 
                                                
                                                Task: Improve the resume based on the job description.

                                                STRICT INSTRUCTIONS:
                                                - Do NOT provide analysis or explanation
                                                - Do NOT repeat match evaluation
                                                - Only return the improved resume
                                                - Keep the content factual and derived from the original resume
                                                - Improve keyword alignment and clarity

                                                Resume:
                                                {resume_txt}
                                                
                                                Job Description:
                                                {job_description}
                                                """),
            }
        ],
        temperature=0.5
    )

    return response.choices[0].message.content

def compare_resumes(resume, job_description):

    client = openai.OpenAI()

    response = client.chat.completions.create(
        model="gpt-5.4",
        messages=[
            {
            "role" : "system" , "content" : (f"""You are a resume evaluator.
                                              Compare the resume provided with the job description provided and
                                              provide a score between 0 and 100
                                             
                                              Along with the match scores, provide
                                              1. Explanation of the match scores,
                                              2. Key strengths of the resume [list of 3-4 bullet points],
                                              3. Key areas for improvement [list of 3-4 bullet points]

                                             Resume:
                                             {resume}
                                             Job Description: 
                                             {job_description}
                                             
                                             Return output in a properly step by step format.
                                             """
                                             )
            }
        ],
        temperature=0.5
    )

    return response.choices[0].message.content

def dynamic_height(text):
    lines = text.count("\n") + 1
    return min(600, max(150, lines * 20))
