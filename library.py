#library of functions
import sys
sys.setrecursionlimit(9001) # make the recursion limit very large so that python won't complain

'''
The only way we can deal with b that isn't a positive integer, we must first be able to define the inverse operation of tetration.
E.g. to calculate 2**1.5, we can do use the distributive proeprty to get (2**1)*(2**0.5),
    where 0.5=1/2, and using the product rule of exponentiation,
    we can guess that (2**0.5)*(2**0.5) = 2, and search for (2**0.5) that way. (perhaps using binary search)
    Then exponentiation can be defined on all positive rational numbers.
    The negative rational numbers can now be defined using the product rule of exponentiation e.g. 2**(1+0.5)=2**0

    Recap: positive fractional exponentiation(a^(p/q)=c)'s solutions are defined by binary search of a_test^p=?c^q.
        And then using with the formative definition of exponentiation, we can add the <1 fractions to get proper fractions i.e. rational numbers.
        Finally we can use the product rule (a^(b)*a^(-b)=1) plus the inverse of multiplication to get the negative rational numbers.

        Note that distributive property==product rule here.

E.g.2 to calculate 2*1.5, we can use the distributive property on (2*1)+(2*0.5)
    And then we can get (2*0.5+2*0.5) = 2 again via the distributive property (distributing the 2 into (0.5+0.5=1))
    ... same as above
    Therefore we can define positive (proper) fractional mulitplication's solution by binary search.
    And then using with the formative definition of multiplication, we can add the <1 fractions to get proper fractions i.e. rational numbers.
    Finally we can use the distributive property plus the inverse of addition (a*(-b)+a*(b)=a*0=0) to get the negative rational numbers.

Now to the real test:
    to calculate b tet a, we must use the distributive property.
    .
    .
    .
    .
    .
I think this can be done easily for alt_tet, but not so much for tet.
Also, the fact that the formal definition of tetration (the one where bracketing starts from top down) is weird (for aϵ[e^(-e), e^(1/e)] there is an upper limit to c, no matter how big b is).
Therefore I opt to explore the property of alt_tet more, as it seems more self-consistent/smooth.
'''

def tet(a, b:int, base=None):
    '''
    The common definition of tetration starts the bracketing from the top (the highest exponent)
    '''
    if base is None:
        base = a # base needs to be recorded so that it doesn't get lost as a is overwritten
    if b<=1:
        return a
    else:
        return tet(base**a, b-1, base)

def alt_tet(a, b:int, base=None):
    '''
    Now trying the second definition...
    '''
    if base is None:
        base = a
    if b<=1:
        return a
    else:
        return tet(a**base, b-1, base)

