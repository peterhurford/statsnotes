## Qualitative vs. Quantitative

* Dealing with qualitative values.  These are values without **ordinality** (inherent relative order).
* Profits is quantitative, because it is a continuous, quantifiable number.  It has ordinality -- $300 in profits is more than $200 in profits.
* Educational achievement is quantitative but not continuous -- there is sixth grade, but there isn't 6.2993th grade.  But it has ordinality -- sixth grade is more than fifth grade.
* Eye color (e.g., green eyes, brown eyes, blue eyes) is neither quantitative nor continuous.  There is no ordinality -- brown eyes are not more than green eyes.
* If I assign people into random groups by number -- Group 1, Group 2, etc -- this appears qunatitative because there are numbers involved, but there is no ordinality -- Group 2 isn't greater than Group 1 just because 2 > 1.
* Therefore, eye color and random number groups are examples of qualitative values, whereas profits and educational achievement are examples of quantitative values.


## Classification

* Classification deals with predicting qualitative values, just as regression dealt with predicting quantitative (and, more specifically, continuous) values.


## Examples of Classification Problems

1.) Someone arrives at a hospital with certain symptoms.  Which disease do they have?

2.) An online transaction took place with certain characteristics.  Was that transaction fraudulent?

3.) A flight took off with certain characteristics.  Where is that flight headed?

4.) A customer takes out a loan and has a certain credit history.  Will that customer default?


## Predicting Default

* "Will a customer default?" is represented mathematically as asking for P(default = Yes).
* This can be modeled as asking whether the probability of default exceeds a certain threshold.  P(default = Yes) = Pr(default) > Threshold.
* We can then model this probability given the credit history of the customer.  P(default = Yes | CreditHistory).
