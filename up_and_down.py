def up_and_down():
    target = input("pressed target: ")
    count = 0
    
    while(1):
        number = input("pressed number: ")
        count = count+1
        if(target == number):
            print "biggo"
            print count
            break
        else:
            if(target>number):
                print "up"
            else:
                print "down"
                
up_and_down()
raw_input()