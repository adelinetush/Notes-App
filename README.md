

# Diary-App

This application was built as part of the andela challenge. 

##### Project Url:
<!-- Put your project url here -->

Technologies:

* Python (Flask web framework)

* PostgresDB

* Vanilla JS + JQuery

* HTML5/CSS

## Setup:

Install the dependencies for the application

 ```pip install -r requirements.txt```
 
### Database Migrations:

Intitiliaze the migrations folder in the root of the application

```python manage.py db init```

_This process is carried out once on install_

Add the migrated tables to the migration:

```python manage.py db migrate```

Update the database 

```python manage.py db upgrade```

#### FLASK API Documentation

* Login

*Endpoint:* _/auth/login_

*Method:* GET

*Variables:* email (string), password(string)

*Response:* ```Boolean(True,False)```


* Register

*Endpoint:* _/auth/register_

*Method:* GET

*Variables:* email (string), password(string), username(string),

*Response:* 
```
{
    "email": "gumball@gmail.com",
    "name": "andelatest",
    "password": "$6$rounds=656000$uQqrvkphjUUNYiDl$XM4Tl31pKdipuzZStV.dBYE8FkBVgoJRKNc4NV1Zc3ekKAJnQaLKgPnbvWL68OBEPsatZ/BViSKhdj4JY4/Im/"
}
```

 * Add Entry

*Endpoint:* _/api/v1/ae_

*Method:* POST

*Variables:* 

```
{
  "email": "gumball@gmail.com", 
  "title": "some title",
  "notes": "Some notes here",
  "date": "01-10-2018"
}
```

*Response:* 

```
[
    {
        "date": "01-10-2018",
        "email": "gumball@gmail.com",
        "id": 1,
        "notes": "Some notes here",
        "title": "some title"
    }
]
```

* Update Entry

*Endpoint:* _/api/v1/ue_

*Method:* POST

*Variables:* 

```
{
    "date": "01-10-2018",
    "id": 1,
    "notes": "more notes 3",
    "title": "some title"
}
```

*Response:* 

```Boolean(True,False)```


* Get Specific Entry


*Endpoint:* _/api/v1/gse_

*Method:* GET

*Variables:* id (int)

*Response:* 

```
[
    {
        "date": "01-10-2018",
        "email": "gumball@gmail.com",
        "id": 1,
        "notes": "more notes 2",
        "title": "some title"
    }
]
```
* Get User Entry


*Endpoint:* _api/v1/gue_

*Method:* GET

*Variables:* email (string)

*Response:* 

```
[
    {
        "date": "01-10-2018",
        "email": "gumball",
        "id": 1,
        "notes": "more notes 3",
        "title": "some title"
    }
]
```




