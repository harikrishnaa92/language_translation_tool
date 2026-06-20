import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌐 Multi-Language Translator")
st.write("Created by HARIKRISHNA KS")

text = st.text_area("Enter Text")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Tamil": "ta",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de"
}

source = st.selectbox("Source Language", list(languages.keys()))
target = st.selectbox("Target Language", list(languages.keys()))

if st.button("Translate"):
    try:
        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success("Translation Successful ✅")
        st.write(translated)

    except Exception as e:
        st.error(f"Error: {e}")