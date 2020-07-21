# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 22:50:54 2020

@author: joy
"""
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from tika import parser



def cleanup():
    resume_file = (r"C:\Users\joy\Downloads\Resume-Saptarshi_Datta.pdf")
    resume_meta_data = parser.from_file(resume_file)
    resume_text = resume_meta_data['content']
    resume_text = str(resume_text)
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    tokenized_words = tokenizer.tokenize(resume_text)
    # convert to lower case
    lower_words = [w.lower() for w in tokenized_words]
    # remove remaining tokens that are not alphabetic
    resume_words = [word for word in lower_words if word.isalpha()]  
    excluded_words = list(stopwords.words("english"))
    level1_key_words = list(filter(lambda x: x not in excluded_words, resume_words))
    level2_key_words = [word for word in level1_key_words if len(word) > 2]
    resume_key_words = level2_key_words 
    print(resume_key_words)

cleanup()


    
    
    
    