Welcome to the Inze project.


This is a application that's being constructed, so some things are very "manual", for now.


*****************************************************************************************************************************
*                                   THIS APPLICATION, AT THIS MOMENT, JUST WORKS FOR NUBANK'S INVOICES!                     *
*****************************************************************************************************************************

To run the application:

First of all, give to the "static" folder, full permissions of read and write, on your OS. These folder is where the application will save the uploaded csv.

The seccond step is to install all the project dependencies. To do this run the following commands on terminal:
    
    $ pip (or pip3) install flask
    $ pip install flask_cors

=============================================================================================================================
!!          IMPORTANT:                                                                                                     !!
!!              THIS APPLICATION AND IT'S INSTALLATION SEQUENCE IS TOTALLY VALID TO THE LINUX BASED OS. FOR OTHERS, THIS   !!  !!              STEPS WOULD BE DIFFERENT                                                                                   !!
!!              (DEPPENDING OF HOW YOU'VE PREPARED YOUR DEVELOPMENT ENVIRONMENT TOO)                                       !!
!!          TIP:                                                                                                           !!
!!              AS A GOOD PRATICE, I RECOMMEND YOU TO INSTALL ALL THIS PACKAGES USING A VIRTUAL ENVIRONMENT.               !!
=============================================================================================================================

After install all the dependencies, you must run the api using the following command:
    $ python csv_api.py
    or
    $ python3 csv_api.py
This will start a flask web api on the 8082 port. That's necessary for the UI can access the application.

The last step is to open the "ui/index.html" folder to get access to a csv upload page. It's allowed to select every kind of file, but the system just will 
process csv files.

When you input your CSV files, the application, at this moment, just return to you a JSON array with your data processed. 
