# CarolinaDataChallenge

##Inspiration
The term ‘Y2K’ refers to a pop culture era from the late 1990s to the early 2010s. Y2K trends, including music, have made a comeback in the 2020s and this nostalgia has proved to be extremely profitable.

##What it does In this project
we analyzed the top songs in each month from 2000 to 2010 to identify music features that lead to high revenue and position in charts.

##How we built it 
We used Python to get data from the Spotify API into a csv format. Then we used R to create the regression models. Lastly, we used Tableau to create the visualizations.

##Challenges we ran into 
Spotify has an API rate limit that limited us from pulling audio features from many songs. Data was a bit difficult to understand and interpret at first.

##Accomplishments that we're proud of 
We tackled the hardest track in the competition and were able to get meaningful data with practical insights in a short timeframe.

##What we learned 
We found that tracks with high revenue tend to be longer, more upbeat, lower energy, slower tempos, and wordier. Tracks with top positions on charts tend to be more suitable for dancing and be in a major key. First Class, a 2022 hit by Jack Harlow, samples Fergie’s Glamorous, a 2006 single. Both tracks have similar audio features such as energy, tempo, and danceability. First Class has a lower energy, slower tempo, and more danceability than Glamorous, which our models recommend. We suggest that music labels optimize the features in our models when selecting which hits to sample and remix.

##What's next for Spotify Track Analysis: 
Audio Features from 2000 to 2010 We would like to add more songs and compare across every decade, across different genres, and across different regions of the world
