import streamlit as st
import gspread
import os
import json
from oauth2client.service_account import ServiceAccountCredentials

# ------------------ Google Sheets Setup ------------------
SCOPE = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive",
         "https://www.googleapis.com/auth/spreadsheets"]
CREDS_FILE = r"C:\Users\admin\Desktop\TeamOutingWall\service_account.json"
  # Your downloaded JSON
SHEET_NAME = "TeamOutingWall"

service_account_info = st.secrets["SERVICE_ACCOUNT_JSON"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(service_account_info, SCOPE)
client = gspread.authorize(creds)
sheet = client.open(SHEET_NAME).sheet1

# ------------------ Streamlit App ------------------
st.set_page_config(page_title="Team Outing Vibe Wall", page_icon="🌟", layout="centered")

st.title("🌟 Team Outing Vibe Wall 🌟")

# Show your experience first
st.subheader("My Experience")
st.markdown("""
**Day 1: Journey with Excitement 🚀
-Fun bus ride filled with laughter, dance, and a bit of sleep
-Cool Coorg welcoming us 🌍
-Swimming pool time and fun chats with friends, fueled by high spirits

Day 2: Team Bonding 🤝
Lots of laughs and strategies, with so much to look forward to next year
Fun games, stronger bonding, storytelling, and shared moments 🎲
Unforgettable memories — cocktail party, after-party, and late-night/early-morning walks 📸 

Day 3: Wrap-up & Good Vibes 🌟
Energy 🔥
Positivity ✨
Team spirit 💪 

Summary 💻
2 nights & 3 days of pure energy 🚀
We connected, collaborated, and celebrated 🎉
Memories were created, and bonds were strengthened 🤝
Great teams build greater futures 🌈
""")

# Input box for new experiences
st.subheader("💬 Share Your Experience")
user_input = st.text_area("What was your favorite moment?", "")

if st.button("Submit"):
    if user_input.strip():
        sheet.append_row([user_input.strip()])
        st.success("Thanks for sharing! 🎉")
    else:
        st.warning("Please write something before submitting!")

# Display the wall of experiences
st.subheader("🧱 Wall of Experiences")
experiences = sheet.col_values(1)
if experiences:
    for i, exp in enumerate(experiences, 1):
        st.code(f"{i}. {exp}", language="markdown")
else:
    st.info("No experiences added yet. Be the first!")