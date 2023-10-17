import streamlit as st
from huggingface_hub import HfApi

# Initialize the HfApi
hf_api = HfApi()

# Main Streamlit app
st.title("Hugging Face Search Interface")

# Create a sidebar with filter options
st.sidebar.header("Filter Options")

# Model Filter Options
st.sidebar.subheader("Model Filter")
model_filter = st.sidebar.text_input("Filter by Model (e.g., text-classification)", key="model_filter")

# Dataset Filter Options
st.sidebar.subheader("Dataset Filter")
dataset_filter = st.sidebar.text_input("Filter by Dataset (e.g., text-classification)", key="dataset_filter")

# Author and Search Options
st.sidebar.subheader("Author and Search")
author = st.sidebar.text_input("Author", key="author")
search = st.sidebar.text_input("Search", key="search")

# Button to trigger the search
if st.sidebar.button("Search"):
    if model_filter:
        models = hf_api.list_models(filter=model_filter)
        st.write(f"Models filtered by '{model_filter}':")
        for model in models:
            st.write(model)
    
    if dataset_filter:
        datasets = hf_api.list_datasets(filter=dataset_filter)
        st.write(f"Datasets filtered by '{dataset_filter}':")
        for dataset in datasets:
            st.write(dataset)
    
    if author:
        models_by_author = hf_api.list_models(author=author)
        st.write(f"Models by author '{author}':")
        for model in models_by_author:
            st.write(model)
    
    if search:
        search_results = hf_api.list_models(search=search)
        st.write(f"Search results for '{search}':")
        for result in search_results:
            st.write(result)
