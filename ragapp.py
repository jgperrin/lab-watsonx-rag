from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import BSHTMLLoader
from langchain.document_loaders import UnstructuredHTMLLoader

from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

import streamlit as st
from watsonxlangchain import LangChainInterface

# Configuration

# Model
selected_model = 'none'
# selected_model = 'meta-llama/llama-2-70b-chat'
# selected_model = 'ibm/mpt-7b-instruct2'
# selected_model = 'ibm/granite-13b-chat-v1'
# selected_model = 'google/flan-t5-xxl'

# Resources
# resource_name = 'null.html'
resource_name = 'About Us - ProfitOptics.html'

# More resources
# more_resource_name = 'null.html'
more_resource_name = 'more.html'

## End configuration

creds = {
    'apikey':'lCFwWIPwg1XaSEftPkXY31B5E4pG-5rgE5SwFh0_htc7', 
    'url': 'https://us-south.ml.cloud.ibm.com'
}

llm = LangChainInterface(
    credentials = creds, 
    model = selected_model, 
    params = {'decoding_method':'sample', 'max_new_tokens':200, 'temperature':0.5}, 
    project_id='ec74a523-e663-4c0a-aa89-6321b2022855')

# jg ec74a523-e663-4c0a-aa89-6321b2022855
# po 7b11331d-df80-4e60-ab84-f540be151b86

@st.cache_resource
def load_external_resource(): 

    loaders = [UnstructuredHTMLLoader(resource_name), UnstructuredHTMLLoader(more_resource_name)]

    index = VectorstoreIndexCreator(
        embedding = HuggingFaceEmbeddings(model_name='all-MiniLM-L12-v2'), 
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    ).from_loaders(loaders)

    return index

index = load_external_resource()

chain = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=index.vectorstore.as_retriever(), input_key='question')

st.title('Ask watsonx.ai 🤖')

if 'messages' not in st.session_state: 
    st.session_state.messages = [] 

for message in st.session_state.messages: 
    st.chat_message(message['role']).markdown(message['content'])

prompt = st.chat_input('Pass Your Prompt here')

if prompt: 
    st.chat_message('user').markdown(prompt)
    st.session_state.messages.append({'role':'user', 'content':prompt})

    response = chain.run(prompt)

    st.chat_message('assistant').markdown(response)
    st.session_state.messages.append({'role':'assistant', 'content':response})