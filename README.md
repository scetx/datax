<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Seal_of_the_United_States_Cyber_Command.svg/1200px-Seal_of_the_United_States_Cyber_Command.svg.png" align="right" width="150"/>

# Visualizing Attacks in Cyberspace - DATA-X: United States Cyber Command

A simulation to model how viruses traverse through computer networks

![demo](https://media.giphy.com/media/ympEDqHCj3OdEGV9Ou/giphy.gif)

More examples of the simulation below

_____

### USCYBERCOM

- A folder containing scripts for our dynamic visualization. 
- Primary language is TypeScript.
- We recommend using Visual Studio Code's platform.
  - How to locally run the program in browser:
    - This is a parcel-based program, so first install Yarn
      - `brew install yarn` for MacOS, or navigate to their [website](https://classic.yarnpkg.com/en/docs/install/#windows-stable) to manually install for other operating systems
    - `yarn install` in VSC to download all dependencies for the project
    - Start parcel with command `yarn start` to view simulation
    
### attacksim
- An ipynb file containing the script for our static visualization. 
- Written in Python. 
- Run file on Jupyter to easily view visuals.
  
### other
- A folder containing earlier drafts of visualizations and simulations.

_____

## Purpose
Since 2010, the United States Cyber Command has been making strives towards cyberspace superiority by taking proactive and risk-aware strategies against adversaries. However, apart from developing cyber-combat methods, the USCC seeks to promote STEM disciplines to facilicate and enhance the nation's cyber talent by stimulating the interest of curious and technical individuals. The simulations that our team has developed will help bridge the knowledge gap between the general public and the complex universe of cyberspace by providing a simplified and accessible model to all. 

Perhaps inquisitive individuals will come across this simulation and wonder how exactly does active threat hunting or other cyber defense methods work in real cyberspace. 

![](https://media.giphy.com/media/TOWeGr70V2R1K/giphy.gif)


## Inspiration for this project
Our mentors at the United States Cyber Command approached us with inspiration from recent COVID-19 simulations which followed SIR epidemic models. In particular, it was an [article written by Harry Stevens](https://www.washingtonpost.com/graphics/2020/world/corona-simulator/) which included visualisations and graphics of what happens when people follow social-distancing rules and adhere to quarantine guidelines.

![Example](https://media.giphy.com/media/R1rR597cItIRhu3kaq/giphy.gif)

Our USCC mentors explained that they wanted us to produce an interactive, web-based visualization along the lines of Stevens' simulation. They suggested that the interface should allow users to adjust parameters (e.g. assumptions about the threat and network derfenses), as well as for the selection of several pre-defined, stylized scenarios to demonstrate the impacts of specific strategies (e.g. perimeter defense, zero-trust networking, and active threat hunting).

## The Project
The main libraries of this project are [react.js](https://reactjs.org/) and [material-UI](https://material-ui.com/). These javascript libraries allow for efficient event-handling, as well as a way to produce visually appealing interactive components such as the sliders and buttons. The structure of the nodes are all automated by a KD-Tree algorithm which finds the nearest neighbors for each node and connects links between them. When we start the simulation, one node is randomly chosen to be infected. Based on the vectors of the initial infected node, the virus travels down this path and infects other nodes and the loop repeats until the simulation is complete. 
___

## Defense Architecture
It's quite intuitive to compare the spread of human virsues to computer viruses. In a [paper](https://pubsonline.informs.org/doi/pdf/10.1287/ited.6.2.32) by CSU Fullerton students, it is proposed that human, animal, plant, and computer networks undergo the same process of susceptibility, infection and recovery; with variables that affect the rate of time for each process. In cybersecurity, the variables that affect the virus outbreak rate and recovery time depend on the strength of the network's defensive methods. Therefore, our demo includes two adjustable sliders for `virus spread rate` and `time in compromised state`. By adjusting these parameters, we are able to model the effects of [zero trust networking](https://www.paloaltonetworks.com/cyberpedia/what-is-a-zero-trust-architecture), and [active threat hunting](https://www.csoonline.com/article/3570725/threat-hunting-explained-taking-an-active-approach-to-defense.html).

### Zero Trust Network
This defensive architecture realizes that trust is a vulnerability. With this method, *microperimeters* are in place at every level to ensure that no trust is given, regardless of whether a user has access to a previous checkpoint. Multi-factor Authentification is a core tenent of this security style, so think of any application where you might have to verify your identity before you are allowed access to information (e.g. Berkeley's DUO two-step verification). To model this, we set `virus spread rate` to a low number. The parameter `time in compromised state` is unaccounted for, because implementing only a zero trust network doesn't automatically ensure the resolution of a virus in a timely matter. 

<p align="center">
  <img src="https://media.giphy.com/media/183w2aHNTpjn365r0X/giphy.gif" alt="animated", align="center" />
</p>

In this run, we can see that the histogram timeline of infected nodes is much flatter in comparison to the simulation runs at the top of this file. 


### Active Threat Hunting
Threat hunting takes a more proactive approach in resolving viruses and attacks. This method of defense assumes that an attacker is always lurking in the network, and looks for signs of suspicious activity in order to prevent cascading effects. We set `virus spread rate` and `time in compromised state` to a low number to model this scenario. 

<p align="center">
  <img src="https://media.giphy.com/media/yhOUIlqYt6rukpEand/giphy.gif", align="center" />
</p>

In this run, we can see that the virus has barely any chance to infect other nodes because it is recovered right away.

## Acknowledgements
We would like to give a big thank you to Jack Herrington, a principal software engineer, and a [Youtuber](https://www.youtube.com/channel/UC6vRUjYqDuoUsYsku86Lrsw) who creates videos on frontend tutorials, as well as other technology deep-dives. We came across his Youtube video on his version of an epidemic simulator, and we reworked and collaborated with Jack on his open-source code to produce this project.
