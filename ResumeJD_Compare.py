import os
import openai
from pathlib import Path

os.environ["OPENAI_API_KEY"] = "[Your Key]"


def enhance_text(resume_txt, job_description):
    client = openai.OpenAI()

    combined_context = f"Job Description: {job_description}\n\nResume: {resume_txt}"

    response = client.chat.completions.create(
        model="gpt-5.4",
        messages=[
            {
                "role": "user", "content": ("You are a resume assistant. Provide a polished resume based on the job "
                                            "description provided below. Ensure that the format is the same as the resume, "
                                            "tone is formal, and incorporate relevant ATS keywords. "
                                            "Ask at the end if the user wants a PDF version.\n\n" + combined_context)
            }
        ],
        temperature=0.5
        # max_tokens=150
    )

    return response.choices[0].message.content
