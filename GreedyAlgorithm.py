#    KNAPSACK
# weight and price of items are given you have to find the best optimal solution
# we use greedy algorithm when we havee to maximize or minimize something

w=[4,3,2]
p=[20,18,14]
max_weight=7

# What we'll do is while knapsack is still not full, we will do a greedy choice.
#  We will choose the item number i which has the maximum value of vi over wi,
#  which is the value per unit of weight. And then if this item fits into knapsack fully, 
# then take of all this item. Otherwise, if there is only few space left in the knapsack, 
# take so much of this item as to fill the knapsack to the end. And then in the end, 
# we'll return the total value of the items that we took and how much did we take of each item.

l=[]
for i in range(len(w)):
    l.append(p[i]/w[i])
l=list(sorted(l,reverse=True))
weight=0
profit=0
while weight<max_weight:
    pass



#
    
