# Welcome to the Inze project.
###

Inze was idealized to help people to understand and follow up their spents with credit cards.
Throught a csv version of invoices, the idea is to classify and organize your spents to let you know, how much, how often and where you're spending your money.
Using charts and graphs the application will show you how you spents are changing during the time and what is the things you've most spent money by the time.

>*This application is being constructed, so some things are very "manual", for now. **AND AT THIS MOMENT, JUST WORKS FOR NUBANK'S INVOICES!***

<br />
<br />
<br />

# To install the application dependencies:

First of all, make sure that the "static" folder, has permissions of read and write, on your OS. These folder is where the application will save the uploaded csv.

The seccond step is to install all the project dependencies. To do this run the following commands on terminal:
    
```bash
    $ pip (or pip3) install -r requirements.txt
```


#### **IMPORTANT:** 
> THIS APPLICATION AND ITS INSTALLATION ARE FULL TESTED ON LINUX BASED OS. FOR OTHERS, THIS STEPS COULD BE DIFFERENT (DEPPENDING OF HOW YOU'VE PREPARED YOUR DEVELOPMENT ENVIRONMENT TOO).
#### **TIP:** 
> AS A GOOD PRATICE, I RECOMMEND YOU TO INSTALL ALL THIS PACKAGES USING A VIRTUAL ENVIRONMENT.


<br />
<br />
<br />

# To run the application:

After install all the dependencies, you must run the api first and then the front-end, using the following command:
```bash
    python inze/manage.py runserver #To start the API.
    cd inze_web && yarnn start #To start the user interface.
```
The API runs on the port 8000 and the frontend runs at port 3000.

That's two commands will start the django application that works as the application API and a react APP that works as the front-end.

Once you input your CSV files, the application, for now, will just list all the spents ordered by date (desc) on a table
