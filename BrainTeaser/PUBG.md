## Question
Suppose every player has the same ELO rating. What is the expected number of players killed by the final winner?

## Answer
DP (The winner has a 1/k chance of being chosen)
$$ E_{k} =  \frac{1}{k}(1 + E_{k-1}) + \frac{k-1}{k}E_{k-1} $$

$$ E_{k} = E_{k-1} + \frac{1}{k} $$

$$ E_{k} \approx ln(k) + \gamma  $$ 
