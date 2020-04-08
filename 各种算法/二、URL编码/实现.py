'''
正常的URL中是只能包含ASCII字符的，也就是字符、数字和一些符号。而URL编码
就是一种浏览器用来避免url中出现特殊字符（如汉字）的编码方式。其实就是将
超出ASCII范围的字符转换成带%的十六进制格式。
'''


from urllib import parse

a = parse.quote( "中国欢迎您" )
print( a )  # %E4%B8%AD%E5%9B%BD%E6%AC%A2%E8%BF%8E%E6%82%A8

b = parse.unquote( a )
print( b )  # 中国欢迎您