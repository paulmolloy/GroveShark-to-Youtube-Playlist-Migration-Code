#creates a playlist in new txt file of all of the songs in two playlists stored in two seperate txt files with each song sepeated by a new line.
def playlistsorter():

    playlist1 = []
    playlist2 = []
    file1 ='paulsplaylist.txt'
    file2 ='alans_groovemerge_playlist.txt'
    newplaylist= playlist2
    with open(file1) as inputfile:
        for line in inputfile:
            playlist1.append(line)

    with open(file2) as inputfile2:
        for line in inputfile2:
            playlist2.append(line)

    for line in playlist1:
        if line not in playlist2:
            newplaylist.append(line)
    newplaylistfile = open("newplaylist.txt", "w")
    for line in newplaylist:
        newplaylistfile.write(line)
        
    print(newplaylist)
    newplaylistfile.close()
    return newplaylist
print playlistsorter()
