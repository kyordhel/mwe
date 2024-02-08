from time import sleep

def foo():
    if cond1: bar() #Some explanation
    if cond2: baz() #Some other explanation
    if cond3: bye() #Even more explanations

    # Another line that does nothing
    while True:
        sleep(1)
    # The following three lines explain
    # what the next for does. Which is
    #basically nothing because it passes
    for i in range(100):
        # Another line that should not print
        pass # And an unnecessary explanation

#end def
