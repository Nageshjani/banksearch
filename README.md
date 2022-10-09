# Indian Bank Finder app
### URL: https://banksearch44.herokuapp.com/


This is simple bank searching django-app. This app's Database is connected to aws rds postgresql database and hosted on heroku.






For frotned : **Javascript,Bootstrap , css**
For Database: **AWS RDS POSTGRESQL**
For Backend: **Python Django**



**This app has Following Main Functionalities**
1. Fetch Banks Data By Using Bank Name & City Name:
   * e.g Bank Name :'HDFC BANK', City:'Ahmedabad'
   * output: List Of All Branches
   
   
   
2. Fetch Specific Bank Data By Using Only IFSC code:
   
   * 'e.g': Ifsc Code :'HDFC0000006'
   * 'Output': Branch Details
 

To import db in postgres: *psql indian_bank < indian_banks.sql*
 
# Running The Serverpython manage.py runserver

# Migrate python manage.py migrate


