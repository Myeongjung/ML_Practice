1. "What will be the output of the following code?

import re
string = 'bat, lat, mat, bet, let, met, bit, lit, mit, bot, lot, mot'
result = re.findall('b[ao]t', string)
print(result)

(X) ['bat', 'bot']
() 'bat, bot'
() ['bat', 'bet', 'bit', 'bot']
() 'bat, bet, bit, bot'

=> The condition of the regular expression is b + a or o + t.

2. Assume a and b are two (20, 20) numpy arrays. 
The L2-distance (defined above) between two equal dimension arrays can be calculated in python as follows:

def l2_dist(a, b):
    result = ((a - b) * (a - b)).sum()
    result = result ** 0.5
    return result 
	
Which of the following expressions using this function will produce a different result from the rest?

() l2_dist(a, b)
() l2_dist(np.reshape(a, (20 * 20)), np.reshape(b, (20 * 20)))
(X) l2_dist(np.reshape(a, (20 * 20)), np.reshape(b, (20 * 20, 1)))
() l2_dist(a.T, b.T)

=> when we perform this "np.reshape(b, (20 * 20, 1))" code, 
the number of a - b results are 40*40. However, other options are 20*20.


3. Consider the following variables in Python:

a1 = np.random.rand(4)
a2 = np.random.rand(4, 1)
a3 = np.array([[1, 2, 3, 4]])
a4 = np.arange(1, 4, 1)
a5 = np.linspace(1 ,4, 4)

Which of the following statements regarding these variables is correct?

() a3.shape == a4.shape
() a4.ndim() == 1
(X) a5.shape == a1.shape
() a1.shape == a2.shape

=> First, ndim() is incorrect, must use like a4.ndim

a1 looks like [1,2,3,4] with (4,) shape
a2 looks like [[1]
					[2]
					[3]
					[4]] with (4, 1) shape
a3 = [[1 2 3 4]] with (1, 4) shape
a4 = [1 2 3] with (3,) shape
a5 = [1. 2. 3. 4.] with (4,) shape

4. Which of the following is the correct output for the code given below?

import numpy as np

old = np.array([[1, 1, 1], [1, 1, 1]])
new = old
new[0, :2] = 0

print(old)


() [[1 1 0][1 1 0]]
() [[1 1 1][1 1 1]]
() [[0 1 1][0 1 1]]
(X) [[0 0 1][1 1 1]]

5. Given the 6x6 NumPy array r shown below, which of the following options would slice the shaded elements?
The shaded area is the middle of array (2X2)

() r[[2,3],[2,3]]
() r[2:3,2:3]
() r[[2,4],[2,4]]
(X) r[2:4,2:4]

6. For the given string, which of the following regular expressions can be used to check if the string starts with 'AC'?
import re 
s = 'ACBCAC'

() re.findall('[^A]C', s)
() re.findall('AC', s)
() re.findall('^[AC]', s)
(X) re.findall('^AC', s)

7. What will be the output of the variable L after the following code is executed?

import re
s = 'ACAABAACAAAB'
result = re.findall('A{1,2}', s)
L = len(result)

() 12
() 8
(X) 5
() 4

=> ['A', 'AA', 'AA', 'AA', 'A']

8. Which of the following is the correct regular expression to extract all the phone numbers from the following chunk of text:

Office of Research Administration: (734) 647-6333 | 4325 North Quad
Office of Budget and Financial Administration: (734) 647-8044 | 309 Maynard, Suite 205
Health Informatics Program: (734) 763-2285 | 333 Maynard, Suite 500
Office of the Dean: (734) 647-3576 | 4322 North Quad
UMSI Engagement Center: (734) 763-1251 | 777 North University
Faculty Adminstrative Support Staff: (734) 764-9376 | 4322 North Quad

() \d{3}[-]\d{3}[-]\d{4}
() \d{3}\s\d{3}[-]\d{4}
() [(]\d{3}[)]\d{3}[-]\d{4}
(X) [(]\d{3}[)]\s\d{3}[-]\d{4}

=> '(' + 3 digits + ')' + white space(\s) + 3 digits + '-' + 4 digits

9. Which of the following regular expressions can be used to get the domain names (e.g. google.com, www.baidu.com) from the following sentence?

'I refer to https://google.com and I never refer http://www.baidu.com if I have to search anything'


() (?<=https:\/\/)([.]*)
(X) (?<=[https]:\/\/)([A-Za-z0-9.]*)
() (?<=https:\/\/)([A-Za-z0-9.]*)
() (?<=https:\/\/)([A-Za-z0-9]*)

=> 
3rd option (?<=https:\/\/)([A-Za-z0-9.]*) can only get 'google.com' because the next domain name starts with 'http://' not 'https://'

10. The text from the Canadian Charter of Rights and Freedoms section 2 lists the fundamental freedoms afforded to everyone. 
Of the four choices provided to replace X in the code below, which would accurately count the number of 
fundamental freedoms that Canadians have?

text=r'''Everyone has the following fundamental freedoms:
    (a) freedom of conscience and religion;
    (b) freedom of thought, belief, opinion and expression, including freedom of the press and other media of communication;
    (c) freedom of peaceful assembly; and
    (d) freedom of association.'''

import re
pattern = X
print(len(re.findall(pattern,text)))

(X) \(.\) 
() (.)
() 'freedom'
() '[a-d]'

=> 'freedom' word appears 6 times in the text but these fundamental freedoms are noted by (a-d).