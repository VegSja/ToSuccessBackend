# ToSuccess - Backend infrastructure
This is the backend infrastructure for the ToSuccess project.
## About
This server is currently hosted by pythonanywhere. For more info visit their website

### Technologies
This REST API was created using DJANGO's restframework and is entirely written in Python.

### Authentication
The API is secured with OAuth authorization. In the frontend the user registers using its google account. The frontend sends a request to Google which gives a token back which gives access to this backend. The user will send this to the backend and the backend registers a new user if it doesnt already exist. After this is successfull the backend sends a access token and refresh token. The accesstoken is switched often to prevent attacks, and a refresh token is needed to regain access.

### HTTP requests supported
It is important to note that every request made to the server needs to be authorised. That implies. In the header of the request, the frontend should attach the access token. Because the access token is constently being refreshed, the user might experience that it is beeing rejected access. That is why the frontend should try to send a refresh request before each HTTP request.

The header of the HTTP request could in Axios look like this:
```
 "Authorization": `Bearer ${this.token}` 
 ```

#### Activities
- https://root/activities/ 
    - GET --> Returns a list of activities for the user which posted the requests
        - Parameters: 
            - date (in day number in year. I.E 31.December is 365 in  a normal year)
            - nb_days (for how many days in the future do you wish to recieve activities?)
    - POST --> Create activity in DB
        - Required JSON fields:
            - activity_name
            - activity_category
            - minutes_after_midnight_start
            - minutes_after_midnight_end
            - date --> As in daynumber of year
            - date_string --> On format DD. MMMMMMM YYYY

- https://root/activities/<int:activity_id>/
    - GET --> Returs only the details of the given activity
    - DELETE --> Deletes the activity from the database

     
#### Categories
- https://root/categories/
    - GET --> Returns every category on a given user
    - POST --> Saves a category to DB
        - Required JSON fields:
            - Name
            - Color --> In hexadecimal
- https://root/categories/<int:category_id>/
    - GET --> Returns the details of a category
    - DELETE --> Deletes given category

#### Stats
- https://root/stats/
    - GET --> Returns hours per day per activity, and total actiivty time in  a given time frame
        - Requires HTTP-parametes:
            - start_date --> Grab date from this date
            - end_date --> To this date

#### Session management
- https://root/google/
    - Required payload:
        - Token from google OAuth
    - Returns:
        - access_token: Token for access to backend
        - refreash_token: Refresh token
- https://root/refresh/
    - Required payload:
        - refresh_token
    - Returns:
        - Valid access token
- https://root/logout/
    - Required patload:
        - Refresh token
        - Access token
- https://root/date/
    - Returns:
        - date --> in date string
        - daynumber --> The current daynumber

