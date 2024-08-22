## Question
There is a 6x8 rectangular chocolate bar made up of small 1x1 bits. We want to break it into the 48 bits. We can break one piece of chocolate horizontally or vertically, but cannot break two pieces together! What is the minimum number of breaks required?

## Answer
for n x 1 we need n-1\
for n x 2 we need 1 + 2*(n-1)\
for n x 3 we need 2 + 3*(n-1)

so for n x m it's $$m \times n - 1 $$