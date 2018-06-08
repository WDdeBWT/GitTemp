import random

word_list = [
    ['formal', '正式的', False],
    ['perform', '执行，做', False],
    ['formation', '形成，创造，（已形成的东西）', False],
    ['reformatory', '感化的，起改革作用的', False],
    ['informed', '了解情况的，见多识广的', False],
    ['informative', '提供情报的，增长知识的', False],
    ['conform', '符合，遵守，顺从', False],
    ['formulate', '阐明，规划，构想', False],
    ['uniformity', '一致性，统一性', False],
    ['formidable', '可怕的，艰难的', False],
]

while(True):
    rd = random.randint(0,len(word_list)-1)
    if word_list[rd][2] != True:
        print('------------------------------')
        print('------------------------------')
        print('------------------------------')
        print('------------------------------')
        print('------------------------------')
        print(word_list[rd][0])
        input()
        print(word_list[rd][1])
        a = input()
        if a == '1':
            word_list[rd][2] = True
