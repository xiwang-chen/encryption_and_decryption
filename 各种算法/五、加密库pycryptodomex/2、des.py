
# 导入DES模块
from Cryptodome.Cipher import DES
import binascii

# 这是密钥
key = b'abcdefgh'
# 需要去生成一个DES对象
des = DES.new( key, DES.MODE_ECB )
# 需要加密的数据
text = 'python spider!'
text = text + (8 - (len( text ) % 8)) * '='
# 加密的过程
encrypto_text = des.encrypt( text.encode() )
# 加密过后二进制转化为ASCII
encrypto_text = binascii.b2a_hex( encrypto_text )
print( encrypto_text )
# 解密需要ASCII 先转化为二进制 然后再进行解密
plaint = des.decrypt( binascii.a2b_hex( encrypto_text ) )
print( plaint )

"""
b'084725d8f5ffafc61814fae0796bfd2f'
b'python spider!=='
"""