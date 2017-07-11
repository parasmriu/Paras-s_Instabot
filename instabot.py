import requests, urllib
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from wordcloud import WordCloud


APP_ACCESS_TOKEN = '1471045833.68a1cf7.c126d9a38536493c97486bc8f8b3879a'
#Token Owner : paras6881
#Sandbox Users : uditk14

BASE_URL = 'https://api.instagram.com/v1/'
#Base URL of Instagram

'''
Function declaration to get your own info
'''

def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    #complete url for requesting the resource
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
    #getting user info and converting it into JSON format

    if user_info['meta']['code'] == 200:
        #checking the status, is everything OK?
        if len(user_info['data']):
            #checking the len of data, does any data exist
            print 'Username: %s' % (user_info['data']['username'])
            #Username
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            #Number of Followers
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            #Number of following
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
            #Number of posts
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'


'''
Function declaration to get the ID of a user by username
'''


def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    # complete url for requesting the resource
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
    # getting user info and converting it into JSON format

    if user_info['meta']['code'] == 200:
        # checking the status, is everything OK?
        if len(user_info['data']):
        # checking the len of user info data, does any data exist
            return user_info['data'][0]['id']
            #Return the id of the provided username
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()


'''
Function declaration to get the info of a user by username
'''


def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    #user_id of provided username
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    # complete url for requesting the resource
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
    # getting user info and converting it into JSON format

    if user_info['meta']['code'] == 200:
        # checking the status, is everything OK?
        if len(user_info['data']):
        # checking the len of data, does any data exist
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'There is no data for this user!'
    else:
        print 'Status code other than 200 received!'


'''
Function declaration to get your recent post
'''


def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    # complete url for requesting the resource
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()
    # getting own info and converting it into JSON format

    if own_media['meta']['code'] == 200:
        # checking the status, is everything OK?
        if len(own_media['data']):
        # checking the len of own media data, does any data exist
            image_name = own_media['data'][0]['id'] + '.jpeg'
            #getting the image name with the extension '.jpeg' for argument passing to urlretrieve
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            #getting image url of image of standard resolution for argument passing
            urllib.urlretrieve(image_url, image_name)
            #urllib is a library in python and urlretrieve is a method of that library
                                        # which helps us to download photo.
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'


'''
Function declaration to get the recent post of a user by username
'''


def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    # user_id of provided username
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    # complete url for requesting the resource
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()
    # getting user media and converting it into JSON format

    if user_media['meta']['code'] == 200:
        # checking the status, is everything OK?
        if len(user_media['data']):
        #checking the len of data, does any data exist
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'


'''
Function declaration to get the ID of the recent post of a user by username
'''

def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print 'There is no recent post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()
'''
Function declaration to get list of likes on a post
'''

def get_like_list(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes?access_token=%s') % (media_id,APP_ACCESS_TOKEN)

    print 'GET request url : %s' % (request_url)
    like_list = requests.get(request_url).json()
    print like_list

    if like_list['meta']['code'] == 200:
        if len(like_list['data']):
            for i in range(0,len(like_list['data'])):
                print 'Username: %s' % (like_list['data'][i]['username'])

        else:
            print 'There is no like for this post!'
    else:
        print 'Status code other than 200 received!'

'''
Function declaration to like the recent post of a user
'''

def like_a_post(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. Try again!'

'''
Function declaration to get list of comments on a post
'''

def get_comment_list(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (media_id,APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_list = requests.get(request_url).json()
    if comment_list['meta']['code'] == 200:

        if len(comment_list['data']):
            for i in range(0, len(comment_list['data'])):
                print comment_list['data'][i]['text']
        else:
            print 'There is no comment for this user media!'
    else:
        print 'Query was unsuccessful!'


'''
Function declaration to make a comment on the recent post of the user
'''


def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment. Try again!"


'''
Function declaration to make delete negative comments from the recent post
'''


def delete_negative_comment(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            #Here's a naive implementation of how to delete the negative comments :)
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, APP_ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()

                    if delete_info['meta']['code'] == 200:
                        print 'Comment successfully deleted!\n'
                    else:
                        print 'Unable to delete comment!'
                else:
                    print 'Positive comment : %s\n' % (comment_text)
        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'

insta_tag = []
def tag_list(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    media_data = requests.get(request_url).json()
    if (media_data['meta']['code'] == 200):
        if len(media_data['data']['tags']):
            insta_tag = media_data['data']['tags']
            str = " ".join(insta_tag)
            wordcloud = WordCloud(stopwords=STOPWORDS, background_color="white", width=1000, height=800).generate(str)
            plt.imshow(wordcloud)
            plt.axis("off")
            plt.show()



def start_bot():
    while True:
        print '\n'
        print 'Hey! Welcome to instaBot!'
        print 'Here are your menu options:'
        print "a.Get your own details\n"
        print "b.Get details of a user by username\n"
        print "c.Get your own recent post\n"
        print "d.Get the recent post of a user by username\n"
        print "e.Get a list of people who have liked the recent post of a user\n"
        print "f.Like the recent post of a user\n"
        print "g.Get a list of comments on the recent post of a user\n"
        print "h.Make a comment on the recent post of a user\n"
        print "i.Delete negative comments from the recent post of a user\n"
        print "j.For wordcloud"
        print "k.Exit"

        choice = raw_input("Enter you choice: ")
        if choice == "a":
            self_info()
        elif choice == "b":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice == "c":
            get_own_post()
        elif choice == "d":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        elif choice=="e":
           insta_username = raw_input("Enter the username of the user: ")
           get_like_list(insta_username)
        elif choice=="f":
           insta_username = raw_input("Enter the username of the user: ")
           like_a_post(insta_username)
        elif choice=="g":
           insta_username = raw_input("Enter the username of the user: ")
           get_comment_list(insta_username)
        elif choice=="h":
           insta_username = raw_input("Enter the username of the user: ")
           post_a_comment(insta_username)
        elif choice=="i":
           insta_username = raw_input("Enter the username of the user: ")
           delete_negative_comment(insta_username)
        elif choice == "k":
            insta_username = raw_input("Enter the username of the user: ")
            tag_list(insta_username)
        elif choice == "j":
            exit()
        else:
            print "wrong choice"

start_bot()