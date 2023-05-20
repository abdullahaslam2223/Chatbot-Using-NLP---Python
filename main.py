from pydantic import BaseModel
from fastapi import FastAPI
import pyodbc
import io
import random
import string
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

from ChatbotResponse import prepare_response

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True)

app = FastAPI()

# Define a request body model
class Item(BaseModel):
    question: str

# Create a route for the POST request
@app.post("/response/")
async def get_response(item: Item):
    response = get_response(item.question)
    return {"data" : response}




def get_response(question):
    connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-22T0AB6\SQLEXPRESS;'
    'DATABASE=Gemstones_BCSF19E034;'
    'UID=sa;'
    'PWD=123'
    )

    cursor = connection.cursor()
    data = prepare_response(cursor)


    # Open the text file in write mode
    with open('data.txt', 'w') as file:
        # Iterate over each element in the array
        for sentence in data:
            # Write the element to a new line in the file
            file.write(sentence + '\n')

    # Data Preparing Ends Here




    # Chatbot Starts from here

    # exit()

    f=open('data.txt','r',errors = 'ignore')
    raw=f.read()
    raw = raw.lower()# converts to lowercase



    sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
    word_tokens = nltk.word_tokenize(raw)# converts to list of words



    lemmer = nltk.stem.WordNetLemmatizer()
    #WordNet is a semantically-oriented dictionary of English included in NLTK.
    def LemTokens(tokens):
        return [lemmer.lemmatize(token) for token in tokens]
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

    def LemNormalize(text):
        return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))



    GREETING_INPUTS = ("hello", "hi", "greetings", "salam", "what's up","hey",)
    GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
    def greeting(sentence):
    
        for word in sentence.split():
            if word.lower() in GREETING_INPUTS:
                return random.choice(GREETING_RESPONSES)
            



    def response(user_response):
        robo_response=''
        sent_tokens.append(user_response)
        TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
        tfidf = TfidfVec.fit_transform(sent_tokens)
        vals = cosine_similarity(tfidf[-1], tfidf)
        idx=vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-2]
        if(req_tfidf==0):
            robo_response=robo_response+"Please ask questions related to this website"
            return robo_response
        else:
            robo_response = robo_response+sent_tokens[idx]
            return robo_response
        



    user_response = question
    user_response=user_response.lower()
    res = ""
    if(user_response=='thanks' or user_response=='thank you'):
        res = "You are welcome"
    else:
        if(greeting(user_response)!=None):
            res = greeting(user_response)
        else:
            res = response(user_response)
            sent_tokens.remove(user_response)


    return res