#Function that calculates the stock price, total profit, comission to broker, and stock sell price. Broker fee is fixed at 3%, broker receives comission for both sale and purchase

numShares = int(input("Enter the number of shares purchased: "));
pricePerShare = float(input("Enter the price paid per one share: "));
numSold = int(input("Enter the number of shares you sold: "));
priceSold = int(input("Enter the price sold per one share: "));
brokerFee = ((numShares * pricePerShare) * .03);
brokerSale = ((numSold * priceSold) * .03);
totalGain = (((numShares * pricePerShare) - brokerFee) - ((numSold * priceSold) - brokerSale));

print();
print("Number of shares purchased:                         ", numShares);
print("Broker Comission (BUY):                             ", brokerFee);
print("Price per share (BUY):                              ", pricePerShare);
print("Number of shares sold:                              ", numSold);
print("Broker Comission (SELL):                            ", brokerSale);
print("Price per share (SELL):                             ", priceSold);
print("Total Gain/Loss:                                    ", totalGain);

