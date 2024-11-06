class GemStone:
    total_gems = 0  
    store_name = "Luxury Gems" 
    
    def __init__(self, carats=None, price=None, name=None, color="Без кольору", origin="Невідоме походження"):
        self.__carats = carats if carats else 0.0
        self.__price = price if price else 0.0
        self.__name = name if name else "Unknown"

        
        self.color = color 
        self.origin = origin  
        GemStone.total_gems += 1
    
    def __del__(self):
        GemStone.total_gems -= 1
        print(f"Камінь {self.__name} видалено")
    
    def get_carats(self):
        return self.__carats
        
    def get_price(self):
        return self.__price
        
    def get_name(self):
        return self.__name
    
    def set_carats(self, carats):
        self.__carats = carats
        
    def set_price(self, price):
        self.__price = price
        
    def set_name(self, name):
        self.__name = name
    
    def __str__(self):
        return (f"Коштовний камінь: {self.__name}, {self.__carats} карат, "
                f"колір: {self.color}, походження: {self.origin}, ціна: {self.__price} грн")
    
    def __repr__(self):
        return (f"GemStone(name='{self.__name}', carats={self.__carats}, "
                f"price={self.__price}, color='{self.color}', origin='{self.origin}')")

def main():
    diamond = GemStone(2.5, 50000, "Діамант", "Безбарвний", "Африка")
    ruby = GemStone(1.8, 25000, "Рубін", "Червоний", "Бірма")
    emerald = GemStone(3.0, 30000, "Смарагд", "Зелений", "Колумбія")
    
    gems = [diamond, ruby, emerald]
    for i, gem in enumerate(gems, 1):
        print(f"\nКамінь {i}:")
        print(f"Назва: {gem.get_name()}")
        print(f"Кількість каратів: {gem.get_carats()}")
        print(f"Ціна: {gem.get_price()} грн")
        print(f"Колір: {gem.color}")
        print(f"Походження: {gem.origin}")
        print(f"Магазин: {GemStone.store_name}")
        print(f"Загальна кількість каменів: {GemStone.total_gems}")
        print(f"Представлення str: {str(gem)}")
        print(f"Представлення repr: {repr(gem)}")

if __name__ == "__main__":
    main()
