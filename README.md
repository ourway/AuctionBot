# The Auction Bot

This Project consists of the market trading bot named Trader Joe and basic votecount algorithms running off of data from actual 2009 election data of the City of Aspen.

# Trader Joe

This is a trading bot that has been designed with a trading strategy for prediction markets mediated by the logarithmic market scoring rule
(LMSR) market maker. The base trading algorithm has access to noisy information about the true probability that an event
will occur. The security payoff depends on the probability of the event. The information received by the trading bot is in the form of biased coin tosses from the true distribution;
one thing to be aware of is that the true distribution can change over time. The Trading bot algorithm is pitted against other competing trading algorithms.

# Voting Counts

The voting count menthods that have been implemented on the data are:

### Approval Voting
### Borda Count
### Instant Runoff
### Plurality Vote

##### The data that have been used on the algorithms can be found at : http://www.preflib.org/data/election/aspen/. 
##### The description of the data format can be found at: http://www.preflib.org/data/format.php.

It can be observed that each of the voting methods have differnt results.
