import itchat
itchat.login()
# itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)[0:]  # 获取微信朋友数据
# 定义计数
male = female = other = 0
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male +=1
    elif sex ==2:
        female += 1
    else:
        other +=1
# 计算总数
total = len(friends[1:])

# 打印好友性别比例
print("男性好友：    %.2f%%" % (float(male)/total*100) + "\n" +
      "女性好友：    %.2f%%" % (float(female)/total*100) + "\n" +
      "其他好友：    %.2f%%" % (float(other)/total*100))
