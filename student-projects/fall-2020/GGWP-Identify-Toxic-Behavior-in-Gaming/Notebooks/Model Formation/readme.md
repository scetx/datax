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
