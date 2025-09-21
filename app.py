import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# ------------------ Google Sheets Setup ------------------
SCOPE = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]
CREDS_FILE = r"C:\Users\admin\Desktop\TeamOutingWall\service_account.json"
  # Your downloaded JSON
SHEET_NAME = "TeamOutingWall"

creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, SCOPE)
client = gspread.authorize(creds)
sheet = client.open(SHEET_NAME).sheet1

# ------------------ Streamlit App ------------------
st.set_page_config(page_title="Team Outing Vibe Wall", page_icon="🌟", layout="centered")

st.title("🌟 Team Outing Experience Wall 🌟")

# Show your experience first
st.subheader("My Experience")
st.markdown("""
**Day 1: Kick-off 🚀**  
- Brainstorming 💡  
- Vision Sharing 🌍  
- Future Roadmaps 📊  

**Day 2: Team Bonding 🤝**  
- Laughs 😂  
- Fun Games 🎲  
- Unforgettable Memories 📸  

**Day 3: Wrap-up & Good Vibes 🌟**  
- Energy 🔥  
- Positivity ✨  
- Team Spirit 💪  

**Summary 💻**  
2 Nights & 3 Days of pure energy 🚀  
We connected, collaborated, and celebrated 🎉  
Memories created, bonds strengthened 🤝  
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