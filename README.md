# MusicArtist
Gathers essential data-points for your favorite music artists from various public sources.

## Installation via PyPi:
```
pip install music_artist
```

## Installation from source:
```
git clone https://github.com/yportne8/MusicArtist.git
cd MusicArtist
python setup.py install
```

### Gather essential data points for your favoriate artist.
```python
>>> from music_artist import MusicArtist
>>> artist = MusicArtist("21 pilots")
Unable to find 21 pilots.
Using closest match instead: Twenty One Pilots

>>> artist.name
'Twenty One Pilots'
>>> artist.albums()
['Blurryface', 'Trench', 'Vessel', 'Scaled And Icy', 'Twenty One Pilots']
>>> artist.singles()
['Shy Away',
 'Choker',
 'Levitate',
 'Heathens',
 'Stressed Out',
 'three songs',
 'The Hype (Alt Mix)',
 'Jumpsuit / Nico And The Niners',
 'Chlorine (Alternative Mix)',
 'Saturday',
 'Cut My Lip (Brooklyn)',
 'Level of Concern',
 'Lane Boy',
 'My Blood']
>>> artist.genres()
['Alternative',
 'Music',
 'Rock',
 'Adult Alternative',
 'Hip-Hop/Rap',
 'Underground Rap',
 'Indie Rock',
 'Rap']
```

### Sample Artist's Top Hits.
```python
>>> artist.tophits()
['Heavydirtysoul | Twenty One Pilots',
 'Stressed Out | Twenty One Pilots',
 'Ride | Twenty One Pilots',
 'Fairly Local | Twenty One Pilots',
 'Tear In My Heart | Twenty One Pilots',
 'Lane Boy | Twenty One Pilots',
 'The Judge | Twenty One Pilots',
 'Doubt | Twenty One Pilots',
 'Polarize | Twenty One Pilots',
 "We Don't Believe What's On TV | Twenty One Pilots",
 'Message Man | Twenty One Pilots',
 'Hometown | Twenty One Pilots',
 'Not Today | Twenty One Pilots',
 'Goner | Twenty One Pilots']
```

### Find Similar Artists
```python
 >>> artist.similar()
 ['AJR ~ Twenty One Pilots',
 'Bastille ~ Twenty One Pilots',
 'Fun. ~ Twenty One Pilots',
 'X Ambassadors ~ Twenty One Pilots',
 'AWOLNATION ~ Twenty One Pilots',
 'Imagine Dragons ~ Twenty One Pilots',
 'Jamie T. ~ Twenty One Pilots',
 'Jon Bellion ~ Twenty One Pilots',
 'Paramore ~ Twenty One Pilots',
 'Prose ~ Twenty One Pilots',
 'Walk the Moon ~ Twenty One Pilots',
 'Yungblud ~ Twenty One Pilots',
 'Best Frenz ~ Twenty One Pilots',
 'Breathe Carolina ~ Twenty One Pilots',
 'Cobra Starship ~ Twenty One Pilots',
 'Hard-Fi ~ Twenty One Pilots',
 'HØØNCH ~ Twenty One Pilots',
 'I Dont Know How But They Found Me ~ Twenty One Pilots',
 'Panic! At the Disco ~ Twenty One Pilots',
 'Quinn XCII ~ Twenty One Pilots',
 'USS (Ubiquitous Synergy Seeker) ~ Twenty One Pilots',
 'Youngblood Hawke ~ Twenty One Pilots',
 'gnash ~ Twenty One Pilots',
 'Goody Grace ~ Twenty One Pilots',
 'MGMT ~ Twenty One Pilots',
 'NF ~ Twenty One Pilots',
 'Parade of Lights ~ Twenty One Pilots',
 'Suckers ~ Twenty One Pilots',
 'Thirty Seconds to Mars ~ Twenty One Pilots',
 'Timeflies ~ Twenty One Pilots',
 '93PUNX ~ Twenty One Pilots',
 'All Get Out ~ Twenty One Pilots',
 'Bohnes ~ Twenty One Pilots',
 'Explorer Tapes ~ Twenty One Pilots',
 'Kulick ~ Twenty One Pilots',
 'L.I.F.T ~ Twenty One Pilots',
 'OneRepublic ~ Twenty One Pilots',
 'Saint PHNX ~ Twenty One Pilots',
 'Dub Pistols ~ Twenty One Pilots',
 'Linkin Park ~ Twenty One Pilots',
 'Death Cab for Cutie ~ Twenty One Pilots',
 'Sigur Rós ~ Twenty One Pilots',
 'MUTEMATH ~ Twenty One Pilots',
 'Cage the Elephant ~ Twenty One Pilots',
 'Justin Bieber ~ Twenty One Pilots',
 'The Chicks ~ Twenty One Pilots',
 'The Chainsmokers ~ Twenty One Pilots']
```