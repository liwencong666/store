
#牛仔裤销量
mc1=(60 + 72 + 35 + 90 + 60 + 60 + 140)
#羽绒服销量
mc2=(10 + 69 + 140 + 10 + 10)
#风衣销量
mc3=(43 + 25 + 43 + 60 + 43 + 78)
#皮草销量
mc4=(63 + 24 + 63 + 57)
#T-shirt销量
mc5=(63 + 45 + 129 + 63 + 58 + 48 + 63)
#衬衫销量
mc6=120
#所有销售量
mc7=1844
#牛仔裤销售额
xse1=(86.3 * mc1)
#羽绒服销售额
xse2=(253.6 * mc2)
#风衣销售额
xse3=(96.8 * mc3)
#皮草销售额
xse4=(135.9 * mc4)
#T-shirt销售额
xse5=(65.8 * mc5)
#衬衫销售额
xse6=(49.3 * mc6)

print("-----------每种衣服销售占比---------------")
print("牛仔裤销售占比为：",round(mc1 / mc7 ,2),"%")
print("羽绒服销售占比为：",round(mc2 / mc7 ,2),"%")
print("风衣销售占比为：",round(mc3 / mc7 ,2),"%")
print("皮草销售占比为：",round(mc4 / mc7 ,2),"%")
print("T-shirt销售占比为：",round(mc5 / mc7 ,2),"%")
print("衬衫销售占比为：",round(mc6 / mc7 ,2),"%")
print("----------------------------------------")


print("-----------每种衣服销售额占比------------------")
print("牛仔裤销售额占比为：",round(xse1 / (xse1 + xse2 +xse3 + xse4 + xse5 + xse6),2),"%")
print("羽绒服销售额占比为：",round(xse2 / (xse1 + xse2 +xse3 + xse4 + xse5 + xse6),2),"%")
print("风衣销售额占比为：",round(xse3 / (xse1 + xse2 +xse3 + xse4 + xse5 + xse6),2),"%")
print("皮草销售额占比为：",round(xse4 / (xse1 + xse2 +xse3 + xse4 + xse5 + xse6),2),"%")
print("T-shirt销售额占比为：",round(xse5 / (xse1 + xse2 +xse3 + xse4 + xse5 + xse6),2),"%")
print("衬衫销售额占比为：",round(xse6 / (xse1 + xse2 +xse3 + xse4 + xse5 + xse6),2),"%")







