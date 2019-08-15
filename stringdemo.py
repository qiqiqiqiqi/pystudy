# coding=utf-8
def stringdemo():
    strDemo = 'Hello Python'
    print(1, strDemo, type(strDemo))
    print(2, strDemo.center(20, '*'))  # 返回一个指定的宽度 width 居中的字符串，如果 width 小于字符串宽度直接返回字符串，否则使用 fillchar 去填充
    print(3, strDemo.capitalize())  # 首字母大写
    print(4, len(strDemo))
    print(5, strDemo.casefold())
    print(6, strDemo.lower())  # lower() 方法只对ASCII编码，也就是‘A-Z’有效，对于其他语言（非汉语或英文）中把大写转换为小写的情况只能用 casefold() 方法
    print(7, strDemo.count('H'))
    print(8, strDemo.startswith('H'))
    print(9, strDemo.endswith('Python'))
    print(10, strDemo.replace('Python', 'py'))
    print(11, '-'.join(['aaa', 'bbb', 'ccc']))
    strTripDemo = '\r\n' + strDemo + '\r\n'
    print(12, strTripDemo)
    print(13, strTripDemo.lstrip())
    print(14, strTripDemo.rstrip())
    print(15, strTripDemo.strip())
    print(16, strTripDemo.find('e'))
    print(17, '2*7={0}'.format(2 * 7))


def operationDemo():
    print(1, '10 / 3={0}'.format(10 / 3))
    print(2, '10 % 3={0}'.format(10 % 3))
    '''
    // 向下取整，取值为不大于结果的最新整数
    '''
    print(4, '(-1) // 2={0}'.format((-1) // 2))  # -1
    print(5, '40 // (-30)={0}'.format(40 // (-30)))  # -2
    print(6, "(-1)//(-2)={0}".format((-1) // (-2)))  # 0
    '''
    ** 幂运算
    '''
    print(7, '2**3={0}'.format(2 ** 3))
    print(8, 'float(7)={0}'.format(float('7')))
    print(9, 'int(-6)={0}'.format(int('  -6  ')))

    print(10, (2.0).is_integer())
    print(11, '2 << 3 ={0};8>>3={1}'.format(2 << 3, 8 >> 3))
    print(12, '5|3={0}'.format(5 | 3))
    print(13, '5&3={0}'.format(5 & 3))
    '''
    ^ 异或
    '''
    print(14, '5^3={0}'.format(5 ^ 3))

    '''
    (1)在计算机里面,负数是以补码存储的 
    (2)原码求补码:取反,+1 
    (3)补码求原码:取反,+1 
    (4)取反操作是在原码上进行的!
    (5) 正数的原码和补码都是其本身
    (6)负数的补码是其正数的原码各位取反,最后再加上1（符号位不变，数值位取反，最后一位加1）
    (7)负数的补码的补码就是其原码
    
    ~a  :确定源码，然后取反
     (~a ) 输出结果 -(a+1) 。
    https://blog.csdn.net/qq_38260497/article/details/86600215
     0000 0101 源码
     1111 1010 取反后是个小于0的数取补码（取反后+1）
     0000 0101 取反
     0000 0110 +1
    '''
    print(15, '~5={0}'.format((-6).to_bytes(4, byteorder='big', signed=True)))
    print(15, '~5={0}'.format(bin((-6))))

    '''
    负数取反需要先得到源码再取反
    0000 0110 补码
    1111 1001 取反
    1111 1010 +1 源码
    0000 0101 取反
    '''
    print(16, '~-6={0}'.format(~(-6)))


def buildInFunction():
    print(1, 'max(2,7)={0}'.format(max(2, 7)))
    print(2, 'max([2, 9, 4, 88])={0}'.format(max([2, 9, 4, 88])))
    '''
    complex 复数
    int 整型
    float 浮点数
    '''
    print(3, 'complex(1,2)={0}'.format(complex(1, 2)))
    print(4, 'complex(1-2j)={0}'.format(complex('1-2j')))
    print(5, 'complex(1-2j)*complex(1,2)={0},{1}'.format(complex('1-2j') * complex(1, 2),
                                                         type(complex('1-2j') * complex(1, 2))))
    for i in range(0, 7, 2):
        print(6, 'range(0, 7, 2)={0},{1}'.format(range(0, 7, 2), i))
    print(7, 'dir(int)={0}'.format(dir(int)))
    print(8, 'divmod(10, 3)={0}'.format(divmod(10, 3)))
    print(9, '{0}'.format(eval("{'name':'linux','age':199}")))
    print(9, '{0}'.format(eval("{'name':'linux','age':age}", {"age": 1822})))
    print(9, '{0}'.format(eval("{'name':'linux','age':age}", {"age": 1822}, {"age": 1821})))
    # print(10, '{0}'.format(eval("__import__('os').system('ls /Users/13324/Desktop/db')")))


def controlFlowDemo():
    a = 0
    while (a < 10):
        if (a % 2 == 0):
            if (a == 6):
                continue
            print(11, 'while a={0}'.format(a))
        elif (a == 3):
            pass
        elif (a == 7):
            break
        else:
            print(12, 'while a={0}'.format(a))
        a += 1


def listDemo():
    listA = [1, 2, 3]
    print(1, listA + listA)
    listA.append(4)
    print(2, listA)
    listA.insert(0, 'u')
    print(3, listA)
    print(4, listA.pop(1), listA)
    print(5, listA.remove(2), listA)
    listA[0] = 'U'
    print(6, listA)
    print(7, listA[0], 'U' in listA)
    listA.extend(listA)
    print(8, listA)
    print(9, listA.count('U'))
    listA.reverse()
    print(10, listA)
    listA = [92, 45, 12, 98, 7]
    listA.sort()
    print(11, listA)

    '''元组，不可修改(可读不可写)'''
    listB = (4, 5, 6)
    print(12, listB)
    '''can only concatenate list (not "tuple") to list'''
    '''+ 同种数据类型可以使用'''
    # listA+listB
    listA.extend(listB)
    print(13, listA)



def setDemo():
    '''set 元素唯一'''
    setA = {1, 2, 1}
    print(1, setA, type(setA))
    '''
    {}创建的是空的dict
    set()创建的是空的set
    '''
    setA = {}
    setB = set()
    print(2, type(setA), type(setB))
    setA = set([2, 8, 3, 9, 7, 3])
    print(3, setA)
    pass


if __name__ == '__main__':
    # stringdemo()
    # operationDemo()
    # buildInFunction()
    # controlFlowDemo()
    # listDemo()
    setDemo()
