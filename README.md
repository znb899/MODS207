## Research question

## Data Collection and Description

We focused on the [top 100 french channels](source.com). Some of these channels were not relevant to our reseach question (for example they were in arabic or were news channel or radio stations that repost on youtube or lacked text alltogether like some kids channels). All in all we kept X channels (annex ?), which are the channels at the top 100 with human scale (independent youtuber or small studios).


| Datum            | Type            | Collection Method                       |
| ---------------- | --------------- | --------------------------------------- |
| title            | string          | YouTube API                             |
| description      | string          | YouTube API                             |
| channel          | string          | YouTube API                             |
| publishTime      | datetime        | YouTube API                             |
| tags             | list of strings | YouTube API                             |
| category         | integer         | YouTube API                             |
| commentNumber    | integer         | YouTube API                             |
| likesNumber      | integer         | YouTube API                             |
| views            | integer         | YouTube API                             |
| favoritesNumber  | integer         | YouTube API                             |
| quality          | string          | YouTube API                             |
| license          | float           | YouTube API                             |
| videoId          | string          | Selenium                                |
| trendingTimes    | integer         | YouTube API                             |
| trendingDuration | datetime        | YouTube API                             |
| rawText          | string          | Youtube transcript API (python package) |

## Data Vizualization

