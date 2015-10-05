## Non-Additive Linear Models

* Variables in a model can have **interaction effects**, where one variable affects another's effectiveness on the DV.
* Consider a marketing example, where you want to predict the impact on sales of advertising on TV or advertising on the radio.  Now imagine that more advertisements on the radio increase the effectiveness of advertising on TV, because some people will hear both.  This is an interaction effect (or a synergy effect as it is called in marketing).
* If you create the equation Y ~= β[0] + β[1]X[1] + β[2]X[2], then there is no way changes in β[2] could affect β[1], so we don't capture any interaction effects.
* Instead, we create a third variable, β[3], that models this interaction effect (called an **interaction term**), and rewrite the model as Y ~= β[0] + β[1]X[1] + β[2]X[2] + β[3]X[1]X[2].
* Now, β[3] shows the influence of X[1] and X[2] on each other, and if β[3] != 0, then a change in X[1] will also lead to a change in the impact of X[2] on Y.

## Heirarchical Principle

* Sometimes β[3] could be statistically significant even if β[1] and β[2] are not.  In this case, however, we still must include β[1] and β[2] in our model if we are to include β[3], regardless of the statistical significance.  This is called the **heirarchical principle**.  Forgetting this principle is how I got a C- on the final for Econometrics class.
* The rationale is that X[1] and X[2] correlate a lot with X[1]X[2] (obviously), so leaving them out alters the meaning of the interaction.  Also, if we know X[1]X[2] has a statistically significant impact, the need to interpret X[1] and X[2] individually is less important, so we don't need to worry about excluding them from the model.


## Interactions Between Quantitative and Qualitative Variables

* Earlier we considered a model that took into account age and gender, as follows: Y = β[0] + β[1]Age + β[2]Gender, where Age is the age in years and Gender is 0 if Male and 1 if Female.  What if there were an interaction effect between age and gender?
* We could then have the model be like this: Y = β[0] + β[1]Age + β[2]Gender + β[3]Age*Gender.
* This means that a male observation would be Y = β[0] + β[1]Age, whereas a female observation would be Y = β[0] + β[1]Age + β[2] + β[3]Age.  β[1]Age represents the **main effect** of age on Y for all genders, whereas β[3]Age would represent the **interaction effect** of age specifically for females on Y.
