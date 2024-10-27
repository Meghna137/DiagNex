import streamlit as st
import requests
from PIL import Image
import io

# Hugging Face API token and endpoints
api_token = "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"  # Replace with your actual token
headers = {"Authorization": f"Bearer {api_token}"}

# Endpoints for the models
biobert_endpoint = "https://api-inference.huggingface.co/models/dmis-lab/biobert-large-cased-v1.1-squad"
gpt_endpoint = "https://api-inference.huggingface.co/models/openai-community/gpt2"  # Use your desired GPT model endpoint

# Streamlit UI
st.markdown("<h1 style='text-align: center;padding: 0px,0px,20px'>DiagNex</h1>", unsafe_allow_html=True)

# Input fields
patient_history = st.text_area("Enter Patient's Medical History:")
patient_age = st.number_input("Enter age", step=1, format="%d")
patient_symptoms = st.text_area("Enter the current symptoms")
gender = st.radio("Gender", options=["Male", "Female"], index=0)

patient_details=str(patient_age)+" year old "+gender+"  with a history of "+patient_history+ "with symptoms like "+patient_symptoms


# Extract Medical Info Function
def extract_medical_info(text):
    payload = {
        "inputs": {
            "question": "What are the patient's main symptoms?",
            "context": text  # Patient history
        }
    }
    response = requests.post(biobert_endpoint, headers=headers, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and len(result) > 0:
            return result[0].get("answer", "No relevant information found.")
        else:
            return "No relevant information found."
    else:
        return f"Error: {response.status_code} - {response.text}"

# Generate Diagnosis Function
def generate_diagnosis(input_text):
    payload = {
        "inputs": input_text  # Full context for GPT model
    }
    response = requests.post(gpt_endpoint, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()[0].get("generated_text", "Unable to generate a diagnosis.")
    else:
        return f"Error: {response.status_code} - {response.text}"

# Streamlit action
if st.button("Diagnose") and patient_details:
    extracted_info = extract_medical_info(patient_details)
    st.write(f"Extracted Medical Information: {extracted_info}")
    
    if extracted_info:
        diagnosis_text = f"The patient presents the following symptoms: {extracted_info}."
        diagnosis = generate_diagnosis(diagnosis_text)
        st.write(f"Diagnosis Suggestion: {diagnosis}")