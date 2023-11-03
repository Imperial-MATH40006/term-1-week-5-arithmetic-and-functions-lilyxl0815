# %%
import time
from autograder_term1week5 import *
_globals = globals()

# %% [markdown]
# # <center> Introduction to Mathematical Computing </center>
# ### <center>Phil Ramsden </center>
# 
# # <center> Worksheet 1: Arithmetic and functions </center>
# 
# **NOTE:** When answering a question, remember to remove the `raise NotImplementedError()` line.
# 
# Don't forget: online Python documentation is at <a href='https://docs.python.org'>docs.python.org</a> and <a href='https://www.w3schools.com/python/'>www.w3schools.com/python/</a>.

# %% [markdown]
# ## Question 0: don't miss this bit!
# 
# In the file called `my_username.txt`, type your <b>short-form College user name</b> (this will usually be one or more letters followed by three or more figures, such as qk4019). Don't use quote marks. Then save the file.

# %%
# 5 Marks
# Do not try to delete this cell
# Run this cell for grading of Question 0
_globals = globals()
question0(_globals)

# %% [markdown]
# ## Question 1(i)
# 
# Calculate: 
# 
# (a) $4^2+1$;
# (b) $4^{2+1}$;
# (c) $2/3$ as a decimal;
# (d) the largest integer smaller than $381/47$;
# (e) $4 \times 2^5$;
# (f) $(4 \times 2)^5$.

# %%
# Assign your solutions to the questions above to the variables below.
q1ia_answer =4**2+1 
q1ib_answer =4**(2+1)
q1ic_answer = 2/3
q1id_answer = 8
q1ie_answer = 4*2**5
q1if_answer = (4*2)**5
print(q1ia_answer)
print(q1ib_answer)
print(q1ic_answer)
print(q1id_answer)
print(q1ie_answer)
print(q1if_answer)
# YOUR CODE HERE
raise NotImplementedError()

# %%
# 6 Marks
# Do not try to delete this cell
# Run this cell for grading
_globals = globals()
question1(_globals)

# %% [markdown]
# ## Question 1(ii)
# 
# Calculate:
# 
# (a) The residue of $372517$ modulo $1820$.
# 
# (b) The residue of $(1417456 + 1191761)$ modulo $1820$.
# 
# (c) The residue of $(1417456 \times 1191761)$ modulo $1820$.
# 
# (d) The residue of $1417456^{1191761}$ modulo $1820$ (for best results use the <code>pow</code> function with three arguments).

# %%
# Assign your solutions to the questions above to the below variables.
q1iia_answer = 372517%1820
q1iib_answer = (1417456+1191761)%1820
q1iic_answer = (1417456*1191761)%1820
start = time.time()
q1iid_answer = pow(1417456,1191761,1820)
duration = time.time() - start
print(q1iia_answer)
print(q1iib_answer)
print(q1iic_answer)
print(q1iid_answer)

# YOUR CODE HERE
raise NotImplementedError()

# %%
# 5 Marks
# Do not try to delete `this cell
# Run this cell for grading
_globals = globals()
question1_ii(_globals)

# %% [markdown]
# ## Question 2(i)
# 
# Using the <code>math</code> module, calculate: (a) $\sqrt{50}$; (b) $\cos \pi/7$; (c) $e^{e^2}$; (d) $\ln 58$; (e) $\log_{10} 58$; (f) $\cot^{-1} 2$; (g) $\coth^{-1} 2$.

# %%
from math import sqrt
from math import cos
from math import exp
from math import log
from math import log10
from math import atan
from math import atanh
from math import pi
q2ia_answer = sqrt(50)
q2ib_answer = cos(pi/7)
q2ic_answer = exp(exp(2))
q2id_answer = log(58)
q2ie_answer = log10(58)
q2if_answer = atan(1/2)
q2ig_answer = atanh(1/2)
print(q2ia_answer)
print(q2ib_answer)
print(q2ic_answer)
print(q2id_answer)
print(q2ie_answer)
print(q2if_answer)
print(q2ig_answer)

# YOUR CODE HERE
raise NotImplementedError()

# %%
# 7 Marks
# Do not try to delete this cell
# Run this cell for grading
_globals = globals()
question2_i(_globals)

# %% [markdown]
# ## Question 2(ii)
# 
# The <code>numpy</code> module contains many of the same functions as <code>math</code> (though they're slightly different, in ways we'll explore). Recalculate (a) - (g) using this module instead. (<em>Much</em> more about <code>numpy</code> later; note that it's not part of the standard Python library, so online documentation is at <a href='https://numpy.org'>numpy.org</a>.)

# %%
from numpy import sqrt
from numpy import exp
from numpy import cos
from numpy import log
from numpy import log10
from numpy import arctan
from numpy import arctanh
q2iia_answer = sqrt(50)
q2iib_answer = cos(pi/7)
q2iic_answer = exp(exp(2))
q2iid_answer = log(58)
q2iie_answer = log10(58)
q2iif_answer = arctan(1/2)
q2iig_answer = arctanh(1/2)
print(q2iia_answer)
print(q2iib_answer)
print(q2iic_answer)
print(q2iid_answer)
print(q2iie_answer)
print(q2iif_answer)
print(q2iig_answer)

# YOUR CODE HERE
raise NotImplementedError()

# %%
# 7 Marks
# Do not try to delete this cell
# Run this cell for grading
_globals = globals()
question2_ii(_globals)

# %% [markdown]
# ## Question 3
# 
# (a) Define variables $p=6$ and $q=9$, and calculate the quantity
# $$x=\left(\frac{q}{2}+\sqrt{\left[\frac{q}{2}\right]^2-\left[\frac{p}{3}\right]^3}\right)^{1/3}+\left(\frac{q}{2}-\sqrt{\left[\frac{q}{2}\right]^2-\left[\frac{p}{3}\right]^3}\right)^{1/3}.$$
# Verify Cardano's Theorem, that $x$ is a solution of the cubic
# $$x^3=p\,x+q.$$

# %%
import math
p = 6
q = 9

x =(q/2+math.sqrt((q/2)**2-(p/3)**3))**(1/3)+((q/2)-math.sqrt((q/2)**2-(p/3)**3))**(1/3)
print(p)
print(q)
print(x)
# YOUR CODE HERE
raise NotImplementedError()

# %%
#1 Mark
assert(x == question3(p, q))
print("Question 3(a) passed!")

# %% [markdown]
# (b) Repeat for $p=3$ and $q=18$.

# %%
import math# import any necessary functions
# Assign your solutions to the questions above to the variables below.
p = 3
q = 18

x = ((q/2)+math.sqrt((q/2)**2-(p/3)**3))**(1/3)+((q/2)-math.sqrt((q/2)**2-(p/3)**3))**(1/3)
print(p)
print(q)
print(x)
# YOUR CODE HERE
raise NotImplementedError()

# %%
#1 Mark
assert(x == question3(p, q))
print("Question 3(b) passed!")

# %% [markdown]
# (c) If you try to repeat for $p=6$ and $q=4$, you may run into a problem. Can you solve it?

# %%
import math
import cmath# import any necessary functions
# Assign your solutions to the questions above to the variables below.
p = 6
q = 4

x = ((q/2)+cmath.sqrt((q/2)**2-(p/3)**3))**(1/3)+((q/2)-cmath.sqrt((q/2)**2-(p/3)**3))**(1/3)
print(p)
print(q)
print(x)
# YOUR CODE HERE


# %%
#1 Mark
assert(x == question3(p, q))
print("Question 3(c) passed!")

# %% [markdown]
# ## Question 4
# 
# Experiment with <b>integer division</b>, and answer the following question:
# 
# For integers $a$ and $b$, the code
# 
# <code>a // b</code>
# 
# always returns
# 
# 1. The least integer greater than or equal to $a/b$;
# 2. The greatest integer less than or equal to $a/b$;
# 3. The nearest integer to $a/b$;
# 4. The number $a/b$, rounded towards zero;
# 5. The number $a/b$, rounded away from zero;
# 6. None of these; it depends on the signs of $a$ and $b$.

# %%
q4_answer = 2
# YOUR CODE HERE
raise NotImplementedError()

# %%
#1 Mark
assert(q4_answer == question4())
print("Question 4 passed!")

# %% [markdown]
# ## Question 5 (i)
# 
# The expressions (a) $\sin^{-1}(-2)$; (b) $\cos^{-1}(-2)$; (c) $\tanh^{-1}(-2)$; (d) $\ln(-2)$
# 
# can all be given sensible mathematical values. Using functions from a suitable Python module, calculate these values.

# %%
# Assign your solutions to the questions above to the variables below.
from cmath import asin,acos,atanh,log
q5ia_answer =asin(-2)
q5ib_answer =acos(-2)
q5ic_answer =atanh(-2)
q5id_answer =log(-2)

print(q5ia_answer)
print(q5ib_answer)
print(q5ic_answer)
print(q5id_answer)

# YOUR CODE HERE
raise NotImplementedError()

# %%
# 4 Marks
# Do not try to delete this cell
# Run this cell for grading
_globals = globals()
question5_i(_globals)

# %% [markdown]
# ## Question 5 (ii)
# 
# The expressions (a) $\sin^{-1}(-2)$; (b) $\cos^{-1}(-2)$; (c) $\tanh^{-1}(-2)$; (d) $\ln(-2)$
# 
# can actually all be calculated using only functions from the <code>numpy</code> module, though there's a bit of a trick to making it work. Find the trick, and make it work!

# %%
import cmath
from cmath import asin, acos, atanh, log# Assign your solutions to the questions above to the variables below.
q5iia_answer =asin(-2)
q5iib_answer =acos(-2)
q5iic_answer =atanh(-2)
q5iid_answer =log(-2)
print(q5iia_answer)
print(q5iib_answer)
print(q5iic_answer)
print(q5iid_answer)

# YOUR CODE HERE
raise NotImplementedError()

# %%
# 4 Marks
# Do not try to delete this cell
# Run this cell for grading
question5_ii(_globals)

# %% [markdown]
# ## Question 5 (iii)
# 
# (a) Using the built-in `pow` function, calculate the residue of $7725423^{3835624}$ modulo $25231211$, assigning your answer to the variable `q5iiia_answer`.

# %%
# Assign your solutions to the questions above to the variable below.
q5iiia_answer = pow(7725423,3835624,25231211)
print(q5iiia_answer)

# YOUR CODE HERE
raise NotImplementedError()

# %%
# 1 Mark
assert(question5iiia_answer == question5_iii_a())
print('test case passed!')

# %% [markdown]
# (b) Wild-card import all the functions from the `math` module as follows:

# %%
from math import *

# %% [markdown]
# Then, attempt your calculation in part (a) for a second time, and note what happens. 
# 
# Explore a bit further if you like. How would you explain what has happened?
# 
# <ol>
#     <li>Wild-card importing all the functions from the <code>math</code> module breaks the <code>pow</code> function; no function called <code>pow</code> is now available.</li>
#     <li>Wild-card importing all the functions from the <code>math</code> module produces a namespace clash between the function called <code>pow</code> that belongs to that module and the built-in function of the same name; from now on, only the <code>math</code> version works, and that can't be used to calculate modular powers.</li>
#     <li>Wild-card importing all the functions from the <code>math</code> module produces a namespace clash between the function called <code>pow</code> that belongs to that module and the built-in function of the same name; from now on, only the built-in version works, and that can't be used to calculate modular powers.</li>
# </ol>
# 
# Fill in the correct numerical value, 1, 2 or 3, below.

# %%
question5iiib_answer = 2
# YOUR CODE HERE
raise NotImplementedError()

# %%
# 1 Mark
assert(question5iiib_answer == question5_iii_b())
print('test case passed!')

# %% [markdown]
# (c) Try the following lines of code:

# %%
from math import *
import builtins
builtins.pow(7725423,3835624,25231211)

# %% [markdown]
# Which of the following statements is the closest to the truth?
# 
# <ol>
#     <li>Once a built-in function has been overwritten in a namespace clash, it can't be used again unless the session is restarted.</li>
#     <li>Namespace clashes with built-in functions can be rectified by importing the <code>builtins</code> module, meaning that there's no need to worry about them.</li>
#     <li>Namespace clashes with built-in functions can be rectified by importing the <code>builtins</code> module, so they may not be fatal, but they're still worth taking care to avoid.</li>
# </ol>
# 
# (This may be a bit of a matter of opinion; but our opinion on it is strong, and we bet you can guess it.)

# %%
question5iiic_answer = 3
# YOUR CODE HERE
raise NotImplementedError()

# %%
# 1 Mark
assert(question5iiic_answer == question5_iii_c())
print('test case passed!')

# %%



