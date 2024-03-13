import google.generativeai as genai

gemini_api_key = "AIzaSyD-WjWHmj8N507xKckF_wYsKQ5nJR4UsA0"
genai.configure(api_key = gemini_api_key)


def f(disease):
    model = genai.GenerativeModel('gemini-pro')
    prompt = "5 best potato " + disease + r"control measures (dont use bold text), return as a json array, dont use \n"
    response = model.generate_content(prompt)
    return response.text

print(f("early blight"))
