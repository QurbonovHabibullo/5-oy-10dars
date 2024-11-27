from autosalon import DataBase

def main():
    db = DataBase()
    print("Autosalon dasturi ishga tushdi.")
    while True:
        print("\nBuyruqlar ro'yxati:")
        print("1. modellarni chiroyli ko'rinishda chiqarish")
        print("2. xodimlar va buyurtmachilarning emayilni birlashtirish")
        print("3. har bir davlatda buyurtmachilar sonini hisoblash")
        print("4. har bir davlatda xodimlar sonini hisoblash")
        print("5. har bir brandda modellarning sonini chiqarish")
        print("6. modellar soni 5 tadan ko'p bo'lgan brandlarni chiqarish")
        print("7. orders jadvalini boshqa jadvallar bilan birlashtirish")
        print("8. modellar umumiy narxini hisoblash")
        print("9. brandlar sonini chiqarish")
        print("10. yangi ma'lumot qo'shish")
        print("11. dasturni to'xtatish")

        buyruq_tanlash = input("\nBuyruq raqamini tanlang: ")

        if buyruq_tanlash == '1':
            sql = """select models.model_name, brands.brand_name, colors.color_name 
                     from models 
                     join brands on models.brand_id = brands.brand_id
                     join colors on models.color_id = colors.color_id"""
            results = db.manager(sql=sql, fetchall=True)
            for row in results:
                print(f"Model: {row[0]}, Brand: {row[1]}, Rang: {row[2]}")

        elif buyruq_tanlash == '2':
            sql = """select email from employees UNION select email from customers"""
            results = db.manager(sql=sql, fetchall=True)
            print("Barcha email adreslar:")
            for email in results:
                print(email[0])

        # Qo'shimcha buyruqlarni shu yerga joylashtiring

        elif buyruq_tanlash == '11':
            print("Dastur to'xtatildi.")
            break

        else:
            print("Noto'g'ri buyruq.")

if __name__ == "__main__":
    main()
