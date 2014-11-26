## Project First Draft

###Problem statement and hypothesis
Reddit is a community message board of sorts where users communicate and organize over just about any topic.  One such subreddit community is called Random Acts of Pizza.  Reddit users post requests for free pizza in this subreddit explaning their situation and why they need pizza.  Some user requests result in free pizaa, while others dont. The goal of this project is to build a model to predict what kind of requests will result in the requester receiving free pizza.  The hypothesis is that users who write a detailed request, have been Reddit users for a long time, who make a request on a weekday, and who have given pizza away before are more likely to receive a free pizza.

###Description of your data set and how it was obtained
This dataset includes 5671 requests collected from the Reddit community Random Acts of Pizza between December 8, 2010 and September 29, 2013 (retrieved on September 30, 2013). All requests ask for the same thing: a free pizza. The outcome of each request -- whether its author received a pizza or not -- is known. Meta-data includes information such as: time of the request, activity of the requester, community-age of the requester, etc.

Each JSON entry corresponds to one request (the first and only request by the requester on Random Acts of Pizza). We have removed fields from the test set which would not be available at the time of posting.

####Data Fields
"giver_username_if_known": Reddit username of giver if known, i.e. the person satisfying the request ("N/A" otherwise).

"number_of_downvotes_of_request_at_retrieval": Number of downvotes at the time the request was collected.

"number_of_upvotes_of_request_at_retrieval": Number of upvotes at the time the request was collected.

"post_was_edited": Boolean indicating whether this post was edited (from Reddit).

"request_id": Identifier of the post on Reddit, e.g. "t3_w5491".

"request_number_of_comments_at_retrieval": Number of comments for the request at time of retrieval.

"request_text": Full text of the request.

"request_text_edit_aware": Edit aware version of "request_text". We use a set of rules to strip edited comments indicating the success of the request such as "EDIT: Thanks /u/foo, the pizza was delicous".

"request_title": Title of the request.

"requester_account_age_in_days_at_request": Account age of requester in days at time of request.

"requester_account_age_in_days_at_retrieval": Account age of requester in days at time of retrieval.

"requester_days_since_first_post_on_raop_at_request": Number of days between requesters first post on RAOP and this request (zero if requester has never posted before on RAOP).

"requester_days_since_first_post_on_raop_at_retrieval": Number of days between requesters first post on RAOP and time of retrieval.

"requester_number_of_comments_at_request": Total number of comments on Reddit by requester at time of request.

"requester_number_of_comments_at_retrieval": Total number of comments on Reddit by requester at time of retrieval.

"requester_number_of_comments_in_raop_at_request": Total number of comments in RAOP by requester at time of request.

"requester_number_of_comments_in_raop_at_retrieval": Total number of comments in RAOP by requester at time of retrieval.

"requester_number_of_posts_at_request": Total number of posts on Reddit by requester at time of request.

"requester_number_of_posts_at_retrieval": Total number of posts on Reddit by requester at time of retrieval.

"requester_number_of_posts_on_raop_at_request": Total number of posts in RAOP by requester at time of request.

"requester_number_of_posts_on_raop_at_retrieval": Total number of posts in RAOP by requester at time of retrieval.

"requester_number_of_subreddits_at_request": The number of subreddits in which the author had already posted in at the time of request.

"requester_received_pizza": Boolean indicating the success of the request, i.e., whether the requester received pizza.

"requester_subreddits_at_request": The list of subreddits in which the author had already posted in at the time of request.

"requester_upvotes_minus_downvotes_at_request": Difference of total upvotes and total downvotes of requester at time of request.

"requester_upvotes_minus_downvotes_at_retrieval": Difference of total upvotes and total downvotes of requester at time of retrieval.

"requester_upvotes_plus_downvotes_at_request": Sum of total upvotes and total downvotes of requester at time of request.

"requester_upvotes_plus_downvotes_at_retrieval": Sum of total upvotes and total downvotes of requester at time of retrieval.

"requester_user_flair": Users on RAOP receive badges (Reddit calls them flairs) which is a small picture next to their username. In our data set the user flair is either None (neither given nor received pizza, N=4282), "shroom" (received pizza, but not given, N=1306), or "PIF" (pizza given after having received, N=83).

"requester_username": Reddit username of requester.

"unix_timestamp_of_request": Unix timestamp of request (supposedly in timezone of user, but in most cases it is equal to the UTC timestamp -- which is incorrect since most RAOP users are from the USA).

"unix_timestamp_of_request_utc": Unit timestamp of request in UTC.

###Description of any pre-processing steps you took
The full script is saved as "raop_code.py" in my project folder.

I read the JSON data into a Pandas DataFrame and created new features using NLTK for the text and DATETIME for the dates.  I also created categorical variables using regular expressions to search for the presence of profanity or "please" in the request text, a word count of the request, as well as the lexical diversity.

I also used GENSIM to run topic modeling on the request texts.  I fit a Latent Dirichlet Allocation (LDA) model and generated 10 different topics that the requests fall into, and generated dummy variables for each. 

###What you learned from exploring the data, including visualizations
Requests from accounts that were created 24 hours before the request were less likely to receive pizza.  Longer requests were positively correlated with receiving pizza.

###How you chose which features to use in your analysis
I chose word count, account age, weekday post, and whether it was the requester's first post in the subreddit as the features to use to start out.  Word count, account age, and whether it was the requester's first post all have a statistically significant effect on whether the requester received pizza.

###Details of your modeling process, including how you selected your models and validated them
I fit the data to a logit model and classified the request as 1 if the probability of receiving pizza was greater than or equal to .5, and 0 if it was less than .5.  

###Your challenges and successes
The model accurately classified 76% of the requests.  While the specificity was 99%, the sensitivity was only .04%.  In other words, the model is an accurate predictor of requests that didn't receive pizza, but a terrible at predicting those who actually did.  This is likely because of a class imbalance, i.e., the majority of requests do not result in receiving pizza.

###Conclusions and key learnings
This is a bad model.
