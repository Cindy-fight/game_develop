class A:
   def foo(self):
      print('called A.foo()')
class B(A):
   pass
class C(A):
   def foo(self):
      print('called C.foo()')
class D(C, B):
   pass

if __name__ == '__main__':
   d = D()
   d.foo()
