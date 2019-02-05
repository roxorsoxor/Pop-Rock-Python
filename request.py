import requests

# Get MBID for artist
# By going to MusicBrainz.org and search
# Refer to blog post on next line for instructions
# https://jotascript.wordpress.com

aliceCooperPerson = 'ee58c59f-8e7f-4430-b8ca-236c4d3745ae'
aliceCooperBand = '4d7928cd-7ed2-4282-8c29-c0c9f966f1bd'

# Loop through Releases array 
# For each Release, get MBID for recordings on that release
# Store MBID for each Recording in an array

# MusicBrainz variables
MusicBrainz_baseURL = 'https://www.musicbrainz.org/ws/2/'

# Part of URL for using artist MBID
MusicBrainz_artistMethod = 'artist/'

MusicBrainz_artistMBID = aliceCooperPerson

# Part of URL for getting MusicBrainz Release Groups info
MusicBrainz_releaseGroups = '?inc=release-groups'

# Get Release-Groups for artist from MusicBrainz
releaseGroups_totalURL = MusicBrainz_baseURL + MusicBrainz_artistMethod + MusicBrainz_MBID + MusicBrainz_releaseGroups + MusicBrainz_apiKey + jsonFormat

# Store MBID for each Release-Group in an array

MusicBrainz_releasegroupMBID = ''

# Loop through Release-Group array


# For each Release-Group, get MBID for releases in that group
# Part of URL for using Release Groups MBID to get Releases
MusicBrainz_releasegroupMethod = 'release-group/'

# Part of URL for getting MusicBrainz Releases info
MusicBrainz_releases = '?inc=releases'

# Get Releases for a Release-Group from MusicBrainz
releases_totalURL = MusicBrainz_baseURL + MusicBrainz_releasegroupMethod + MusicBrainz_MBID + MusicBrainz_releaseGroups + MusicBrainz_apiKey + jsonFormat

# Store MBID for each release in an array

# Loop through each release in the release array

# Part of URL for using Release MBID
MusicBrainz_releaseMethod = 'release/'

MusicBrainz_releaseMBID = ''

# For each Release, get MBID for all Recordings and store them in an array

# Part of URL for getting MusicBrainz Recordings info
MusicBrainz_recordings = '?inc=recordings'

# Store MBID for Recordings in an array

# Recording MBID isn't used at MusicBrainz but at LastFM
MusicBrainz_recordingMBID = ''

# MusicBrainz response format
MusicBrainz_jsonFormat = '&fmt=json'

# Total MusicBrainz URL
MusicBrainz_totalURL = MusicBrainz_baseURL + MusicBrainz_artistMethod + MusicBrainz_MBID + MusicBrainz_releaseGroups + MusicBrainz_apiKey + jsonFormat







response = requests.get('')

# LastFM variables
LastFM_baseURL = 'http://ws.audioscrobbler.com/2.0/?method='

# Part of URL for getting LastFM artist info
LastFM_artistInfo = 'artist.getinfo&mbid='

LastFM_artistMBID = MusicBrainz_artistMBID

# Part of URL for getting LastFM album info
LastFM_albumInfo = 'album.getinfo&mbid='

LastFM_albumMBID = '' # item in array of MusicBrainz_releaseMBID 

# Part of URL for getting LastFM album info
LastFM_trackInfo = 'track.getinfo&mbid='

LastFM_trackMBID = '' # item in array of MusicBrainz_recordingMBID 

# LastFM API key
LastFM_apiKey = '&api_key=333a292213e03c10f38269019b5f3985'

# LastFM response format
LastFM_jsonFormat = '&format=json'

# Total LastFM URL
LastFM_totalURL = LastFM_baseURL + LastFM_artistInfo + LastFM_MBID + LastFM_apiKey + LastFM_jsonFormat

# Other LastFM
LastFM_artistListeners = ''
LastFM_artistPlaycount = ''
LastFM_albumListeners = ''
LastFM_albumPlaycount = ''
LastFM_trackListeners = ''
LastFM_trackPlaycount = ''

# Get artist Listeners and Playcount from LastFM

# Get Listeners and Playcount for each Album (using Release MBID) by an Artist

# Get Listeners and Playcount for each Track (using Recording MBID) on an Album

f = open ('artist.json', 'a') # a is for append if artist dict already started
f.write ('variable goes here for data from MusicBrainz')
f.close()

# Questions to ask 
## Which artists, albums, tracks, have a lower listener-to-play ratio?

response = requests.get('https://en.wikipedia.org/wiki/Nobel_Prize')