import streamlit as st
import google.generativeai as genai
from langdetect import detect

# Gemini API Key (replace with your actual key)
API_KEY = "AIzaSyCsS1F2Sb7RDm-9pnf5FzDfKChG1r4woZc"
genai.configure(api_key=API_KEY)

# Personal filmy story & facts as context
context_prompt = """
You are a friendly, filmy, romantic and funny chatbot who knows everything about Aaryan and Preeti.
Here's what you know:

- They met during a college fest. Aaryan danced dressed as a girl on 'Chikni Chameli'. Preeti was impressed and started talking to him. They went on a date the very next day, 31st March, to Pal Gaon for go-karting.
- Preeti loves singing, food, fashion, and strong tall guys. She’s independent and lives life on her terms.
- Aaryan and Preeti used to talk every night for 2 months. Now they are in the friend-zone.
- Funny things: Aaryan always cracks jokes when they meet. He loves teasing her.
- Inside jokes: Preeti sleeps without a bra and has had several exes. She’s broken many hearts.
- Weird habits: They greet each other by showing their tongues 😜

Always reply in a friendly, playful, flirty and emotional tone. Answer in Hindi, Hinglish, or English based on the question's language. If the user exits, say "Bye bye darling – TAKE CARE ❤️"
"""

# Load Gemini model
model = genai.GenerativeModel(model_name="models/gemini-pro")
chat = model.start_chat(history=[])

st.set_page_config(page_title="Ask About Us 💖", layout="centered")
st.title("Chatbot")
st.markdown("<h4 style='text-align: center;'>Ask me anything about You 😉</h4>", unsafe_allow_html=True)

# Chat loop
user_input = st.text_input("You:", placeholder="Type your question about Aaryan & Preeti...", key="input")

if user_input:
    lang = detect(user_input)
    prompt = context_prompt + f"\nUser asked in {lang}: {user_input}"

    with st.spinner("Thinking..."):
        response = chat.send_message(prompt)
        st.markdown(f"<div style='background-color:#f7f7f7;padding:10px;border-radius:10px;margin-top:10px;'>🤖 <b>Bot:</b> {response.text}</div>", unsafe_allow_html=True)

# Exit message
if st.button("🚪 Exit Chat"):
    st.markdown("<h3 style='text-align:center;color:#ff4b4b;'>Bye bye darling – TAKE CARE ❤️</h3>", unsafe_allow_html=True)
