from pymongo import MongoClient 
#  Tạo một biến bằng đoạn string MongoDB UMI 
# 59100 là port cổng vào, sửa dbuser và dbpassword chính là user của database là admin và password ybox2013
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

# 1. Connect to database 
client = MongoClient(mongo_uri)

# 2. Get database
db = client.get_default_database()

# 3. Create a collection
# games = db['games']

# # 4. Create a document
# new_game = {
#     "title" : "Hứng Bia",
#     "description" : "Best Game Ever"
# }



# # 5. Insert documents into collection 
# games.insert_one(new_game)


# 6. Read all documents 

# all_game = games.find()
# # Kiểu dữ liệu của all_game sẽ là list các dictionary
# first_game = all_game[0]
# print(first_game['description'])

