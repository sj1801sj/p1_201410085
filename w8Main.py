﻿def CharCount(word):
    d=dict()
    for c in word:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    print d
    
CharCount('parksojeong')



def lab8():
	word='parksojeong'

def main():
	lab8()

if __name__=="__main__":
	main()

raw_input()