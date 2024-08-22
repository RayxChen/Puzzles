## Question
A & B are alternately picking balls from a bag without replacement. The bag has k black balls and 1 red ball. Winner is the one who picks the red ball. Who is more likely to win, the on who starts first, or second?

## Answer
It doesn't really need calculation. 1 red ball has equal prob to be in all the positions. if k is odd which means k+1 is even, then A and B have the same chance to draw from the bag, but if k is even then k+1 is odd, the first one has one more chance to draw so he has higher prob to win. \
_ _ 1 _ _ _ \
_ _ _ 1 _ _  \
_ _ _ 1 _ _ _ 

P(xi): prob to win at ith draw

$$ P(A1) = \frac{1}{k+1}$$

For B2 it should not be conditioned on A1's failure 
$$ P(B2) = \frac{1}{k}$$ 

$$ P(A3) = P(\overline {A1})P(\overline {B2}) \frac{1}{k-1} = (1 - \frac{1}{k+1})(1 - \frac{1}{k}) \frac{1}{k-1} = \frac{1}{k+1}$$


if k = 2n + 1
$$ P(A) = (n+1)\frac{1}{2n+2} = \frac{1}{2} $$
if k = 2n (+1 red ball)
$$ P(A) = (n+1)\frac{1}{2n+1} = \frac{n+1}{2n+1} > \ \frac{1}{2}$$ 


