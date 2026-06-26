Booklist=[445,"think and grow rich","nepolan hill";44.9]
print[Booklist]
print()
print(Booklist)
print(type(Booklist))

print(len(Booklist))

for i in Booklist:

    print(i)
    print(Booklist[2])
    print(type(Booklist[2]))
    print(type(Booklist[3]))
    Booklist.append("ABC publisher")
    print(Booklist)
    Booklist.insert(1,1977)
    print(Booklist)
    Booklist.remove(44.9)
    print(Booklist)
    


