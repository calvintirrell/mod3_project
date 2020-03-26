# mod3_project

Business Understanding:

While our data did not come with much of a description, we concluded that it was data provided from a phone service provider trying to figure out how to keep customers from leaving. We then decided from this conclusion that the most important thing for this company to be able to predict is if a customer is about to leave so that they may be able to incentivise a customer to keep doing business with them. With this knowledge of the problem we then determined having a small false negative rate (predicting a customer would stay when are actually canceling their service) would be the most important factor to building a successful model. Now you might be thinking what about false positives (predicting a customer would leave when they actually are staying), well in this case it is a lot cheaper for a company to give someone a better deal when they are planning on staying anyway than losing a customer that they thought would keep doing business with them. Which brought us to focusing on our Recall score first and foremost and an f1 score second to make sure we are not just giving away incentives. 


Data Understanding:

Again we did not have any backround explanations on what each category meant, but the luckily enough the labels were simple and easy to understand. A couple question still did pop up though that we needed to make assumptions on, with the biggest of all being 'is account length categorized in days, weeks or months?'.

Data Preparation:

Step 1: Ran multiple models on the given data without any editing to the features. Doing this showed us that Random Forest and Gridsearchcv models gave us the best Recall values for our data. So from here we began our journey into feature engineering to find out which model between these too would give us the best balance between high recall and f1 scores.

Step 2: For feature engineering we tried alot of things from using OneHotEncoder to encode our State and Zipcode categories, to adding and dividing columns together to create new features. Though overall we found out our model had the highest correlation being the total amount a person was spending on this service.


