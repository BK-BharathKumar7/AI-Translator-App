import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="AI Translator App",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 AI-Powered Translator")
st.write("Translate text between multiple languages.")

languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese (Simplified)": "zh-CN"
}

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target_lang = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

text = st.text_area(
    "Enter text to translate",
    height=150,
    placeholder="Type something here..."
)

st.caption(f"Character Count: {len(text)}")

if st.button("Translate"):

    if not text.strip():
        st.warning("Please enter some text.")
    
    elif source_lang == target_lang:
        st.warning("Source and target languages must be different.")
    
    else:
        try:
            with st.spinner("Translating..."):

                translated_text = GoogleTranslator(
                    source=languages[source_lang],
                    target=languages[target_lang]
                ).translate(text)

            st.subheader("Translated Text")
            st.success(translated_text)

            st.download_button(
                label="Download Translation",
                data=translated_text,
                file_name="translated_text.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(
                "Translation service is currently unavailable. "
                "Please try again."
            )
