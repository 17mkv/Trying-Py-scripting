from ftplib import FTP
import os
import json

def GetSecrets():
    with open('C:\\Users\\MLA\\keys.json', 'r') as f:
        keys_data = json.load(f)
    path = keys_data["path"]
    username = keys_data["user"]
    password = keys_data["password"]
    ftp = keys_data["ftpserver"]
    return ftp, path, username, password


def GetShproty(dir_path):
    if not dir_path: return
    try:
        files = os.listdir(dir_path)
        if files:
            files.sort(key=lambda x: os.path.getctime(os.path.join(dir_path, x)))
            last_file = os.path.join(dir_path, files[-1])
            if last_file: return last_file
    except Exception as e:
        print("Error", e)
def FuckMom(path):
    try:
        arr = path.split(".")
        if arr[-1] == "afi":
            out_name = arr[0].split('\\')[-1]
            with open(f"{path}", 'rb') as folder:
                ftp.storbinary(f'STOR {out_name}.afi', folder)
        else:
            origin_path = GetShproty(path)
            out_name = origin_path.split('\\')[-1].split('.')[0]
            with open(f"{origin_path}", 'rb') as folder:
                ftp.storbinary(f'STOR {out_name}.afi', folder)
    except Exception as e:
        print("Vse v govne", e)

def GetSochelnik():
    dir_list = [os.path.join(path, x) for x in os.listdir(path)]
    if dir_list:
        date_list = [[x, os.path.getctime(x)] for x in dir_list]

        sort_date_list = sorted(date_list, key=lambda x: x[1], reverse=True)

        if (sort_date_list[0][0]):
            FuckMom(sort_date_list[0][0])
        else:
            print("create directory eblan")

ftpserver, path, user, password = GetSecrets()

ftp = FTP(ftpserver)
ftp.login(user=user, passwd=password)
GetSochelnik()
