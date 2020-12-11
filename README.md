# Police Bias
## Summary
The tragic deaths of Ahmaud Arbery, Breonna Taylor, George Floyd, and countless other black lives lost to police brutality and senseless violence have spurred calls for policy reform and police accountability among the public. There is a greater consensus in the role racial inequality plays in our criminal justice system since the beginning of the pandemic. 

But how can we use data to prove that racism and unjust practices from police officers are intertwined? Our problem statement is how might we quantify and visualize bias in police departments over a period of time to determine if police accountability has changed alongside increased public pressure?

As a solution, we developed a police bias diagnostic tool that helps the general public, policy makers, and police departments identify bias in law enforcement by analyzing past department records and displaying the results in a detailed analytic report. Our tool calculated an overall diagnostic score that takes into account racial bias and excessive force, using stop data, excessive force reports, and population demographics over four years in seven different U.S. cities. The resulting diagnostic scores and calculations are presented in an interactive Tableau dashboard that enables users to understand just how great the difference in police treatment is between people of color and white Americans.

## Project Components
### 1. [`uncleaned_data`](/uncleaned_data)

We sourced our datasets from official city and police department websites. We only analyzed cities who (1) publicly released official data and (2) included both drive stops and use of force data. This inevitably introduced bias, as no evaluation could be done on police departments who did not avail records for public use. To compensate, we found variability in other aspects of our data: population size and geographical location, enabling us to increase sample size without compromising on the integrity of our data sources. We covered every region to ensure our findings could be relevant to stakeholders from all across the United States: West (Portland, OR), Midwest (Bloomington, IN; Cincinnati, OH), South (Austin, TX), and Northeast (New York City, NY). 

Some files were uploaded in a `.csv` file format, while others were uploaded as an Excel spreadsheet. In these datasets, column names and values were often abbrievated or codified. They were difficult to interpret without data dictionaries that were enclosed in separate Excel spreadsheets. Using Python's `pandas` library, we loaded `.csv` and/or `.xlx` files into a dataframe to extract and calculate the features we needed for our project. Some police departments published all of their detention and arrest data in a single file, while others created separate files for drive stops only. In the former case, we specifically isolated entries related to stops and frisks, as reported by the attending officer in the records. In some cases, missing values were listed as strings instead of NaN values. We replaced those with proper NaN values in order to correctly account for the number of stops we did and did not have full information on.

We then used official census data to determine the demographics of the city. Since census data is only reported every 10 years, we used official population projection tables for each year in 2016-2019. This data was used to quantify whether members of given racial groups were disproportionally impacted by drive stops and use of force.

### 2. [`data_clean`](/data_clean)
For each city, we compiled the above information into a standard dataframe containing:
- Year
- Total Population
- Percentage of Population that is Black
- Percentage of Population that is White
- Percentage of Population that is Hispanic
- Percentage of Population that is Asian/Pacific Islander
- Number of Drive Stops Involving Black Drivers
- Number of Drive Stops Involving White Drivers
- Number of Drive Stops Involving Hispanic Drivers
- Number of Drive Stops Involving Asian/Pacific Islander Drivers
- Use of Force on Black Drivers
- Use of Force on White Drivers
- Use of Force on Hispanic Drivers
- Use of Force on Asian/Pacific Islander Drivers

Note: We also included the above categories for drivers listed as belonging to "other" races. However, there was ambiguity in regards to how responding police officers applied this racial categorization. As such, we did not include this set of cases in our visualizations.

Our dataframe transformations displayed the data in a clear, consistent, and comprehensible manner across cities.

We've included an example of the data cleaning process in the [/uncleaned_data/Example -Bloomington Data Cleaning](https://github.com/anissarashid/police-bias/tree/main/uncleaned_data/Example%20-Bloomington%20Data%20Cleaning) folder.

### 2. [`bias_scores`](/bias_scores)

We calculated bias scores using an original algorithm developed in consultation with public policy experts. The Jupyter Notebooks containing our algorithm and methodology can be found in [`notebooks/.ipynb_checkpoints`](notebooks/.ipynb_checkpoints).

For more information on how we calculated scores, please refer to our [scoring algorithm methodology](https://docs.google.com/document/d/14HGTZGBeoiHT3_NmvRMxozWnmfPMWz_MEgOWPrAoF8k/edit).

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

## Instructions for Use


### 1. Download the repository on Github
Go to https://github.com/anissarashid/police-bias to view the project. 
* Click on the green Code button. 
* Click Download ZIP.

### 2. Install Tableau 
Follow instructions at https://www.tableau.com/products/desktop (https://www.tableau.com/academic/students recommended for students)

### 3. Opening the Dashboard and Connecting Data Sources

Once Tableau is installed on your device, open the Tableau workbook found in the visualizations folder, called **visualizations** of this repository.

The data source connection to Tableau may display an error when you open the notebook. If this occurs hit "no" in the error message prompt. Then the dashboard will prompt you to connect a data source. Select **Locate File** then select **all_cities_bias_scores_final_w_pcts.xlsx** from the /police-bias-main/data_clean folder. 

Note: This error may pop up more than once, possibly several times, so hit "no" again when that prompt shows up, and then re-connect that same data source, all_cities_bias_scores_final_w_pcts.xlsx from the data_clean folder. 

### 4. Running the Jupyter Notebook

There are a few different options you can use to run the Jupyter Notebooks found in the repository:
* You can run the notebooks locally using Jupyter Notebook: https://jupyter.org/install
* You can also run the notebooks using Google Colab:
  1. To do so, upload the data-clean and notebooks folders into your Google Drive
  2. Open the ipynb using Google Colab
* You can also use https://deepnote.com/ for teams
* You can also use https://datahub.berkeley.edu/hub/login?next=%2Fhub%2F should you have a Calnet login.

### 5. Adding your own city
1. Create a csv file with the same parameters as the csv files in the data-clean folder
2. Save as [cityname].csv
3. Make a copy of the Final-Bias-Algorithm.ipynb and replace it with your city name
4. Replace the current city csv with the new cities csv
5. Run all cells and save bias score as [cityname]_bias_score.csv in the bias-scores folder

### 6. Updating the visualizations
1. Open up the master sheet, all_cities_bias_scores_final_w_pcts .xlsx, from the data-clean folder
2. Open [cityname]_bias_score.csv from the bias-scores folder and copy all of the cells
3. Paste these cells into the master excel sheet and save this sheet and save this sheet
4. Open Tableau, update the Data Source, and refresh the dashboard
5. Copy and paste worksheets from another city and update the filter to the new specified city. 
6. Create a dashboard for the new city with these updated worksheets. 

## Credits
Developed by Tiffany Yu, Anissa Rashid, Madeleine Liu, Lena Bertozzi, Inola Cohen, and Ethan Shang. Supported by UC Berkeley’s SCET Data-X course.
