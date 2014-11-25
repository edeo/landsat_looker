# Course Project -- Predicting neighborhood growth in Washington, D.C. using real estate data
#####By Dan Matthews

### Null Hypothesis

There is no way to predict above-average neighborhood growth in Washington, D.C. using real estate data.

### Alternative Hypothesis
Using data from Trulia.com, it is possible to predict which neighborhoods will have above-average growth on a year over year basis.

## Background

### Reason for choosing this project
Growing up in D.C. and watching it develop these past 20+ years has been a fascinating experience.  This was especially highlighted when I left for four years for University and returned to a vastly different  landscape.  Given the massive growth and gentrification Washington has experienced in the last decade, I thought it may be an interesting endeavour to attempt to identify if there are any meaningful traits high-growth neighborhoods have in common.   

### Data Dictionary
| Header | Header |
| -------- | -------- | 
| hood_requests | list of the 124 neighborhoods in Washington, D.C. and corresponding unique IDs used by Trulia| 
| hoods | list of 124 unique neighborhood IDs in Washington, D.C. | 
| stats | raw data pulled using the Trulia API containing all info Trulia stores on neighborhoods in its original data structure |
| avg_prices | cleaned average pricing data for each of the 124 neighborhoods separated by week| 
| traffic | cleaned visitor traffic data from Trulia.com (% of all neighborhoods in DC) |

### Initial Data Structure
 *  listingStats
   * listingStat
     * [0] *9 elements*
       * listingPrice
         * subcategory
           * [0]
             * averageListingPrice
              * medianListingPrice
              * numberOfProperties
              * type
       * weekEndingDate
         * [date]
 * location
   * city
     * Washington
   * heatMapURL
     * [url]
   * neighborhoodGuideURL
     * [url]
   * neighborhoodId
     * [int]
   * neighborhoodName
     * [string]
   * searchResultsURL
     * [url]
   * state
     * DC
 * trafficStats
   * trafficStat
     * [0] *31 elements*
       * date
         * [date]
        * percentCityTraffic
          * [int]
        * percentNationalTraffic
          * [int]
        * percentStateTraffic
          * [int]

### Final Data Structure
avgPrices.csv:

|Neighborhood ID: | 3456 | 7548 | 7548 |
| -------- | -------- | -------- | -------- |
| 2012-01-04 | 839425 | 557224 | 8796563 |
| 2012-01-04 | 879371| 566829 | 875932 |
| 2012-01-04 | 773456 | 547223 | 854821 |
| ---- | ---- | ---- | ---- |
| 2014-01-04 | 534724 | 437349 | 658245 |
| 2014-01-04 | 768414 | 876539 | 864945 |
| 2014-01-04 | 573369 | 436234 | 854832 |

traffic.csv

|Neighborhood ID: | 3456 | 7548 | 7548 |
| -------- | -------- | -------- | -------- |
| 2012-01-04 | 1.2 | 3.4 | 2.3 |
| 2012-01-04 | 1.4| 6.3 | 6.3 |
| 2012-01-04 | 1.5 | 2.3 | 1.2 |
| ---- | ---- | ---- | ---- |
| 2014-01-04 | 2.3 | 2.3 | 3.3 |
| 2014-01-04 | 4.5 | 2.5 | 2.8 |
| 2014-01-04 | 3.4 | 5.4 | 2.9 |

## Data Exploration and Analysis
I began by gathering all the data from Trulia.com using their python package.  The data came in a number of nested dictionaries as explained above in the Initial Data Structure section.  A majority of my time was spent cleaning and aggregating this data into usable data structures.  To date, I have finally prepared my data for analysis and will be using the rolling window functions found in Pandas to analyze my data over time.  Speficially, I am anticipating `rolling_var` and `ewma` (exponentially-weighted moving average) to be the most helpful formulae in prediting `avgPrices` and `traffic`.
### Data Issues
* The initial data structure was a nightmare to tackle and get meaningful data from.
* Converting time strings into Timestamp objects so as to take advantage of the Pandas time functions.  I used `datautil` in Pandas to accomplish this.


### Achievements To Date
* Obtained data using Trulia's API
* Cleaned data using Pandas
* Explored the Time Series in Python for Data Analyis enough to understand and apply the formulae

