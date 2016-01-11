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
    print """
    Running perfomance test...
    [%d]:
    Ready, Play the song...""" % (count+1)

    input_keyword = commands.getoutput('osascript getsonginfo.scpt')
    song_info = ytt.searchSong(input_keyword)
    videoID = ytt.returnPlausibleVideoID(song_info)

    if videoID == False or videoID == None:
      # TODO: Exception Handdling
      #log_info: Cannot Find on Youtube and so put F as evaluation
      evaluations.append("F")
      count = count + 1
    else:
      url = "http://youtu.be/" + videoID
      webbrowser.open_new(url)
      print "Evaluation(T/F)",
      evaluation = raw_input(': ')
      evaluations.append(evaluation)
    
      print "(q: quit, c: continue)"
      select = raw_input(': ')
      count = count + 1

  precision = float(evaluations.count("T")) / len(evaluations)
  
  print "w(manual input)"
  w = int(raw_input(': '))

  recall = float(evaluations.count("T")) / ((evaluations.count("T")) + w)

  f_value = 2 * precision * recall / precision + recall

  now = datetime.datetime.today()
  file_name = './testlog/test' + now.strftime("%Y-%m-%d-%H-%M-%S")
  f = open(file_name, 'w')

  result_log = """
  Output: [%d] Trials
  Precision: %f
  Recall: %f
  F-value: %f
  """ % (count, precision, recall, f_value)
  
  f.write(result_log)
  f.close
  print result_log
  print "Write output in test log file..."

if __name__ == '__main__':
  main()
