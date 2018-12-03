# EXPERIMENTING WITH DOCKER
# MATTHEW BRANDEBURG - 3 DECEMBER 2018

import pandas as pd
import numpy as np
from flask import Flask


### PART ONE: JUST GET IT TO PRINT TO CONSOLE
## USING THE FOLLOWING CMNDS ONCE INSIDE:
# 1. docker build -t demo:v1 .
# 2. docker run -it --rm --name:demoLive demo:v1 /bin/sh
# 3. python testfile.py

#### DEMO CODE:
# df = pd.DataFrame(np.random.randn(6,4), columns=list('ABCD'))
# print(df.head())
##### it works! 

# PS: using the following Docker file:
# FROM python
# RUN mkdir /app
# COPY testfile.py /app/
# WORKDIR /app
# RUN pip install flask
# RUN pip install pandas

##################################################
##################################################
##################################################
##################################################

##### PART 2: MESSING WITH FLASK:
## NEW DOCKER FILE ADDS THE FOLLOWING LINES:
# EXPOSE 5000
# ENV FLASK_APP=testfile.py
# CMD flask run --host=0.0.0.0


# DIFFERENT RUN CMDS:
# docker build -t demo:v2 .
# docker run -d -p 5000:5000 --name:demoLive2 demo:v2
# ** without --rm you will need to stop and rm container manually after done


#### MY CODE:
app = Flask(__name__)

@app.route("/") #THESE ARE URL DIRECTORS AFTER :5000
def hello():
    # return "Hello World!" # WORKS! 
    # (but have to comment out - cannot do multiple returns on a page)
    # NOTICE THE QUOTES AROUND RETURN JOB


    ### TRY POSTING IN MY APP 
	df = pd.DataFrame(np.random.randn(6,4), columns=list('ABCD'))
	df2 = pd.DataFrame.to_html(df)
	# return "{}".format(df2) # it works!
	#if I do df2.head(), I get that string has no attribute 'head'
	
	# BECAUSE OF DF2.HEAD ISSUES - MORE TRANSFORMATIONS
	df3 = df.head() #have to go back to df instead of df2 b/c already to_html()'d it
	df3 = pd.DataFrame.to_html(df3)
	return "{}".format(df3)


