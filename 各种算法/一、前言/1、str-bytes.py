'''
我们所说的加密方式，都是对二进制编码的格式进行加密的，对应到Python中，则是我们的Bytes。

所以当我们在Python中进行加密操作的时候，要确保我们操作的是Bytes，否则就会报错。

将字符串和Bytes互相转换可以使用encode()和decode()方法。如下所示：

'''


# 方法中不传参数则是以默认的utf-8编码进行转换
a = "中国欢迎您".encode( "utf-8" )
print( a )  # b'\xe4\xb8\xad\xe5\x9b\xbd\xe6\xac\xa2\xe8\xbf\x8e\xe6\x82\xa8'

b = a.decode("utf-8")
print( b )  # 中国欢迎您