import requests
import json

TOKEN = 'your_token_here'

def get_all_posts():
    ''' Get all facebook posts on your timeline after specified unix datetime '''
    query = ("SELECT post_id, actor_id FROM stream WHERE filter_key = 'others' AND source_id = me() AND created_time > 1460507400")
    payload = {'q': query, 'access_token': TOKEN}
    r = requests.get('https://graph.facebook.com/fql', params=payload)
    result = json.loads(r.text)
    return result['data']

def comment(wallposts):
    ''' Get all users, comment and like on all the posts '''
    for wallpost in wallposts:
        try:
            payload = {'access_token': TOKEN}
            r = requests.get('https://graph.facebook.com/%s' % wallpost['actor_id'], params=payload)
            url = 'https://graph.facebook.com/%s/comments' % wallpost['post_id']
            user = json.loads(r.text)
            # print user

            message = "Thank You " + user['first_name'] + " :)"
            print message
            payload = {'access_token': TOKEN, 'message': message}
            s = requests.post(url, data=payload)
            payload = {'access_token': TOKEN}
            t = requests.post("https://graph.facebook.com/"+wallpost['post_id']+"/likes", data=payload)
            print "Wall post %s done" % wallpost['post_id']
        except:
            print "could not print"	        

if __name__ == '__main__':
    comment(get_all_posts())
