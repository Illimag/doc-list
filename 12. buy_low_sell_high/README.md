Buy Low Sell High

This is a conceptual algorithm that I'm trying to figure out how to write.

To start out, maybe what the algorithm will do is from 10 currency pairs it picks one. 

How will it pick out:

Maybe based on year to year, month to month, week to week, day to day trend.

It is not easy to predict the future, but maybe it just needs to be one that has a high probablity.

After it picks out 1 currency pair, it will do a buy order.

For EX: 

	XLM/USD

	DAY[0] = .10
	BUY 1

	DAY[1] = .09
	DAY[2] = .07
	DAY[3] = .09
	DAY[4] = .10
	DAY[5] = .12
	DAY[6] = .13
	SELL 1

With this method the algorithm will wait until the price of the currency pair is ALWAYS higher than the purchased price, so there can never be a loss..

The risks are that maybe the price will drop and never go back to the purchased price.

So maybe there should be something in the algorithms that states, if the price of the currency pair drops a certain amount then sell.

For EX:

	if XLM/USD
		Decreases more than 50%
	Sell

Also there should be something that tells it when to sell it at it's high point.

For EX:

	if XLM/USD
		Increases more than 30%
	Sell

The algorithm should place buy orders and then hold onto them, as in keep track of them while placing more buy orders.

For EX:
	
	DAY[0]
	XLM/USD BUY @ .10
	DAY[1]
	XRP/USD BUY @ .32
	DAY[2]
	BAT/USD BUY @ .13
	XLM/USD SELL @ .13
	DAY[3]
	XLM/USD BUY @ .11

There needs to be a way to reduce the level of risk.

Basically only making 1 trade per day, is too high risk. Because it will either be 100% correct or 0% correct.

So instead of making 1 trade per day, it maybe better to make 5 trades a day. This way if 2 trades end up incorrect and need to be sold for less than purchase price, the 3 trades can make up the difference as well as a profit.

The main focus is to always be increasing the holdings. It doesn't matter about the money being made.

As so.

What needs to be done is trade against other crytocurrency trading pairs.

For example:

Stellar Lumens : XLM

Ripple : XRP

Bitcoin : BTC

XLM/BTC : 0.00002161

XRP/BTC : 0.00006168

XLM/USD : 0.11519894

XRP/USD : 0.32934736

BTC/USD : 5337.83333073

So to allow certain kinds of trades, need to find an exchange that had these types of trading pairs.

So for example:

XRP/XLM : 2.814

BTC/XLM : 45,871.56

There is the StellarX platform.