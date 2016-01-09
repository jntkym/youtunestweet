#!/usr/bin/python
# -*- coding: utf-8 -*-

import youtunestweet as ytt
import commands
import webbrowser

def main():
  evaluations = []
  
  select = 'c'
  while(select!='q'):
    print "Running perfomance test..."
    print "Ready, Play the song..."

    kw = commands.getoutput('osascript getsonginfo.scpt')
    r = ytt.searchSong(kw)
    url = "http://youtu.be/" + ytt.returnPlausibleVideoID(r)
    webbrowser.open_new(url)
    
    print "Evaluation(T/F)"
    evaluation = raw_input(': ')
    evaluations.append(evaluation)
    
    print "(q: quit, c: continue)"
    select = raw_input('>>> ')

  precision = float(evaluation.count("T")) / len(evaluation)
  #recall = 
  #f_value = 
  print precision
  #ログファイルに書き込む

if __name__ == '__main__':
  main()
