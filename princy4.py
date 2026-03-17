import streamlit as st
import streamlit.components.v1 as components

# Page setup
st.set_page_config(page_title="Happy Birthday Sister 🎉", layout="centered")

# Session control
if "page" not in st.session_state:
    st.session_state.page = 1

# ---------- PAGE 1 ----------
if st.session_state.page == 1:

    st.markdown("<h1 style='text-align: center;'>🎂 Happy Birthday Dear Sister 💖</h1>", unsafe_allow_html=True)

    st.markdown("""
    ### 💌 Birthday Wishes
    Dear Sister,  
    Tu meri life da sab ton special hissa ae ❤️  
    Rabb kare tera har din khushi naal bhareya hove 😊  
    Tu hamesha hassdi reh te success paandi reh ✨  
    """)

    st.write("")

    if st.button("Open Your Surprise 🎁"):
        st.balloons()
        st.session_state.page = 2


# ---------- PAGE 2 ----------
elif st.session_state.page == 2:

    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    body {
        display: flex;
        flex-direction: column;
        align-items: center;
        background: #fce4ec;
        padding: 20px;
    }

    .book {
        width: 600px;
        height: 400px;
        position: relative;
        perspective: 1500px;
    }

    .page {
        position: absolute;
        width: 100%;
        height: 100%;
        display: flex;
    }

    /* Single Page */
    .single {
        justify-content: center;
        align-items: center;
        background: white;
        border-radius: 10px;
        padding: 20px;
        transform-origin: left;
        transition: transform 1s;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }

    /* Double Page */
    .double {
        background: white;
        border-radius: 10px;
        overflow: hidden;
        transform-origin: left;
        transition: transform 1s;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }

    .left, .right {
        width: 50%;
        padding: 20px;
    }

    .left {
        border-right: 2px solid #ddd;
    }

    .flipped {
        transform: rotateY(-180deg);
    }

    button {
        margin-top: 20px;
        padding: 12px 25px;
        border: none;
        background: #ff6f91;
        color: white;
        border-radius:
