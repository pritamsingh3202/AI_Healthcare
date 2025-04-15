# step 1: stepup GROQ API

import os

GROQ_API_KEY= os.environ.get('GROQ_API_KEY')

# step 2: Covert image to required format

import base64
img_path= "acne.webp"
img_file= open(img_path, "rb")
encoded_img= base64.b64encode(img_file.read()).decode('utf-8')

# step 3: Step Multimodel LLm

from groq import Groq

client = Groq()
query="Is there something worong with my skin?"
model= "llama3-70b-8192" 

messages=[
    {
        "role": "user",
        "content":[
            {
                "type": "text",
                "text": query
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{encoded_img}",
                },
            },
        ],
    }
]

chat_completion = client.chat.completions.create(
    messages= messages,
    model= model
)

print(chat_completion.choices[0].message.content)