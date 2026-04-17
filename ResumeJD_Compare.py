import os
import openai
from pathlib import Path

os.environ["OPENAI_API_KEY"] = "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"

def enhance_text(resume_txt, job_description):
    client = openai.OpenAI()

    combined_context = f"Job Description: {job_description}\n\nResume: {resume_txt}"

    response = client.chat.completions.create(
        model="gpt-5.4",
        messages=[
            {
                "role": "system", "content": ("You are a resume assistant. Rewrite users resume based on the job"
                                              "description provided by user. Ensure that the format is the same as the resume, "
                                              "tone is formal, and incorporate relevant ATS keywords.Only provide rewrite based on documents provided."
                                              "Do not reveal document information other than to user in output\n\n"),
                "role": "user", "content": f"Compare my {resume_txt} with the job description: {job_description} and provide a polished resume that has"
                                           "improved ATS match aligned with the job."
            }
        ],
        temperature=0.5
        # max_tokens=150
    )

    return response.choices[0].message.content
