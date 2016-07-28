import random
import other_bots
import traders
import run_experiments
import plot_simulation
import numpy as np


class MyBot(traders.Trader):
    name = 'my_bot'

    def simulation_params(self, timesteps,
                          possible_jump_locations,
                          single_jump_probability):
        """Receive information about the simulation."""
        # Number of trading opportunities
        self.timesteps = timesteps
        # A list of timesteps when there could be a jump
        self.possible_jump_locations = possible_jump_locations
        # For each of the possible jump locations, the probability of
        # actually jumping at that point. Jumps are normally
        # distributed with mean 0 and standard deviation 0.2.
        self.single_jump_probability = single_jump_probability
        # A place to store the information we get
        self.information = []
        self.belief = 50.0
        self.ssumprice, self.lsumprice = 0.0, 0.0

    def new_information(self, info, time):
        """Get information about the underlying market value.

        info: 1 with probability equal to the current
          underlying market value, and 0 otherwise.
        time: The current timestep for the experiment. It
          matches up with possible_jump_locations. It will
          be between 0 and self.timesteps - 1."""
        self.information.append(info)

    def trades_history(self, trades, time):
        """A list of everyone's trades, in the following format:
        [(execution_price, 'buy' or 'sell', quantity,
          previous_market_belief), ...]
        Note that this isn't just new trades; it's all of them."""
        self.trades = trades

    def trading_opportunity(self, cash_callback, shares_callback,
                            check_callback, execute_callback,
                            market_belief):
        """Called when the bot has an opportunity to trade.

        :type execute_callback: object
        cash_callback(): How much cash the bot has right now.
        shares_callback(): How many shares the bot owns.
        check_callback(buysell, quantity): Returns the per-share
          price of buying or selling the given quantity.
        execute_callback(buysell, quantity): Buy or sell the given
          quantity of shares.
        market_belief: The market maker's current belief.

        Note that a bot can always buy and sell: the bot will borrow
        shares or cash automatically.
        """
        # Place a randomly sized trade in the direction of
        # our last information. What could possibly go wrong?
        # quantity = random.choice(xrange(1, 100))
        # if (self.information[-1] == 1
        # and check_callback('buy', quantity) < 99.0):
        # execute_callback('buy', quantity)
        # elif check_callback('sell', quantity) > 1.0:
        # execute_callback('sell', quantity)

   '''     if 0 < len(self.trades) < 3:
            execprices = []
            for row in self.trades:
                execprices.append(row[0])
            for x in range(0, len(execprices)):
                self.ssumprice += float(execprices[x])
                self.lsumprice += float(execprices[x])
            self.ssumprice /= len(execprices)
            self.lsumprice /= len(execprices)
        elif 3 < len(self.trades) < 20:
            execprices = []
            for row in self.trades:
                execprices.append(row[0])
            for x in range(len(execprices) - 3, len(execprices)):
                self.ssumprice += float(execprices[x])
            for x in range(0, len(execprices)):
                self.lsumprice += float(execprices[x])
            self.ssumprice /= 3
            self.lsumprice /= len(execprices)
        elif len(self.trades) >= 20:
            temptrade = self.trades[-20:]
            execprices = []
            for row in temptrade:
                execprices.append(row[0])
            for x in range(len(execprices) - 3, len(execprices)):
                self.ssumprice += float(execprices[x])
            for x in range(len(execprices) - 20, len(execprices)):
                self.lsumprice += float(execprices[x])
            self.ssumprice /= 3
            self.lsumprice /= 20
        # print self.ssumprice
        # print self.lsumprice
'''
        avg = 0.0

        for x in range(0, len(self.information)):
            avg += self.information[x]

        avg = (avg*100) / len(self.information)

        self.belief = (self.belief + avg + market_belief) / 3
        # print "belief %d avg %d market %d" % (self.belief, avg, market_belief)

        Flag = True
        x = 20
        while True:
            if check_callback('sell', x) > self.belief and Flag:
                execute_callback('sell', x)
                Flag = False
            elif check_callback('buy', x) < self.belief and Flag:
                execute_callback('buy', x)
                Flag = False
            else:
                if x == 1:
                    break
                x -= 1


        '''
        if self.belief < self.lsumprice:
            execute_callback('sell', 2)
        elif self.belief > self.lsumprice:
            execute_callback('buy', 2)
        '''


def main():
    bots = [MyBot()]
    bots.extend(other_bots.get_bots(5, 2))
    # Plot a single run. Useful for debugging and visualizing your
    # bot's performance. Also prints the bot's final profit, but this
    # will be very noisy.
    #plot_simulation.run(bots, lmsr_b=150, timesteps=100)

    # Calculate statistics over many runs. Provides the mean and
    # standard deviation of your bot's profit.
    run_experiments.run(bots, simulations=1000, lmsr_b=150, num_processes=2, timesteps=100)

# Extra parameters to plot_simulation.run:
# timesteps=100, lmsr_b=150

# Extra parameters to run_experiments.run:
# timesteps=100, num_processes=2, simulations=2000, lmsr_b=150

# Descriptions of extra parameters:
# timesteps: The number of trading rounds in each simulation.
# lmsr_b: LMSR's B parameter. Higher means prices change less,
# and the market maker can lose more money.
# num_processes: In general, set this to the number of cores on your
# machine to get maximum performance.
# simulations: The number of simulations to run.

if __name__ == '__main__':  # If this file is run directly
    main()
