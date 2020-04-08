'''
非对称加密 
典型的非对称加密 
典型的如RSA等，常见方法，使用openssl ,keytools等工具生成一对公私钥对，使用被公钥加密的数据可以使用私钥来解密，
反之亦然（被私钥加密的数据也可以被公钥解密) 。

在实际使用中私钥一般保存在发布者手中，是私有的不对外公开的，只将公钥对外公布，就能实现只有私钥的持有者才能将数据解
密的方法。 这种加密方式安全系数很高，因为它不用将解密的密钥进行传递，从而没有密钥在传递过程中被截获的风险，而破解密
文几乎又是不可能的。

但是算法的效率低，所以常用于很重要数据的加密，常和对称配合使用，使用非对称加密的密钥去加密对称加密的密钥。

简介 
RSA加密算法是一种非对称加密算法。在公开密钥加密和电子商业中RSA被广泛使用。

该算法基于一个十分简单的数论事实：将两个大素数相乘十分容易，但那时想要对其乘积进行因式分解却极其困难，因此可以将乘积公
开作为加密密钥，即公钥，而两个大素数组合成私钥。公钥是可发布的供任何人使用，私钥则为自己所有，供解密之用

而且，因为RSA加密算法的特性，RSA的公钥私钥都是10进制的，但公钥的值常常保存为16进制的格式，所以需要将其用int()方法转换
为10进制格式。
'''

import rsa


# rsa加密
def rsaEncrypt(str):
    # 生成公钥、私钥
    (pubkey, privkey) = rsa.newkeys( 512 )
    print("pub: ", pubkey)
    print("priv: ", privkey)
    # 明文编码格式
    content = str.encode( 'utf-8' )
    # 公钥加密
    crypto = rsa.encrypt( content, pubkey )
    return (crypto, privkey)


# rsa解密
def rsaDecrypt(str, pk):
    # 私钥解密
    content = rsa.decrypt( str, pk )
    con = content.decode( 'utf-8' )
    return con


(a, b) = rsaEncrypt( "hello" )
print('加密后密文：')
print(a)
content = rsaDecrypt( a, b )
print('解密后明文：')
print(content)  