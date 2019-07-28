def stringdemo():
    strDemo = 'Hello Python'
    print(1, strDemo, type(strDemo))
    print(2, strDemo.center(20, '*'))#返回一个指定的宽度 width 居中的字符串，如果 width 小于字符串宽度直接返回字符串，否则使用 fillchar 去填充
    print(3,strDemo.capitalize())#首字母大写
    print(4,len(strDemo))
    print(5,strDemo.casefold())
    print(6,strDemo.lower())#lower() 方法只对ASCII编码，也就是‘A-Z’有效，对于其他语言（非汉语或英文）中把大写转换为小写的情况只能用 casefold() 方法
    print(7,strDemo.count('H'))
    print(8,strDemo.startswith('H'))
    print(9,strDemo.endswith('Python'))
    print(10,strDemo.replace('Python','py'))
    print(11,'-'.join(['aaa','bbb','ccc']))
    strTripDemo='\r\n'+strDemo+'\r\n'
    print(12,strTripDemo)
    print(13,strTripDemo.lstrip())
    print(14,strTripDemo.rstrip())
    print(15,strTripDemo.strip())
    print(16,strTripDemo.find('e'))
    print(17,'2*7={0}'.format(2*7))


if __name__ == '__main__':
    stringdemo()
