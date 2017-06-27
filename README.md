# Song-to-Genre-Classifier
Song to Genre Classifier using artificial neural networks

Ever since I started hearing music recommended to me by services such as Pandora or Spotify, I've always been extremely disappointed in the music selections that "I might like". I find that I really don't like most of the music that I'm recommended. The reason for this is that their recommendation systems are not designed how they should be. They use what's called "collaborative filtering". Collaborative filtering bases their recommendations on historical usage data. Essentially, using k nearest neighbors or a logistic regression classifier to find songs that might be similar to something you'd like. 
The problem with this is:   

1. People are unique - not everyone likes the same music (obviously)
2. I want to hear UNPOPULAR music
3. I want to hear music that is similar to what I'm listening to...not what someone else thinks I'd like

So, in order to do this, I believe we should take an approach similar to how Shazam matches a "fingerprint" of a song to its database, and use an artificial neural net to match a "fingerprint" of a song to another very closely related fingerprint. However, before I take on that endeavor, I'd like to first see if I can classify a song into a genre, to see how accurate this approach could be....

  So, first off, an introduction to the project, and we begin by viewing a song by it's inherent signal process: [Signal Processes by Genre](https://github.com/G1NO/Song-to-Genre-Classifier/blob/master/Intro_load_data.ipynb)
  
  Pretty cool to be able to visualize a song like this...as a signal. You can start to see the different patterns among the different genres. 
  
  
