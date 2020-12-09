# AdShift
AdShift aims to identify bias in advertising models and diversify their audience targeting strategies to combat such bias. This project was developed in collaboration between students in the Data-X course at UC Berkeley and mentors from Kinesso of Interpublic Group, with all members listed below:
#### &nbsp;&nbsp;&nbsp;&nbsp; Data-X:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ◦&nbsp;&nbsp;Shaya Barry ([shayabarry@berkeley.edu](mailto:shayabarry@berkeley.edu))  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ◦&nbsp;&nbsp;Dillon Eskandar ([dilloneskandar@berkeley.edu](mailto:dilloneskandar@berkeley.edu))  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ◦&nbsp;&nbsp;Wei Huang ([wei_huang@berkeley.edu](mailto:wei_huang@berkeley.edu))  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ◦&nbsp;&nbsp;Fernanda Ramos ([framos0421@berkeley.edu](mailto:framos0421@berkeley.edu))  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ◦&nbsp;&nbsp;Sneha Sudhakar ([sneha_sudhakar@berkeley.edu](mailto:sneha_sudhakar@berkeley.edu))  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ◦&nbsp;&nbsp;Zichen Zhao ([zzc@berkeley.edu](mailto:zzc@berkeley.edu))  
#### &nbsp;&nbsp;&nbsp;&nbsp; Kinesso:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ◦&nbsp;&nbsp;Bill Lyman, Director of R&D ([william.lyman@kinesso.com](mailto:william.lyman@kinesso.com))  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ◦&nbsp;&nbsp;Graham Wilkinson, EVP of Product Strategy & Innovation ([graham.wilkinson@kinesso.com](mailto:graham.wilkinson@kinesso.com))  

## Introduction and Problem
Kinesso is the marketing intelligence engine of Interpublic Group, and as a company, it focuses on using data and technology to improve media and marketing performance. Kinesso directs the purchase of millions of digital advertising impressions every second using advanced targeting strategies. 

One of the major issues with Kinesso’s advertisement targeting model, however, is its inherent bias against various underrepresented populations. This bias problem starts with a lack of true diversity in the population data used as a foundation of the advertisement targeting model. The algorithms used to award advertising space to the highest bidders are influenced by audiences that have a history logging impressions. Combined with the fact that these algorithms are also limited by brand marketing budgets, cheaper ad space for more easily reachable audiences is prioritized over potentially more expensive ads for less represented people groups. This problem is perpetuated by the fact that the model is currently built upon a very complex positive feedback loop. So, while its intention is to maximize a given brand’s return on investment, it continually narrows the group of people it selects from and neglects groups that have been marginalized for various reasons. 

## Solution
AdShift's approach to debiasing has two major components. It first identifies where bias exists within the current advertisement targeting models by comparing demographic datasets to reached datasets on features such as, ethnicity, income, and age group. These insights are then used to diversify target audiences, suggesting new opportunities for brands to allocate resources towards underrepresented demographics in the future.

### *Measuring and Visualizing Bias*

### *Diversifying Target Audiences*

Our project began by analyzing a demographic dataset which is used to represent the target audience and an dataset of impressions from Kinesso which is used to represent the actual audience reached by the current targeting model. 

The exploratory analysis for the demographic data consists of exploring the three features of age, ethnicity, and income brackets for every zipcode in the dataset. The data is broken down by zip code then categorizing by the three features and reports the count for such bracket. The analysis was also focused on zip codes and included functions where the input was a zip code and the output was a visualization of the distribution of ages or ethnicity or income for that zip code. 
