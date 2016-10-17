##[Square Them](http://task-00000010.itrace.systems/square.php) (60pts)

+ Precondition:
  + Max sum < 512
  + Each numbers is not equal
  + 10 Questions
  + Time limit 2 minutes
  + You know what to do ^_^

+ Eample :
  + Sum each Rows: 15
  + Sum each Cols: 15
  + Numbers (From Left to Right. First row to the last) : 2,9,4,7,5,3,6,1,8
  + POST numbers=2,9,4,7,5,3,6,1,8

||15|15|15|
|:---:|:---:|:---:|:---:|
|15|  2  |  9  |  4  |
|15|  7  |  5  |  3  |
|15|  6  |  1  |  8  |

##Writeup
Using Magic Square Number Formula to generate the answer

X = N / 3

||N|N|N|
|:---:|:---:|:---:|:---:|
|N|  X+3  |  X-4  |  X+1  |
|N|  X-2  |  X    |  X+2  |
|N|  X-1  |  X+4  |  X-3  |

###"Python it and get it done"

##Flag :
###ITRACE{m4g1c_squ4r3_is_s0_m4th}
