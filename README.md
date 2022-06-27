# youtube_comments_sentimental_analysis

## Initial sentiment analysis steps

    1. Scrape youtube comments form shape of you <<youtubeCommentScraper.py>>
    2. Preprocessed the scraped data <<preprocessing.ipynb>>
    3. Labelled the sentiments using textBlob package <<Labeling_with_textBlob.ipynb>>
    4. Model traing with 68k features <<Model_training>>
    5. Observed model performrance <<ConfusionMaterix.ipynb>> <<initial_model.png>>

    The model did not perform good for neagtive comments.

## Limit feature size

    1. Limit the feature size to 25k <<Model_training>>
    2. Observed the confusion matrix and found it to be biased with positive values <<25k_features.png>>

    The model perforemd worse for the neagtive labels and became mopre bias towards the positive labels

## Change the sample size, make occurance of all polarity data equal (i.e., each 859)

    1. Changed code in labelling notebook as labelled_data_limit_datapoints.csv
    <<Labeling_with_textBlob.ipynb>>
    2. Trained the model <<Model_training.ipynb>>
    3. Observed model performance <<ConfusionMatrix.ipynb>>

    The model performs good for each catagory espicially the negative polarity which was seen privously not as good
