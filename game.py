#-*- coding: UTF-8 -*-
#引入模块
import random
import sys
#游戏规则
winlist = [['石头','剪刀'],['剪刀','布'],['布','石头']]

#选择列表
choiceList =['石头','剪刀','布']

#用户提示
prompt = '''请选择：,
(1)石头
(2)剪刀
(3)布
(4)退出'''

while True:
	try:
		choicenum =int(input(prompt))
		if choicenum == 3:
			break
		compchoice = random.choice(choiceList)			
		userchoice = choiceList[choicenum-1]
		compare = [compchoice,userchoice]
		print('你选择了%s,电脑选择了%s'%(userchoice,compchoice))
		#输赢判断
		if userchoice == compchoice:
			print('战平！')
		elseif compare in winlist:
			print('你输了，再来一局')
		else:
			print('你赢啦！')
