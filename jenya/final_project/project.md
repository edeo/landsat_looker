Name: Effectiveness of promotional campaign with the use of various value promo codes.

Objective:
	Analyse promo codes campaign and determine if the amount of promo code influences the user's ride volume.
	Compare event_driven promo codes vs user_referred promo code programs.

Desired_outcome:
	User takes at least one extra ride after the promo_code ride.

Background:
	Company regularly performs marketing campaigns where a new user received a promo code valued at either $5, $10, or $20. There is currently no research done to show which of the amounts is most effective in attracting long-term users if at all

Definitions:
	* New user: a user who has never had an account with the company before
	* Promo-code ride: a ride that a user takes with the use of received promo code
	* Frequent user: a new user who will take at least one more ride besides the initial "promo code ride"
	* Event driven promocode: promo code that was distributed at a marketing event or media campaign rather than through user generated referral
	* User referral promo_code: a promo code that is passed through an existing user. 

Study groups:
      * User referral campaign: a promo code that is passed through an existing user. "Refer a friend. You get $15 and your friend gets $15 towards their first ride".
      * Other promo code campaign: a promo code is shared through media other than existing user.

Hypothesis:
	* A user is directly influenced by the amount of the promo code. The higher the promo code value, them more likely user will take a future ride.
	* A user is indifferent to the amount of the promo code and will as likely to take another ride with a $5 promo code as with $20.

Bonus: If amount does not have direct correlation to likelyhood of repeated purchase, determine other attributes that might affect it.
       * "friend" influence. If referred by a person who is an active user vs non-active user
       * Location. Cities with higher number of providers, or higher ride volume
       * Gender of the user. Hypothesis: women are more likely to choose a safe cab ride rather than an Uber ride.


_END_

Ideas:
	* Research trends in the taxi rides
	* Design ride grading algorythm and find how ride grading correlates to other attributes.
	* Attempt to predict if higher grades improve successful ride pickup
	* Attempt to predict correlation between increased ride quantity and user behavior vs driver behavior
	* Research correlation between successful ride pickup and other trends:
		 * current marketing efforts (PR campaigns, promo codes)
		 * number of successfull fin transactions
		 * number of user_on_site (gps issues, user not showing up => driver upset and not willing to accept future rides)
		 * [!!!] tip amount the driver receives from the app user and how it affects driver's desire to accept future rides
		   	 ** do app users tip higher/lower in the app than other users that pay by cash or cc
		 * fleet trainig / overall driver rating
		 * seasonal or weather changes
		 * 

Assumptions:

Data:
	* data available for 2009 - 2014
	* data will be queried according to research needs
	* data will be available either in one or many tables
