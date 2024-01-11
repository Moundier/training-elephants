# server-py

A server for python machine learning 

- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `deactivate`

### Documenting ideas
1. User-Based Recommendation: Retrieves, from similar users, their most interacted items.
   - (Idea): Recommends items based on the preferences (filters) and behaviors (interactions) of users with similar profiles.
	- (Func): get_similar_users()
	- (Func): get_last_10_recommendations_from_user_recommendation_history()

2. Item-Based Recommendation:Retrieves user interactions and returns similar items based on previous interactions.
   - (Idea): Recommends items that are similar to those the user has interacted with in the past. (interactions_history)
	- (Func): save_each_interaction -> get from interaction_history_table
	- (Func): find_most_interacted_items_per_week -> interaction_history_table
	- (Func): generate_item_based_recommendation -> send to user
	- (Func): delete_too_old_recommendation_history() -> yearly

3. Content-Based Recommendation: Users select filters, and based on those, the system returns similar items.
   - (Idea): Recommends items that are similar in content or characteristics to those explicitly specified by the user.
	- (Func): user_choose_contents() -> max of 20
	- (Func): limit by 20, just as Youtube, so users cant choose more than 20 or limit by 10, and get the other 10 from item-based
	- (Func): user can change, but we remove by ascending order the previous firsts

### Todo list (09/12/2023)
- [x] Implement User-based recommendation
- [x] Implement Item-based recommendation
- [x] Implement Content-based recommendation

### Todo List (20/12/2023)
- [ ] Elaborate Persistence Backend (Java)
- [ ] Elaborate Algorithmic Backend (Python)

[We must have other users for performing user_based_recommendation]
[We must have similar_items for performing item_based_recommendation]
[User must set some filters for performing content_based_recommendation]
[Initially we recommend_from_the_previous_history, but only if there is any]
[Then we recommend the top 10 or 20 most popular]
[??We return directly the prev interactions or, we get the prev interactions, and on them we run item-based recommendation]
[Create an admin space with angular]
[This admin space controls the system, based on the metrics] [example: users that login_counter more the 2 times a day are a good source of ]

### Mobile Ideas
- Continue Reading Section
- Most Popular


- Netflix sees indirectly, what kindof content category fits well for me
