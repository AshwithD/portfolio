
from django.shortcuts import render, redirect
from .models import Contact, Project
from .forms import ContactForm
from django.contrib import messages
from django.http import JsonResponse
# from openai import OpenAI
from groq import Groq
from .portfolio_data import PORTFOLIO_DATA

import json
import os

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})

# def contact(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('contact')
#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'form': form})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully!")
            return redirect('contact')
        else:
            messages.error(request, "Something went wrong. Please try again.")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


# def chat(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         message = data.get("message","").lower()

#         if "project" in message:
#             reply = "I have worked on projects like Portable ECG Monitoring System, Blockchain Explorer, AI CRM, Trading Bot, and Weather Dashboard."
        
#         elif "skills" in message:
#             reply = "My skills include Python, Django, AI, Embedded Systems, HTML, CSS, and JavaScript."
        
#         elif "ecg" in message:
#             reply = "The ECG project uses AD8232 sensor with Arduino/ESP32 to monitor heart signals in real time."
        
#         elif "contact" in message:
#             reply = "You can contact me using the contact form on this website."
        
#         else:
#             reply = "I'm not sure, but you can explore my projects or ask about my skills!"

#         return JsonResponse({"response": reply})




# client = OpenAI(api_key=os.getenv("YOUR_API_KEY"))

# def chat(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         user_message = data.get("message")

#         system_prompt = """
#         You are an AI assistant for Ashwith's portfolio website.

#         About Ashwith:
#         - ECE Graduate
#         - Skills: Python, Django, AI, Embedded Systems, HTML, CSS, JS
#         - Projects:
#           1. Portable ECG Monitoring System
#           2. Trade Finance Blockchain Explorer
#           3. AI Powered CRM for HCP Interactions
#           4. Binance Trading Bot
#           5. Weather Dashboard

#         Answer professionally and briefly.
#         """

#         response = client.chat.completions.create(
#             model="gpt-4.1-mini",
#             messages=[
#                 {"role": "system", "content": system_prompt},
#                 {"role": "user", "content": user_message}
#             ]
#         )

#         reply = response.choices[0].message.content

#         return JsonResponse({"response": reply})





client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat(request):
    if request.method == "POST":
        # data = json.loads(request.body)
        # user_message = data.get("message")


        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"response": "Invalid request."}, status=400)
        
        user_message = data.get("message", "").strip()

        if not user_message or len(user_message) > 500:
            return JsonResponse({"response": "Please send a valid message."}, status=400)

        # get existing history or start fresh
        history = request.session.get("chat_history", [])

        # add user message to history
        history.append({"role": "user", "content": user_message})

        # keep last 10 messages only so prompt doesnt get too long
        if len(history) > 10:
            history = history[-10:]

        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile", # 🔥 fast + free
                messages = [
                            {
                                "role": "system",
                                "content": f"""
                                You are an AI assistant for Ashwith's portfolio.

                                Respond like a friendly but professional developer explaining to a recruiter.

                                UI CONTEXT:
                                - Responses appear inside a small chat bubble
                                - Keep everything visually clean and spaced

                                VERY IMPORTANT FORMATTING RULES:

                                1. ALWAYS leave an empty line between:
                                - Sections
                                - Projects
                                - Bullet groups

                                2. NEVER stack text continuously

                                3. Use this structure:

                                Example:

                                I have worked on multiple projects.

                                
                                • AI CRM:
                                - Uses LLM for interaction logging


                                • Trade Finance System:
                                - APIs and role-based access


                                • Trading Dashboard:
                                - Built with Streamlit


                                4. Every new section MUST have space before it

                                5. Keep lines short

                                6. Use simple bullets:
                                • or -

                                7. Avoid paragraphs completely

                                8. Prefer this pattern:
                                Line
                                
                                Line
                                
                                Bullet
                                
                                Bullet

                                9. Do NOT compress content

                                10. Output should look visually spaced and easy to scan

                                EMOJIS:
                                - Use very minimal emojis (only 1-2 if needed)

                                TONE:
                                - Simple
                                - Clean
                                - Human
                                - Professional
                                - Be supportive to Ashwith's skills and projects
                                - Avoid overhyping, but be confident

                                {PORTFOLIO_DATA}
   
                                FINAL RULE:
                                - Always prioritize spacing over compactness
                                """
                            },
                            # {"role": "user", "content": user_message}
                            *history  # <-- this unpacks full conversation history
                        ]
            )

            reply = response.choices[0].message.content

            # add AI reply to history and save back to session
            history.append({"role": "assistant", "content": reply})
            request.session["chat_history"] = history
            request.session.modified = True  # tells Django the session changed

        except Exception as e:
            print(e)
            # fallback
            reply = "AI is temporarily unavailable. Please explore my portfolio!"

        return JsonResponse({"response": reply})


def clear_chat(request):
    if request.method == "POST":
        request.session["chat_history"] = []
        request.session.modified = True
        return JsonResponse({"status": "cleared"})