#Giraudo Francesco Es. 19

def cheese_and_crackers(cheese_count, boxes_of_crackers): #function cheese_and_crackers definition with two args
    print(f"You have {cheese_count} cheese!")   #print the amount of cheese
    print(f"You have {boxes_of_crackers} boxes of crackers!")   #print the boxes of crackers
    print("Man that is enough for a party!") 
    print("Get a blanket.\n")

print("We can just give the functions numbers directly: ")
cheese_and_crackers(20,30)  # calling the function cheese and crackers with numbers as arguments

print("OR, we can use varibles from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # calling the function using variables

print("We can do math inside of: ")
cheese_and_crackers(10+20, 5+6) # calling the function using math operations as arguments

print("And we can combine the two, variables and math: ")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000) # calling the function combining math and variables

#Study Drills
#   1. Go back through the script and type a comment above each line explaining in English what it
#      does.
#   2. Start at the bottom and read each line backward, saying all the important characters.
#   3. Write at least one more function of your own design, and run it 10 different ways.

def sumOfTwo_OrMore(a,b,*otherArgs):
    c = []
    c.extend(otherArgs)
    tot = a + b
    for element in c:
        tot += element
    print(f"The sum is: {tot}")

addend1, addend2, addend3 = 7,2,9

sumOfTwo_OrMore(addend1, addend2)
sumOfTwo_OrMore(addend1, addend2, addend3)

sumOfTwo_OrMore(addend1+1, addend1-3, addend3**2)
sumOfTwo_OrMore(addend1**2, addend3**0)

sumOfTwo_OrMore(4, 56, -34)
sumOfTwo_OrMore(4-1, 5)

sumOfTwo_OrMore(addend1 - addend2, addend1)
sumOfTwo_OrMore(addend1+addend3, addend2)

sumOfTwo_OrMore(1,2)
sumOfTwo_OrMore(1,2,3,4,5,6)