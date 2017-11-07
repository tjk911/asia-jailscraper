Setting up the environment
--------------------------

We created a virtual environment (using `virtualenv env`) which allowed us to write our scraper in a safe environment. 

A virtual environment can be thought of as a sandbox - we can do whatever we want and then just step out of it.

We then activated it by running the command `source env/bin/activate`.

From there we created a file called **`app.py`** with the command `touch app.py`, where we will write the actual code required to scrape the site we're looking for.

Next, we installed *`requests`* and *`BeautifulSoup`* by running `pip install requests` and `pip install BeautifulSoup`.

Fetching the webpage
--------------------------

We opened up **`app.py`** and at the top, we imported the three libraries that we needed for this part of the project.

 - Requests ([the documentation is here, linked to their quickstart page](http://docs.python-requests.org/en/latest/user/quickstart/))
 - CSV ([the documentation is here, linked to the writer part that we used](https://docs.python.org/2/library/csv.html))
 - BeautifulSoup ([the documentation is here, linked to their latest 'Get Started' page](https://www.crummy.com/software/BeautifulSoup/bs4/doc/))

We had the URL that we wanted ready, and defined it as `url`
We used *requests* to fetch the `url` and called the result `response`
We needed, specifically, the HTML of the page which was inside of `response.content`, so we created another variable called `html`

---
note: we could have combined all this into a single line by typing 
> `html = requests.get("http://apps2.whatcomcounty.us/onlineapps/jailrosters/bookings/booking.jsp").content`

But that would have been really ugly - as you can see above. Generally it's better to write code that you can read instead of code that's efficient.

---- 

Using BeautifulSoup
--------------------------

We used *BeautifulSoup* to "read" the ugly `html` and we called it `soup`.

Changing over to Firefox/Chrome, we right-clicked and inspected the table we were interested in scraping. We looked for a defining attribute of the table by hovering over the different elements.

We found that it was the attribute 
>xmlns = "http://www.w3.org/1991/xhtml"

So we used BeautifulSoup to find that table, and we creatively called it `table`.

> table = soup.find('table', attrs={"xmlns":"http://www.w3.org/1991/xhtml"})

---
(to be continued)

Future Goals
----

1. Run file daily
2. Match with another list of names
3. A way to be notified