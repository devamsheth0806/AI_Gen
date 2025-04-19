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

if st.button("Get Recommendations"):
    with st.spinner("Sending to backend..."):
        payload = {
            "identifier_from_purchaser": "streamlit_user_001",  # can be dynamic
            "input_data": {"text": user_input}
        }

        try:
            response = requests.post(f"{BACKEND_URL}/start_job", json=payload)
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            st.error(f"❌ Backend Error: {e}")
            st.stop()

        # Step 2: Display Recommendation Summary
        st.success("✅ Recommendations Received!")
        st.markdown("### 🔎 Agent Summary")
        st.write(data.get("summary", "No summary provided."))

        # Step 3: Show Top 3 Options as Radio Buttons
        options = data.get("recommended_options", [])
        if not options:
            st.warning("No options received from backend.")
            st.stop()

        option_strings = [f"{opt['label']}: {opt['description']} (${opt['price']}/month)" for opt in options]
        selected = st.radio("Choose your preferred deployment option:", option_strings)

        # Step 4: Confirm Button → Redirect to Payment
        if st.button("💳 Proceed to Payment"):
            selected_index = option_strings.index(selected)
            selected_option = options[selected_index]

            payment_url = selected_option.get("payment_url") or data.get("payment_url")
            if not payment_url:
                st.error("Payment URL not found.")
            else:
                st.success("✅ Redirecting to Masumi Payment Page...")
                st.markdown(f"👉 [Click here to pay]({payment_url})", unsafe_allow_html=True)
