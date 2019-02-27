# Python-Flask Program
2/26/2019 Update:
Keep trying to slove the data trans between from forms to making file, because we use session, i am wondering if i could use a dict or something to save the information. Also, could I make a json file to save the items i need to choose? It is much easier to maintaince.

SLOVED: data trans from customer choosen - > makefile
Need to be done: Finished All the choices. 


2/24/2019 Update:

In the beginning , i think use session is a good idea. But after learning , maybe @login_required is better solution. For the information got from form, it is similar like what you got from website when running a web crawler(of course lol), so I need a helper function to cleasn the data.




2/23/2019 Update:

Finished the Login.html, base.html and index.html with flask_bootstrap. Using csrf and wtforms and flask_wtf to make sure that the user input the right keywords to enter index.html. Also i want to use session["key"] to save a secret key so that i could verify the customer got the index.html from login.html, not just input index.html in the address.





2/21/2019 Update:

This is a Python - FLask Program. I am tring to make a personal website to generate a txt file with special formate for a software. I will use flask to host it. Although django is more powerful, but i think dont think i will use all the functions. So flask is better for me.

Used Package:
Pip3 Install Flask ,
Pip3 Install Flask-WTF ,
Pip3 Install bootstrap-flask ( not flask-bootstrap cause it is too old ) ,
pip3 install flask-sqlalchemy ,
pip3 install flask-mail
pip3 install flask-login
