import json
from pprint import pprint
import pandas as pd

# reading in training data to pandas dataframe
df = pd.read_json('data/train.json')

import nltk
import re
from nltk import word_tokenize

# setting to new variable and converting the Series to a list
request_text = df.request_text_edit_aware
request_text_list = request_text.tolist()

# tokenizing the request_text_list using a list comprehension
request_token_list = [word_tokenize(request) for request in request_text_list]

# calculating the word count for each tokenized list using a list comprehension
request_word_count = [len(tokens) for tokens in request_token_list]
df['word_count'] = pd.Series(request_word_count)

# calculating the lexical diversity of each request (number of unique words divided by total)
def lexical_diversity(x):
    if len(x) > 0:
        return len(set(x)) / len(x) 
    else: 
        return 0

# calculating the lexical diversity of each request using a list comprehension
lex_div = [lexical_diversity(tokens) for tokens in request_token_list]
df['lexical_diversity'] = pd.Series(lex_div)

# calculate number of long words in each request
long_words = []
for tokens in request_token_list:
    words = [w for w in tokens if len(w) > 12]
    long_words.append(words)

# calculating the number of long words in each request using a list comprehension
count_long_words = [len(set_of_words) for set_of_words in long_words]
df['long_word_count'] = pd.Series(count_long_words)
        
# creating list comprehension to check for 'please' and profanity
please = [1 if re.search('please', i) else 0 for i in request_text] 
df['please'] = pd.Series(please)
profanity = [1 if re.search('shit|fuck.|bitch|ass', i) else 0 for i in request_text] 
df['profanity'] = pd.Series(profanity)

# creating variables for the request title and turning it from Series to a list
title = df.request_title
title_list = title.tolist()

# tokening the list using a list comprehension
title_token_list = [word_tokenize(title) for title in title_list]

# creating a list of the word count using a list comprehension
title_word_count = [len(tokens) for tokens in title_token_list]
df['title_word_count'] = pd.Series(title_word_count)

# checking for 'please' and 'love' in the title
please_in_title = [1 if re.search('please', i) else 0 for i in title] 
df['please_in_title'] = pd.Series(please_in_title)
love_in_title = [1 if re.search('love', i) else 0 for i in title] 
df['love_in_title'] = pd.Series(love_in_title)

# check for length
username = df.requester_username
username_list = username.tolist()

username_length = []
for i in username_list:
    count = len(i)
    username_length.append(count)

df['username_length'] = pd.Series(username_length)

# check for declared throwaway account
throwaway = [1 if re.search('throwaway', i) else 0 for i in username] 
df['throwaway'] = pd.Series(throwaway)

#account age
age = df.requester_account_age_in_days_at_request
df['day'] = [1 if i <= 1 else 0 for i in age]
df['month'] = [1 if i > 1 and i <= 30 else 0 for i in age]
df['year'] = [1 if i > 30 and i <= 365 else 0 for i in age]
df['longtime'] = [1 if i > 365 else 0 for i in age]

# creating shorter feature names
df['comments'] = df.requester_number_of_comments_at_request
df['posts'] = df.requester_number_of_posts_at_request
df['age'] = df.requester_account_age_in_days_at_request

#features that represent subreddit reputation
#dummy variable for whether it was the users first post to raop
first_post = df.requester_days_since_first_post_on_raop_at_request
df['first_post'] = [1 if i == 0 else 0 for i in first_post]

#dummy variable for whether the user has commented before
sub_comments = df.requester_number_of_comments_in_raop_at_request
df['has_commented'] = [1 if i >= 1 else 0 for i in sub_comments]

#continuous variable for number of posts
sub_posts = df.requester_number_of_posts_on_raop_at_request

#three types of flair to identify reciprocity (shroom=received, PIF=given after
#received, and None=neither)
flair = df.requester_user_flair
df['no_flair'] = [1 if i == 'None' else 0 for i in flair]
df['received'] = [1 if i == 'shroom' else 0 for i in flair]
df['given_after_received'] = [1 if i == 'PIF' else 0 for i in flair]

#identify weekends, weekdays, nights, days, and times near holidays
import datetime
timestamp_utc = df.unix_timestamp_of_request_utc
day_time_str = [datetime.datetime.utcfromtimestamp(int(i)).strftime('%Y-%m-%d %H:%M:%S') for i in timestamp_utc]
day_of_week = [datetime.datetime.utcfromtimestamp(int(i)).weekday() for i in timestamp_utc]
df['weekday'] = [1 if i < 5 else 0 for i in day_of_week]

# converting requester_received_pizza feature to an integer
df['target'] = [1 if i == True else 0 for i in requester_received_pizza]

'''
Topic Modeling
'''

import lda
from gensim import corpora, models, similarities
import numpy as np
import stop_words

documents = request_text_list

# remove common words and tokenize
stopwords = stop_words.get_stop_words("english")
new_words = 'get last will right get can like really just got back make now'.split()
stopwords.extend(new_words)
stoplist = set(stopwords)
texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

# remove words that appear only once
all_tokens = sum(texts)
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
texts = [[word for word in text if word not in tokens_once] for text in texts]

# store the corpus of words
dictionary = corpora.Dictionary(texts)
# dictionary.save('raop.dict')
# dictionary.load('raop.dict')

# counts the number of occurences of each distinct word, converts the word to its 
# integer word id and returns the result as a sparse vector. 
corpus = [dictionary.doc2bow(text) for text in texts]
# corpora.MmCorpus.serialize('raop.mm', corpus)

'''
Training the corpus using various models  
ONLY FIT THE MODEL ONCE BECAUSE TOPICS CHANGE AFTER EVERY RUN!
Load the saved model file to apply the model to new documents
'''

# Latent Dirichlet Allocation, LDA
lda = models.ldamodel.LdaModel(corpus, id2word=dictionary, num_topics=10, passes=3)
corpus_lda = lda[corpus]
lda.save('model.lda')
    
'''
LOAD THE MODELS BEFORE TRYING TO RUN SIMILARITY QUERIES!
'''

lda = models.LdaModel.load('model.lda')

# applying the LDA model to identify topic for each request using
# similarity queries
docs = request_text_list
lda_topics = []
for doc in docs:
    vec_bow = dictionary.doc2bow(doc.lower().split())
    vec_lda = lda[vec_bow]
    vec_lda.sort(key=lambda item: -item[1])
    lda_topics.append(vec_lda[0][0])
   
# printing the topics and the words associated with each topic
for i in lda.show_topics():
    print i
    
# generating a feature for the topics
df['lda_topics'] = pd.Series(lda_topics)
    
# generating dummies for each topic
topics = pd.get_dummies(df['lda_topics'], prefix='topic')
df = pd.concat([df, topics], axis=1)
 
'''
Logistic Regression
'''

import statsmodels.formula.api as smf
from sklearn.cross_validation import train_test_split

# Split the data into train and test sets
train, test = train_test_split(df,test_size=0.3)

msk = np.random.rand(len(df)) < 0.8
train = df[msk]
test = df[~msk]

# Convert them back into dataframes, for convenience
train = pd.DataFrame(data=train, columns=df.columns)
test = pd.DataFrame(data=test, columns=df.columns)

# Run a logistic regression on the balance variable
pizza = smf.logit('target ~ word_count + requester_account_age_in_days_at_request + first_post + has_commented + weekday + requester_upvotes_minus_downvotes_at_request', data = train).fit()
pizza.summary()

# Create predictions using the balance model on the test set
test['pred'] = pizza.predict(test)
test['pred_class']= np.where(test['pred'] >= 0.5, 1, 0)

# Accuracy
accuracy = sum(test.pred_class == test.target) / float(len(test.target))

# Specificity: For those who didn't receive pizza, how many did it predict correctly?
test_nd = test[test.target == 0]
sum(test_nd.pred_class == 0) / float(len(test_nd))

# Sensitivity: For those who did receive pizza, how many did it predict correctly? 
test_d = test[test.target == 1]
sum(test_d.pred_class == 1) / float(len(test_d))

# generate metrics
from sklearn import metrics
print metrics.accuracy_score(test.target, test.pred_class)
print metrics.confusion_matrix(test.target, test.pred_class)
print metrics.roc_auc_score(test.target, test.pred)

# plot ROC curve
fpr, tpr, thresholds = metrics.roc_curve(test.target, test.pred)
plt.figure()
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')

# Predicting the test set provided by Kaggle 
# Change first line of code to "df = pd.read_json('data/test.json')" and re-run everything
# before fitting the model
df['pred'] = pizza.predict(df)
df['requester_received_pizza']= np.where(df['pred'] >= 0.5, 1, 0)

# Write to csv for submission
my_cols = ['request_id', 'requester_received_pizza']
df[my_cols]
df[my_cols].to_csv('kaggle_raop.csv', index=False)
