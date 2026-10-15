import random
import streamlit as st

st.set_page_config(
    page_title="A Little Appreciation",
    page_icon="💛",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      .stApp {
        background: radial-gradient(circle at top left, #25304a 0, #111827 42%, #0b1020 100%);
        color: #f8fafc;
      }
      .block-container { max-width: 1050px; padding-top: 2.5rem; padding-bottom: 3rem; }
      .hero {
        padding: 2.4rem 2rem; border-radius: 26px;
        background: linear-gradient(135deg, rgba(245, 190, 95, .18), rgba(255,255,255,.04));
        border: 1px solid rgba(245, 190, 95, .35);
        text-align: center; margin-bottom: 1.5rem;
      }
      .eyebrow { text-transform: uppercase; letter-spacing: .22em; color: #f6ca7a; font-size: .78rem; }
      .hero h1 { color: #fff7e6; font-size: clamp(2rem, 5vw, 3.6rem); margin: .6rem 0; }
      .hero p { color: #dbe3f0; font-size: 1.1rem; }
      .panel {
        background: rgba(255,255,255,.055); border: 1px solid rgba(255,255,255,.11);
        padding: 1.35rem; border-radius: 20px; min-height: 190px;
      }
      .panel h3 { color: #f6ca7a; }
      .quote {
        font-size: 1.25rem; line-height: 1.65; color: #fff7e6;
        background: rgba(246,202,122,.09); border-left: 4px solid #f6ca7a;
        border-radius: 12px; padding: 1.2rem 1.4rem; margin: .8rem 0 1.2rem;
      }
      .footer { color: #aab5c8; text-align: center; margin-top: 2.5rem; font-size: .9rem; }
      div.stButton > button {
        background: linear-gradient(90deg, #f6ca7a, #f0a94a); color: #1b2232;
        border: 0; border-radius: 12px; font-weight: 700; padding: .65rem 1rem;
      }
      div.stButton > button:hover { border: 1px solid #fff0cc; color: #111827; }
      label, .stTextInput label, .stTextArea label { color: #e5eaf3 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

APPRECIATION_MESSAGES = [
    "You make family feel a little more like a team. That matters more than you know. 💛",
    "Thanks for showing up, bringing good energy, and being someone people can count on.",
    "You deserve appreciation for the big things you do—and the small things people might miss.",
    "A great brother-in-law is part family, part friend, and occasionally part unpaid comedian. 😄",
    "Life gave our family one more good person when it brought you into it. We're lucky to have you.",
    "Behind every strong family is someone who helps make the moments better. Thank you for being you.",
]

FUNNY_LINES = [
    "Brother-in-law status: officially family, permanently roastable. 😂",
    "Thanks for being an awesome brother-in-law. Please accept this digital award; the trophy budget was denied.",
    "You're not just a brother-in-law. You're family—with lifetime membership and absolutely no cancellation policy.",
    "A little appreciation today, because roasting you every other day is apparently not enough.",
    "You're a top-tier brother-in-law. Don't let this compliment go to your head.",
]

st.markdown(
    """
    <div class="hero">
      <div class="eyebrow">A small project with a big heart</div>
      <h1>For Someone Who Makes Family Better 💛</h1>
      <p>A little appreciation, a few laughs, and a reminder that you're valued.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("Personalize the page")
    name = st.text_input("His name or nickname", value="My Awesome Brother-in-Law")
    your_name = st.text_input("From", value="Your favorite in-law 😄")
    relationship_detail = st.text_input(
        "One thing you appreciate about him",
        value="the way you show up for family",
    )
    custom_memory = st.text_area(
        "A favorite memory (optional)",
        placeholder="Write a funny or meaningful memory here...",
    )

st.markdown(
    f"""
    <div class="hero">
      <div class="eyebrow">This one's for you</div>
      <h1>{name.strip() or "My Awesome Brother-in-Law"}</h1>
      <p>Not every hero wears a cape. Some just become part of the family.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns(2, gap="large")
with left:
    st.markdown(
        f"""
        <div class="panel">
          <h3>🌟 Why you're appreciated</h3>
          <p>Thank you for {relationship_detail.strip() or "being you"}.</p>
          <p>Family isn't only about being related. It's about kindness, trust, laughter,
          and the people who make ordinary days feel special.</p>
          <p><b>Today, this little corner of the internet is all about you.</b></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with right:
    st.markdown(
        """
        <div class="panel">
          <h3>🏆 Official brother-in-law award</h3>
          <p><b>Category:</b> Legendary family member</p>
          <p><b>Special skills:</b> Being there, bringing laughs, and making family stronger</p>
          <p><b>Renewal:</b> Automatic, for life</p>
          <p><b>Fine print:</b> Light roasting may continue indefinitely.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")
st.subheader("💌 A message for you")
st.markdown(
    '<div class="quote">You may hear jokes and get roasted, but underneath all of that is genuine love and respect. Thank you for being part of our family and making it better just by being yourself.</div>',
    unsafe_allow_html=True,
)
if st.button("✨ Give me another appreciation message"):
    st.session_state["appreciation"] = random.choice(APPRECIATION_MESSAGES)
st.markdown(
    f'<div class="quote">{st.session_state.get("appreciation", APPRECIATION_MESSAGES[0])}</div>',
    unsafe_allow_html=True,
)

col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.subheader("😂 The official roast corner")
    if st.button("Tell me a brother-in-law joke"):
        st.session_state["funny"] = random.choice(FUNNY_LINES)
    st.info(st.session_state.get("funny", "Click the button for a loving roast. The respect is real; the sarcasm is complimentary."))
with col2:
    st.subheader("📸 A memory to keep")
    if custom_memory.strip():
        st.markdown(f'<div class="quote">{custom_memory.strip()}</div>', unsafe_allow_html=True)
    else:
        st.markdown(
            '<div class="panel">Add a favorite memory in the sidebar to make this page more personal. A tiny detail can mean more than a thousand generic words.</div>',
            unsafe_allow_html=True,
        )

st.markdown(
    f'<div class="footer">Made with ❤️ and a little sarcasm by {your_name.strip() or "Your favorite in-law"}<br/>A small reminder: you are loved, valued, and appreciated.</div>',
    unsafe_allow_html=True,
)
