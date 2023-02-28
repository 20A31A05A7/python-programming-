class a:
    def asd(self):
        print("a is klu")
    def sdf(self):
         print("a-sdsf")
class b:
    def asd(self):
        print("b is kllu")
    def sdf(self):
        print("B-sdf")
a_obj=a()
b_obj=b()
for i in (a_obj,b_obj):
    i.asd()
    i.sdf()
