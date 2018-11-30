class Item:
    Num = 0
    Name = ""
    Text = ""
    Level = 0
    def __init__(self,num,name,text,level):
        self.Num = num
        self.Name = name
        self.Text = text
        self.Level = level

class inventory:
    def __init__(self):
        self.inven = [Item(-1," "," ",-1) for i in range(0,8)]
    def Insert(self,num,item):
        self.inven[num] = item
    def Reset(self):
        self.inven.clear()

ItemIndex = []
# 노말 5
ItemIndex.append(Item(0,"공격력 포션","획득시 공격력 +1",0))
ItemIndex.append(Item(2,"붕대","획득시 최대체력 +1",0))
ItemIndex.append(Item(3,"표창","획득시 탄막의 모양이 바뀌고 공격력이 +1 증가된다.",0))
ItemIndex.append(Item(4,"속도 포션","탄막 속도가 증가된다.",0))
ItemIndex.append(Item(5,"오래된 양피지","공격력 +1,최대 체력 +1",0))
#레어 6
ItemIndex.append(Item(1,"탄막 알약","획득시 탄막 숫자 +1",1))
ItemIndex.append(Item(6,"랜덤상자","획득시 무작위 아이템을 획득한다.",1))
ItemIndex.append(Item(7,"저주","최대체력 -1, 공격력 증가 +2",1))
ItemIndex.append(Item(9,"부적[수호]","피격시 플레이어 주변의 탄막이 사라진다.",1))
ItemIndex.append(Item(11,"미술작품","최대체력 +2, [노말]오래된 양피지가 존재하는 경우 공격력 + 2",1))
ItemIndex.append(Item(12,"카오스 박스","소지한 모든 아이템을 랜덤으로 바꾼다.",1))

#유니크 6
ItemIndex.append(Item(8,"부적[번개]","적이 공격당할 때 2% 확률로 번개를 일으킨다.(공격력 20) ",2))
ItemIndex.append(Item(13,"고급 랜덤박스","유니크 혹은 전설의 무작위 아이템을 얻는다.",2))
ItemIndex.append(Item(14,"저주의 보석","최대체력 -1, 공격력 증가 +5, [레어]저주가 이미 존재하는 경우 최대체력 +4",2))
ItemIndex.append(Item(15,"비약","최대 체력이 2배가 된다..",2))
ItemIndex.append(Item(16,"자유의 날개","25% 확률로 피격을 무효화한다.",2))
ItemIndex.append(Item(17,"부적[수호2]","피격시 플레이어 주변의 넓은 범위의 탄막이 사라진다, [레어] 부적[수호]가 존재하는 경우 피격시 맵상의 모든 탄막을 제거한다.",2))
ItemIndex.append(Item(10,"신비의 악보","최대체력 +1, 2발의 유도탄을 발사한다.",2))
#전설 4
ItemIndex.append(Item(18,"관통","탄막에 관통능력을 얻는다.",3))
ItemIndex.append(Item(19,"융합체","공격력 +5, 최대체력 +4, 탄막숫자 +3, 탄막속도 +2",3))
ItemIndex.append(Item(20,"냉기폭풍","적이 받는 피해를 2배로 증가시킨다, 탄막 속도가 줄어든다., 탄막이 바뀐다.",3))
ItemIndex.append(Item(21,"골든타임","보상을 2개 선택 할 수 있다.",3))

