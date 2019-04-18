
# TEAM SeeTheLight(STL) - ANGAZA APP

## Contributors
[Simon Injiri](https://www.github.com/injiri)<br>
[Brian Wandera](https://www.github.com/wandesky)<br>
[Charles Njenga](https://www.github.com/Hackitect)<br>
[Catherine Wanjiru](https://www.github.com/kateshiru)<br>



The Project consists of a machine learning model that is the backend of our project. When given a link for a news story, it generates a report on the credibility of that article. It does this by using a trained model that is able to detect real of fake news. The logic for this is accessible through an API hosted on Heroku and our different front ends will query this API to return 4 variables i.e. percentage of confidence, whether real or fake, subjectivity and polarity.

## Machine Learning Model
Training the model
we researched a lot on the methods and processes of detecting fake news and also give credit to various individuals who had done previous works on machine learning to tackle this problem.
https://www.npr.org/sections/alltechconsidered/2016/12/05/503581220/fake-or-real-how-to-self-check-the-news-and-get-the-facts
http://www.cs.cmu.edu/~dhdavis/LSFinalProject.pdf 
Machine learning projects are reliant on finding good datasets. If the dataset is bad, or too small, we cannot make accurate predictions. A collection of labeled fake news and real news (top credible news sources from https://webhose.io/free-datasets/ was used to train a Naive Bayes model to predict probabilities of fake news based on article text. The metrics are subjectivity, polarity, real, fake.
Machine learning works by finding a relationship between a label (real or fake)  and its features. We do this by showing an object (our model) a bunch of examples from our dataset, the dataset used in this case had about 4000 articles of which 2000 were identified fake articles and 2000 were identified real stories. Each example helps define how each feature affects the label. We refer to this process as training our model.
Features are independent variables which affect the dependent variable called the label. In this case, we have 2 labels i.e. real and fake that is affected by all the features that denote a story as either real or fake. We used the estimator object from the Scikit-learn library for simple machine learning. Estimators are empty models that create relationships through a predefined algorithm

Algorithms used include
- Naive Bayes Classifier technique - prior probability that news is real / fake then combine with bayesian measure of likelihood, Finally we classify news as real/fake since its class membership achieves the largest posterior probability for that particular label.
- Logistic Regression
- Neural Network (MLPclassifier) - Multi Layer Perceptron (from scikit-learn) - supervised learning algorithm that learns a function f  by training on a dataset

## IP address/Domain reputation checker
The Angaza API also queries the Tallos Intelligence Resources and the Public API for Apility.io for much of the analytics in regards to IP and Domain Checker. These three checks -IP address blacklist, Domain blacklist and IP address historical blacklist- are summarized and returned as a global score for the IP address.

This API call also returns detailed information about the IP address from different sources:
- when the domain was registered and the registrar
- IP Geolocation
- AS information
- WHOIS informaton
- Blacklists where the IP address was found (if any).
- Blacklists where the Hostname was found (if any).


## Android Application
The project does not require a user to download any machine learning library but only download the apk of the application from this site https://drive.google.com/file/d/1nAvX97uhTnjMkT_q4RkZ4-tbi_gMBIsv/view?usp=sharing.
After installing the android application, the user will be able to paste the urls into the application and it is parsed in the API of the machine Learning model

![alt text](https://github.com/AndelaHacks/see-the-light/blob/develop/photos/WhatsApp%20Image%202018-11-10%20at%2011.46.47%20AM.jpeg)

## Web Plugin 
It works on the same procedure as the android app but by having a Web Extension being installed in the browser which extacts the webpage being browsed and parses the data using the Machine Learning model API.

## API Endpoints
The API endpoint to check the authenticity of a news article is:
[Click Here To View A Demo of the API]
```(https://stl-v2.herokuapp.com/api/v2/get?url=https://stackoverflow.com/questions/24892035/python-flask-how-to-get-parameters-from-a-url)```

