# drf-authentications

In project All Type of DRF Authentications are Applied

Basic Authention: 

Users of the REST API can authenticate by providing their in each request username and password within an HTTP header. To use this method of authentication with HTTP methods, such as POST, PATCH, and DELETE must also be provided, as well as a user username and password.

It appropriate for testing only but to use in production make it over https only


Session Authention: 

Users of the REST API can authenticate by providing their  request username and password within an HTTP header only one time than using session id we futher proceeded.To use this method of authentication with HTTP methods, such as POST, PATCH, and DELETE must also be provided, as well as a user username and password.

It appropriate for testing only but to use in production make it over https only




Token Authention: 

Users of the REST API can authenticate by providing their username and password  and we will provide them unique token now by using these token we can give them grant and deny for different parts of api.
In user send token in each request than server will authenticated and provide them appropriate response to clients.

To use this method of authentication with HTTP methods, such as POST, PATCH, and DELETE must also be provided, as well as a user username and password.

It appropriate for testing only but to use in production make it over https only


JWT Authention: 

Users of the REST API can authenticate by providing their username and password  and we will provide them unique token now by using these token we can give them grant and deny for different parts of api.
In user send token in each request than server will authenticated and provide them appropriate response to clients.
Now These are not stored in our system beacuse we using third-party pacakges so it goog for performance of website that not making much querie to it backend(db).
Token will expire in specific time and using refresh token user can reshresh their api token

It appropriate for those webiste having those having lots of user requests and request rate high and JWT is  also better and secure than Other Authentication Scheme's 
