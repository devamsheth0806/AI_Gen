import streamlit as st
import requests
import json

# Replace with your actual backend URL (local or deployed)
BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="Deployment Advisor", layout="centered")
st.title("🚀 AI Deployment Advisor with Masumi Payment")

# Step 1: Text Input
user_input = st.text_area("📝 Describe your deployment requirements:", 
                          placeholder="E.g. I want a low-cost scalable app under $50/month in US East.")

if "recommendations" not in st.session_state:
    st.session_state.recommendations = None
    st.session_state.summary = ""
    st.session_state.payment_url = ""
    st.session_state.options_dict = {}


if st.button("Get Recommendations"):
    with st.spinner("Sending to backend..."):
        payload = {
            "requirements": user_input
        }

        try:
            response = requests.post(f"{BACKEND_URL}/analyze", json=payload)
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            st.error(f"❌ Backend Error: {e}")
            st.stop()

        st.session_state.summary = data.get("summary", "")
        st.session_state.recommendations = json.loads(data.get("recommendations", "{}"))
        st.session_state.payment_url = data.get("payment_url", "")
        st.session_state.options_dict = st.session_state.recommendations

if st.session_state.recommendations:
    # Step 2: Display Recommendation Summary
    st.success("✅ Recommendations Received!")
    
    st.subheader("🔎 Agent Summary")
    st.write(st.session_state.summary)

    st.subheader("💡 Recommended Options")
    
    option_strings = [
        f"{key}: {val['description']} (${val['monthly_cost']}/month)"
        for key, val in st.session_state.options_dict.items()
    ]
    selected_option_string = st.radio("Choose your preferred deployment option:",
                                      options=option_strings,
                                      key="selected_option")
    
    # Step 4: Confirm Button → Redirect to Payment
    if st.button("💳 Proceed to Payment"):
        # Find selected key (e.g., A, B, C)
        selected_key = selected_option_string.split(":")[0]

        payment_url = f"{BACKEND_URL}/deploy"
        payload = {'select_option': selected_key}
        try:
            response = requests.post(payment_url, json=payload)
            st.success("Deployement Successful...")
        except Exception as e:
            st.exception('Unable to pay')
