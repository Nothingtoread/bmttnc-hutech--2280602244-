def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_string=input("Nhập chuỗi cần đảo ngược: ")
print("Chuỗi đão ngược là: ",dao_nguoc_chuoi(input_string))