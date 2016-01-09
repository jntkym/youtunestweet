tell application "iTunes"
  repeat
    if (player state) is playing then
      set currentSong to name of current track
      set currentArtist to artist of current track
      exit repeat
    end if
  end repeat

  repeat
    if (player state) is paused then
      exit repeat
    end if
  end repeat
end tell

return ((currentArtist) as string) & " - " & ((currentSong) as string)
