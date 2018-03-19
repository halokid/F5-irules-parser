# -*- coding: utf-8 -*-
#author: r00x

import re
'''
其实一开始的出发点就是错的， 因为我们是要在文件中获取 pool, path, domain 这些信息， 而不是获取
switch, if, elseif, else 等这些无用的信息， 加上 文件内容也不是太大， 而且文件特征非常多变，所以
我们还是采取逐行读取的方式， 然后只是拿我们要的关键信息就可以了， 这样的话就可以免去匹配N多特征的烦恼， 而且匹配
N多特征的做法效率很低很低~~ 是一种蠢方法


我们要拿的最大基数， 其实就是 pool， 因为 domain, path 都有可能比 pool 的基数少的。
目前能想到的一种比较明智的做法就是， 每匹配到 有关于 domain,  path, pool  的行的时候， 我们据给 一个 dict
加入一条 记录， 这条记录也是一个 dict，  key 分别是  domain， path， pool 就可以了， domain 这个东西可以
沿用上一个循环的

而且逐行读取还有一个好处就是， 正则匹配起来比较简单， 程序不会那么难读
'''



def parserRules():
  '''
  逐行读取
  :return:
  '''
  # f = open('../rules/case1.txt', 'r')
  # file_name = 'case1.txt'
  # file_name = 'case2.txt'
  # file_name = 'case3.txt'
  # file_name = 'case4.txt'
  file_name = 'case5.txt'
  f = open('../rules/' + file_name, 'r')
  lines = f.readlines()
  all_info = []
  line_info = {}

  #有path的话， 就沿用到 发现有 pool 的时候， 给pool用
  path = ''
  domain = ''
  for line in lines:
    #如果行开头是 #的话， 就不用理会
    tmp_comm = re.findall(r"#(.*)\n", line)
    if tmp_comm:
      continue

    # print 'line ---------------------------------', line

    tmp_domain = getDomain(line)
    if tmp_domain != '':
      domain = tmp_domain

    tmp_path = getPath(line)
    if tmp_path != '':
      path = tmp_path

    #碰到有path才组合数据
    pool = getPool(line)
    if pool != '':
      line_info['pool'] = pool
      line_info['path'] = path
      line_info['domain'] = domain


    if pool != '':
      print 'line_info --------------------------------------- ', line_info





def getPool(line):
  tmp = re.findall(r"pool(.*)\n", line)
  print 'pool tmp ---------------------------', tmp
  if tmp:
    return tmp[0].strip()
  else:
    return ''



def getPath(line):
  tmp = re.findall(r"/(.*)\"", line)
  print 'path tmp ---------------------------', tmp
  if tmp:
    return tmp[0].strip().replace('*', '')
  else:
    tmp2 = re.findall(r"default", line)
    if tmp2:
      return 'default'
  return ''





def getDomain(line):
  tmp = re.findall("\[HTTP::host\] equals(.*)}", line)
  print 'domain tmp ---------------------------', tmp
  if tmp:
    return tmp[0].replace('"', '').strip()
  else:
    return ''












