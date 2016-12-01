#Formats txt file exported from grooveshark into a better format for adding them to a youtube playlist.
#Returns list of lines which do not match the expected format of a song (some songs uploaded just had mispelled song name and no artist album etc)
def grooveformatter():
    playlist1 = []
    formattedpl = ['[{"title":"iamback\'s Playlist 1","titleList":[']
    irregulars = []
    file1 = 'alans_groovemerge_playlist.txt.'
    start= '[{"title":"Alan\'s Merged Playlist","titleList":['
    with open(file1) as inputfile:
        for line in inputfile:
            playlist1.append(line.replace('\n', ''))
            
    for song in playlist1:
        details = song.split(',')
        if len(details) == (3 or 4):
            if details[0] != '"SongName"':
                (formattedpl.append((details[1] + details[0]).replace('""',' ')+','))
        if len(details) !=(3 or 4):
            irregulars.append(details[:-1])
    formattedpl[-1] = formattedpl[-1][:-1]  
    formattedpl.append(']}]')                        
    newplaylistfile = open("alan_merged_formatted.txt", "w")
    for line in formattedpl:
        newplaylistfile.write(line)
        
    
    newplaylistfile.close()
    return irregulars
print grooveformatter()
        
