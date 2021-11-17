from fastapi import FastAPI
import snowflake.connector
import uvicorn
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification
# import tensorflow as tf
import tensorflow_hub as hub
from fastapi.responses import FileResponse
from numpy import savetxt
import json


ctx = snowflake.connector.connect(
    user='*********',
    password='*********',
    account='*********.us-central1.gcp'
    )
cs = ctx.cursor()

class sentence(BaseModel):
    id=int
    content: str

app = FastAPI()

@app.post("/summarizer")
def summarizers(summ_id: sentence, text: sentence):
    summarizer = pipeline("summarization")
    summ=summarizer(text.content, max_length=20, min_length=5)
    for i in summ:
        summary=(i['summary_text'])
    cs.execute("USE WAREHOUSE COMPUTE_WH ")
    cs.execute("USE DATABASE NLP") 
    cs.execute("USE schema PUBLIC")
    sql = cs.execute("INSERT INTO SUMMARY (SUM_ID, TEXT, SUM_TEXT) VALUES ('"+str(summ_id.content)+"', '"+text.content+"', '"+summary+"');")
    print("Hello")
    return {"message": text.content, "summ": summ}

@app.post("/name_entity_recog")
def name_entity_recog(ner_id: sentence,text: sentence):
    ner = pipeline("ner")
    ner_results = ner(text.content)
    ents=[]
    ner=' '
    for i in ner_results:
        j=i["entity"]
        ents.append({'word':i["word"],'entity':i["entity"]})
    for k in ents:
        ner += ' ' + json.dumps(k)
    cs.execute("USE WAREHOUSE COMPUTE_WH ")
    cs.execute("USE DATABASE NLP") 
    cs.execute("USE schema PUBLIC")
    sql = cs.execute("INSERT INTO NAMED_ENTITY_RECONG (NER_ID, TEXT, NER_TEXT) VALUES ('"+str(ner_id.content)+"', '"+text.content+"', '"+ner+"');")
    return {"message": text.content, "ents": ents}
    
@app.post("/word_emb")
def word_emb(we_id: sentence, text: sentence):
    embed = hub.load("https://tfhub.dev/google/Wiki-words-250/2")
    embeddings = embed([text.content])
    print(type(embeddings))
    cs.execute("USE WAREHOUSE COMPUTE_WH ")
    cs.execute("USE DATABASE NLP") 
    cs.execute("USE schema PUBLIC")
    sql = cs.execute("INSERT INTO WORD_EMB (WE_ID, TEXT, WE_TEXT) VALUES ('"+str(we_id.content)+"', '"+text.content+"', '"+str(embeddings)+"');")
    savetxt('data.csv', embeddings, delimiter=',')
    print('successful!')
    return FileResponse("data.csv")
