# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
import main_parser
import main_parser_optimize as mpo

def testParserCase1():
  main_parser.parserCase1()



def testDealParser():
  domain, urls, pools = main_parser.parserCase1()
  print 'domain---------------------------', domain
  print 'urls---------------------------', urls
  print 'pools---------------------------', pools

  for k in urls:
    print 'k---------------', k
    i = 0
    for item in urls[k]:
      print '\turl---------------', item
      print '\tpool---------------', pools[k][i]
      i += 1


def testMainParser():
  main_parser.parserRules()



def testParserOp():
 mpo.parserRules()



