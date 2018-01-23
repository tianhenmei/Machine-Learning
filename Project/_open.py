#-*- coding:utf-8 -*-
letter = open('./letter.txt')
letter_str = letter.read()
letter.close()
print(letter_str)


print('**abs(x): return the absolute value of a number********************************************')
print(abs(-1))
print(abs(1))
print(abs(-0.34567))


print('**all(iterable): return true if all elements of the iterable are true********************************************')
arr = [0,1,2,3,4]
arr_1 = [2,3,4,5]
print(all(arr))
print(all(arr_1))

print('**any(iterable): return true if any element of the iterable is true********************************************')
brr = [0,1,2,3,4]
brr_1 = [2,3,4,5]
brr_2 = [0,0]
print(any(brr))
print(any(brr_1))
print(any(brr_2))

print('**input(prompt): 相等于 eval(raw_input(prompt)) ，用来获取控制台的输入. raw_input() 将所有输入作为字符串看待，返回字符串类型。而 input() 在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（ int, float）********************************************')
# c = input("请用户输入一个字符：")
# print(c+" 的ASCII 码为", ord(c))
# print(ord(c)," 对应的字符为", chr(ord(c)))


#print('**ascii(object):返回一个可打印的对象字符串方式表示，如果是非ascii字符（如汉字）就会输出\x，\u或\U等字符来表示。与python2版本里的repr()是等效的函数********************************************')
print(ascii('http://www.baidu.com&lt;中文'))

print('**repr(object): return the absolute value of a number********************************************')
print({"name":'joey',"age":24,"country":'中国'})



print('**basestring(): 方法是 str 和 unicode 的超类（父类），也是抽象类，因此不能被调用和实例化，但可以被用来判断一个对象是否为 str 或者 unicode 的实例，isinstance(obj, basestring) 等价于 isinstance(obj, (str, unicode))********************************************')
print(isinstance('hello world',str))
# print(isinstance('hello world',basestring))   # 不存在
print(isinstance('hello world',int))



print('**bin(): 返回一个整数 int 或者长整数 long int 的二进制表示***********************')
print(bin(10))

print('**bool(x) 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False************')
print(bool(0))
print(bool())
print(bool(2))
print(issubclass(bool,int))  #bool 是 int 子类

print('**bool(x) 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False************')
str1 = 'for i in range(0,10): print(i)'
c = compile(str1,'','exec')     # 编译为字节代码对象
#print(c)
#exec(c)
#eval(c)
str2 = '3 * 4 + 5'
a = compile(str2,'','eval')
#print(a)
#print(eval(a))



print('**dir() ************')
print(dir())
class Shape:
    def __dir__(self):
        return ['choulaogong','sunzongyu','joey']

print(dir(Shape()))

name = ['choulaogong','sunzongyu','joey']
print(list(enumerate(name)))
for ni,nn in enumerate(name):
    print(ni,nn)


print(divmod(278,33))

#  execfile('./turtle.py') # not in the new version

print(dict([('choulaogong','laogong'),('sunzongyu','laogong'),('joey','laogong')]))

def is_odd(n):
    return n %2 == 0    
new_list = filter(
    is_odd
    ,[1,2,3,4,5,6,7,8,9])
print(list(new_list))

#print(float('123ofnoaf'))  # error
#print(float('wfwon234'))  # error
#print(float('234fowaenf999'))  # error


print("{:2f}".format(3.14234))
print("{:0>4d}".format(18))
print("{:0<4d}".format(18))

L=[('b',2),('a',1),('c',3),('d',4)]
#def lmba(x,y):
#    cmp(x[1],y[1])
#print(sorted(L,cmp = lmba))

for i in iter([1,2,3]):
    print(i)

print(round(8.22344412,3))
print(round(8.0000,2))

__import__('_turtle')

















