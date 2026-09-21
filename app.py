import streamlit as st
import pandas as pd
import re

st.set_page_config(page_title="AIMDP InboxAgent - نور القرآن", layout="wide", page_icon="📧")

# --- LOGO SECTION ---
# Upload your image to GitHub as logo.jpg
st.image("logo.jpg", use_container_width=True) 
st.markdown("<h3 style='text-align:center; color:#4B2BB7'>نور القرآن - صباحكم معطر بذكر الله</h3>", unsafe_allow_html=True)

st.markdown("# 📧 AIMDP Solutions - InboxAgent")
st.markdown("### AI Triages Your Inbox in Seconds • Powered by نور القرآن")

# ... rest of your InboxAgent code from before ...
SAMPLE_EMAILS = [
    {"from":"customer@urgent.com","subject":"URGENT - Shipment stuck","body":"Need update NOW, client angry. MSKU123456","time":"2 min ago"},
    {"from":"john@bigclient.com","subject":"Quote request 800kg to LAX","body":"Need quote 800kg electronics MIA→LAX","time":"1h ago"},
    {"from":"accounting@client.com","subject":"Invoice #1023 overdue $4,500","body":"Payment overdue 15 days","time":"3h ago"},
    {"from":"vendor@rates.com","subject":"New rates October - PDF","body":"Updated rates MIA-JFK","time":"15 min ago"},
    {"from":"noreply@newsletter.com","subject":"Newsletter","body":"Newsletter content","time":"1h ago"},
]

if st.button("🤖 Run InboxAgent - Triage Inbox", type="primary", use_container_width=True):
    for email in SAMPLE_EMAILS:
        body = (email['subject'] + " " + email['body']).lower()
        if "urgent" in body: label = "🔴 URGENT"
        elif "quote" in body: label = "💰 QUOTE"
        elif "invoice" in body: label = "💳 COLLECTION"
        elif "rates" in body: label = "📊 RATE UPDATE"
        else: label = "📰 LOW"
        
        with st.expander(f"{label} - {email['subject']} - {email['from']}"):
            st.write(email['body'])
            st.text_area("AI Draft Reply:", value=f"Reply for {label} - Salam, will update soon...", key=email['subject'])

st.divider()
st.link_button("Get InboxAgent → pinedad@gmail.com", "mailto:pinedad@gmail.com", use_container_width=True)
