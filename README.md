# webscrap--BeutifulSoup
It's a small but highly efficient task which helps the users to track a product and get a pvt mail  when there is a fall in price or discount !!


Basic reuirements :- python 3.7 0r pycharm ,Beautiful Soup , requests.

It will call the beautifulSoup to import the  objects, documents, links and services required to web scrap !
It's a smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.

URL = The product link which you want to scrap

Give a varaible named preferably headers,
headers = dict { "key" : 'values' }

key = user agent.
value = To get this, type " my user agent" in google and paste it

create a function to CHECK PRICE

var a = requests.get ( url, headers )
the url and the headers will fetch the data from the concerned site , that is the work of .get

varb = call BeautifulSoup( get content from page )

html.parser , it will break the contents with the help of html syntax

print( varb.prettify())
it will print whole of the contents from that page.

title = get the product tile using the product-id (.get_text)
price = get the product price using the price-id (.get_text)[slicing the value]

convert the price into float and replace the rupees symbol with none.

 when the price is less than actual price , you will receive a mail ! bingo ! 
 
 create a function to SENT MAIL!
 
 start the server by calling the smtplib.SMTP , its gennrally a networking protocal which calls the function by using 
 
 server.echlo, this is a command which is like helo to the host server and the client server 
 
 server.starttls, it starts the connection between the servers with host 
 
 server.ehlo, the client server will respond to it 
 
 server.login ( which uses a mail id , two way authentication cose for secure connectivity )
 
 server.sendmail with a subject and the respective amazon link 
 
FINALLY ,  server.quit() which will quit the server connection. 

