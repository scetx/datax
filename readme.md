# GGWP - Identifying Toxic Behavior in Gaming
Much like the general internet, racism and sexism thrive in the gaming world. Despite this area of the internet being established for years, people still experience unwarranted aggression from other players. Based on various surveys, we know that gamers on all platforms and variety of games face harrassment, abuse, and general toxicity every day. It is a widespread, universally prevalent problem plaguing the world of gaming. 

The bigger companies in the industry have had the funds, manpower, and resources to throw at this - and hence have come up with a number of ways to alleviate the problems to a certain extent. However, the smaller independent game developers or even smaller companies, must focus on the quality of the game itself to make a name for themselves and thrive in this competitive industry. However, this focus combined with a lack of resources at the onset leads to them having to compromise in other places. Such compromise comes back to be a big problem when their game really explodes onto the scene and/or goes viral causing an extreme increase in the gaming traffic. In such cases, the prevalence of out-of-control toxicity could prove to be a very poor user-experience for newer players of the game - causing them to keep away. This toxicity, thus, could very well be the reason behind the smaller gaming company not making it in the industry. 

With the intention of cleansing the gaming community of harassment as much as possible and helping smaller companies stay focused on the development of the game itself - rather than the logistics of handling toxicity, the goal of this project is to 1) create a detection method for tagging toxic behavior/players and 2) provide insights on toxic behavior/players.

Most, if not all, games nowadays have in-game chat enabled for players. With our solution, we aim to empower smaller game developers with a powerful chat application that they can integrate into their games directly. The beauty of our chat application? It's ability to prevent players from dishing out toxicity by 1) preventing them from sending the message and 2) reporting toxic players to the game moderators pre-emptively - before the message is sent. Such pre-emption, will allow gaming companies to get some insight into the players playing their games, and take appropriate action as required without needing other players to be exposed to such toxicity (and then having to report it). 

## This repo consists of two main high-level components: the model notebooks and the UI components.
More details are displayed in the corresponding folder's readme.

- **WebDeployment** contains the code for the UI, the server, and the pickled models for deployment.
- **Notebooks** contains the various notebooks used for the following purposes:
  - Model architecture
  - Toxic behavior/player insights
  - Player profiling
