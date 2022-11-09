from instagramy import *
import api
import requests
import time
import shutil

base_url_2 = "https://api.telegram.org/bot"+api.api_key+"/sendMessage"

def send_message(delay):
    user = InstagramUser(api.user_name)
    data_list = "followers : " + str(user.number_of_followers)+'\n'+"following : "+str(user.number_of_followings)+'\n'+"post : "+str(user.number_of_posts)+'\n'+user.biography+'\n\n'+user.fullname
    parameters_2 = {
        "chat_id" : "5561977987",
        "text" : data_list
    }

    requests.get(base_url_2,data = parameters_2)
    time.sleep(delay)
    try:
        shutil.rmtree(api.del_file_1)
        shutil.rmtree(api.del_file_2)
    except:
        pass
