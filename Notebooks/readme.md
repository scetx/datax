# GGWP: Identifying Toxic Behavior in Gaming
Much like the general internet, racism and sexism thrive in the gaming world. Despite this area of the internet being established for years, people still experience unwarranted aggression from other players. With the intention of cleansing the gaming community of harassment as much as possible, the goal of this project is to 1) create a detection method for tagging toxic behavior/players and 2) provide insights on toxic behavior/players.

# Contents
The jupyter notebooks map the thought process and learning path of creating this identifier and insights. 

### Model Formation
0) **ggwp0_languages.ipynb**
    - Labeling languages of in-game chat messages across 21 million rows
1) **ggwp1_eda_and_kmeans.ipynb**
    - Data cleaning
    - Exploratory data analysis
    - K-means clustering
2) **ggwp2_preprocess_and_features.ipynb**
    - Additional preprocessing
    - Additional features
3) **ggwp3_jigsaw_classifier.ipynb**
    - Initial model for identifying toxicity
4) **ggwp4_classifier_on_dota.ipynb**
    - Applying the initial model to the Dota dataset
    - Exploratory data analysis according to labels
5) **ggwp5_word_embedding.ipynb**
    - Applying word embeddings to the initial model
      - Finding the proper word vector corpus
      - Applying word embeddings to the model, first with a normal average
      - Applying word embeddings to the model with a weighted average, the weights being from Tfidf
6) **ggwp8_final_model.ipynb**

### Insights on Toxic Behavior/Players
7) **ggwp6_thresholds_cleaning**
    - Label thresholds and cleaning of common false positives
8) **ggwp7_insights**
    - Using sentence-transformers to find natural clusters of toxic messages
    - Segmenting time, finding trends across labels
        - Every 5 minutes
        - Pre-, early, mid, late game
