#Exeption
def not_prime(num):
    flag = False
    try:
        if type(num) == int:
            if num > 1:
                for k in range(2,num):
                    if num % k == 0:
                        flag = True
                        break
            elif num <=1:
                raise ValueError("Nhap sai")
            else:
                flag = True        
    except:
        print("Ngoai le!!!")
        def can_bac_hai(n):
    try:
        if type(n) == str:
            raise ValueError("Gia tri truyen vao la kieu chuoi!!!")
        elif n < 0:
            raise ValueError("Gia tri truyen vao phai lon hon 0!!!")
        else:
            k = math.sqrt(n)
            print("Can bac hai cua so {} la: {}".format(n,k))
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    can_bac_hai(10)