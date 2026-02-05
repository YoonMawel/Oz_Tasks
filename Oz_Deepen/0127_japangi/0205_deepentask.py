from abc import ABC, abstractmethod

class Abstract(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.take = 0

    def create(self):
        self.money()
        if not self.confirm(): # 해당 단계에서 반환된 값이 False면 중단
            return
        self.ready()
        self.process()
        self.here()

    def money(self):
        self.take = int(input(f"{self.name} 돈을 투입하세요.: "))

    def confirm(self):
        if self.take >= self.price:
            print(f"{self.name} 금액 검증 완료 (필요: {self.price}원)")
            return True
        else:
            print(f"{self.name} 금액이 부족합니다. (모자란 금액: {self.price - self.take})")
            return False

    @abstractmethod
    def ready(self): # 이것만 추상 메서드
        pass

    def process(self):
        print(f"{self.name} 제품 배출 완료")

    def here(self):
        print(f"{self.name} 거스름돈 {self.take - self.price}")


class CoffeeVendingMachine(Abstract):
    def __init__(self):
        super().__init__("[커피 자판기]", 1200)

    def ready(self):
        print(f"{self.name} 원두 분쇄 중...")
        print(f"{self.name} 추출 중...")
        print(f"{self.name} 컵에 담는 중...")


class ColaVendingMachine(Abstract):
    def __init__(self):
        super().__init__("[콜라 자판기]", 800)

    def ready(self):
        print(f"{self.name} 냉장 상태 확인 중...")
        print(f"{self.name} 배출구로 이동 중...")


class RamenVendingMachine(Abstract):
    def __init__(self):
        super().__init__("[라면 자판기]", 1500)

    def ready(self):
        print(f"{self.name} 컵면 배출")
        print(f"{self.name} 뜨거운 물 주입 중...")


coffee = CoffeeVendingMachine()
coffee.create()

cola = ColaVendingMachine()
cola.create()

ramen = RamenVendingMachine()
ramen.create()