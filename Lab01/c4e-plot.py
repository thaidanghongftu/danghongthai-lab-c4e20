import matplotlib 

# Do matplotlib nó lại dùng 1 thằng đồ hoạ bên ngoài nên nó sẽ dùng lệnh sau 
matplotlib.use("TkAgg")


from matplotlib import pyplot 
#  Các bước tiến hành : 
# 1. Prepare data, ví dụ tỷ lệ % và tên 
labels = ["Web", "Android", "iOS", "React Native"] 
values = [40, 25, 20, 15]
colors = ["green", "blue", "orange", "gold"]
explode = [ 0, 0, 0, 0.2 ]

# 2. Plot 
pyplot.pie(
    values, 
    labels =  labels , 
    colors = colors ,
    explode = explode

)
pyplot.axis('equal')

# 3. Show / Vẽ đồ thị 
pyplot.show() 

