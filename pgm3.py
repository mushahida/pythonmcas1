# Python program to print positive Numbers in a List
list1 = [11, -21, 0, 45, 66, -93]
new=[n for n in numif n>0]
print(new)
# Python program to print Square of Numbers
print()
list1= [1,2,3,4,5]
newlist=[s*s for s in list1]
print(newlist)

#vowel
def Check_Vow(string, vowels): 
  final = [each for each in string if each in vowels]
  print("Total Vowels: ", len(final))
  print(final, "\n")   
# Driver Code 
string = "Geeks for Geeks is doing good job" 
vowels = "AaEeIiOoUu" 
Check_Vow(string, vowels); 

#ordinal value
def Ord_Word(word):  
   for s in word:   
     print("Ordinal value of : ", s, "is ", ord(s)) 
 
Ord_Word("hallucination") 