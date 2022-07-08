#Cho trước chuỗi s được nhập từ bàn phím, bạn hãy viết chương trình để đảo ngược thứ tự xuất hiện của các từ trong chuỗi s và sau đó hiển thị ra màn hình chuỗi đã được xử lý. 

s = str(input())
s = s.split()
s.reverse()
a = " "
print(a.join(s))