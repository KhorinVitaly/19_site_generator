# Encyclopedia

This repo illustrate how python script can generate static web site from markdown articles. 
It's just for education, script will work with directory structure only like in repo.

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Quickstart

Launch script in terminal  

```bash
python3 generator.py 
[I 170816 19:14:17 server:283] Serving on http://127.0.0.1:5500
[I 170816 19:14:17 handlers:60] Start watching changes
[I 170816 19:14:17 handlers:62] Start detecting changes
```

After that you can browse http://127.0.0.1:5500 and test how pages change if you change articles or teamplates. 
 
Else site published on GitHub Pages you can look it on https://khorinvitaly.github.io 

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
