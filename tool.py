import os
import random
import threading
import requests
from user_agent import generate_user_agent
import pycountry
from datetime import datetime
import requests
import uuid
from user_agent import generate_user_agent
from secrets import token_hex
import os
try:
    import random
    import threading
    import requests
    from user_agent import generate_user_agent
    import pycountry
    from datetime import datetime
except ModuleNotFoundError:
    os.system('pip install user_agent pycountry requests')    
#from mahos import Hit

cone = token_hex(8).upper()   
bone = token_hex(8).upper()  
uid = uuid.uuid4()
lopp = str(uuid.uuid4())
Lol = str(uuid.uuid4())
Gio = str(uuid.uuid4())
bb = 0
gg = 0
GM = 0
BM = 0
# الألوان
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m'  # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق
C = '\033[2;35m'  # وردي
B = '\x1b[38;5;208m'  # برتقالي
Y = '\033[1;34m'  # ازرق فاتح
M = '\x1b[1;37m'  # ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'  # ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'

print(f'''Available TikTok , Hotmail''')

token = input(f' {F}({C}1{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐓𝐨𝐤𝐞𝐧{F}  ' + Z)
print(X + ' ═════════════════════════════════  ')
ID = input(f' {F}({C}2{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐈𝐃{F}  ' + Z)

def tlg(email):
    username = email.split('@')[0]
    patre = {
        "Host": "www.tiktok.com",
        "sec-ch-ua": "\" Not A;Brand\";v\u003d\"99\", \"Chromium\";v\u003d\"99\", \"Google Chrome\";v\u003d\"99\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
        "sec-fetch-site": "none",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "accept-language": "en-US,en;q\u003d0.9,ar-DZ;q\u003d0.8,ar;q\u003d0.7,fr;q\u003d0.6,hu;q\u003d0.5,zh-CN;q\u003d0.4,zh;q\u003d0.3"
    }
    
    tikinfo = requests.get(f'https://www.tiktok.com/@{username}', headers=patre).text
    
    try:
        getting = str(tikinfo.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
        try:
            id = str(getting.split('id":"')[1]).split('",')[0]
        except:
            id = ""
        try:
            name = str(getting.split('nickname":"')[1]).split('",')[0]
        except:
            name = ""
        try:
            bio = str(getting.split('signature":"')[1]).split('",')[0]
        except:
            bio = ""
        try:
            country = str(getting.split('region":"')[1]).split('",')[0]
        except:
            country = ""
        try:
            private = str(getting.split('privateAccount":')[1]).split(',"')[0]
        except:
            private = ""
        try:
            followers = str(getting.split('followerCount":')[1]).split(',"')[0]
        except:
            followers = ""
        try:
            following = str(getting.split('followingCount":')[1]).split(',"')[0]
        except:
            following = ""
        try:
            like = str(getting.split('heart":')[1]).split(',"')[0]
        except:
            like = ""
        try:
            video = str(getting.split('videoCount":')[1]).split(',"')[0]
        except:
            video = ""
        try:
            secid = str(getting.split('secUid":"')[1]).split('"')[0]
        except:
            secid = ""
        try:
            countryn = str(pycountry.countries.get(alpha_2=country)).split("name='")[1].split("'")[0]
        except:
            countryn = ""
        try:
            countryf = str(pycountry.countries.get(alpha_2=country)).split("flag='")[1].split("'")[0]
        except:
            countryf = ""
        binary = "{0:b}".format(int(id))
        i = 0
        bits = ""
        while i < 31:
            bits += binary[i]
            i += 1
        timestamp = int(bits, 2)
        try:
            cdt = datetime.fromtimestamp(timestamp)
        except:
            cdt = ""
        kls = f"""───────────────\n⎌ Email ➢ {email} \n⎌ ᴜѕᴇʀɴᴀᴍᴇ ➢ {username} \n⎌ ѕᴇᴄᴜɪᴅ ➢ {secid} \n⎌ ɴᴀᴍᴇ ➢ {name}\n⎌ ғᴏʟʟᴏᴡᴇʀѕ ➢ {followers} \n⎌ ғᴏʟʟᴏᴡɪɴɢ ➢ {following}\n⎌ ʟɪᴋᴇ ➢ {like}\n⎌ ᴠɪᴅᴇᴏ ➢ {video}\n⎌ ᴘʀɪᴠᴀᴛᴇ ➢ {private}\n⎌ ᴄᴏᴜɴᴛʀʏ ➢ {countryn} {countryf}\n⎌ ᴄʀᴇᴀᴛᴇᴅ ᴅᴀᴛᴇ ➢ {cdt}\n⎌ ɪᴅ ➢ {id}\n⎌ ʙɪᴏ ➢ {bio}\n─────────────── BY : @iiisup"""
        requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={kls}')
    except:
        error_message = f'''
        صاد لك حساب بدون ما اعطا معلومات
        Email >> {email}
        User >> {username}
        BY : @iiisup
        '''        
        requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={error_message}')
        
def mahos(email):
    global gg, bb
    proxy_list = [
    '135.181.150.104:8080',
    '135.181.45.15:8080',
    '34.151.231.232:3129',
    '128.140.7.236:8080',
    '128.140.7.236:8080',
    '34.254.90.167:9812',
    '129.154.225.163:8100',
    '80.51.221.125:8080',
    '114.129.19.139:8080',
    '34.151.231.232:3129',
    '183.221.242.107:8443',
    '135.181.45.15:8080',
    '103.84.253.10:80',
    '154.70.107.81:3128',
    '204.199.174.13:999',
    '102.165.51.172:3128',
    '103.159.96.110:8085',
    '176.95.54.202:83',
    '35.247.221.112:3129',
    '170.79.12.75:9090',
    '190.61.97.229:999',
    '103.83.179.78:2016',
    '77.89.35.50:8080',
    '35.247.221.112:3129',
    '40.76.245.70:8080',
    '64.225.8.118:9989',
    '190.19.114.104:8080',
    '149.154.157.17:5678',
    '114.4.233.34:8080',
    '186.97.102.68:999',
    '62.201.223.7:8183',
    '202.8.74.9:8080',
    '157.245.144.111:8080',
    '183.221.242.103:9443',
    '36.74.163.65:8080',
    '201.131.239.233:999',
    '218.207.72.202:3128',
    '171.6.7.198:8080',
    '79.106.170.34:8989',
    '162.212.156.172:8080',
    '179.63.149.4:999',
    '186.121.235.66:8080',
    '103.36.35.135:8080',
    '190.217.105.194:8080',
    '176.95.54.202:83',
    '182.53.85.34:8080',
    '103.69.108.78:8191',
    '36.37.146.119:32650',
    '186.150.201.38:8080',
    '35.198.9.82:3129',
    '61.139.26.94:3128',
    '103.169.19.130:8080',
    '35.198.63.193:3129',
    '34.95.187.223:3129',
    '45.174.87.18:999',
    '202.69.38.82:8080',
    '200.123.29.45:3128',
    '186.121.235.66:8080',
    '103.52.213.131:80',
    '45.61.187.67:4000',
    '45.61.187.67:4006',
    '45.61.187.67:4001',
    '45.61.187.67:4004',
    '45.61.187.67:4009',
    '34.118.86.227:8585',
    '34.125.184.194:8080',
    '34.174.159.253:8585',
    '34.172.175.72:8585',
    '34.162.190.6:8585'
]

    proxy = random.choice(proxy_list)
    url = "https://www.tiktok.com/passport/web/user/check_email_registered?shark_extra=%7B%22aid%22%3A1459%2C%22app_name%22%3A%22Tik_Tok_Login%22%2C%22app_language%22%3A%22en%22%2C%22device_platform%22%3A%22web_mobile%22%2C%22region%22%3A%22SA%22%2C%22os%22%3A%22ios%22%2C%22referer%22%3A%22https%3A%2F%2Fwww.tiktok.com%2Fprofile%22%2C%22root_referer%22%3A%22https%3A%2F%2Fwww.google.com%22%2C%22cookie_enabled%22%3Atrue%2C%22screen_width%22%3A390%2C%22screen_height%22%3A844%2C%22browser_language%22%3A%22en-us%22%2C%22browser_platform%22%3A%22iPhone%22%2C%22browser_name%22%3A%22Mozilla%22%2C%22browser_version%22%3A%225.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2014_4%20like%20Mac%20OS%20X%29%20AppleWebKit%2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Version%2F14.0.3%20Mobile%2F15E148%20Safari%2F604.1%22%2C%22browser_online%22%3Atrue%2C%22timezone_name%22%3A%22Asia%2FRiyadh%22%2C%22is_page_visible%22%3Atrue%2C%22focus_state%22%3Atrue%2C%22is_fullscreen%22%3Afalse%2C%22history_len%22%3A17%2C%22battery_info%22%3A%7B%7D%7D&msToken=vPgBDLGXZNEf56bl_V4J6muu5nAYCQi5dA6zj49IuWrw2DwDUZELsX2wz2_2ZYtzkbUF9UyblyjQTsIDI5cclvJQ6sZA-lHqzKS1gLIJD9M6LDBgII0nxKqCfwwVstZxhpppXA==&X-Bogus=DFSzsIVLC8A-dJf6SXgssmuyRsO1&_signature=_02B4Z6wo00001dTdX3QAAIDBDn9.7WbolA3U3FvAABfU8c"

    data = f"email={email}&aid=1459&language=en&account_sdk_source=web&region=SA"

    hed = {
        "User-Agent": generate_user_agent(),
    }
    r = requests.post(url, headers=hed, data=data, proxies={'http://': proxy}).text
    if '"data":{"is_registered":1},"message":"success"' in r:
        gg += 1
        tlg(email)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''━━━━━━━━━━━━━━━━━━━━━━━━━
[0] Dev : @iiisup | TikTok HIT        
━━━━━━━━━━━━━━━━━━━━━━━━━
{F} [1] {F} {F}HIT  -  تم الصيد    » 「{gg}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{Z} [2] {Z} {Z}BAD IG - مش متاح   » 「{bb}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{A} [3] {A} {A}Good GM - جيميل صح » 「{GM}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{X} [4] {X} {X}BAD - ايميل خاطئ   » 「{BM}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{U} [5] {U} {U}email  » 「{email}」| 
━━━━━━━━━━━━━━━━━━━━━━━━━''')
    else:
        bb += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''━━━━━━━━━━━━━━━━━━━━━━━━━
[0] Dev : @iiisup | TikTok HIT        
━━━━━━━━━━━━━━━━━━━━━━━━━
{F} [1] {F} {F}HIT  -  تم الصيد    » 「{gg}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{Z} [2] {Z} {Z}BAD IG - مش متاح   » 「{bb}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{A} [3] {A} {A}Good GM - جيميل صح » 「{GM}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{X} [4] {X} {X}BAD - ايميل خاطئ   » 「{BM}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{U} [5] {U} {U}email  » 「{email}」| 
━━━━━━━━━━━━━━━━━━━━━━━━━''')
def mazen(email):
    global GM, BM
        
    cookies = {
    'mkt': 'ar-SA', 'MicrosoftApplicationsTelemetryDeviceId': f'{uid}',
    'MUID': f'{Lol}',
    'mkt1': 'ar-YE',
    'amsc': 'W9SIFWwMGN+lVLl6SXoWchVNp2qClnCuHjeF7QqnZMl/n5lD6GGbuCZYqSNeCIyEtyCYN3ix9oyis7w7wkzr4FWwnrQnXmfKBWr6FSbBP/bQKXYf2uaxg0yKArHa2BUSSlLnEH9qwUfj2ibtbjAZEjfuRU8uqj3qGwYrK0YUPEMgtIUXqrdVrijI22r0pmCfpWP9UtfZ0e1Mz8jY76J81CutcwPlgBvVXu4jCvwPOGrfBXVb20wOfcwjKmvBhUfBibq1R94qCrIuaJ2cx37s1a71J8eNmy0H4qcTktDcT9VwwFQvcIjasVUWF+H9Squj:2:3c',
    'clrc': '{%2219808%22%3a[%22d7PFy/1V%22%2c%22+VC+x0R6%22%2c%22FutSZdvn%22]}',
    'fptctx2': 'taBcrIH61PuCVH7eNCyH0LNKRXFdWqLJ6b8ywJyet7VHu2Dd9BXNW%252bWOjjY9QtHGccY75UXlolq7OQ5NwLS8ulzCNvB52TOa2XQDsllTzEALKmePIHAjVXf0frBvoOMHhq7Gd2bZpaUtuFdvIkr98uCmEbU2N8YLSeCowRh3ORr9%252bwe3QzLrxlDijQlX40QVBOU04soGUp5I9t%252by%252bGWh8nmWteV692zgYpY%252bNJcJOWOI1vkYRBG%252bTBre30MUYSRyuI1yulPfgxmoC9raQw7l9evL7ca7dpfnA9rjK243TA5gubEKnf6JioH%252fjHNMbbaoON18n%252bfQ39cwFC5yYtYD3Q%253d%253d',
    'ai_session': '8c6RMHMQDDRmS3ZN+3LmdZ|1711402756284|1711402756284',
    'MSFPC': 'GUID=1f0959d32e1a4951957795da73aad529&HASH=1f09&LV=202403&V=4&LU=1710624081495',
}
    headers = {
    'authority': 'signup.live.com',
    'accept': 'application/json',
    'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
    'canary': 'tStZYdKJC3VJdgW+hM2SbJM2fj2Dfd7pyuMSWRJLB18MCaCm5dZSKLL/k4sK+r13IpYJp1s3fEarGTfrLpXcbbf0kviYUuVQ5l4I6L28hqCtHJ4h289pv4KFpDlfXnw2dFBXsWG5pATPEPakKvwbFgwJENAONouVfa8qNQbsjU8J2b8bhBhaGYOA6mnNAhRQwySn27hzabmZY6PT6nhHu0MdQYbgPZ4LI2mhoDP6miLyjOnN6p6EYVyV71+/7f9N:2:3c',
    'content-type': 'application/json',
    'hpgid': '200639',
    'origin': 'https://signup.live.com',
    'referer': f'https://signup.live.com/signup?contextid={cone}&opid={bone}&bk=1711402639&sru=https://login.live.com/login.srf%3fcontextid%3d{cone}%26opid%3d{bone}%26mkt%3dAR-YE%26lc%3d9217%26bk%3d1711402639%26uaid%3d{lopp}&uiflavor=web&lic=1&mkt=AR-YE&lc=9217&uaid={lopp}',
    'scid': '100118',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'tcxt': '2L2fSRxywqPP8YGo5RdhQWcLjc4ZJO6rG13Z7OKFNYAq/S1rfBxLjRja7oHJXiJGSQqOMo3NC8QpATpm0d0TXVFPf//W6dHuOR3vJSAaloAvAo+RuqHUCG2JlpF8vb9a5rLVkTkh423Ml+/cudrz9rmdhnVSgDMUBxCp+XRLpuMvlGQZBYbyI7wMCaEOS/Qhv5OiI44jFNWrkGLJ3ZjyO/gTB+ITyRSkoEv8PnXUwjlL8xUOD0xLMNLt40FnKiBjWOBq7ABLKaCCyrkBuDU+hcyXnxjVL4vL0H8Q40mvpB2fxOckTDmYP5H2tRf+qAJffc+RFB/TUx31WOHAb2rGnWdE7wt8uTgxsGXM7u6iWCcd6sqIj9/XY4XIa/QRM/PACQE2fhL+WilQ78lRM0Fx4G/EFFfXtBltzYyPBCqUbP3Zpp1iZXKJg/tKu4i5Armz7h3bWwjfvcj6C68bHEbfekGLuOX79a1gFWou7PhwZvK/YViOwsq6rSMBPhAtoA27vmxigDGKN9JFp4GWDm2pTJ/BCYUdNDj3wOm1TWuRhs+oCdnfgrrx5UrxGPKi7GSxE3jBJZ+hU4MbVpvh8CnGittcNDIRiF/7hV989TpbTy4=:2:3',
    'uaid': lopp,
    'uiflvr': '1001',
    'user-agent': generate_user_agent(),
    'x-ms-apitransport': 'xhr',
    'x-ms-apiversion': '2',
}
     
    json_data = {
    'signInName': email,
    'uaid': lopp,
    'includeSuggestions': True,
    'uiflvr': 1001,
    'scid': 100118,
    'hpgid': 200639,
}
    res = requests.post(
    f'https://signup.live.com/API/CheckAvailableSigninNames?contextid={cone}&opid={bone}&bk=1711402639&sru=https://login.live.com/login.srf%3fcontextid%3d{cone}%26opid%3d{bone}%26mkt%3dAR-YE%26lc%3d9217%26bk%3d1711402639%26uaid%3d{lopp}&uiflavor=web&lic=1&mkt=AR-YE&lc=9217&uaid={lopp}',
    cookies=cookies,
    headers=headers,
    json=json_data,
).text
    if '"isAvailable":true' in res:

        GM += 1
        mahos(email)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''━━━━━━━━━━━━━━━━━━━━━━━━━
[0] Dev : @iiisup | TikTok HIT        
━━━━━━━━━━━━━━━━━━━━━━━━━
{F} [1] {F} {F}HIT  -  تم الصيد    » 「{gg}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{Z} [2] {Z} {Z}BAD IG - مش متاح   » 「{bb}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{A} [3] {A} {A}Good GM - جيميل صح » 「{GM}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{X} [4] {X} {X}BAD - ايميل خاطئ   » 「{BM}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{U} [5] {U} {U}email  » 「{email}」| 
━━━━━━━━━━━━━━━━━━━━━━━━━''')
    else:
         BM += 1
         os.system('cls' if os.name == 'nt' else 'clear')
        
         print(f'''━━━━━━━━━━━━━━━━━━━━━━━━━
[0] Dev : @iiisup | TikTok HIT        
━━━━━━━━━━━━━━━━━━━━━━━━━
{F} [1] {F} {F}HIT  -  تم الصيد    » 「{gg}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{Z} [2] {Z} {Z}BAD IG - مش متاح   » 「{bb}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{A} [3] {A} {A}Good GM - جيميل صح » 「{GM}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{X} [4] {X} {X}BAD - ايميل خاطئ   » 「{BM}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{U} [5] {U} {U}email  » 「{email}」| 
━━━━━━━━━━━━━━━━━━━━━━━━━''')

def generate_emails():
    session = requests.Session()
    u = 'https://www.tiktok.com/'
    response = session.get(u)
    r = session.cookies.get_dict()
    ttwid = r['ttwid']
    h = {'user-agent': str(generate_user_agent())}
    r2 = session.get('https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=0.84&browser_language=ar-IQ&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20aarch64&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7136188745632548358&device_platform=web_pc&focus_state=true&from_page=search&history_len=40&is_fullscreen=false&is_page_visible=true&keyword=aegos&os=linux&priority_region=&referer=&region=IQ&screen_height=796&screen_width=360&tz_name=Asia%2FBaghdad&verifyFp=verify_l9zrjkcx_XSZCv5U7_xzys_4UEP_8m1a_TibJS3izVTHL&webcast_language=ar&msToken=qfFKcpRIe_b543Hfa7buaE31PLWDv6-_TQYqevIaTVOPrUNjuwuHR2z0_cEadFELKqD9p6fLuWk8tgAO9lDmVCUX4vqnit3V4rX9zvJfLCbhs9U2apBgYHmKpXPp6DLl2wZy35z0xD6g6TSu_NIh&X-Bogus=DFSzswVLk-tANxW1S02v8OxPBxgg&_signature=_02B4Z6wo00001IuO8aAAAIDBSFHuFzoQUMCLjvUAAEGFfa', headers=h).cookies.get_dict()
    msToken = r2['msToken']

    while True:
        user = 'qwertyuiopasdfghjklzxcvbnm.'
        num = '456789'
        rng = int("".join(random.choice(num) for i in range(1)))
        usery = ''.join(random.choice(user) for i in range(rng))
        url = f'''https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=0.8&browser_language=ar-EG&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F108.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7167115569976100357&device_platform=web_pc&focus_state=true&from_page=search&history_len=5&is_fullscreen=false&is_page_visible=true&keyword={usery}&os=windows&priority_region=&referer=&region=IQ&screen_height=864&screen_width=1536&tz_name=Asia%2FBaghdad&webcast_language=ar&msToken=KUTYcDl8obce6sFgarFzTuyTp-uxz8sU5cFUq8fRme8gW7CZGE6IZyE04u9ugaO2fHPnE4oeSshscAF2kdNp43hjOfwbTaGSnH8ExR0LPs9VmBMkHykqXbOwL8XLgu3hMkdEin3jkM1d4ZBE&X-Bogus=DFSzswVLK1sANG9HSkI1-OYklT6o&_signature=_02B4Z6wo00001LRkx7AAAIDBahKfFq1mHTi0ZMMAAE696a'''
        he = {
            'accept': '*/*',
            'accept-language': 'ar-YE,ar-YE;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6',
            'cookie': 'passport_csrf_token=446c23e1b656077bd01b1f379ff01c64; passport_csrf_token_default=446c23e1b656077bd01b1f379ff01c64; tiktok_webapp_theme=dark; cookie-consent={"ga":true,"af":true,"fbp":true,"lip":true,"bing":true,"ttads":true,"reddit":true,"version":"v8"}; _ttp=2HZr0KnJ2pqKwJRyQ8myJ28Lpa8; __tea_cache_tokens_1988={"user_unique_id":"7160599742786815489","timestamp":1667850947815,"_type_":"default"}; passport_auth_status=c8fe9febc06f8f7a271309fa9e4f80e9,; passport_auth_status_ss=c8fe9febc06f8f7a271309fa9e4f80e9,; tt_csrf_token=CSVYu9wW-NbmqJ_cgNMHwEIItUNZGwDPM-hU; tt_chain_token=K01fXiH8q/IKwxFnx8jzcA==; _abck=951F354EE38142028A7429E8C92DB598~0~YAAQVvvOF6YBsxSFAQAAMc+wPgl24s0qz4P3iMup3WLL4PWyu/iF6+jb4qL2RfvMEKOGTv6dPfAH9AA2Hm+t/Z/Qn1TlkKHzKXk+KmuWj5d1dmCzqXD0BWgAUcMFCLRinQHou0lzh0ImXOw3B98dRIVnofWMwN8L8JxOErAxrQfi2JIEgTjNECxiZFYaqhpfLqyAUXBESaQxfCYfbNwLNwAAZvjpAfc1viGc/I9vlRIeVc2jYPA5/YUVwAytWPIOb2RuvdrXc2bfybwD3ffG0godURyE+r0QSJapjZK7kfVwbPGnVLal0dzAQM6MK2iDC5YhXugMYw9ZXB2CIaYRg4Cqy/t6BabKM9i+ZJgdvwWQQ6ljnk0pa1bKBsAYL79BxNMrQWccpQxQhUm9n09604O82PBKq8E=~-1~-1~-1; bm_sz=304AE404FA2929B0E90042E8314D20CA~YAAQVvvOF6kBsxSFAQAAMc+wPhIfC1eYkaU2YudlghSK8pNrkVcLYapeM/xrzvQbQkT9quFNwKNHsG4xkv6anwuDXn+BSd+gzoBWSdRZJscGEzPghGpbTStjyG61DtaJIqpkgjW7q6BEP37XgXgrWfHRdmoN5zraADDH7wpkIQ3UlBq5rj88cFl1IY4CUg2DSRugvtjKk+vcNV5AUjQ++v859Tv3vYF3Ga6m5lifIf0u50u/dC1xeVz0p4ew+7U21dwrDdNrai63bM7T9ArdMNk1q+2YK55FJU7tdQwtKtdLtnI=~4407620~4277556; ak_bmsc=EE17F7D340A941EB628DF68B5981EA8D~000000000000000000000000000000~YAAQVvvOF/8BsxSFAQAAS/SwPhJbeUd2XpuVnfaiGo9WDUNsMw3AUn4T4r4BtvFH6pwejSxQJ/K4aoQUK/hGU8InWjW8iSyWgKZxkNIl6lgAAvUdX8CiKcyfyQKJYfQcPDyxW6dnF6+VF2/BABsRcYTw9LUX6MjuhvgtLs1uh3AbWeHxdZFDhp/YYwjrPxoOEXgItQjGUSsxRhgRubItrsXwhW20gW9y+I7Eq22TORlAZOn+jyrl2bYH6C4yxD8yld+5OcSAQ3zKJfQLUjNj03BMgtlIyYT74OIh6GwUzgtjpGLUCzpqdeiOFZdfZApTnRoTK9J01CpUY+YxrThJKz4dScjK1V78LSd2CkfUakgFa7TXfZ1fgfPX/RW2nkWTe9SZtvDH3f62qd9b5oNojffOAM0fpnNeX06hNWSNDRRuiHOmv3m49PN2cJhknh753LdNdt81kj8LJ3SEe1y3sfHb0nPwafPExOaSSrXviHwj4+yLWrZw+dXy3Q==; sid_guard=5d52768f6a4a876314ea37244edfd0d0|1671794088|21600|Fri,+23-Dec-2022+17:14:48+GMT; uid_tt=9392403db19bcfc1eb8eb48532fd8d5e; uid_tt_ss=9392403db19bcfc1eb8eb48532fd8d5e; sid_tt=5d52768f6a4a876314ea37244edfd0d0; sessionid=5d52768f6a4a876314ea37244edfd0d0; sessionid_ss=5d52768f6a4a876314ea37244edfd0d0; sid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; ssid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; bm_sv=F556D2E15739C190D1B417337724D81E~YAAQVvvOF8ACsxSFAQAAaICxPhJ1QOpVK0jJSh0nuEay3Iz+L/0up1OoP09MVnndgBSzTjunJoYxBBQH4BTuDkQIQY+zt9kedbGoP5/7AUt2jVEq7DfEwQYdr31ZvZiHlhdU2Q5jwNvbZvNzQSokkwHoGbPqes9c4kV0ZGJuEuWc3pLurp0dkRkEBTY0UrcljYpQayw5/w7+4BlpmrMR5UAHElAGf2njGNpz3vRls+WGkTy9l8jRTCEseWkwnA9X~1; ttwid=' + ttwid + '; odin_tt=70015f10b12827e4d2b9cce32ead78da9bd1f5af11487a83ba408d86d9a4fb55ec780a14ad91b601d9fe256fcb8160786311c12ef294e6bf285fbbf7eed8dff8080f26ed1bcedbdfca7244743dcbc60e; msToken=' + msToken + '; msToken=' + msToken + '; s_v_web_id=verify_lc0f2h1w_v9MWasYr_Uw4b_4j2o_8gdZ_QkWrSxI57MTt',
            'referer': 'https://www.tiktok.com/search/user?q=its.veba&t=1671705430400',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A025F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'}
        rr = session.get(url, headers=he).json()
        np = 0
        try:
            while True:
                np += 1
                name = rr['user_list'][np]['user_info']['unique_id']
                email = name + '@hotmail.com'
                mazen(email)
        except (KeyError, IndexError):
            pass

Threads = []
for _ in range(2):
    t = threading.Thread(target=generate_emails)
    t.start()
    Threads.append(t)

for thread in Threads:
    thread.join()