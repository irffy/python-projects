import os
import sys

print(os.getenv("fname"))
print(os.getenv("sname"))
print(sys.argv[1])

#Set env variables as example:
# export fname ="Irfan"
# export sname="Ahmed"

#call the program as
# python env_vars hello --> Result is: Irfan Ahmed hello