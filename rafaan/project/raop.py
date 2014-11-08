import json
from pprint import pprint
import pandas as pd
import datetime


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
request_text = df.request_text_edit_aware[:5]
request_text_list = request_text.tolist()

#tokenizing every request in request_list and saving them as a new list called tokenized_list
request_token_list = []
for i in request_text_list:
    tokens = word_tokenize(i)
    request_token_list.append(tokens)

#tokenizing the request_text_list using a list comprehension
request_token_list2 = [word_tokenize(request) for request in request_text_list]

#calculating the word count of each tokenized request
request_word_count = []
for tokens in request_token_list:
    length = len(tokens)
    request_word_count.append(length)

#calculating the word count for each tokenized list using a list comprehension
request_word_count2 = [len(tokens) for tokens in request_token_list2]

#calculating the lexical diversity of each request (number of unique words divided by total)
def lexical_diversity(x):
    return len(set(x)) / len(x) 
    
lex_div = []
for tokens in request_token_list:
    num = lexical_diversity(tokens)
    lex_div.append(num)

#calculating the lexical diversity of each request using a list comprehension
lex_div2 = [lexical_diversity(tokens) for tokens in request_token_list2]

#calculate number of long words in each request
long_words = []
for tokens in request_token_list:
    words = [w for w in tokens if len(w) > 2]
    long_words.append(words)
    
count_long_words = []
for set_of_words in long_words:
    length = len(set_of_words)
    count_long_words.append(length)
    
count_long_words2 = [len(set_of_words) for set_of_words in long_words]

#check for existence of 'please' and return binary variable list using for-loop
please = []
for i in range(0,len(text)):
    value = text[i].lower().find("hi")
    if value == -1:
        result = 0
        please.append(result)
    else: 
        result = 1
        please.append(result)
        
#creating list comprehension to check for 'please' and profanity
please2 = [1 if re.search('hi', i) else 0 for i in text] 
profanity = [1 if re.search('shit|fuck.|bitch|ass', i) else 0 for i in text] 

#do much of the same as above for title and username
#creating variables for the request title and turning it from Series to a list
title = df.request_title[:5]
title_list = title.tolist()

#tokenizing the list using a normal for-loop
title_token_list = []
for i in title_list:
    tokens = word_tokenize(i)
    title_token_list.append(tokens)

#tokening the list using a list comprehension
title_token_list2 = [word_tokenize(title) for title in title_list]

#creating a list of the word count using a for-loop
title_word_count = []
for tokens in title_tokenized_list:
    title_length = len(tokens)
    title_word_count.append(title_length)

#creating a list of the word count using a list comprehension
title_word_count2 = [len(tokens) for tokens in title_token_list]

#checking for 'please' and 'love' in the title
please_in_title = [1 if re.search('please', i) else 0 for i in title] 
love_in_title = [1 if re.search('love', i) else 0 for i in title] 

#check for length
username = df.requester_username[:5]
username_list = username.tolist()

un_word_count = []
for i in username_list:
    count = len(i)
    un_word_count.append(count)
    
#check for declared throwaway account
throwaway = [1 if re.search('throwaway', i) else 0 for i in username] 

#social factors of success
#status (people give to higher status), similarity (users give to people 
#like themselves)
#check distribution for each of the following create categories (ex. age: 24hrs, month, year, longer)

#descriptive stats
requester_account_age_in_days_at_request
age = df.requester_account_age_in_days_at_request
plt.hist(age, bins=100, range=(age.min(),age.max()))
plt.hist(age, bins=30, range=(0,30))
plt.hist(age, bins=2, range=(0,1))
plt.show
df['day'] = [1 if i <= 1 else 0 for i in age]
df['month'] = [1 if i > 1 and i <= 30 else 0 for i in age]
df['year'] = [1 if i > 30 and i <= 365 else 0 for i in age]
df['longtime'] = [1 if i > 365 else 0 for i in age]

comments = df.requester_number_of_comments_at_request
plt.hist(comments, bins=100, range=(comments.min(),comments.max()))
plt.hist(comments, bins=30, range=(0,30))
plt.hist(comments, bins=2, range=(0,1))
plt.show

posts = df.requester_number_of_posts_at_request
plt.hist(posts, bins=100, range=(posts.min(),posts.max()))
plt.hist(posts, bins=30, range=(0,30))
plt.hist(posts, bins=2, range=(0,1))
plt.show

#calculate total upvotes/total votes
upvotes = df.requester_upvotes_minus_downvotes_at_request
total_votes = df.requester_upvotes_plus_downvotes_at_request
df['karma'] = upvotes/total_votes
    
#features that represent subreddit reputation
#dummy variable for whether it was the users first post to raop
first_post = df.requester_days_since_first_post_on_raop_at_request
df['first_post'] = [1 if i == 0 else 0 for i in first_post]

#dummy variable for whether the user has commented before
sub_comments = df.requester_number_of_comments_in_raop_at_request
plt.hist(sub_comments, bins=2, range=(0,1))
df['has_commented'] = [1 if i >= 1 else 0 for i in sub_comments]

#continuous variable for number of posts
sub_posts = df.requester_number_of_posts_on_raop_at_request
plt.hist(sub_posts)

#three types of flair to identify reciprocity (shroom=received, PIF=given after
#received, and None=neither)
flair = df.requester_user_flair
df['no_flair'] = [1 if i == 'None' else 0 for i in flair]
df['received'] = [1 if i == 'shroom' else 0 for i in flair]
df['given_after_received'] = [1 if i == 'PIF' else 0 for i in flair]

#identify weekends, weekdays, nights, days, and times near holidays
timestamp_utc = df.unix_timestamp_of_request_utc
day_time_str = [datetime.datetime.utcfromtimestamp(int(i)).strftime('%Y-%m-%d %H:%M:%S') for i in timestamp]
day_of_week = [datetime.datetime.utcfromtimestamp(int(i)).weekday() for i in timestamp_utc]
df['weekday'] = [1 if i < 5 else 0 for i in day_of_week]
