## graphr ##

graphr is a wrapper for the python sympy library

### Usage ###

Input should use the following format:

    operation expression args

`operation`: The list of operations implemented can be found below.

`expression`: Typically the first argument of the sympy function.

`args`: Any additional arguments that the sympy function excepts.


#### Operations ####

- "define"        : self.set_variable,
- "diff"          : sympy.diff,
- "dsolve"        : sympy.dsolve,
- "exit"          : exits graphr (0 arguments required),
- "integrate"     : sympy.integrate,
- "limit"         : sympy.limit,
- "plot"          : sympy.plotting.plot,
- "solve"         : sympy.solve,