# GGWP: Identifying Toxic Behavior in Gaming
Much like the general internet, racism and sexism thrive in the gaming world. Despite this area of the internet being established for years, people still experience unwarranted aggression from other players. With the intention of cleansing the gaming community of harassment as much as possible, the goal of this project is to 1) create a detection method for tagging toxic behavior/players and 2) provide insights on toxic behavior/players.

# Contents
The jupyter notebooks map the thought process and learning path of creating this identifier and insights. 

### Model Formation
0) **ggwp0_languages.ipynb** - The Dota dataset contains multiple languages. The focus will be centered onto English.
    - Labeling languages of in-game chat messages across 21 million rows
1) **ggwp1_eda_and_kmeans.ipynb** - After getting the English subset: cleaning, EDA, and K-means
    - Data cleaning
    - Exploratory data analysis
    - K-means clustering
2) **ggwp2_preprocess_and_features.ipynb** - Size was still an obstacle so stopwords and uncommon words were removed, more features were looked into
    - Additional preprocessing
    - Additional features
3) **ggwp3_jigsaw_classifier.ipynb** - Needing labels after K-means provided no distinct results, a Wikipedia comments dataset was used to create a classifier
    - Initial model for identifying toxicity
4) **ggwp4_classifier_on_dota.ipynb** - Applying the Wikipedia comments model onto the Dota dataset
    - Applying the initial model to the Dota dataset
    - Exploratory data analysis according to labels
5) **ggwp5_word_embedding.ipynb** - Adding word embeddings to the model to account for more words and evasions
    - Applying word embeddings to the initial model
      - Finding the proper word vector corpus
      - Applying word embeddings to the model, first with a normal average
      - Applying word embeddings to the model with a weighted average, the weights being from Tfidf
6) **ggwp8_final_model.ipynb** - What's under the hood of the UI

### Insights on Toxic Behavior/Players
7) **ggwp6_thresholds_cleaning** - Thresholds had to be adjusted to account for false positives in addition to more brute force cleaning
    - Label thresholds and cleaning of common false positives
8) **ggwp7_insights**
    - Using sentence-transformers to find natural clusters of toxic messages
    - Segmenting time, finding trends across labels
        - Every 5 minutes
        - Pre-, early, mid, late game
