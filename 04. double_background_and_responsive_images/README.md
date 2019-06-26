# Double background-images and responsive 3 sizes images
Overlaying background-images, screen-size and image optimization.

# Overlaying background-images:
Using CSS you can overlay background-images over each other. This is great when you want to make bottom image a gif and the top has a low opacity so it is transparent. This allows you to edit the color of the gif without editing it. You can also load multiple gifs over each other as a background.

# Background-images screen-size optimization:
With CSS and Media Queries there are the following sizes for screens:

/* Smartphones (portrait and landscape) ----------- */
@media only screen 

and (min-device-width : 320px) 
and (max-device-width : 480px)

/* Smartphones (landscape) ----------- */
@media only screen 

and (min-width : 321px)

/* Smartphones (portrait) ----------- */
@media only screen 

and (max-width : 320px)

/* iPads (portrait and landscape) ----------- */
@media only screen 

and (min-device-width : 768px) 
and (max-device-width : 1024px)

/* iPads (landscape) ----------- */
@media only screen 

and (min-device-width : 768px) 
and (max-device-width : 1024px) 
and (orientation : landscape)

/* iPads (portrait) ----------- */
@media only screen 

and (min-device-width : 768px) 
and (max-device-width : 1024px) 
and (orientation : portrait)

/* Desktops and laptops ----------- */
@media only screen 

and (min-width : 1224px)

/* Large screens ----------- */
@media only screen 

and (min-width : 1824px)

In the images folder there are 8 of the same background(firstback) that are different sizes. The different between the firstbackbigcomp(1.02 MB) -> Large Screen(min-width : 1824px) and firstbackmobile1(66.7 KB) -> Smartphone(min-device-width : 320px) are that when the user views the website on a large desktop they will get the higher pixel/size image while on a smartphone they will get the lower pixel/size image. So the background-images are optimized toward specific devices which allows fastest load time while loading optimized image size by device.

# Images Optimization:
Picture is stretch across screen so according to the max-width of the screen it will load one of three sizes.

Small: max-width: 700px

Medium: max-width: 1400px

Large: min-width: 1401px

Example image:

Small: codepart1ver3.png (31.9 KB)

Medium: codepart1ver2.png (93.5 KB)

Large: codepart1ver1.png (256 KB)


# Advantages of optimizing images with CSS:
Images files are widely used in web development. To be able to optimize them would decrease the amount of data sent from the server to the client. This is especially useful when the user is using mobile. The user would download >100 KB instead of a 1 MB file while keeping good pixel quality. While a desktop user would download the 1 MB file instead of the >100 KB so they wouldn't have a pixelated image. 