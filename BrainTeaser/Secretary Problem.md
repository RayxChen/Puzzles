## Question

Imagine you're interviewing candidates for a secretary position. There are n candidates, and you want to hire the best one. The candidates are interviewed one by one in random order, and after each interview, you must decide immediately whether to hire that candidate or not. If you reject a candidate, you cannot go back and hire them later. The goal is to maximize the probability of hiring the best candidate.

## Answer

Pass over first m candidates. The probability of selecting the best candidate when they appear at position k given that k > m is:

$$
P(\text{best candidate at } k) = \frac{1}{n}
$$


select best candidate at k = the best of k-1 must be in the m
$$
P(\text{select best candidate at } k \mid \text{best candidate at } k) = \frac{m}{k-1}
$$

The total probability of success is then given by summing this over all possible positions \( k \) from \( m+1 \) to \( n \):

$$
P(\text{success}) = \sum_{k=m+1}^{n} \frac{m}{k-1} \times \frac{1}{n}
$$



$$
P(\text{success}) \approx \frac{1}{e} \approx 0.368
$$

