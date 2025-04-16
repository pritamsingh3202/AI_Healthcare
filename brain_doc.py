# step 1: stepup GROQ API
from dotenv import load_dotenv
load_dotenv()


import os

GROQ_API_KEY= os.environ.get('GROQ_API_KEY')

# step 2: Covert image to required format

import base64


# img_path= "acne.webp"
def encode_img(img_path):
    img_file= open(img_path, "rb")
    return base64.b64encode(img_file.read()).decode('utf-8')


# step 3: Step Multimodel LLm

from groq import Groq

query="Is there something worong with my skin?"
model= "meta-llama/llama-4-maverick-17b-128e-instruct" 

def analyze_img_with_query(query, model, image):
    client = Groq()
   

    messages=[
        {
            "role": "user",
            "content":[
                {
                    "type": "text",
                    "text": query
                # }
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image}",
                    },
                },
            ],
        }
    ]

    chat_completion = client.chat.completions.create(
        messages= messages,
        model= model
    )
    return chat_completion.choices[0].message.content