# Song-to-Genre-Classifier
## Song to Genre Classifier using Deep Learning

Ever since I started hearing music recommended to me by services such as Pandora or Spotify, I've always been disappointed in the music selections that they think "I might like". For example, just the other day I created a station from a song by Nirvana on Spotify. I wanted to hear some 90's grunge songs that day. However, just a few songs into the playlist that Spotify created, I started to hear songs from artists like, Led Zeppelin and Jimi Hendrix. Now, while I enjoy these Classic Rock bands, it just didn't fit into the genre that I was looking for. The reason for this is that their recommendation systems are built on what's called "collaborative filtering". Collaborative filtering bases their recommendations on historical usage data. Essentially, the system uses k nearest neighbors or a logistic regression classifier to recommend songs from other users who have listened to the same song as I just listened to. So, if Bob and I liked the same song, then I must like some other songs that Bob likes. 

### The problem with this is:   

1. My commonality with Bob in music taste may end there. What if Bob loves Barbara Streisand and Brittany Spears?
2. I want to hear UNPOPULAR music that most people don't listen to... Music that hasn't hit mainstream yet
3. I want to hear music that has similar audio characteristics (beat, intensity, rhythm, etc) to what I'm listening to.

So, in order to do this, I believe we should take an approach similar to how Shazam matches a "fingerprint" of a song to its database. I'd like to use an artificial neural net to match a "fingerprint" of a song to another very closely related "fingerprint". However, before I take on that endeavor, I'd like to first see if I can classify a song's "fingerprint" into a genre, and see how accurate this approach could be....

  So, first off, an introduction to the project, and we begin by viewing a song by it's inherent signal process: [Signal Processes by Genre](https://github.com/G1NO/Song-to-Genre-Classifier/blob/master/Intro_load_data.ipynb)
  
  Pretty cool to be able to visualize a song like this...as a signal. You can start to see the different patterns among the different genres...
  
  
