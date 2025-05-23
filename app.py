# Anix AI - Risk Profiling Assistant with Real ML Model

import streamlit as st
import pickle

# Set Page Config
st.set_page_config(
    page_title="Anix AI - Risk Profiler",
    page_icon=":bar_chart:",
    layout="centered",
)

# Load the model and encoders


with open('risk_model_logistic.pkl', 'rb') as file:
    model, label_encoders = pickle.load(file)

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
    # Encode user input
    user_input = {
        "Horizon": horizon,
        "Loss_Tolerance": loss_tolerance,
        "Experience": experience,
        "Goal": goal,
        "Reaction": reaction
    }

    input_encoded = []
    for feature, value in user_input.items():
        encoder = label_encoders[feature]
        encoded_value = encoder.transform([value])[0]
        input_encoded.append(encoded_value)

    # Predict risk category
    prediction = model.predict([input_encoded])[0]
    risk_label = label_encoders["Risk_Category"].inverse_transform([prediction])[0]

    # Output
    st.success(f"🎯 **Your Predicted Risk Profile: {risk_label}**")

    if risk_label == "Conservative":
        st.info("You prefer safety and low volatility. Ideal for capital protection strategies.")
    elif risk_label == "Balanced":
        st.info("You prefer moderate growth with reasonable capital protection.")
    else:
        st.info("You are willing to accept higher volatility for potentially higher long-term returns.")

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
