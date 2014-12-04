Ed O'Brien
DAT3
11/25/2014


#Problem statement and hypothesis

How can we choose what companies we investigate in a better way to increase the probability of chosing companies that have minium wage and 
overtime violations? Can we use health inspection data to predict Fair Labor Standards Act ( the law that regulates minumum wage and overtime pay)
violations?

NYC has a data set of over 500,000 rows on the restaurantes in the city. I am hoping to use features from that 
data set to predict minimum wage and overtime violations.

Description of your data set and how it was obtained
I used two tables: nycwagefull.csv and nyc.csv.
nycwagefull.csv is a row for every wage and hour investigation that has happened in the state of new york since 2008.
nyc.csv is the health inspection data for health inspecitons in reasturantes in NYC. 

Description of any pre-processing steps you took
I have several files showing how I processed the raw data.
The main problem was that the addresses in the two files were not written in a standard format, so when I tried to join the two tables,
there were not many matches. Pandas sees ' 233 east third street' and '233 E third street' and '233 east 3rd st' as three distinct strings.

First I brought in the two tables in as different data frames. 

I got help creating a regular expression script to strip these strings of elements that might cause two addresses to not match. 

after creating a series from this regular expression, I added it back to both data frames.  I called that series 'clean' since it was a cleaned version of the address. 

I then filtered the nycwagefull.csv data frame for only investigations that happened in zipcodes inside new york city. 
I had done this before on the larger csv that is all investigations since 1985, however many of the restuarants have closed down, so 
it didn't help for matching businesses up. 

after the filter I tried merging the two frames together on the clean column. I found that there were a lot of incorrectly 
connected because there were two many addresses that when stripped of thier information would match addresses that were not 
really the same. 

see my project in project_obrien.py and planb.py

What you learned from exploring the data, including visualizations
I learned that I have to either come up with a new stretagy to match the companies, or I need a new stragey for predicting 
violations. 

I think I am going to try and predict based on the industry and state that the companies are in. 


How you chose which features to use in your analysis
Details of your modeling process, including how you selected your models and validated them
Your challenges and successes
Possible extensions or business applications of your project
Conclusions and key learnings

"""
get all of the nychealth data.
my gut "hypothesis" is that there will be some coorolation between people who volate
wage laws and people who violate health code laws. 
my first goal was to sort the data and then try and see if i can join
the health records by the location and business.

question : as "score" rises, does probability for labor violation rise? 
if they are flagged critically, does that make it more likely?:
Or, explore 538 arcticle.    
