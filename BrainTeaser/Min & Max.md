## Question
Given an array of n numbers. Finding minimum takes n-1 comparisons. Finding maximum takes n-1 comparisons. If you had to simultaneously find both minimum and maximum, can you do it in less than 2n-2 comparisons?

## Answer
The key is to pair up the min and max.
Find the max (then min is automatically the other one in the pair) of n/2 pair. Then find the max of the max in pair and min of the min in pair. Total comparisons 3n/2.