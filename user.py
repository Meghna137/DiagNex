import streamlit as st

# Custom CSS for transitions and styling
st.markdown("""
    <style>
    body {
        background-color: #f8f9fa; 
        text-align: center;
    }

    .gradient-title {
        font-size: 64px;
        background: linear-gradient(135deg, #ff7e5f, #feb47b); 
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: slideIn 1s ease forwards; 
    }

    .tagline {
        font-size: 24px; 
        margin-top: 10px; 
        color: #333; 
        opacity: 0; 
        animation: fadeIn 1s ease forwards;  
        animation-delay: 0.5s; 
    }

    @keyframes slideIn {
        0% {
            transform: translateY(-50px);
            opacity: 0;
        }
        100% {
            transform: translateY(0);
            opacity: 1;
        }
    }

    @keyframes fadeIn {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    .button-container {
        position: absolute; 
        top: 15px;
        right: 15px;
    }

    .login-signup {
        margin-bottom: 20px; 
    }

    .circular-button {
        padding: 10px 20px; 
        font-size: 16px; 
        border-radius: 50px;
        border: 2px solid #ff7e5f; 
        background-color: white;
        cursor: pointer; 
        transition: background-color 0.3s, color 0.3s; 
    }

    .circular-button:hover {
        color: white; 
    }
    </style>
""", unsafe_allow_html=True)

# UI
st.markdown('<h1 class="gradient-title">Diagnex</h1>', unsafe_allow_html=True)
st.markdown('<div class="tagline">Your AI-Powered Medical Diagnosis Assistant</div>', unsafe_allow_html=True)
st.sidebar.title("Authentication")
choice = st.sidebar.radio("Choose an option", ["Login", "Signup"])

# Initialize user data
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}

# Function for Login
def login(username, password):
    if username in st.session_state.user_data and st.session_state.user_data[username] == password:
        return True
    return False

#signup
def signup(username, password):
    if username in st.session_state.user_data:
        return False
    st.session_state.user_data[username] = password
    return True
#login
if choice == "Login":
    st.sidebar.subheader("Login Form")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        if login(username, password):
            st.success("Logged in successfully!")
            st.session_state.page = "main"  # Update the page to page2
            
        else:
            st.error("Invalid credentials. Please try again.")

#Forms
elif choice == "Signup":
    st.sidebar.subheader("Signup Form")
    username = st.sidebar.text_input("Choose a Username")
    password = st.sidebar.text_input("Choose a Password", type="password")

    if st.sidebar.button("Signup"):
        if signup(username, password):
            st.success("Account created successfully!")
            st.session_state.page = "main"  # Update the page to page2
        else:
            st.error("Signup failed. Username already exists.")

