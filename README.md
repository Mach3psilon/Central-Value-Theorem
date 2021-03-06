If we add up a large number of values from almost any distribution, the distribution of the sum converges to normal. More specifically, if the distribution of the values has mean and standard deviation μ and σ, the distribution of the sum is approximately N(n*μ, n*(σ^2)). This is called the Central Limit Theorem.

 

Conditions:

The values have to be drawn independently.
The values have to come from the same distribution (although this requirement can be relaxed).
The values have to be drawn from a distribution with finite mean and variance.
The number of values you need before you see convergence depends on the skewness of the distribution.
 

The Central Limit Theorem explains, at least in part, the prevalence of normal distributions in the natural world. Most characteristics of animals and other life forms are affected by a large number of genetic and environmental factors whose effect is additive. The characteristics we measure are the sum of a large number of small effects, so their distribution tends to be normal. Another example can be the weight of a bag of potato chips which is actually the sum of the weights of many small independent contributions from each single chip.

 

I've plotted normalized histograms of generated values and normalized histograms of sums of generated values together with the theoretical normal distribution curve :

 

Experiment 1: Values are sampled from a standard uniform distribution independently. Number of values is 2.

Experiment 2: Values are sampled from a standard uniform distribution independently. Number of values is 10.

Experiment 3: Values are sampled from a standard uniform distribution independently. Number of values is 50.

Experiment 4: Values are sampled from a standard uniform distribution but not independently. Dependence is introduced by the following condition: If the current total is smaller than 40, the values are sampled from a uniform distribution between 0.5 and 1.5, otherwise between -0.5 and 0.5. Number of values is 100.

Experiment 5: Values are sampled from a distribution of semi-circle of radius 1 centered at 2. Number of values is 2.

Experiment 6: Values are sampled from a distribution of semi-circle of radius 1 centered at 2. Number of values is 10.

Experiment 7: Values are sampled from a distribution of semi-circle of radius 1 centered at 2. Number of values is 50.
