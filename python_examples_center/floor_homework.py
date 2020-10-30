"""
@author zhangyachao
@studentNo 2001220198
@date 10/18/2020
"""
def judgeRealFloor():
    while True:
        try:
            floor = int(input("请输入floor:"))
        except:
            print("楼层信息非法，请重新输入!")
        else:
            if floor == 14 or floor == 18 or floor == 0:
                floor = "输入不正确，请输入正确的楼层"
            elif floor < 14:
                pass
            elif floor < 18:
                floor -= 1
            else:
                floor -= 2
            print("实际楼层:", floor)

if __name__ == '__main__':
    judgeRealFloor()