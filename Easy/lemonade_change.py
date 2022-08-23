"""At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a
time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10,
or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer
pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every
customer with the correct change, or false otherwise.



Example 1:

Input: bills = [5,5,5,10,20]
Output: true
Explanation:
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
Example 2:

Input: bills = [5,5,10,10,20]
Output: false
Explanation:
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.


Constraints:

1 <= bills.length <= 105
bills[i] is either 5, 10, or 20."""

"""This solution is rather simplistic, and it just emulates step-for-step what you would imagine this looking like IRL.
Definitely feels like there's a better solution than this."""


def lemonadeChange(bills):
    stock = []

    for bill in bills:
        if bill == 5:
            stock.append(5)
        elif bill == 10 and 5 in stock:
            stock.append(10)
            stock.remove(5)
        elif bill == 20 and (5 in stock and 10 in stock):
            stock.append(20)
            stock.remove(10)
            stock.remove(5)
        elif bill == 20 and (stock.count(5) >= 3):
            stock.append(20)
            stock.remove(5)
            stock.remove(5)
            stock.remove(5)
        else:
            return False

    return True


"""This is the exact same idea as the solution above, but implemented with a dictionary rather than a list. It's much
faster, but it still seems slow, and there's probably still something better."""


def lemonade_change2(bills):
    stock = {5: 0,
             10: 0}

    for bill in bills:
        if bill == 5:
            stock[5] += 1
        elif bill == 10 and stock[5]:
            stock[10] += 1
            stock[5] -= 1
        elif bill == 20 and stock[5] and stock[10]:
            stock[5] -= 1
            stock[10] -= 1
        elif bill == 20 and stock[5] >= 3:
            stock[5] -= 3
        else:
            return False

    return True


# After looking
"""Turns out there wasn't anything much better."""
