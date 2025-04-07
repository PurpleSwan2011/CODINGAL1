class flashcard:
        def __init__(self,word,meaning):
                self.word=word
                self.meaning=meaning
        def __str__(self):
                return self.word+'('+self.meaning+')'
flash=[]
print("welcs")
while(True):
        word=input("enter:")
        meaning=input("enter:")
        flash.append(flashcard(word,meaning))
        option=int(input("enter0,if u want to add another flashcard otherwise enter i:"))
        if(option):
                break
print("\nur flashcards")
for i in flash:
        print(">",i)