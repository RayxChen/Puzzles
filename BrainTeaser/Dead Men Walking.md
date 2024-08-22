## Question
Assume 100 zombies are walking on a straight line, all moving with the same speed. Some are moving towards left, and some towards right. If a collision occurs between two zombies, they both reverse their direction. Initially all zombies are standing at 1 unit intervals. For every zombie, you can see whether it moves left or right, can you predict the number of collisions?

## Answer

label the zombies from 1-100, when a collision happens we can just swap the number of zombies so that equivalently they can pass each other. Then for zombie at position x, if it moves to left the collisions will be the sum of the zombies whose position < x moving to the right. Similar logic for the other side.
