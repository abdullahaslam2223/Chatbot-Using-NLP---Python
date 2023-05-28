from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pyodbc
# import io
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

origins = ["https://localhost:44364"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    corpus = prepare_response(cursor)


    # with open('data.txt', 'w') as file:
    #     for sentence in corpus:
    #         file.write(sentence + '\n')


    # with open('data.txt', 'r') as file:
    #     content = file.read()

    # corpus = nltk.sent_tokenize(content)


    nltk.download('punkt')

    def tokenize(text):
        return nltk.word_tokenize(text.lower())
    

    corpus_tokens = [tokenize(text) for text in corpus]

    # Convert tokens to strings
    corpus_strings = [' '.join(tokens) for tokens in corpus_tokens]

    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus_strings)

    def get_most_similar_answer(question):
        question_tokens = tokenize(question)
        question_string = ' '.join(question_tokens)
        question_vector = vectorizer.transform([question_string])
        similarities = cosine_similarity(question_vector, tfidf_matrix)
        most_similar_index = similarities.argmax()
        if similarities[0][most_similar_index] > 0:
            return corpus[most_similar_index]
        else:
            return None


    GREETING_INPUTS = ("hello", "hi", "greetings", "salam", "what's up","hey",)
    GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
    def greeting(sentence):
    
        for word in sentence.split():
            if word.lower() in GREETING_INPUTS:
                return random.choice(GREETING_RESPONSES)
            

    user_response = question
    user_response=user_response.lower()
    res = ""
    if(user_response=='thanks' or user_response=='thank you'):
        res = "You are welcome"
    else:
        if(greeting(user_response)!=None):
            res = greeting(user_response)
        else:
            answer = get_most_similar_answer(user_response)
            if answer:
                res = answer
            else:
                res = "Please ask relevant question!"
    
    return res.capitalize()
