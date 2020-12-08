# Police Bias
## Summary
The tragic deaths of Ahmaud Arbery, Breonna Taylor, George Floyd, and countless other black lives lost to police brutality and senseless violence have spurred calls for policy reform and police accountability among the public. There is a greater consensus in the role racial inequality plays in our criminal justice system since the beginning of the pandemic. 

But how can we use data to prove that racism and unjust practices from police officers are intertwined? Our problem statement is how might we quantify and visualize bias in police departments over a period of time to determine if police accountability has changed alongside increased public pressure?

As a solution, we developed a police bias diagnostic tool that helps the general public, policy makers, and police departments identify bias in law enforcement by analyzing past department records and displaying the results in a detailed analytic report. Our tool calculated an overall diagnostic score that takes into account racial bias and excessive force, using stop data, excessive force reports, and population demographics over four years in seven different U.S. cities. The resulting diagnostic scores and calculations are presented in an interactive Tableau dashboard that enables users to understand just how great the difference in police treatment is between people of color and white Americans.

## Project Components
### 1. [`data_clean`](/data_clean)

We sourced our datasets from official city and police department websites. Using Python's `pandas` library, we loaded the `.csv` and/or `.xlx` files into a dataframe to extract and calculate the features we needed for our project. We also used official census data to determine the demographics of the city. Since census data is only reported every 10 years, we used official population projection tables for each year in 2016-2019. For each city, we compiled this information into a dataframe containing:
- Year
- Total Population
- Population Percentage of Each Race
- Number of Drive Stops, by Driver Race
- Use of Force, by Driver Race

For example, we obtained our New York City stop data [here](https://www1.nyc.gov/site/nypd/stats/reports-analysis/stopfrisk.page). Some files were uploaded in a `.csv` file format, while others were uploaded as an Excel spreadsheet. In these datasets, column names and values were often abbrievated or codified. They were difficult to interpret without data dictionaries that were enclosed in separate Excel spreadsheets. Our dataframe transformations displayed the data in a clear, consistent, and comprehensible manner across cities.

### 2. [`bias_scores`](/bias_scores)

We calculated bias scores using an original algorithm developed in consultation with public policy experts. The Jupyter Notebooks containing our algorithm and methodology can be found in [`notebooks/.ipynb_checkpoints`](notebooks/.ipynb_checkpoints).

### 3. [`notebooks`](/notebooks)

For each city, we used our cleaned dataframes to calculate:
- Logit Scores
- Racial Bias Z-Scores
- Confidence Intervals
- Excessive Force Scores
- Diagnostic Scores

### 4. [`visualizations`](/visualizations)

Using Tableau, we created visualizations of:
- Percentage of Drive Stops Involving Force, by City and Year
- Percentage of Drive Stops Involving Force, by Race, City, and Year
- Percentage of Stops Involving Drivers of a Given Race Relative to their Population for each Race, by City and Year
- Racial Bias Scores for All Cities Over Time
- Use of Force Scores for All Cities Over Time
- Diagnostic Scores for All Cities Over Time

This information is viewable for each city, or in aggregate across all cities.

The data source connection to tableau may error when you open the notebook. If this occurs simply follow the prompt to connect a new data source and connect the all_cities_bias_scores_final_w_pcts.xlsx file from the data_clean folder.

