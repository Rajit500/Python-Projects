
import streamlit as st
import time

st.title("Countdown Timer")

minutes = st.number_input("Enter minutes", min_value=0)  # st.text_input for string
seconds = st.number_input("Enter seconds", min_value=0, max_value=59)

if st.button("Start Timer"):
    total_seconds = int(minutes * 60 + seconds)

    timer_display = st.empty()  # Empty placeholder

    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)  # Divide for minute and modulus for second
        timer_display.title(f"{mins:02d}:{secs:02d}")
        time.sleep(1)
        total_seconds -= 1

    timer_display.title("Time's up!")

