import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Script Generator", page_icon="🧠")
st.title("🧠 AI YouTube Script Generator")
st.write("Topic dein, aur AI se YouTube script paayein! 💡")

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
topic = st.text_input("🎯 Topic daalein (e.g., 'Mutual Funds kya hote hain?')")

if st.button("✍️ Generate Script"):
    if not topic:
        st.warning("⚠️ Kripya topic daalein!")
    else:
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(topic)
            st.success("✅ Script Ready:")
            st.write(response.text)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
