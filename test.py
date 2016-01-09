#!/usr/bin/python
# -*- coding: utf-8 -*-

#TODO: refactoring

import youtunestweet as ytt
import commands
import webbrowser
import datetime

def main():
  evaluations = []
  
  count = 0
  select = 'c'
  while(select!='q'):
    print "Running perfomance test..."
    print "Ready, Play the song..."

    kw = commands.getoutput('osascript getsonginfo.scpt')
    r = ytt.searchSong(kw)
    result = ytt.returnPlausibleVideoID(r)

    # TODO: Exception Handling
    if result == False or result == None:
      print "Cannot Find on Youtube",
      print "Put the F",
      evaluations.append("F")
      count = count + 1
    else:
      url = "http://youtu.be/" + ytt.returnPlausibleVideoID(r)
      webbrowser.open_new(url)
      print count+1,
      print "Evaluation(T/F)",
      evaluation = raw_input(': ')
      evaluations.append(evaluation)
    
      print "(q: quit, c: continue)"
      select = raw_input('>>> ')
      count = count + 1

  precision = float(evaluations.count("T")) / len(evaluations)
  print precision
  # log出力
  d = datetime.datetime.today()
  f_name = './testlog/test' + d.strftime("%Y-%m-%d-%H-%M-%S")
  f = open(f_name, 'w')
  f.write("precision: %f" % precision)
  f.close

if __name__ == '__main__':
  main()
