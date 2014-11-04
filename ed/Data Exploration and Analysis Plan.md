I'm still at the data cleaning phase and organization of the project.

I have a data set with all of the wage and hour violations in the country for the last 6 years, it has 188000 records.

I have data sets for New York, Chicago and San Fransisco for health inspection violations.

I am going to merge the whd data set with the health violations data set.

Then I will create a binary variable for "has ever violated" for  the health inspections.

Each health inspection for the data sets has different qualifiers for the severity of violations.

New york has "CRITICAL FLAG,	SCORE	, and GRADE"

San Fransisco has a "risk category"  from low to high, and a violation type

Chicago has a "pass/fail" a "Risk" from "one to three" and the violation type.

I will build my model first on the binary of whether or not the establishment has every had a violation, 
then build it on a binary variable for whether it has had a high risk variable. 

Beyond that I will explore if the score in the new york data has an impact on the probability that it will also have a 
whd violation.

Also I will explore if there is a coorelation between different types of violations of the health inspections and if that also
correlates to a higher probability for whd violations. 





