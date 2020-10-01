import io
import random
import string # to process standard python strings
import warnings
import numpy as np
import yaml
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
warnings.filterwarnings('ignore')

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) # for downloading packages

# uncomment the following only the first time
#nltk.download('punkt') # first-time use only
#nltk.download('wordnet') # first-time use only


#Reading in the corpus
with open('chatbot.txt','r', encoding='utf8', errors ='ignore') as fin:
    raw = fin.read().lower()

#TOkenisation
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words

GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "what's up","hey","hloo"]
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "I am glad! You are talking to me"]

CONDITION_INPUT =["not", "feeling"," well", "drouzy"]
CONDITION_RESPONSE=["i am here to help you.can you tell me more about your health condition so that i can treat you more better","i am here to help u.Can you tell me about your symptoms"]

PROBLEM=("commoncold","common cold","migrane","acne","allergies","diarrhoea","drymouth","dry mouth","mouthulcers","mouth ulcers","earache","fever","flu","foodpoisoning","headache","indigestion","itching","migrane")
MEDICATION={
    "commoncold":"paracetemol,caffine",
    "migrane":"almotripan,electripan"
}
SYMPTOMS=("runningnose","mildheadache","soarthroat","sneezing")
HOMEREMEDIES={
    "commoncold":"go for steaming with breathein capsules,try to avoid cool foods"
}

def greeting(sentence):

    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def first(sentence):

    for word in sentence.split():
         if word.lower() in CONDITION_INPUT:
            return random.choice(CONDITION_RESPONSE)

def medication(sentence):
    for word in sentence.split():
        pp=word.lower()
        if pp in MEDICATION:
            soln=MEDICATION[pp]
            return soln

def homeremedies(sentence):
    for word in sentence.split():
        pp=word.lower()
        if pp in HOMEREMEDIES:
            soln=HOMEREMEDIES[pp]
            return soln

def find(sentence):
    for word in sentence.split():
        pp=word.lower()
        return pp




# Preprocessing
lemmer = WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))





# Generating response
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
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        sent_tokens.remove(user_response)
        robo_response = robo_response+sent_tokens[idx]
        fp=open('reference.txt',"w")

        fp.write(robo_response)
        fp.close()
        with open('reference.txt') as fp:
            lines=fp.readlines()
        ans=lines[1]
        return ans


def chat(user_response):
    user_response=user_response.lower()

    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you'):
            flag=False
            return(" You are welcome..")
        else:
            if(greeting(user_response)!=None):
                    return(greeting(user_response))
            elif(first(user_response)!=None):
                    return(first(user_response))
            elif(medication(user_response)!=None):
                    return("so it's prefferable to use these tablets" '\n' +medication(user_response)+'\n\n')
            elif(homeremedies(user_response)!=None):
                    return("it is suggested to follow these homeremedies")
                    return(homeremedies(user_response))
            elif(find(user_response)!=None):
                     return(find(user_response))

            else:
                return(response(user_response))
                fp = open('reference.txt', "r+")
                fp.truncate()


    else:
        (flag==false)

