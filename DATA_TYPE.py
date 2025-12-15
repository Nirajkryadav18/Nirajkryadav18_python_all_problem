# object type /data type 
# number =1234,3.2344,3+4j,0b111,Decimal(),
# srting 'spam','bol',b'a\x01c',u'sp\xc4m'
# List : [1,[2,'three'],list(range(10))];
# Typle:(1,'span',4,'u'),tuple('span'),namedtuple;
# Dictionary: {'food','span','tast': 'yum'} dict
# Set:set('abc'),{'a','b','c'};
# Boolean:True,fulse;
# None: none means emtpy
# Function,modual,classes;
#  Advance: Decorators Generator,Iterator;

mylist=[1,2,3,4,['a','b','c'],5]
print (mylist)

number=12+12
print(number)

decimal=2.5*5
print(decimal)

pow=2**2
print(pow)


username="chaiourcode"
len(username)
print(len)

myTup=(1,2,3)
print(myTup)

l1=[1,2,3]
l2=l1        # mutable valur in table
print(l1)
l1[0]=44
print(l1)
print(l2)

# mutable means change the value ;
l1=[1,2,3]
l2=l1
l2=[1,2,3]
l1[0]=55
print(l1)
print(l2)

n=[1,3,5]
m=n
print(m)
print(n)


# number data type ;
x=3
y=5
print(x+y)


# sring type of data type;
chai="masala chair"
first_char=chai[0]
print(first_char)

# slice the value;
chai='masala chai'
slice_chai=chai[0:6]
print(slice_chai)

num_list="0123456789"
num_list[:]
print(num_list)
 

#  this code providing the charecter changing upper to lower this function
chai='Masala chai'
print(chai.upper())
print(chai.lower())

#  this code providing the repace the value 
chai="Lemon chai"
print(chai.replace("Lemon","Ginger"))


#  split the value ;
chai="Lemon,Ginger,Masala, mint"
print(chai.split())

#  find the charecter;
chai="masala Chai"
print(chai.find("chai"))


#  counting the value of charecter;
chai="masala chai chai chai"
print(chai.count("chai"))

# joint opration; means space provinding know;
chai_variety=["lemon","masala","ginger"]
print("-".join(chai_variety))

# List type of data type;
tea_varities=["black","Green","Oolong","White"]
print(tea_varities)
print(tea_varities[-1])
# slicing;
print(tea_varities[2:3])
# under varities change know;
tea_varities[3]="Harbal"
print(tea_varities)
# loops used; 
for tea in tea_varities:
     print(tea,end="-")


#  dictionary date type ;
chai_type={"masala","spicy","ginder","zesty","green","mind"}
print(chai_type)
# print(chai_type["masala"])

#  delete tha data 
chai_type={'masala': 'spicy','green':'fresh'}
del chai_type["green"]
print(chai_type) 

#  print the squared of number in range;
squared_num={x:x**2 for x in range(6)}
print(squared_num)