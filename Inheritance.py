class Parent1:
    value1="This is a Parent1's Value 1"
    value2="This is a Parent1's Value 2"
class Parent2:
    value1="This is a Parent2's Value 1"
    value2="This is a Parent2's Value 2"
class Child(Parent1,Parent2):
     pass
parentObj1=Parent1()
parentObj2=Parent2()
childObj=Child()
print(parentObj1.value1)
print(parentObj1.value2)
print(parentObj2.value1)
print(parentObj2.value2)
