import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translator", page_icon="🌐")

st.title("🌐 Language Translation Tool")

text = st.text_area("Enter text to translate")

source = st.selectbox(
    "Source Language",
    ["auto", "english", "hindi", "telugu", "tamil"]
)

target = st.selectbox(
    "Target Language",
    ["english", "hindi", "telugu", "tamil"]
)

if st.button("Translate"):
    if text:
        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        st.subheader("Translated Text")
        st.success(translated)
    else:
        st.warning("Please enter some text.")