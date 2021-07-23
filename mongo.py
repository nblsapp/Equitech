# import pymongo, dns
# import json, os
# client = pymongo.MongoClient(os.environ['MONGO'])

# db = client.Equitech

# courses = db.Courses
# files = db.Files
# servers = db.Servers

# def setup():
#     old_file = json.load(open('static/json/servers.json'))
#     file = []
    
#     for i in range(0, len(old_file)): 
#       file.append({}) #should work now YAYAYAYAYAYAY
#       file[i]['_id'] = i + 1
#       file[i]['Name'] = old_file[i][0]
#       file[i]['Invite'] = old_file[i][1]
#       file[i]['Messages'] = old_file[i][-3]
#       file[i]['Users'] = old_file[i][-2]
#       file[i]['Owner'] = old_file[i][-1]
#     print(file)
#     servers.insert_many([i for i in file])
# setup()
  