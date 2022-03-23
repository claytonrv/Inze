# Welcome to the Inze project.
###

Inze was idealized to be a helper to understand and follow up spents with credit cards.
Using a csv version of invoices, the idea is to classify and organize your spents, and show their behaviors during the time to bring up, how much, how often and where money is being spent.
Using charts and graphs the application shows how the spents are changing during the time and what is the most spent categories where the money is going to.

>*This application is being constructed, so some things are quite "manual", for now. **Currently it only works for Nubank's invoices***

<br />
<br />
<br />

# To install the application dependencies:

First step is to install all the project dependencies. To do this run the following commands on terminal:
    
```bash
    $ pip install -r inze/requirements.txt

    $ cd inze_web && yarn install
```

<br />
<br />
<br />

# To run the application locally:

After install all the dependencies, you must run the api first and then the front-end, using the following commands:
```bash
    python inze/manage.py runserver #To start the API.
    cd inze_web && yarn start #To start the user interface.
```
The API runs on the port 8000 and the frontend runs at port 3000.

That's two commands will start the django application that works as the application API and a react APP that works as the front-end.

Once you input your CSV files, the application, for now, will just list all the spents ordered by date (desc) on a table
