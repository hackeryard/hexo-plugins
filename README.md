# hexo-plugins
Useful plugins for hexo beginners to quickly build his own blog 

Generate README.MDOWN using hexo's public/archives/index.html

Quick look at: [Hackeryard Blog]("https://hackeryard.github.io")
First, install prerequisites:
```
pip3 install lxml requests
```
Secondly, put the generate_readme.py under the hexo blog dir:

hexo_blog
- public
- generate_readme.py
- ...

And Then, generate it:
```
python3 generate_readme.py [your_blog_url]
```

Tested on Win10 and Centos7, any question you'd like to open an issue.

