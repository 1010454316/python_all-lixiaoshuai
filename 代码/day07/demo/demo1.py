# author:jason
'''
    方法：函数
    好处：一本万利，一次书写，处处使用。
    def  【方法名】(参数列表):
        方法体
        [return]
    方法名：  多个单词组成，第二个单词开始，首字母就要大写。 totalStudentNumber : 驼峰式命名法
    参数列表：
        1.单值传输
        2.*args:元组：能不定数量的接受参数
        3.**kwargs:字典
        4.注意：3个参数列表的为位置是禁止调换。
'''

# 就用方法来打印1~100以内的数据：(方法的递归(循环)调用)
i = 1

def  printNum(i):
    if i <= 100:
        print(i)
        i = i + 1
        printNum(i)

printNum(i)




















# a = 5
# b = 3
# c = 1
# d = 8
#
# def getSum(a,b,c,d):
#     s = getSum1(a,b) +  getSum1(c,d)
#     return s
#
# def getSum1(a,b):
#     return a + b
#
# print(getSum(a,b,c,d))














'''
def  showInfo(asdfasdfasf,*args,**kwargs):
    # print(name,"------",age)
    print(args)
    for i in args:
        print(i)
    print(kwargs["password"],"-----------",kwargs["address"])

showInfo("张佳玮",89,"男",1.76,156,password=159746,address="北京市昌平区沙河北大桥桥底下")
'''














def  getSum(a,b):
    c = a + b
    return c



