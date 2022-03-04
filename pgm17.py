Diction={'red':'#FF0000','green':'#008000','black':'#000000','white':'#FFFFFF'}
print("Sorted Dictionary is:")
for w in sorted(Diction,key=Diction.get):
    print(w,Diction[w])
print("Sorted Dictionary in Reverse Order:")
for w in sorted(Diction,key=Diction.get,reverse=True):
    print(w,Diction[w])
