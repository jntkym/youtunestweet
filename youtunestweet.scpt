tell application "iTunes"
  set artist_name to artist of (current track) as string
  set track_name to name of (current track) as string
end tell

do shell script "python ./youtunestweet.py -artist \"" & artist_name & "\" -song \"" & track_name & "\""