# Anix AI - Risk Profiling Assistant with Branding

import streamlit as st

# Set Page Config
st.set_page_config(
    page_title="Anix AI - Risk Profiler",
    page_icon=":bar_chart:",
    layout="centered",
    initial_sidebar_state="auto",
)

# Optional: You can add your Anix AI Logo here
# Example if you upload logo.png in the same folder:
# st.image("anix_ai_logo.png", width=200)

# Title and Tagline
st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color:#00468C;">Anix AI</h1>
        <h3 style="color:#0072B5;">Client Risk Profiling Assistant</h3>
        <p style="color:gray;">Empowering Wealth Management with Intelligent Insights</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Risk Profiling Form
with st.form(key='risk_form'):
    st.subheader("📝 Please answer the following:")
    horizon = st.selectbox("What is your investment horizon?", ["1 year", "3 years", "5+ years"])
    loss_tolerance = st.selectbox("How much loss are you willing to tolerate in a year?", ["<5%", "5%-15%", ">15%"])
    experience = st.selectbox("What is your investment experience?", ["None", "Some", "Extensive"])
    goal = st.selectbox("What is your primary investment goal?", ["Capital Preservation", "Moderate Growth", "Aggressive Growth"])
    reaction = st.selectbox("How do you react to market downturns?", ["Panic", "Stay Calm", "Invest More"])
    
    submit_button = st.form_submit_button(label="🔎 Predict My Risk Profile")

# Prediction Logic
if submit_button:
    score = 0

    if horizon == "5+ years":
        score += 2
    elif horizon == "3 years":
        score += 1

    if loss_tolerance == ">15%":
        score += 2
    elif loss_tolerance == "5%-15%":
        score += 1

    if experience == "Extensive":
        score += 2
    elif experience == "Some":
        score += 1

    if goal == "Aggressive Growth":
        score += 2
    elif goal == "Moderate Growth":
        score += 1

    if reaction == "Invest More":
        score += 2
    elif reaction == "Stay Calm":
        score += 1

    if score >= 8:
        risk_profile = "Aggressive"
    elif 5 <= score < 8:
        risk_profile = "Balanced"
    else:
        risk_profile = "Conservative"

    # Output Result
    st.success(f"🎯 **Your Risk Profile: {risk_profile}**")

    if risk_profile == "Conservative":
        st.info("You prefer safety and low volatility. Ideal for capital protection strategies.")
    elif risk_profile == "Balanced":
        st.info("You prefer moderate growth with reasonable capital protection.")
    else:
        st.info("You seek high long-term growth and accept higher volatility.")

# Footer
st.markdown(
    """
    <hr style="border:1px solid #d3d3d3;">
    <div style="text-align: center;">
        <small style="color:gray;">© 2025 Anix AI | Powered by Streamlit</small>
    </div>
    """,
    unsafe_allow_html=True
)
