class Bird:
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"{self.name} 출발!!!")

    def sound(self):
        if self.name == '앵무새':
            print("까악")
        elif self.name == '참새':
            print("짹짹")
        elif self.name == '비둘기':
            print("구구")
        else:
            print("해당 조류는 존재하지 않습니다.")

    def fly(self):
        if self.name == '앵무새':
            print("날개를 힘차게 날았습니다.")
        elif self.name == '참새':
            print("날개를 빠르게 날았습니다.")
        elif self.name == '비둘기':
            print("날개를 부드럽게 날았습니다.")
        else:
            print("해당 조류는 존재하지 않습니다.")

    def meter(self):
        if self.name == '앵무새':
            print("결과는 2m 입니다.")
        elif self.name == '참새':
            print("결과는 8m 입니다.")
        elif self.name == '비둘기':
            print("결과는 12m 입니다.")
        else:
            print("해당 조류는 존재하지 않습니다.")

#parrot = Bird("앵무새")
#twit = Bird("참새")
#googoo = Bird("비둘기")

a = Bird(input("새의 이름을 입력하세요.: "))

#parrot.start()
#parrot.sound()
#parrot.fly()
#parrot.meter()

a.start()
a.sound()
a.fly()
a.meter()