import streamlit as st
from langdetect import detect

# ----------------- Chatbot Brain ------------------
def get_response(user_input):
    try:
        lang = detect(user_input)
    except:
        lang = "en"

    q = user_input.lower()

    if "meet" in q or "kaise mile" in q or "first time" in q:
        ans = {
            "hi": "Hum pehli baar college ke fest mein mile the jab maine ladki ban ke Chikni Chameli pe dance kiya tha. Usne dekh ke impress ho ke mujhse baat ki aur agle din date pe chal diye! ❤️",
            "en": "We met for the first time at a college fest where I danced on Chikni Chameli dressed as a girl. She was impressed and came to talk, and we went on a date the very next day!",
        }
    elif "favourite" in q or "pasand" in q:
        ans = {
            "hi": "Use gana gaana, naye kapde pehnna aur tasty khana pasand hai. Strong ladke uski type hain 💪",
            "en": "She loves singing, wearing new clothes, and delicious food. And yes, she likes strong tall guys 💅",
        }
    elif "funny" in q or "mazaak" in q or "prank" in q:
        ans = {
            "hi": "Har milne pe hum jokes aur pranks karte hain. Taang kheenchna toh jaise routine hai! 😂",
            "en": "Every time we meet, it’s full of jokes and pranks. Pulling each other's legs is our love language! 😜",
        }
    elif "ex" in q or "kitne" in q:
        ans = {
            "hi": "Uske kaafi ex reh chuke hain... aur sabko kaat bhi chuki hai! 🐍",
            "en": "She had quite a few exes... and well, she’s broken a lot of hearts too! 💔",
        }
    elif "weird" in q or "habit" in q or "jeebh" in q:
        ans = {
            "hi": "Ham dono ek dusre ko jeebh dikhate hain jab milte hain. Weird but cute hai na? 😛",
            "en": "We both greet each other by showing our tongues. Weird but kinda cute, right? 😛",
        }
    elif "friend zone" in q or "ab kya" in q:
        ans = {
            "hi": "Abhi toh friend zone mein hoon... lekin pyaar toh ab bhi pura hai ❤️",
            "en": "Right now it's a friend-zone phase... but the love is still strong ❤️",
        }
    else:
        ans = {
            "hi": "Ye baat toh thodi personal hai... lekin tum pooch rahe ho toh chhupayenge kya? 😉",
            "en": "That’s a bit personal... but since you asked, I won’t hide it from you 😉",
        }

    return ans.get(lang, ans["en"])


# ----------------- Streamlit UI ------------------
st.set_page_config(page_title="OnePreeti Chatbot", page_icon="💖")
st.markdown("""
    <style>
    .main {
        background-color: #fff0f5;
        padding: 2rem;
        border-radius: 1rem;
        text-align: center;
    }
    .chatbox {
        border: 2px solid #ff69b4;
        border-radius: 10px;
        padding: 10px;
        background-color: #fff;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main'><h2>💬 Ask me anything about You</h2></div>", unsafe_allow_html=True)

user_input = st.text_input("Your Question:", placeholder="Type here in English, Hindi or Hinglish...")

if user_input:
    reply = get_response(user_input)
    st.markdown(f"<div class='chatbox'>{reply}</div>", unsafe_allow_html=True)

# ----------------- Exit Event ------------------
st.markdown("""
    <script>
    window.addEventListener('beforeunload', function (e) {
        alert("bye bye darling - TAKE CARE 💔");
    });
    </script>
""", unsafe_allow_html=True)
