# -*- coding: utf-8 -*-
#author: r00x

import re

'''
其实只要拿到 每个 if, elseif, switch 里面的内容就可以了， 可以作为一个 dict， if， elseif 就是这个dict 的key
然后把具体的 if , elseif 里面的内容 全部都当作 key 的 value  赋值给 key 就是了
'''

def checkCase():
  '''
  choose the case for the case txt
  '''
  print 'xx'



def parserCase1():
  '''
  parser case1
  '''
  f = open('../rules/case1.txt', 'r')
  # print f.read()
  content = f.read()

  parser_dict = {'if': []}
  #if, elseif
  if_part = re.findall(r"if(.*){", content)
  print if_part
  for item in if_part:
    tmp = re.findall("\[HTTP::host\] equals(.*)}", item)
    print 'tmp---------------------------', tmp
    tmp = tmp[0].replace('"', '').strip()
    print 'tmp---------------------------', tmp
    parser_dict['if'].append(tmp)


  #switch, 这个是专门解释  switch 的， 不解释 default
  # switch_part = re.findall(r"switch(.*)(.|\n)*?\}", content)
  # switch_part = re.findall(r"switch(.|\n)*?(.*)default", content, re.S)
  switch_part = re.findall(r"switch(.|\n)*?(.*)default", content, re.S)
  print 'switch_part-------------------', switch_part[0][1]
  #看看 有多少个 default
  if 'default' in switch_part[0][1]:
    print 'more default-------------------------------------'


  return parser_dict












