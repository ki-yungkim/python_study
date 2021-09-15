#!/usr/bin/env python
# coding: utf-8

# In[80]:


import random
# 전체 명단
members = ['a', 'b', 'c', 'd','e', 
           'f', 'g', 'h', 'i', 'j', 
           'k', 'l', 'm', 'n', 'o', 
           'p', 'q']

# num : 조당 몇명으로 할지
num = 4

def randomTeam(members, num):
    print('총', len(members), '명')
    teamNum = len(members)//num
  
    for i in range(0, teamNum):
        team = random.sample(members, num)
        print(i+1,'팀', team)
        
        #뽑힌 멤버는 리스트에서 제거
        for j in range(num):
            members.remove(team[j])
    
    # 인원수 적은 조
    #members가 비어있으면 출력X
    if members:
        print(teamNum + 1, '팀', members)
    
    
randomTeam(members, num)

