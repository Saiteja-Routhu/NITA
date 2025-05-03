import google.generativeai as genai

genai.configure(api_key="AIzaSyA4QfQvdkN4EdxSZW-UjHnlWAvVCVzSKMs")

models = genai.list_models()
for m in models:
    print(m.name)
