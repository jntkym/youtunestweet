on replaceText(myText, serchStr, replaceStr)
  set theDelim to AppleScript's text item delimiters
  set AppleScript's text item delimiters to serchStr
  set the List to every text item of myText
  set AppleScript's text item delimiters to replaceStr
  set myText to theList as string
  set AppleScript's text item delimiters to theDelim
  return myText
end replaceText

tell application "iTunes"
  set artist_name to artist of current track
  set track_name to name of current track
end tell

set artist_name to replaceText(artist_name, "\"", " ")
set track_name to replaceText(track_name, "\"", " ")
do shell script "python ~/youtunetweet.py \"" & artist_name & "\" \"" & track_name & "\""
