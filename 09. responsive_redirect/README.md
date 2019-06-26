# responsive_redirect
URL redirect methods for Desktop and Mobile applications. 

# iframe Redirect:
Using JavaScript create two variables: Phone and Web. Each variable has its own iframe with it's own src link. Then create another variable with the screen width. If screen width is smaller than 768 then it is var Phone  = iframe src.

With this method in mind, I created two heroku servers hosting applications built specifically towards mobile or desktop. Then entered the URL to the correct iframe variables. Then created a S3 bucket with AWS for the single html page as the main server. The html page on AWS redirects to the heroku applications without leaving the AWS server. 

# direct Redirect:
The index.html page loads the Javascript that says if the screen is greater or equal to 699 then load index_desktop.html instead. If the screen is not greater than nothing happens and the index.html loads normally. 

# When mobile responsive isn't optimal:
Mobile responsive web design is a great solution to a wide spread problem. But for some applications there just isn't a really good way to optimize it to mobile. Designing web applications mobile first is nice in theory, but the viewing experience with desktop is so different that it could end up being easier to design two seperate applications. 