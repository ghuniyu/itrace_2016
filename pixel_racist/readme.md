##[Pixel Racist Challenge](http://task-00001001.itrace.systems/racist.php) (70pts)
---
>Task : Find the color with the least amount. and send post request with color parameters e.g. "color=fff000"

##Writeup
---
`racist.php` will be generate new random pixel image with random color every time we doing a request.
we have to find the color with the least amount

i'm using python `PIL` to getting every pixel in the images and groupby from itertools to grouping color decimals
then, just find the smallest group to get the answer.

###"Python it and we've done"

##Flag :
###`ITRACE{y0u_6uy5_4r3_4wes0m3}`
