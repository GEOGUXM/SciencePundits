from app import app
from flask import render_template, request
from app import app
import RunTrainTest as rtt 

@app.route('/')
@app.route('/index',methods = ['GET','POST'])
def index():
    user = {'nickname': 'Miguel'}  # fake user
    # list of dictionaries 
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }]
    # article_url = request.form['text']
    return render_template("index.html",title='Home',user=user,posts=posts)
    #return render_template("index.html")

# def index2():
#     user = {'nickname': 'Miguel'}  # fake user
#     posts = [  # fake array of posts
#         { 
#             'author': {'nickname': 'John'}, 
#             'body': 'Beautiful day in Portland!' 
#         },
#         { 
#             'author': {'nickname': 'Susan'}, 
#             'body': 'The Avengers movie was so cool!' 
#         }
#     ]
#     return render_template("index.html",
#                            title='Home',
#                            user=user,
#                            posts=posts)

@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    article_url = request.form['text']
    # call the flask main function 

    tweets2  = rtt.flask_main(article_url)
    # posts = [  # fake array of posts
    #     { 
    #         'author': {'nickname': 'John'}, 
    #         'body': 'Beautiful day in Portland!' 
    #     },
    #     { 
    #         'author': {'nickname': 'Susan'}, 
    #         'body': 'The Avengers movie was so cool!' 
    #     }]

    pundit_tweets = []

    print "Stage 5: Got Tweet2 into Flask"
    for tweet in tweets2: 
        if(tweet['score'] > 1): 
            pundit_tweets.append({'screen_name': tweet['screen_name'], 'tweet': tweet['tweet'], 'score':tweet['score']})
            #time.sleep(2)
        else: 
            break
    return render_template("test.html",pundit_tweets=pundit_tweets)
    #return processed_text

# @app.route('/')
# @app.route('/tweets')
# def my_form_post():
#     article_url = request.form['text']
#     processed_text = rtt.main(article_url)
#     # processed_text2 = ['a','b','c'] 
#     return processed_text
