# iframe_nav
Custom navigation built with iframe, Javascript, Jquery

# Folder system
real_css

    - main.css

real_js

    - index.js

index.html

test_page_1.html

test_page_2.html

test_page_3.html

# Problem:
Wanted a navigation that would allow the user to navigate to different pages without the website reloading. Basically a single page application type navigation. But didn't want to use a framework because heavy boilerplate code. Looked into Vue but wanted something even more simple, didn't want to add another library.

# Solution: 
Index.html has nav and iframe. Iframe allows .html page to load on another .html page, also will load all files on same server no problem. Navigation with click event that passes data-src of li element's .html to iframe's src. This allows the user to stay on index.html page while the navigation loads different .html pages on top of it depending on what button is clicked on the nav. 

# Addition: 
Added CSS .active1 class which shows which button is currently active. Then with jQuery created function that removesClass .active1 from current and addClass to clicked via classSelector.

Ran into issue when trying to build button on loaded page. An example would be if there is two buttons on test page 1, (Go to test page 2) and (Go to test page 3). If test page 2 button is clicked via href the page is loaded but navigation css .active1 would not be on correct li. More difficult because the selected id of buttom is in the DOM of test_page_1.html but it would need to change the css of the navigation in the DOM of index.html. 

The solution was using parent and window.frame functions to allow cross-DOM selecting. To test if this works the code needs to be uploaded to a live server. Test will not work local. 