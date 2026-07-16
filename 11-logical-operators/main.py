# logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be true
#                     and = both conditions  must be true
#                     not = inverts the condition (not False,  not True)

username = input("masukan username: ")
password = input("masukkan password: ")
umur = int(input("umur: "))
member = input("kamu member? (Y/N): ")

if username == "mascin" and password == "asin":
    print("login berhasil")
    if umur >= 13 or member == "Y":
        print("akses warnet diizinkan")
    else:
        print("akses warnet ditolak")
else:
    print("login gagal")

