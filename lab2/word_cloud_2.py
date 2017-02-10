"""
Method:         Word cloud
Data Variables: text
Author:         Timur Kasatkin
"""

# https://github.com/amueller/word_cloud
# pip install wordcloud

from wordcloud import WordCloud

"""
text - string consists of words separated by space
"""
def word_cloud(text):
  wordcloud = WordCloud(width=400,
                        height=400,
                        background_color='white').generate(text)

  plt.axis("off")
  return plt.imshow(wordcloud)