#set uses curly brackets, braces
#you CAN NOT have duplicates in the set .
# unordered. You can't iterate. there is no 0th or 1st element.bro, no order
#we can cast a list to sets which means it will get rid of the repeated elements
#and convert it riht back in a list again.
s={"blueberry", "rasberry"}
print(s)
#it spits out result in random order. sets are like a bag of thing
s.add('stawberry')
s.add('blueberry')
s.add('4')
print(s)
#list to sets
l=[1,1,1,1,1,1,4,4,4,4,4,2,2,2,2,2,2,,9,,9,9,9,9,9,3,3,3,3,3]
le=set(l)
li=list(le)
print(li)
#function of Venn Diagram
library_1={"Harry Potter", "Monster calls", "Romeo and Juliet"}
library_2={"Monster calls", "Peaky Binder", "Die Young"}
Book_town=library_1.union(library_2)
print(Book_town)
similar_books=library_1.intersection(library_2)
diff_book=library_1.difference(library_2)
#this function would return elements from list1 that are not in list 2.
print(similar_books)
print(diff_book)
