## Prototype web app for Biobots Code Challenge

This is a rough prototype to read through the bioprinter prints dataset "bioprint-data.json".
The data is ingested in a mongoDB collection and accessed through an app built with Django.

## MongoDB Database initialization

[MongoDB Installation](https://docs.mongodb.com/manual/installation/)

Importing the JSON dataset in mongoDB:

> mongoimport --db 'biobots' --collection 'bioprints' --drop --file 'bioprint-data.json' --jsonArray

## Running the web app in Dev Server

> python manage.py runserver


## Web app usage

url: [localhost/bioprintviewer]('http://localhost/bioprintviewer/')

enter either:
1. User ID of the form 'user_XXX'
2. 'manager' for access to all bioprinter users' data


## Troubleshooting DB Connector

Updating connector / Synching DB:
> python manage.py syncdb

If SITE_ID issue:
> AutoField (default primary key) values must be strings representing an ObjectId on MongoDB (got u'1' instead). Please make sure your SITE_ID contains a valid ObjectId string.

Solve with:
```bash
> python manage.py shell
```

```python
> from django.contrib.site import site
> s = Site()
> s.save()
> exit()
```

```bash
> python manage.py tellsiteid

The default site's ID is u'57c4b5a4393d508ac41f0cde'. To use the sites framework, add this line to settings.py:
SITE_ID=u'57c4b5a4393d508ac41f0cde'
```
