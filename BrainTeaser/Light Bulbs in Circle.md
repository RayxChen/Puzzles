## Question
In a circle are light bulbs numbered 1 through n, all initially on. At time t, you examine bulb number t, and if it’s on, you change the state of bulb t + 1 (modulo n); i.e., you turn it off if it’s on, and on if it’s off. If bulb t is off, you do nothing. Prove that if you continue around and around the ring in this manner, eventually all the bulbs will again be on.

## Answer

n (n > 1) bit binary number 111

t=0
101

t=1
101

t=2
001

t=3
001

t=4
001

t=5
101

t=6
111

t=7
110...

for every position in the binary number it can either be 1 or 0 (as its previous position can either be 1 or 0) except full 0 (as there will be no last execution to switch the last 1 to 0). Then this creates a power set except full 0, these states will keep rotating so it will go back to full 1 again.



