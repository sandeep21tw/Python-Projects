a = 0
b = "hello"
c = [1,2,3,4]

def what():
    """
    if i do this i will get error
    Error is: UnboundLocalError: local variable 'a' reference before assignment
    a = a + 1

    note: b = a + 1 is working fine.

    The real question is why that error? I can easily access the value
    of global but i try to modify i can't do that

    why is that?

    now, you may say that python allow us to only access global variables
    but you cannot modify them, ...
    if that was the case then why do the variable b is getting modified
    without any error with this statement
    b = a + 1

    hmmm, interesting... It is worth to find out what's going on here.!

    note: i also need to find out how the global works here!

    like this line below if written above a = a + 1 won't give error

    #global a

    ####
    Wait maybe You just cannot modify global variables in functions here but you
    can just access them but if that's the case why b is modified above

    Well, b isn't modified above they just created local variable named b having
    the value of a + 1, i think same goes for a, a is local variable

    hmmm, ooohhh

    Well, if that is the case and a is the local variable then why is it giving
    error in the case as just take the value of global a and store it in local
    a


    hmm, you are right!

    because python interpreter is getting confused because of having two a
    on the same line
    if two a are same line, it is thinking that we are modifying a local variable
    a using the "local variable" a but there is no local variable a in our case
    because infact we are using the global variable a here.

    i think you could do something like this

    a = 43
    a = a + 1

    instead of a = a + 1

    in this case, we have declared the variable locally! and modifying it, now

    # This means final verdict is:
    - we can access global variables inside functions but cannot modify them
    - same name as global variables can be created inside functions(haha that's
    why the confusin arised in the first place)
    - global keyword can be used to change the global variable
    - python get confused in statements like a = a + 1 if it is inside local
    scope like functions,
    
    """
    # global a
    a = a + 1
    print(a)
    print(b)
    print(c)


what()
