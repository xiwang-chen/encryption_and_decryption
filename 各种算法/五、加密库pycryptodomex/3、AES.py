'''
高级加密标准（英语：Advanced Encryption Standard，缩写：AES），在密码学中又称Rijndael加密法，
是美国联邦政府采用的一种区块加密标准。这个标准用来替代原先的DES，已经被多方分析且广为全世界所使用。
经过五年的甄选流程，高级加密标准由美国国家标准与技术研究院（NIST）于2001年11月26日发布于FIPS PUB 197，
并在2002年5月26日成为有效的标准。2006年，高级加密标准已然成为对称密钥加密中最流行的算法之一。

AES在软件及硬件上都能快速地加解密，相对来说较易于实作，且只需要很少的存储器。
作为一个新的加密标准，目前正被部署应用到更广大的范围。
特点与思想：抵抗所有已知的攻击。 在多个平台上速度快，编码紧凑。 设计简单。 
 

AES为分组密码，分组密码也就是把明文分成一组一组的，每组长度相等，每次加密一组数据，直到加密完整个明文。
在AES标准规范中，分组长度只能是128位，也就是说，每个分组为16个字节（每个字节8位）。密钥的长度可以使用128位、
192位或256位。密钥的长度不同，推荐加密轮数也不同。
'''

from Cryptodome.Cipher import AES
from Cryptodome import Random

from binascii import a2b_hex

# 要加密的明文
data = '南来北往'
# 密钥key必须为 16（AES-128）， 24（AES-192）， 32（AES-256）
key = b'this is a 16 key'
# 生成长度等于AES 块大小的不可重复的密钥向量
iv = Random.new().read( AES.block_size )
print(iv)
# 使用 key 和iv 初始化AES 对象， 使用MODE_CFB模式
mycipher = AES.new( key, AES.MODE_CFB, iv )
print( mycipher )
# 加密的明文长度必须为16的倍数， 如果长度不为16的倍数， 则需要补足为16的倍数
# 将iv(密钥向量)加到加密的密钥开头， 一起传输
ciptext = iv + mycipher.encrypt( data.encode() )
# 解密的话需要用key 和iv 生成的AES对象
print( ciptext )
mydecrypt = AES.new( key, AES.MODE_CFB, ciptext[:16] )
# 使用新生成的AES 对象， 将加密的密钥解密
decrytext = mydecrypt.decrypt( ciptext[16:] )

print( decrytext.decode() )