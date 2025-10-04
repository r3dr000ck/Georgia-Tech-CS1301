import streamlit as st

st.title("Japan Trivia Quiz")
st.write("Welcome to Japanese quiz! Let's see how much you know about Japan 🇯🇵!")
st.image("Images/tokyo.jpg", width=450)

if "score" not in st.session_state: #NEW
    st.session_state.score = 0
if "answered" not in st.session_state: #NEW
    st.session_state.answered = set()

def submit(q, check, ans):
    if check:
        st.success("Correct🎉") #NEW
        st.session_state.score += 1
    else:
        st.error(f"Incorrect. Correct answer: {ans}") #NEW

    st.session_state.answered.add(q)

st.divider()

ttl = 5
answered = len(st.session_state.answered)
progress = st.progress(answered / ttl, text=f"Progress: {answered} / {ttl}") #NEW
st.metric("Your Score", st.session_state.score) #NEW

st.subheader("Question 1")
q1 = st.radio(
    "What is the capital of Japan?",
    ["Tokyo", "Osaka", "Kyoto", "Paris"],
    index=None
) #NEW
st.button("Submit", key="q1_submit", disabled=("q1" in st.session_state.answered), on_click=lambda: submit("q1", q1 == "Tokyo", "Tokyo")) #NEW

st.subheader("Question 2")
st.image("Images/cur.jpg", width=250)
q2 = st.selectbox(
    "What is the currency of Japan?",
    ["Euro", "Pound", "Peso", "Yen", "Rupee"],
    index=None
) #NEW
st.button("Submit", key="q2_submit", disabled=("q2" in st.session_state.answered), on_click=lambda: submit("q2", q2 == "Yen", "Yen"))

st.subheader("Question 3")
st.image("Images/yakitori.jpeg", width=250)
q3 = st.text_input(
    "What is this food called in Japanese?",
    max_chars=30,
    placeholder="Type your answer here"
) #NEW
st.button("Submit", key="q3_submit", disabled=("q3" in st.session_state.answered), on_click=lambda: submit("q3", q3.lower() == "yakitori", "Yakitori"))

st.subheader("Question 4")
q4 = st.slider(
    "How many prefectures are there in Japan?",
    min_value=1,
    max_value=100,
    value=1 
) #NEW
st.button("Submit", key="q4_submit", disabled=("q4" in st.session_state.answered), on_click=lambda: submit("q4", q4 == 47, "47"))

st.subheader("Question 5")
q5 = st.number_input(
    "What is Japan's international dialing code?",
    min_value=1,
    max_value=999,
    step=1
) #NEW
st.button("Submit", key="q5_submit", disabled=("q5" in st.session_state.answered), on_click=lambda: submit("q5", int(q5) == 81, "81"))

if answered == ttl:
    if st.session_state.score == ttl:
        st.balloons() #NEW
        st.success("Perfect score! Are you Japanese? 🇯🇵")
        st.image("Images/congrats.jpg", width=300)
    elif st.session_state.score >= 4:
        st.success("Awesome! 🎉")
    else:
        st.info("You need to watch more anime! 😊") #NEW