import streamlit as st
import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
#A singl efunction to do all these steps
def transform_text(text):
    text = text.lower() #step 1
    text = nltk.word_tokenize(text)
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i);
    text = y[:] # this makes shalow copy now if we clear y it will not clear text and text is an list
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i);
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i)) # to stem down loving to love and remove e and ings etc.
    return " ".join(y)
# tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("SMS Spam Dection")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    # preprocess
    transformed_sms = transform_text(input_sms)
#     #vectorize
#     vector_input = tfidf.transform([transformed_sms])
#     # predict
#     result = model.predict(vector_input)[0]
#     #display result
#     if result ==1:
#         st.header("SPAM!")
#     else:
#         st.header("NOT SPAM!")

