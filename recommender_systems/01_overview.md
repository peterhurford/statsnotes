#### Goals of Recommender Systems

* Recommender systems exist to make money.
* Optimizing making money is difficult, instead one typically optimizes secondary goals:
  * **Relevance** - a recommender system should return results that are relevant to the user.
  * **Novelty** - a recommender system should return results that the user has not seen before.
  * **Serendipity** - a recommender system should show _some_ results that _surprise_ the user and unlock new tastes and avoid staleness of recommendations.
  * **Diversity** - a diverse set of recommendations is more likely to have a hit and will be more interesting.

#### Two Problems for Recommendation

* **The prediciton problem** - For a grid of user-product combinations, fill in the unobserved values with predictions of how the user would rate the item. This is also called the **matrix completion problem**.
* **The ranking problem** - Match a user with the top _k_ recommendations for that user. (Or, match a product with the top _k_ users who would be most interested in that product.) This can, but does not have to, involve predicting the entire matrix.
