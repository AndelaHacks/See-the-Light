# TEAM SeeTheLight(STL) - ANDELA NEWS HACKATHON

## Contributors
[Simon Injiri](https://www.github.com/injiri)<br>
[Brian Wandera](https://www.github.com/wandesky)<br>
[Charles Njenga](https://www.github.com/Hackitect)<br>
[Catherine Wanjiru](https://www.github.com/kateshiru)<br>



The Project consists of a machine learning model that is the backend of our project. The ML model tests and trains it's data using the WebHouse Dataset which we implemented as an API used in the Android app and the front end web plugin.

The output displays a percentage confidence of real or fake, similarity of text to title, and polarity of the text.

## IP address/Domain reputation checker
The service checks if the domain / IP Address is in any blacklist and also compares the historical information of the IP address.
These three checks -IP address blacklist, Domain blacklist and IP address historical blacklist- are summarized and returned as a global score for the IP address.

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

## Web Plugin 
It works on the same procedure as the android app but by having a Web Extension being installed in the browser which extacts the webpage being browsed and parses the data using the Machine Learning model API.




