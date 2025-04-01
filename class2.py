class class_reverse:
    def __init__(self,word_s):
      self.s=word_s
    def reverse_word(self):
      return self.s[::-1]
word = input("enter:")
rev_ob=class_reverse(word)
result=rev_ob.reverse_word()
print("reversed string:",result)