# GroveShark-to-Youtube-Playlist-Migration-Code
Code to combine exported Grooveshark playlists and convert them so they could be added as Youtube playlists.


When grooveshark was shut down in  April 2015 I was left with only exported txt files of all of my playlists. I decided to write some python code to combine them into 
one big playlist. Later I wrote another program 'grooveformatter.py to convert the format from:
		<code>"SongName","ArtistName","AlbumName"</code> 
    with each song separeated by new lines to

		[{"title":"myPlaylistName","titleList":["Bob Dylan With God On Our Side",..., "learn my lesson well kaiser Chiefs" ]}]
so that I could easily use code someone else wrote to create a youtube playlist of the first youtube result of each song so I could listen to my playlists again. 

NOTE: Any lines in the txt file that did not match the pattern were returned so I could look through them by hand.
