
# The Trading bot

This is a trading strategy for prediction markets mediated by the logarithmic market scoring rule
(LMSR) market maker. The base trading algorithm has access to noisy information about the true probability that an event
will occur. The security payoff depends on the probability of the event. The information received by the trading bot is in the form of biased coin tosses from the true distribution;
one thing to be aware of is that the true distribution can change over time. The Trading bot algorithm is pitted against other competing trading algorithms.
