# Project RAG (Spring 2024)

Retrieval-Augmented Generation for Question-Answering on PDFs

## Overview
This project guides you through building a Retrieval-Augmented Generation (RAG) system to answer questions based on uploaded PDF documents. You'll integrate a RAG solution and a user-friendly interface to achieve the following:

- PDF Upload and Indexing
- Vector-Based Retrieval
- Question Answering
- GUI Application
- [Bonus] PDF Deletion
- Demo: A reference demo using Vectara AI platform can be found here: https://github.com/forrestbao/vectara-python-cli.

## RAG Solution & UI Frameworks
You'll be assigned one RAG solution and one UI framework:

### RAG Solutions:

- Pinecone + Language Model (e.g., GPT-3.5) (without LangChain or LlamaIndex)
- LangChain
- LlamaIndex

### UI Frameworks:
- Streamlit
- Gradio
- Dash
- Funix.io

### Key Challenges
- Optimal Text Chunking: Experiment with chunk sizes (e.g., 100, 200 words) with 25% overlap for best results.
- Retrieval Efficiency: Retrieve the top 5 most relevant chunks.

## How to Submit
- GitHub Repository: Create a public repo for your RAG and UI integration.
- README Instructions: Provide clear instructions on running the demo.
- Demo Walkthrough: Include instructions and video clips demonstrating each feature.

## Presentation Video: Create a 5-minute video showcasing the system and the UI.
[Bonus] Cloud Deployment: Deploy your demo for public testing.
## Milestones
- Feb. 28: GitHub repo setup.
- March 7: Complete PDF upload/indexing via the command line (e.g., python upload.py --pdf_file=example.pdf) Include README and a demo video.
- March 30: Implement query-based answer generation on the command line (e.g., python query.py --question="What is the meaning of life?") - - Provide README and a demo video.
- April 20: Create the GUI app, integrating all features. Update README and produce a final demo video.
## Tips
- Answer Generation: Consider a smaller language model like Llama-2 for local execution (see resources).
- Embedding: Use simple encoder models like BERT or sentence-transformers.
## Tech Stack-Specific Tips
- Pinecone: Refer to this demo (using GPT-3.5): https://github.com/pinecone-io/examples/blob/master/learn/generation/langchain/handbook/05-langchain-retrieval-augmentation.ipynb
## References
- LangChain: https://python.langchain.com/docs/modules/data_connection/
- Google on RAGs: https://cloud.google.com/blog/products/ai-machine-learning/rags-powered-by-google-search-technology-part-1
- Retrieval Augmented Generation: https://www.pinecone.io/learn/retrieval-augmented-generation/
- Instructor's Semantic Search Demo: https://github.com/forrestbao/pebble/blob/master/NLP/semantic_search.ipynb