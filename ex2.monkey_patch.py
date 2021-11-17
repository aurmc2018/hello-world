import m
def monkey_f(self):
   print("monkey_f()")
m.MyClass.f = monkey_f
obj = m.MyClass()
obj.f()
