amount = int(input("enter your amount"))
note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10
print(note_1,note_2,note_3)