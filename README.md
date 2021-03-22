# Coronavirus twitter analysis

In this project, I will scan ALL geotagged tweets sent in 2020 to monitor the spread of the coronavirus on social media.

**Learning Outcomes:**

1. work with large scale datasets
1. work with multilingual text
1. use the MapReduce divide-and-conquer paradigm to create parallel code

## Background

Approximately 500 million tweets are sent everyday.
Of those tweets, about 1% are *geotagged*.
That is, the user's device includes location information about where the tweets were sent from.
The lambda server's `/data-fast/twitter\ 2020` folder contains all geotagged tweets that were sent in 2020. (700 GB)
In total, there are about 1.1 billion tweets in this dataset.

The tweets are stored as follows.
The tweets for each day are stored in a zip file `geoTwitterYY-MM-DD.zip`,
and inside this zip file are 24 text files, one for each hour of the day.
Each text file contains a single tweet per line in JSON format.

I followed the [MapReduce](https://en.wikipedia.org/wiki/MapReduce) procedure to analyze these tweets.

<img src=mapreduce.png width=100% />


# Process

1. `map.py` file tracks the usage of the hashtags on both a language and country level.

1. A shell script `run_maps.sh` loops over each file in the dataset and runs `map.py` on that file.
    Use the `nohup` command to ensure the program continues to run after you disconnect and the `&` operator to ensure that all `map.py` commands run in parallel.


1. Run the map file on all the tweets in the `/data-fast/twitter\ 2020` folder. 
   You might need to grant execution access with `chmod u+x src/map.py`
    Then run `./src/map.py`
   The output of running `map.py` should be two files now, one that ends in `.lang` for the lanuage dictionary ,
   and one that ends in `.country` for the country dictionary.
   you should have a large number of files in your `outputs` folder.



1. `reduce.py` file combines all of the `.lang` files into a single file,
   and all of the `.country` files into a different file.
   `./src/reduce.py --input_paths outputs/geoTwitter*.lang --output_path=reduced.lang`
    and `./src/reduce.py --input_paths outputs/geoTwitter*.country --output_path=reduced.country`
   
1. `visualize.py` file counts the total number of occurrences of each of the hashtags.
    For example, run:
    `./src/visualize.py --input_path=reduced.lang --key=#coronavirus | head > viz/lang/#coronavirus`


# Outcomes:
[Here](https://github.com/ohorban/twitter_coronavirus/tree/master/viz) you can see how many tweets were posted containing a certain hashtag based on the language of the tweet and the country where the tweet was posted
Additionally, I created a file `generate_graph.py` that uses matplotlib to build pie charts of the data. For example, running this command: `./generate_graph.py --input_file= viz/country/#corona` will build this graph:
<img src=example_pie.jpg />
The graph shows the distribution of tweets with #corona based on country that the tweet was posted from. Here, we see that 33.5% of all tweets with #corona where posted in USA.
