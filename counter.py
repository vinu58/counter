array = ("xy","yz","yy","xy","xy","yy")

counts = {}
for n in array:
    total = counts.get(n,0)
    #print total
    counts[n] = total + 1
print counts
    
 


      
