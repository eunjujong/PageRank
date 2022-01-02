# PageRank Algorithm Using MRJob

The implementation of the PageRank algorithm has been done using MRJob. 
We used two datasets for testing: a smaller dataset containing a node representation of webs and a larger dataset containing web link pairs.
We created an adjacency list processor to produce an input file contaning an adjacency list with the initial probvability of $\frac{1}{n}$ for all the nodes except for any dangling nodes. 
We have also accounted for dangling handling in the implementation. During the process of generating the datasets, we randomly linked the nodes, which created dangling nodes. 
Instead of omitting dangling nodes, we decided to handle them and take into account the random jump factor $\alpha=(1-m)$. The random jump factor will be applied when the total page rank is accumulated.

# Install MRJob
```
pip install mrjob
from mrjob.job import MRJob
```
The data contains two columns of URLs. The URLs we used were collected from the following source:
https://gist.github.com/demersdesigns/4442cd84c1cc6c5ccda9b19eac1ba52b

The examples of the data format is shown as follows: 
```
http://www.youtube.com http://www.yandex.ru
http://www.facebook.com http://www.twitter.com
http://www.baidu.com http://www.baidu.com
http://www.yahoo.com http://www.instagram.com
http://www.amazon.com http://www.amazon.com
http://www.wikipedia.org http://www.qq.com
http://www.qq.com http://www.qq.com
http://www.google.co.in http://www.bing.com
http://www.twitter.com http://www.msn.com
http://www.live.com http://www.live.com
http://www.taobao.com http://www.taobao.com
```

# Run 
We create a text file containing adjacency list of the data links and use the text file in the pagerank.
We can set the number of iterations by using the coomand --iteration followed by the number of iterations. 
```
python adj_process.py adj_list.txt
python pagerank.py --iteration 100 adj_list.txt
```
The results are displayed as follows: a URL, a list of linked URLs, and its rage rank (importance).


