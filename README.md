## graphr ##

graphr is a wrapper for the python sympy library

### Usage ###

Input should use the following format:

    operation expression args

`operation`: The list of operations implemented can be found below.

`expression`: Typically the first argument of the sympy function.

`args`: Any additional arguments that the sympy function excepts.


#### Operations ####

- "diff"          : sympy.diff,
- "integrate"     : sympy.integrate,
- "exit"          : exits graphr (0 arguments required),
- "solve"         : sympy.solve,