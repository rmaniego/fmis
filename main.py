import package
from package import hi, hello
from package import module1, module2
from package import SampleClasses, Class1

# accessing a variable inside a module inside a package
value = package.module1.CONSTANT_VARIABLE
print(f"\nCONSTANT_VARIABLE = {value}")

# calling a function inside a module inside a package
package.module1.function1()
package.module2.goodbye()

# calling functions inside a module
module1.function2("Sample Argument")
a, b = module1.function3(1, 2)
module2.goodbye()

# calling functions
hi()
hello()

# instantiating classes
class1 = Class1()
class2 = SampleClasses.Class2("Class #2")
class2.method()