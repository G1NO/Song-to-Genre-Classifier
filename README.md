# Song-to-Genre-Classifier
Song to Genre Classifier using artificial neural networks

Ever since I started hearing music recommended to me by services such as Pandora or Spotify, I've always been extremely disappointed in the music selections that "I might like". Guess what guys, I don't like 85% of the music that you think I'd like. The reason for this is that their recommendation systems are not designed how they should be. They used what's called "collaborative filtering". Collaborative filtering bases their recommendations on historical usage data from past users. Essentially, using k nearest neighbors or a logistic regression classifier to find songs that might be similar to something you'd like. 
The problem with this is:   
1. People are unique - not everyone likes the same music
2. I want to hear NEW music
3. I want to hear UNPOPULAR music
4. I want to hear music that is similar to what I'm listening to...not what someone else thinks I'd like

So, in order to do this, I believe we should take an approach similar to how Shazam matches a "fingerprint" of a song to its database, and use an artificial neural net to match a "fingerprint" of a song to another very closely related fingerprint. However, before I take on that endeavor, I'd like to first see if I can classify a song into a genre, to see how accurate this approach could be....

<a https://github.com/G1NO/Song-to-Genre-Classifier/blob/master/Intro_load_data.ipynb />
