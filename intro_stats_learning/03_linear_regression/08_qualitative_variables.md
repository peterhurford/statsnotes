## Handling Qualitative Variables in Linear Regression

* What if we want to predict with a qualitative variable instead, or in addition to, quantitative variables?
* It turns out linear regression can handle predicting with qualitative variables by transforming them into quantitative variables.  These variables are called **dummy variables**.
* For example, a model that takes into account age and gender could be coded as follows: Y = β[0] + β[1]Age + β[2]Gender, where Age is the age in years and Gender is 0 if Male and 1 if Female.  Thus, a male observation would be Y = β[0] + β[1]Age whereas a female observation would be Y = β[0] + β[1]Age + β[2].
* In that gender case, β[2] is the average difference between males and females, β[0] + β[1]mean(Age) is the overall average for males and β[0] + β[1]mean(Age) + β[2] is the overall average for females.
* The choice to code females as 1 and males as 0 is arbitrary and choosing otherwise does not affect the regression -- it only affects the interpretation of β[2].

## Handling More than Two Levels

* Gender was easy because it only had two levels.  Harder would be to code something like race, where there is more than two levels.
* Since there is no ordinality among race, you cannot code race as 0, 1, 2, 3, etc.  Instead, you have to code it across multiple dummy variables.
* If we added race to our age + gender model, it would look like this: Y = β[0] + β[1]Age + β[2]Gender + β[3]Asian + β[4]White + β[5]Black, where Asian is 1 if the participant is asian (0 otherwise), White is 1 if the participant is white (0 otherwise), and Black is 1 if the particiant is black (0 otherwise).  The average Black male would be Y = β[0] + β[1]mean(Age) + β[5] and the average white female would be Y = β[0] + β[1]mean(Age) + β[2] + β[4].  A male who didn't fit into any of our racial categories would be just Y = β[0] + β[1]*mean(Age).
