from django.shortcuts import render
from myapp.models import CollaborativeList, Song
from django.http import HttpResponse


# Create your views here.
def addSongToPlaylist(request, playlistID):
    try:
        playlist = CollaborativeList.objects.get(id=playlistID)
        song = Song.objects.get(id=request.GET.get('song'))
    except CollaborativeList.DoesNotExist:
        return HttpResponse('"message" : "Playlist does not exist, invalid list id"')
    except Song.DoesNotExist:
        return HttpResponse('"message" : "Song does not exist, invalid song id"')

    playlist.songs.add(song)
    playlist.save()
    response = '"Song ' + str(song.name) + " added to playlist " + str(playlist.name) + '"'
    return HttpResponse('"message" : ' + response)


def removeSongFromPlaylist(request, playlistID):
    try:
        playlist = CollaborativeList.objects.get(id=playlistID)
        song = Song.objects.get(id=request.GET.get('song'))
    except CollaborativeList.DoesNotExist:
        return HttpResponse('"message" : "Playlist does not exist, invalid list id"')
    except Song.DoesNotExist:
        return HttpResponse('"message" : "Song does not exist, invalid song id"')

    playlist.songs.remove(song)
    playlist.save()
    response = '"Song ' + str(song.name) + " removed from playlist " + str(playlist.name) + '"'
    return HttpResponse('"message" : ' + response)


def sortList(request, playlistID):
    try:
        playlist = CollaborativeList.objects.get(id=playlistID)
    except CollaborativeList.DoesNotExist:
        return HttpResponse('"message" : "Playlist does not exist, invalid list id"')

    response = "[ "
    sortedList = playlist.songs.order_by('name')
    for song in sortedList:
        response += '"' + str(song) + '", '
    response += ' ]'
    return HttpResponse('"message" : ' + response)
