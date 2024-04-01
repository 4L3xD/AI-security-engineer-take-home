import google.generativeai as genai
from env import GOOGLE_API_KEY

class Gemini():
    def __init__(self):
        genai.configure(api_key=GOOGLE_API_KEY)

    def nlp(self, user_msg):
        user_msg = user_msg
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(m.name)

        model = genai.GenerativeModel('gemini-pro')
        #response = model.generate_content("What is the meaning of life?")
        #print(response.text)
        response = model.generate_content(user_msg)

        # Speech Analysis
        # print(response.prompt_feedback)
        return response.text