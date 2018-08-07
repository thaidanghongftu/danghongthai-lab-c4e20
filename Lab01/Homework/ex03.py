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
posts = db["posts"]
# # 4. Create a document
# new_game = {
#     "title" : "Hứng Bia",
#     "description" : "Best Game Ever"
# }

new_post = {
    "title" : "Sinh Nhật Bác",
    "author" : "Đặng Hồng Thái",
    "content" : """
    
    Con sinh ra khi Bác không còn nữa
    Chỉ biết về Người qua mẩu chuyện, dòng thơ
    Qua những thước phim mờ lịch sử
    Gặp được Người chỉ trong giấc mơ…

    Con tự nhủ giữa dòng đời đổi khác
    Nhân cách Người con học suốt đời con
    Nghĩ về Người làm lòng con thanh tịnh
    Sống thanh cao giản dị không mòn

    Tuổi trẻ hôm nay là tương lai đất nước
    Kinh tế thị trường, học bạn nhưng phải biết ta
    Biết giữ gìn truyền thống của ông cha
    Đừng cá nhân, ích kỷ mà phải biết vị tha!

    Rồi mai đây bạn bè con sẽ thành cán bộ
    Con cũng chẳng thể mãi như bây giờ
    Học gương Người cần kiệm liêm chính chí công vô tư
    Làm lãnh đạo phải vì dân trước nhất

    …
    Con chưa vào lăng thăm Bác Hồ
    Chưa thăm nhà sàn Bác ở đơn sơ
    Ao cá nhỏ nước thường ăm ắp
    Nhớ Bác ngày xưa vẫn lặng như tờ…

    Sắp sinh nhật Bác rồi con nhớ
    79 xuân xưa nay xuân vẫn nở hoa
    Cứ mỗi tháng 5 như Bác vẫn bên ta
    Đất nước này tự hào ta có Bác!

    17/5/2012
    """

}

# # 5. Insert documents into collection 
# games.insert_one(new_game)
posts.insert_one(new_post)

# 6. Read all documents 

# all_game = games.find()
# # Kiểu dữ liệu của all_game sẽ là list các dictionary
# first_game = all_game[0]
# print(first_game['description'])

