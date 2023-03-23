## 레진 계산기(Resin Calculator) Ver 1.0
## Author: Doheum Kim

# 모듈(Module)
from math import ceil

# 전역변수(Global Variables)
mat = int()     # 재료(경험치 or 모라) / Material (Experience or Mora)
re = ''         #재실행 여부 확인(Confirm whether to execute again)
mora = [0,0]    #모라(Mora)
e = {'exp':list(),'cur_exp':0,'target_exp':list(),'drop':[-1,0,0,0,0]}  # 국붕이의 경험, 모험가의 경험, 영웅의 경험 / 현재 경험치, 목표 경험치, 드랍보상(지맥)
                                                                        # Wanderer's Advice, Adventurer's Experience, Hero's Wit / Current Exp, Target Exp, Drop Reward(Outcrop)

## 전역변수 설명(Global Variables Description)

'''
mora[0]     #보유 모라(Owned Mora)
mora[1]     #목표 모라(Goal Mora)

e['exp'][0]      #초록책(Green Exp Book)
e['exp'][0]      #파란책(Blue Exp Book)
e['exp'][0]      #보라책(Purple Exp Book)

e['target_exp'][0]      #목표 초록책(Goal Green Exp Book)
e['target_exp'][1]      #목표 파란책(Goal Blue Exp Book)
e['target_exp'][2]      #목표 보라책(Goal Purple Exp Book)

e['drop'][0]        #월드렙(World Level)
e['drop'][1]        #최소 경험치(Minimum Exp)
e['drop'][2]        #최대 경험치(Maximum Exp)
e['drop'][3]        #평균 경험치(Average Exp)
e['drop'][4]        #모라(Mora)
'''


### 함수(Function) ###

def main(a):
    global mat,e
    mat = a
    lst =['','경험치 선택','모라 선택']
    print(f'{lst[mat]}\n잘못 입력하면 다시 입력해야 합니다')
    dash(18)
    while not (mat == 1 or mat == 2):
        mat = int(input('경험치:1 모라:2: '))
    while not (0 <= e['drop'][0] <= 8):
        e['drop'][0] = int(input('월드렙: '))
        dash(18)

    drop_by_lev(e['drop'][0])
    setting(mat)


def dash(n):    # "-" 출력(Print)
    print('-'*n)

def setting(mat):   #기본세팅(Default Settings)
    global e,mora
    
    if mat == 1:      #경험치책 계산(Exp Calculate)
        print('현재 가지고 있는 경험치 책 개수를 입력하세요')
        e['exp'] = list(map(int,input('초록 파랑 보라책(숫자만)\nex: 0 0 247\n입력: ').split(' ')))
        dash(30)

        e['cur_exp'] = e['exp'][0]*1000 + e['exp'][1]*5000 + e['exp'][2]*20000    #현재 경험치량(Current Experience Dimensions)
        print(f"현재 경험치량: {e['cur_exp']}")
        calc('exp')


    elif mat == 2:      #모라 계산(Mora Calculate)
        print('현재 가지고 있는 모라를 입력하세요(숫자만)')
        mora[0] = int(input('ex: 1525000\n입력: '))
        calc('mora')

def calc(mat):
    global e,mora
    dash(30)
    if mat == 'exp':
        print('원하는 책 개수를 입력해주세요')
        e['target_exp'] = list(map(int,input('초록 파랑 보라책(숫자만)\nex: 3 0 418\n입력: ').split(' ')))
        dash(30)

        e['target_exp'][0] *= 1000      #초록책 경험치(Green Book Exp)
        e['target_exp'][1] *= 5000      #파란책 경험치(Blue Book Exp)
        e['target_exp'][2] *= 20000     #보라책 경험치(Purple Book Exp)
        e['target_exp'].append(e['target_exp'][0]+e['target_exp'][1]+e['target_exp'][2])    #경험치 총합(Total Exp)
        #print(e)        # DEBUG


        need = e['target_exp'][3] - e['cur_exp']

        if need <0:
            need = e['cur_exp'] - e['target_exp'][3]
            a = -1
        elif need >= 0:
            a = 1
        
        ex1 = need//20000                       #보라책(Purple Exp Book)
        ex2 = (need-ex1*20000)//5000            #파란책(Blue Exp Book)
        ex3 = (need-ex1*20000-ex2*5000)//1000   #초록책(Green Exp Book)

        if a == 1:
            print(f'필요한 경험치: {need}\n보라책 {ex1}개, 파란책 {ex2}개, 초록책 {ex3}개')
            input('엔터 눌러서 넘기기\n\n\n')
            outcrop(mat,need)
        elif a == -1:
            ex1,ex2,ex3 = -1*ex1, -1*ex2, -1*ex3
            print(f'소모할 경험치: {need}\n보라책 {ex1}개, 파란책 {ex2}개, 초록책 {ex3}개')
            input('엔터 누르면 종료')

    elif mat == 'mora':
        print('원하는 모라를 입력해주세요')
        mora[1] = int(input('입력: '))
        need = mora[1]-mora[0]
        outcrop(mat,need)
        

    
    
'''
e['drop'][0]        #월드렙(World Level)
e['drop'][1]        #최소 경험치(Minimum Exp)
e['drop'][2]        #최대 경험치(Maximum Exp)
e['drop'][3]        #평균 경험치(Average Exp)
e['drop'][4]        #모라(Mora)
'''
def outcrop(mat,need):   #지맥(Ley Line Outcrop)
    global e,re,mora
    dash(40)
    if mat == 'exp':
        lst = ['','최소','최대','평균']
        for i in range(1,4):
            cnt = ceil(need/e['drop'][i])
            #remain = str(need/e['drop'][i]).split('.')[1]
            #if cnt == 0:
            #    cnt = 1
            remain = cnt * e['drop'][i] - need#round((int(remain) / 10**len(remain)) * e['drop'][i])
            resin = cnt * 20
            time = [0,0,resin * 8]
    
            ex1 = remain//20000                       #보라책(Purple Exp Book)
            ex2 = (remain-ex1*20000)//5000            #파란책(Blue Exp Book)
            ex3 = (remain-ex1*20000-ex2*5000)//1000   #초록책(Green Exp Book)]
    
            time[1] = time[2] // 60
            time[2] -= time[1] * 60
            prt_time = f'{time[1]}시간 {time[2]}분'
            #print( e['drop'][i],cnt,remain,time,prt_time,'a')      #DEBUG
    
            if time[1] >= 24:
                time[0] = time[1] // 24
                time[1] -= time[0] * 24
                prt_time = f'{time[0]}일 {time[1]}시간 {time[2]}분'
                
    
            print(f'{lst[i]}치: 지맥 {cnt}번(경험치 {remain} 남음)\n보라책 {ex1}개, 파란책{ex2}개, 초록책{ex3}개 남음\n레진 {resin}개({prt_time}) 필요')
            dash(40)
    
    
    elif mat == 'mora':
        if need < 0:
            print(f'{abs(need)}모라 쓰기')
        else:
            cnt = ceil(need/e['drop'][4])
            resin = cnt * 20
            time = [0,0,resin * 8]
            remain = cnt * e['drop'][4] - need

            time[1] = time[2] // 60
            time[2] -= time[1] * 60
            prt_time = f'{time[1]}시간 {time[2]}분'

            if time[1] >= 24:
                time[0] = time[1] // 24
                time[1] -= time[0] * 24
                prt_time = f'{time[0]}일 {time[1]}시간 {time[2]}분'

            print(f'지맥 {cnt}번({remain}모라 남음)\n레진 {resin}개({prt_time}) 필요')
            dash(40)




    re = input('\n\n\n엔터 누르면 종료, 아무거나 치면 재실행\n\n\n')
    if re != '':
        re = ''
        e['drop'][0] = -1
        main(int(input('1: 경험치, 2: 모라\n입력: ')))



def drop_by_lev(world_lev):

    if world_lev == 0:
        e['drop'][1] = 22000
        e['drop'][2] = 28000
        e['drop'][3] = 25000
        e['drop'][4] = 12000

    elif world_lev == 1:
        e['drop'][1] = 35000
        e['drop'][2] = 42000
        e['drop'][3] = 38500
        e['drop'][4] = 20000

    elif world_lev == 2:
        e['drop'][1] = 50000
        e['drop'][2] = 55000
        e['drop'][3] = 52500
        e['drop'][4] = 28000

    elif world_lev == 3:
        e['drop'][1] = 65000
        e['drop'][2] = 70000
        e['drop'][3] = 67500
        e['drop'][4] = 36000

    elif world_lev == 4:
        e['drop'][1] = 70000
        e['drop'][2] = 95000
        e['drop'][3] = 82500
        e['drop'][4] = 44000

    elif world_lev == 5:
        e['drop'][1] = 90000
        e['drop'][2] = 115000
        e['drop'][3] = 102500
        e['drop'][4] = 52000

    elif 6 <= world_lev <= 8:
        e['drop'][1] = 110000
        e['drop'][2] = 135000
        e['drop'][3] = 122500
        e['drop'][4] = 60000


### 실행부분(Execution part) ###
dash(25)
print('원신 지맥 계산기 Ver 1.0\nAuthor: Doheum Kim')
dash(25)
main(0)
