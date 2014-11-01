import json
from pprint import pprint
import pandas as pd

#reading in training data to pandas dataframe
df = pd.read_json('data/train.json')

#descriptive statistics
df.describe()
df.info()

pd.scatter_matrix(df)
plt.show

#print column names vertically
for i in df.columns:
    print i

target = df.requester_received_pizza

#relevant features
#textual factors of success
#conduct NLP and topic modeling to identify politeness, evidentiality, 
#sentiment (very positive vs very negative requests, and length of request.
#perform topic modeling using non-negative matrix factorization of a TF-IDF weighted
#bag of words representation of the requests.
#word count
#lexicon diversity
#profanity
#big word count
import nltk
import re
from nltk import word_tokenize

#setting the first 5 rows equal to s and converting the Series to a list
requests = df.request_text_edit_aware[:5]
request_list = requests.tolist()

#tokenizing every request in request_list and saving them as a new list called tokenized_list
tokenized_list = []
for sentence in list:
    tokens = word_tokenize(sentence)
    tokenized_list.append(tokens)

#calculating the word count of each tokenized request
word_count = []
for tokens in tokenized_list:
    length = len(tokens)
    word_count.append(length)

#calculating the lexical diversity of each request (number of unique words divided by total)
def lexical_diversity(text):
    return len(set(text)) / len(text) 
lex_div = []
for tokens in tokenized_list:
    num = lexical_diversity(tokens)
    lex_div.append(num)

#calculate number of long words in each request
long_words = []
for tokens in tokenized_list:
    words = [w for w in tokens if len(w) > 10]
    long_words.append(words)
count_long_words = []
for set_of_words in long_words:
    length = len(set_of_words)
    count_long_words.append(length)

#check for existence of 'please' and return binary variable list
please = []
for i in range(0,len(requests)):
    value = requests[i].lower().find("hi")
    if value == -1:
        result = 0
        please.append(result)
    else: 
        result = 1
        please.append(result)
#list comprehension version
please2 = [1 if re.search('hi', w) else 0 for w in requests] 

profanity = [1 if re.search('shit|fuck.|bitch|ass', request) else 0 for request in requests] 

#do much of the same as above for title and username
request_title
#check for length and numbers
requester_username

#social factors of success
#status (people give to higher status), similarity (users give to people 
#like themselves)
#check distribution for each of the following create categories (ex. age: 24hrs, month, year, longer)
requester_account_age_in_days_at_request
requester_number_of_comments_at_request
requester_number_of_posts_at_request
#calculate total upvotes/total votes
requester_upvotes_minus_downvotes_at_request
requester_upvotes_plus_downvotes_at_request
#features that represent subreddit reputation
requester_days_since_first_post_on_raop_at_request
requester_number_of_comments_in_raop_at_request
requester_number_of_posts_on_raop_at_request
#three types of flair to identify reciprocity (gotten pizza, given pizza, neither)
requester_user_flair

#identify weekends, weekdays, nights, days, and times near holidays
unix_timestamp_of_request_utc

