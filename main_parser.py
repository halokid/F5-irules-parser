# -*- coding: utf-8 -*-
#author: r00x

import re

'''
其实只要拿到 每个 if, elseif, switch 里面的内容就可以了， 可以作为一个 dict， if， elseif 就是这个dict 的key
然后把具体的 if , elseif 里面的内容 全部都当作 key 的 value  赋值给 key 就是了
'''


def parserRules():
  '''
  主要解释入口
  '''
  f = open('../rules/case1.txt', 'r')
  content = f.read()
  if checkCase1(content):
    print 'it is case1'
  else:
    print 'not case1'



def checkCase1(txt):
  '''
  choose the case for the case txt
  '''
  if 'if' in txt and 'elseif' in txt and 'default' in txt:
    return True

  return False








def parserCase1():
  '''
  parser case1
  '''
  # f = open('../rules/case1.txt', 'r')
  f = open('../rules/case2.txt', 'r')
  # print f.read()
  content = f.read()

  parser_dict = {'if': []}
  domain = []
  #if, elseif
  if_part = re.findall(r"if(.*){", content)
  print if_part
  for item in if_part:
    tmp = re.findall("\[HTTP::host\] equals(.*)}", item)
    print 'tmp---------------------------', tmp
    tmp = tmp[0].replace('"', '').strip()
    print 'tmp---------------------------', tmp
    parser_dict['if'].append(tmp)
    domain.append(tmp)        #all domain names


  #switch, 这个是专门解释  switch 的， 不解释 default
  # switch_part = re.findall(r"switch(.*)(.|\n)*?\}", content)
  # switch_part = re.findall(r"switch(.|\n)*?(.*)default", content, re.S)
  #fixme: 这个是正确的
  # switch_part = re.findall(r"switch(.|\n)*?(.*)default", content, re.S)
  #fixme: 这个更正确
  switch_part = re.findall(r"switch(.|\n)*?(.*)}", content, re.S)
  print 'switch_part-------------------', switch_part[0][1]
  #看看 有多少个 default
  if 'default' in switch_part[0][1]:
    print 'more default-------------------------------------'

  # tmp_default = switch_part[0][1].split('default')
  tmp_default = switch_part[0][1].split('elseif')
  print 'default tmp len ----------------------------', len(tmp_default)
  urls = {}
  pools = {}
  if len(tmp_default) > 1:
    print 'more default xxx---------- start parser url------------------------'
    #--------------------------URL ----------------
    i = 0
    for url_block in tmp_default:
      print 'url block-------------------------------------', url_block
      urls_list = parserUrl(url_block)
      urls_list.append("default")
      urls[domain[i]] = urls_list
      i += 1
    print 'urls --------------------------------------------', urls

     #--------------------------POOL ----------------
    i = 0
    for pool_block in tmp_default:
      print 'pool block-------------------------------------', pool_block
      pool_list = parserPool(pool_block)
      # pool_list.append("default")
      # if i > 0:
      #   pool_list[len(pool_list)] =
      pools[domain[i]] = pool_list
      i += 1

    #-------------------------- DEFAULT ----------------
    # parserDefault(content)

    print 'pools --------------------------------------------', pools

  # return parser_dict
  return domain, urls, pools




def parserUrl(txt):
  '''
  get the url content
  :param txt:
  '''
  res = re.findall(r"/(.*)\"", txt)
  print 'url res---------------------', res
  return res


def parserPool(txt):
  '''
  get the pool content
  '''
  res = re.findall(r"pool(.*)\n", txt)
  res_tmp = []
  for item in res:
    res_tmp.append(item.strip())
  print 'block res---------------------', res_tmp
  return res_tmp



def parserDefault(txt):
  '''
  get the default content
  '''
  # res = re.findall(r"default(.*){\npool", txt, re.S)
  # res = re.findall(r"default(.|\n)*?(.*)}", txt, re.S)
  # res = re.findall(r"default(.|\n)*?(.*)}(.|\n)", txt, re.S)
  res = re.findall(r"default(.|\n)*?pool(.*)}(.|\n)", txt, re.S)
  print 'defalt res---------------------', res
  return res











