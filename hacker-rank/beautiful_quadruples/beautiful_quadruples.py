#! /usr/bin/env python

# (1,1,1,2):

    # 01
# XOR
    # 01
# =   00

    # 00
# XOR
    # 01
# =   01

    # 01
# XOR
    # 10
# =   11

##########

# 0 XOR 0 = 0     0 XOR 1 = 1     --> 0 XOR Y = Y
# 1 XOR 0 = 1     1 XOR 1 = 0     --> 1 XOR Y = Y'

##########

123
---     Non-zero? If yes: !, if duplicate: -
111     !
112     !
113     !
121     -
122     !
123     

List: 111, 112, 113, 122

##########

1342
----    Non-zero? If yes: !, if duplicate: -

1111    
1112    !
1121    -
1122    
1131    !
1132    !
1141    !
1142    !

1211    -
1212    -
1221    -
1222    !
1231    -
1232    !
1241    -
1242    !

1311    -
1312    -
1321    -
1322    -
1331    
1332    !
1341    !
1342    !

List: 1112, 1113, 1114, 1123, 1124, 1134, 1222, 1223, 1224, 1234, 1233

##########

4213
----    Non-zero? If yes: !, if duplicate: -

1111    
1112    ! 
1113    !
1211    -
1212    
1213    !

2111    -
2112    -
2113    -
2211    -
2212    !
2213    !

3111    -
3112    -
3113    !
3211    -
3212    -
3213    !

4111    !
4112    !
4113    !
4211    -
4212    !
4213    !



##########

from sys import exit

DEBUG = False





