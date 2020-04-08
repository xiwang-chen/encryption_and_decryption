'''
Python内置的base64模块可以直接进行base64的编解码

'''

import base64

a = base64.b64encode( b"hello world" )
print( a )  # b'aGVsbG8gd29ybGQ='

b = base64.b64decode( a )
print( b )  # b"hello world"