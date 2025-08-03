import streamlit as st
import random
from questions import QUESTIONS

st.title("Encyclopedic Board Game - Streamlit Version")

if "posA" not in st.session_state:
    st.session_state.posA = 1
if "posB" not in st.session_state:
    st.session_state.posB = 1
if "turn" not in st.session_state:
    st.session_state.turn = "A"
if "message" not in st.session_state:
    st.session_state.message = "Player A, answer your question to start."

def next_turn():
    st.session_state.turn = "B" if st.session_state.turn == "A" else "A"
    st.session_state.message = f"Player {st.session_state.turn}, answer your
