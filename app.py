import streamlit as st
import pandas as pd
import os
from src.preprocess import clean_text
from src.entity_extractor import EntityExtractor

st.set_page_config(page_title="Contract Analysis System", page_icon="📄", layout="wide")

st.title("📄 Contract Analysis System")
st.markdown("Extract important entities (`PERSON`, `ORG`, `DATE`, `MONEY`, `GPE`) from legal or contract text using a pretrained NLP model.")

# Load the model with Streamlit caching so it doesn't reload on every interaction
@st.cache_resource
def load_extractor():
    return EntityExtractor()

with st.spinner("Loading NLP Model..."):
    extractor = load_extractor()

st.sidebar.header("Input Options")
input_method = st.sidebar.radio("Choose how to provide the contract:", ("Text Input", "File Upload"))

contract_text = ""

if input_method == "Text Input":
    st.subheader("Enter Contract Text")
    contract_text = st.text_area("Paste your contract or legal text here:", height=300)
    # Provide a button to load a sample
    if st.button("Load Sample Contract"):
        sample_path = os.path.join("data", "sample_contract.txt")
        if os.path.exists(sample_path):
            with open(sample_path, 'r', encoding='utf-8') as f:
                contract_text = f.read()
            st.rerun()

else:
    st.subheader("Upload Contract File")
    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
    if uploaded_file is not None:
        contract_text = uploaded_file.read().decode("utf-8")
        st.text_area("File Content Preview:", value=contract_text, height=300, disabled=True)

if st.button("Analyze Contract", type="primary"):
    if not contract_text.strip():
        st.warning("Please provide some text to analyze.")
    else:
        with st.spinner("Extracting entities..."):
            cleaned_text = clean_text(contract_text)
            entities = extractor.extract_entities(cleaned_text)
            
            st.subheader("Analysis Results")
            if entities:
                st.success(f"Successfully extracted {len(entities)} entities!")
                
                # Display as dataframe
                df = pd.DataFrame(entities)
                # Rename columns for better UI
                df_display = df.rename(columns={"text": "Entity", "label": "Type"})
                st.dataframe(df_display, use_container_width=True)
                
                # Save to CSV
                results_dir = "results"
                os.makedirs(results_dir, exist_ok=True)
                output_path = os.path.join(results_dir, "extracted_entities.csv")
                df.to_csv(output_path, index=False)
                st.info(f"Results have been saved to `{output_path}`")
            else:
                st.info("No matching entities found in the provided text.")
