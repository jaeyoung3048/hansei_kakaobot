from backend.settings.base import *

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kakaobot_ex',
        'USER': 'root',
        'PASSWORD': get_secret("RDS_PASSWORD"),
        'HOST': 'chatbot-db.cldsxmn3fud0.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306',
    }
}