import streamlit as st

# Set the page configuration
st.set_page_config(page_title="My Hugging Face Spaces", layout="wide")

# Inject custom CSS for styling
st.markdown(
    """
    <style>
    /* Global Styling */
    body {
        background-color: #f4f4f4;
        color: #333;
        font-family: 'Helvetica', sans-serif;
    }
    /* Title Styling */
    h1 {
        color: #4CAF50; /* Green title color */
        font-weight: bold;
        margin-bottom: 20px;
    }
    /* Markdown Text Styling */
    .markdown-text, .stMarkdown p {
        color: white !important; /* Custom color for markdown text set to black */
        font-size: 16px;
    }
    /* Add space below markdown text */
    .markdown-text {
        color: white;
        margin-bottom: 30px; /* Add space below the markdown text */
    }
    /* Button Styling */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 10px;
        border: none;
        margin: 5px;
        cursor: pointer;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #45a049;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a title for the interface
st.markdown("<h1>Access My Hugging Face Spaces</h1>", unsafe_allow_html=True)

# Provide a brief description
st.markdown("""
<div class='markdown-text'>
Welcome! Below are the links to the various Hugging Face Spaces I've created. 
Click on the buttons to access each Space directly.
</div>
""", unsafe_allow_html=True)

# Add an additional line break for extra spacing
st.markdown("<br>", unsafe_allow_html=True)


# Create equally spaced buttons using columns
col2, col3, col4= st.columns([2, 2, 2])

with col2:
    if st.button("Go to Multilingual Invoice Extractor"):
        js = "window.open('https://huggingface.co/spaces/amank4212/MultilingualInvoiceExtractor')"
        st.components.v1.html(f"<script>{js}</script>", height=0)

with col3:
    if st.button("Chat with Gemini while maintaining Chat history"):
        js = "window.open('https://huggingface.co/spaces/amank4212/ChatHistory')"
        st.components.v1.html(f"<script>{js}</script>", height=0)

with col4:
    if st.button("Explore your Resume"):
        js = "window.open('https://huggingface.co/spaces/amank4212/ATS')"
        st.components.v1.html(f"<script>{js}</script>", height=0)

# Footer or additional information
st.markdown("---")
st.markdown("© 2024 by Aman Kumar. All rights reserved.")
