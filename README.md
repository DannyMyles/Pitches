# Pitches

## Author:  [DannyMyles](https://github.com/DannyMyles/)

## Description
An application that allows users to use that one minute wisely. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.

You can view the site at:


## User Stories
* As a user, I would like to see the pitches other people have posted.
* As a user, I would like to vote on the pitch they liked and give it a downvote or upvote.
* As a user, I would like to be signed in for me to leave a comment
* As a user, I would like to receive a welcoming email once I sign up.
* As a user, I would like to view the pitches I have created in my profile page.
* As a user, I would like to comment on the different pitches and leave feedback.
* As a user, I would like to submit a pitch in any category.
* As a user, I would like to view the different categories. 


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display pitch categories | **On page load** | List of various categories of pitches |
| Display tabs with  category | **On Tab link click** | Clickable links to open pitches by category |
| Display profile | **Click profile page** | Redirected to a page with your profile |
| Display pitches | **On page load** | Each pitch displays author, title, pitch, date comment tab |
| To add a pitch  | **Click an add pitch** | Redirected to the pitch collection form|

## Application link


## SetUp / Installation Requirements
Run 
``git clone https://github.com/DannyMyles/Pitches.git``

or download the zip file from github.

After extracting the files, 

1. Navigate to the project folder
>`` cd Pitches.`` 

2. Creating a virtual environment
>``virtualenv virtual.``

3. Activating the virtual environment
>``source virtual/bin/activate.``

4. Running the application
>``python3 manage.py server``


### creating a DATABASE
1. Go to your terminal Install postgress bt [run]
>``sudo apt-get install postgresql postgresql-contrib libpq-dev``
2. Open your shell by using 
>``psql``
3. Create database by 
>``CREATE DATABASE pitchy``
4. Connect to your database by
> ``/c pitchy``
<!-- 5.To view your database structure use
 >``select from Users;`` -->


##### Exporting database configurations
* export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}

* Use ``pip install`` with the version of your text editor
* To render the page live locally, run ``Python3 manage.py run``

## Known Bugs
* Still editing on mail search authentification for signup template.

## Technologies Used
* Python3.8
* Flask
* Bootstrap5
* Css3
* Html5

## License

Copyright (c) 2021 DannyMyles
