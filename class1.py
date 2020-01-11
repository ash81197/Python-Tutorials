class student:
    def __init__(self, fname, lname, marks):
        self.fname = fname
        self.lname = lname
        self.marks = marks
    def emailId(self):
        return('{}{}@gmail.com'.format(self.fname, self.lname))
        # email = fname + lname + '@gmail.com'
    
s1 = student("abc", "bca", 90)

##s1.fname = "Banwar"
##s1.lname = "Gulshan"

s2 = student("bca", "abc", 9)

##s2.fname = "Aashish"
##s2.lname = "Gupta"

print(s1.fname, s1.lname, s1.marks)
print(s2.fname, s2.lname, s2.marks)

# print('Email of person is {}{}@gmail.com'.format(s1.fname, s1.lname))
s3 = student('a', 'b', 90)
print(s3.emailId())

'''

class stu
{

}stu;

void main()
{
# stu obj;
}
'''
