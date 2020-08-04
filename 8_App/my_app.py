import streamlit as st
import numpy as np 
import pandas as pd 
#import time
import nltk
import string
import re
import joblib
from itertools import compress
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.linear_model import LogisticRegression

# Imports PIL module  
from PIL import Image 


from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import StandardScaler
  



nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer()
stemmer = nltk.stem.PorterStemmer()
nltk.download('stopwords')

from nltk.corpus import stopwords 
ENGLISH_STOP_WORDS = stopwords.words('english')

def my_tokenizer(sentence):
    
    for punctuation_mark in string.punctuation:
        # Remove punctuation and set to lower case
        sentence = sentence.replace(punctuation_mark,'').lower()

    # split sentence into words
    listofwords = sentence.split(' ')
    #listoflemmatized_words = []
    list_of_words = []
    
        
    # Remove stopwords and any tokens that are just empty strings
    for word in listofwords:
        if ((not word in ENGLISH_STOP_WORDS) and (word!='')) and (not re.search("\d", word)):
            # Lemmatize words
            lemmatized_word = lemmatizer.lemmatize(word)
            
            # append the word into the list of listoflemmatized_words
            # in case the word includes the newline \n, we replace with ""
            stemmed_word = stemmer.stem(lemmatized_word)
            list_of_words.append(stemmed_word.replace("\n",''))
            
            
    return list_of_words


def to_string(list_of_words):
    return str(" ".join(list_of_words))


all_genres=['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 
                'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 
                'Musical', 'Mystery', 'Romance', 'SciFi', 'Sport', 'Thriller', 'War']
my_model = joblib.load("my_model.pkl")
bagofwords = joblib.load("bagofwords.pkl")
coef_df = pd.DataFrame(my_model.coef_.T, columns=all_genres, index=bagofwords.get_feature_names())


def conversion(y_pred):
    my_list=list(compress(all_genres, y_pred[0]))
    return my_list


def get_genre(plot):
    #print("This is the plot of the movie:", plot)
    plot_cleaned=str(to_string(my_tokenizer(plot)))
    #print(plot_cleaned)
    plot_cleaned_series = pd.Series(plot_cleaned)
    X_test = bagofwords.transform(plot_cleaned_series[0:1])
    y_pred=my_model.predict(X_test)
    #print(y_pred)
    y_conv=conversion(y_pred)
    #print(y_conv)
    return str(y_conv).strip("[]").replace("'",'')

def is_spoiler(plot, review):
    plot_cleaned=str(to_string(my_tokenizer(plot)))
    review_cleaned=str(to_string(my_tokenizer(review)))
    plot_cleaned_series = pd.Series(plot_cleaned)
    review_cleaned_series = pd.Series(review_cleaned)
    X_plot = bagofwords.transform(plot_cleaned_series[0:1])
    X_review = bagofwords.transform(review_cleaned_series[0:1])
    if cosine_similarity(X_plot, X_review) > 0.0895:
        result="Spoiler Alert"
    else:
        result="Spoiler Free"
    return result




# open method used to open different extension image file 
image = Image.open(r"image.jpeg")  
st.image(image, use_column_width = False)


st.title('Movie App')

user_input=st.text_area("Please enter the movie plot to predict its genre(s)")

def output(input):
    if input== "":
        output=""
    else:
        output=get_genre(input)
    return output

def output2(input1, input2):
    if input2== "":
        output2=""
    else:
        output2=is_spoiler(input1, input2)
    return output2

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Processing the data
genres = output(user_input)
# Notify the reader that the data was successfully loaded.
#data_load_state.text('Loading data...done!')

st.subheader(f'The genre(s) of the movie: \n {(genres)}')
data_load_state.text('')

user_input2=st.text_area("Please write a review")

st.subheader(f'Is it a spoiler? \n {(output2(user_input, user_input2))}')




