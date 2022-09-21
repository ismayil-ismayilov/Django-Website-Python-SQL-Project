# Review-website---Python-SQL-Project
- - - 
### Info
The website to post a review about Mediamarkt stores, Departments in Germany and Poland. The website is built on Django Framework. 

### Requirements
The main goal of the project to make a fully functioning website:
    - sign up, login and logout (certain pages should have access only to logged in users)
    - obtain access to full functionality of the application using web/windows interface
    - connect and operate on the SQLite database:
        * min number of tables equals 5
        * SQL queries (incl. complex selects [based on 3 tables], indexes, triggers, views)


### Project Description
Below is a short project description. You may find whole project report in the PDF file.

A signed up and logged in user has an access to a page where it is possible to review a Media Markt department. For that, he has to choose City and Media Markt Store, and regarding Department.
Reviews are on 5 star rating.
Logged in user can edit his own but not delete the review or edit to other users' reviews.
Everyone has an access to reviews statistics dashboard. On that page, a visitor/user can see average rating per each City, Store and Department.
    * Both  –  ORM and Raw SQL queries has been used in the project to calculate and group the average ratings by city, store and departments.

