
import streamlit as st
import requests
from requests.auth import HTTPBasicAuth
import os



st.title("Insight")
st.sidebar.header("Select the NLP Service")
nlp_options = st.sidebar.selectbox(
    label="",
    options=["Select from drop down",
            "Summarization",
            "Named Entity Recognition",
            "Word_Embedding",
            ])
st.sidebar.header("Select the Service Provider")
if nlp_options=="Select from drop down":
    service_options = st.sidebar.selectbox(
        label="",
        options=["Select from NLP Service first",
                ])
if nlp_options=="Summarization":
    service_options = st.sidebar.selectbox(
        label="",
        options=["Select from drop down",
                "Hugging Face",
                "IBM"
                ])
if nlp_options=="Named Entity Recognition":
    service_options = st.sidebar.selectbox(
        label="",
        options=["Select from drop down",
                "IBM",
                "Tf.hub"
                ])
if nlp_options=="Word_Embedding":
    service_options = st.sidebar.selectbox(
        label="",
        options=["Select from drop down",
                "Tf.hub"
                ])
heading= '<p style="font-family:sans-serif; color:White; font-size: 48px;">NLP</p>'
st.write("The submission is for DAMG-7245 Assignment2")
st.markdown(heading, unsafe_allow_html=True)
if nlp_options=="Summarization" and service_options=="Hugging Face":
    max_lengthy = st.slider('Maximum summary length (words)', min_value=5, max_value=40, value=20, step=5)

    num_beamer = st.slider('Speed vs quality of summary (1 is fastest)', min_value=1, max_value=8, value=4, step=1)

    index_=st.text_area('Enter Index:', height=3)

    text_ = st.text_area('Enter Text Below (maximum 800 words):', height=300) 

    submit = st.button('Generate')

    if submit:

        st.subheader("Summary:")

        with st.spinner(text="This may take a moment..."):
            data = '{"summ_id": {"content": "'+index_+'"},"text": {"content": "'+text_+'"} }'
            response=requests.post(url="https://nlpservices-fastapi-v1-th4rn5qo6a-uc.a.run.app/summarizer", data=data, headers={'Content-Type': 'application/json'})
            st.write(response.content)


if nlp_options=="Summarization" and service_options=="IBM":
    max_lengthy = st.slider('Maximum summary length (words)', min_value=5, max_value=40, value=20, step=5)

    num_beamer = st.slider('Speed vs quality of summary (1 is fastest)', min_value=1, max_value=8, value=4, step=1)

    text_ = st.text_area('Enter Text Below (maximum 800 words):', height=300) 

    submit = st.button('Generate')

    if submit:

        st.subheader("Summary:")

        with st.spinner(text="This may take a moment..."):
            print(text_)
            data="{ \"text\": [ \""+text_+"\" ]}"
            response=requests.post(url="http://*********************", 
                                data=data, headers={'Content-Type': 'application/json'})
            st.write(response.content)


if nlp_options=="Named Entity Recognition" and service_options=="IBM":
        
    text_ = st.text_area('Enter Text Below (maximum 800 words):', height=300) 

    submit = st.button('Generate')
    if submit:

        st.subheader("Named Entity Recognition:")

        with st.spinner(text="This may take a moment..."):
            auth = HTTPBasicAuth('apikey', '************************')
            data ="{\"text\":\""+text_+"\",\"features\":{\"entities\":{},\"keywords\":{\"emotion\":true}}}" 
            response=requests.post(url="https://*************************", 
            data=data, auth=auth,headers={'Content-Type': 'application/json'})
            st.write(response.content)


if nlp_options=="Named Entity Recognition" and service_options=="Tf.hub":
        
    index_=st.text_area('Enter Index:', height=3)
        
    text_ = st.text_area('Enter Text Below (maximum 800 words):', height=300) 

    submit = st.button('Generate')
    if submit:

        st.subheader("Named Entity Recognition:")

        with st.spinner(text="This may take a moment..."):
            data = '{"ner_id": {"content": "'+index_+'"},"text": {"content": "'+text_+'"} }'
            response=requests.post(url="https://nlpservices-fastapi-v1-th4rn5qo6a-uc.a.run.app/name_entity_recog", data=data, headers={'Content-Type': 'application/json'})
            st.write(response.content)

if nlp_options=="Word_Embedding" and service_options=="Tf.hub":

    index_=st.text_area('Enter Index:', height=3)

    text_ = st.text_area('Enter Text Below (maximum 800 words):', height=300) 

    submit = st.button('Generate')
    if submit:

        st.subheader("Named Entity Recognition:")

        with st.spinner(text="This may take a moment..."):
            data = '{"we_id": {"content": "'+index_+'"},"text": {"content": "'+text_+'"} }'
            response=requests.post(url="https://nlpservices-fastapi-v1-th4rn5qo6a-uc.a.run.app/word_emb", data=data, headers={'Content-Type': 'application/json'})
            st.write(response.content)


