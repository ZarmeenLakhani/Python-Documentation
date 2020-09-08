#Tuple is a lot like list but it has paranthesis instead of square brackets
l=[1,2,3]
t=(1,2,3)
#In tuples you can't add or remove elements. Very secured data structure. You can't make any edits.
#tuples have particular structural order
About_me=("Zarmeen Lakhani", 20, "student")
About_me1=("Shazmeen Lakhani", 23, "student")
About_me2=("Armeen Lakhani", 25, "medical officer")
About_me3=("Pashmeen Lakhani", 27, "Genomics Researcher")
sisters=[About_me,About_me1,About_me2,About_me3]
#(name,age,profession)=About_me
#print(profession)
#print(name) IGNORED FOR TESTING
# Tuplets are not callable. We packed them with an attribute.
for name,age,profession in sisters:
    print(name)
