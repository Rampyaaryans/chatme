import streamlit as st
import requests
from langdetect import detect

# DeepSeek API Setup
API_KEY = "sk-2f463da5a21d4e4c9f3b6b029f31136e"
API_URL = "https://api.deepseek.com/v1/chat/completions"

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

st.set_page_config(page_title="Ask About Us 💖", layout="centered")
st.title("💌 OnePreeti Chatbot")
st.markdown("<h4 style='text-align: center;'>Ask me anything about You 😉</h4>", unsafe_allow_html=True)

# Chat loop
user_input = st.text_input("You:", placeholder="Type your question about Aaryan & Preeti...", key="input")

if user_input:
    lang = detect(user_input)
    full_prompt = context_prompt + f"\nUser asked in {lang}: {user_input}"

    with st.spinner("Thinking..."):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        data = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": context_prompt},
                {"role": "user", "content": user_input}
            ]
        }

        response = requests.post(API_URL, headers=headers, json=data)

        if response.status_code == 200:
            output = response.json()['choices'][0]['message']['content']
            st.markdown(f"<div style='background-color:#f7f7f7;padding:10px;border-radius:10px;margin-top:10px;'>🤖 <b>Bot:</b> {output}</div>", unsafe_allow_html=True)
        else:
            st.error("Something went wrong. Please try again later.")

# Exit message
if st.button("🚪 Exit Chat"):
    st.markdown("<h3 style='text-align:center;color:#ff4b4b;'>Bye bye darling – TAKE CARE ❤️</h3>", unsafe_allow_html=True)
