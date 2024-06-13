import matplotlib.pyplot as plt
class Restaran:
    def __init__(self):
        self.menu = {
            "lag'mon": 20,
            "shashlik": 30,
            "somsa": 10,
            "mastava": 15,
            "suyuq": 35,
            "norin": 40,
            "manti": 18,
            "salat": 12,
            "choy": 5
        }
        
    def is_admin(self):
        i=3
        password = input("Passwordni kiriting: ")
        while True:
            if password == "123":
                return True
            i-=1
            if i==0:
                return False
            
            
    def add_dish(self):
        new_dish = input("Qanaqa ovqat qo'shasiz.\n>>> ")
        while True:
            try:
                price = float(input("Narxini kiriting.\n>>> "))
                break
            except ValueError:
                print("\n Faqat son kirita olasiz")
        if new_dish in self.menu.keys():
            print(f"\n{new_dish} allaqachon qo'shilgan.")
        self.menu[new_dish] = price
        print(f"\n{new_dish} muaffaqiyatli qo'shildi")
        

    def remove_dish(self):
        self.all_dishes()
        remove_dish = input("\nQaysi ovqatbi olib tashlamoqchisiz?")
        if remove_dish not in self.menu.keys():
            print(f"{remove_dish} topilmadi!")
        del self.menu[remove_dish]
        print(f"\n{remove_dish} muaffaqiyatli o'chirildi.")
        
        
    def change_price(self):
        self.all_dishes()
        new_price_dish = input("Qaysi ovqatni narxini o'zgartirasiz?\n>>> ")
        while True:
            try:
                new_price = float(input("Narxini kiriting.\n>>> "))
                break
            except ValueError:
                print("\n Faqat son kirita olasiz")
        if new_price_dish not in self.menu.keys():
            print(f"\n{new_price_dish} ovqat topilmadi.")
        self.menu[new_price_dish] = new_price
        print(f"\n{new_price_dish} muaffaqiyatli qo'shildi")
        
        
    def all_dishes(self):
        print(f"MENU")
        for num, menu in enumerate(self.menu.items(), 1):
            print(f"{num}. {menu[0]}  {menu[1]}")
    
    
    def order_dish(self):
        print("Xush kelibsiz!")
        print("Qanday ovqatlardan tanlaysiz?")

        for index, (dish, price) in enumerate(self.menu.items(), start=1):
            print(f"{index}. {dish} - {price} so'm")

        total_amount = 0
        ordered_dishes = {}

        while True:
            try:
                user_order = input("Zakaz raqamini kiriting (yoki 'stop' deb yozing): ")

                if user_order.lower() == "stop":
                    break

                order_index = int(user_order) - 1

                if 0 <= order_index < len(self.menu):
                    dish, price = list(self.menu.items())[order_index]
                    total_amount += price
                    ordered_dishes[dish] = ordered_dishes.get(dish, 0) + 1
                    print(f"{dish} zakaz berildi.")
                else:
                    print("Noto'g'ri raqam. Iltimos, menyudagi raqamni kiriting.")

            except ValueError:
                print("Iltimos, faqat raqam kiriting yoki 'stop' deb yozing.")

        print("\nJami summa:", total_amount, "so'm")
        print("Siz zakaz berdingiz:")
        for dish, quantity in ordered_dishes.items():
            print(f"- {dish} x {quantity}")
        plt.figure(figsize=(10, 6))  # Adjust figure size as needed
        plt.bar(ordered_dishes.keys(), ordered_dishes.values(), color='skyblue')
        plt.title("Buyurtma qilingan ovqatlar")
        plt.xlabel("Ovqat nomi")
        plt.ylabel("Soni")
        plt.xticks(rotation=45, ha='right')  # Rotate labels for better readability
        plt.show()
        
        


    
    
    def admin(self):
        print("1. mahsulot qo'shish")
        print("2. Mahsulot narxini yangilash")
        print("3. mahsulotni o'chirish")
        print("4. Bosh menu")


restaran = Restaran()


def main():
    print("1. Admin sifatida kirish")
    print("2. Mijoz sifatida kirish")
    print("3. Chiqish")
        
    while True:
        try:
            select = int(input("Quyidagilardan birini tanlang👇\n>> "))
            if select not in [1,2,3]:
                raise ValueError
        except ValueError:
            print("Faqat 1, 2 va 3 ni tanlang.")
        match select:
            case 1:
                print("case1")
                a=restaran.is_admin()
                if a:
                    while True:
                        restaran.admin()
                        choice = int(input("Yuyidagilardan birini tanlang"))
                        
                        match choice:
                            case 1:
                                restaran.add_dish()
                            case 2:
                                restaran.change_price()
                            case 3:
                                restaran.remove_dish()
                            case 4:
                                break
                            case _:
                                print("1-4 oralig'ida son kiriting.")
            case 2:
                restaran.order_dish()
            case 3:
                break                    

main()