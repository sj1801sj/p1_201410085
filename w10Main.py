allData = [
["Coffee","Water","Milk","Icecream"],
["Espresso","No","No","No"],
["Long Black","Yes","No","No"],
["Flat White","No","Yes","No"],
["Cappuccino","No","Yes","No"],
["Affogato","No","No","Yes"]
    ]

data=allData[1:]
print data
print "coffee count =", len(data)

for i in data:
    print i[0], i[2]

for i in data:
    if i[2].upper()=="YES":
        print "milk coffee=", i[0]
print "milk coffee count=", len(i[2])

print float(len(i[2]))/float(len(data))


raw_input()