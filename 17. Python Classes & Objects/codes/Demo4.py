# Python __init__() function
# Code by studyopedia

class Students:

    def __init__(self, sname, ssub, sgrade):
        self.sname = sname
        self.ssub = ssub
        self.sgrade = sgrade

    # custom function
    def demofunc(self):
        print("I am "+self.sname)
        print("I am interested in the Subject "+self.ssub)

# create 3 objects
st1 = Students("Amit", "Programming", "A+")
st2 = Students("Rohit", "Science", "A")
st3 = Students("Shreyas", "Maths", "B+")

# call the custom functions using objects
st1.demofunc()
st2.demofunc()
st3.demofunc()




