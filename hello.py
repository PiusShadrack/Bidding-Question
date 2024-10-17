my_list=[]
bid_continue=True

while bid_continue==True:
    bid=int(input("Enter bidding amount: \n"))
    my_list.append(bid)
    
    answer=input("Is there another bidder? yes/no: ").lower
    if answer=="yes":
        bid_continue=True
    elif answer=="no":
        #bid_continue=False
        exit()
    
        
print(my_list)