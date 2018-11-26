from Object import *
import random
from pico2d import*

class GLOBAL:
    # stage = title, main, level, stage, end
    stage = "main"
    prev_stage = "main"

    # level menu
    g_Level = -1
    g_Hard = 0
    g_Type = 0
    g_ATT = False

    # in game stage
    g_StageTime = 0
    stageback = 1

    # main menu
    WindowX = 800
    WindowY = 800
    GameX = WindowX / 8 * 5
    MyMouse = [WindowX / 2, WindowY / 2]
    g_Time = 0
    g_TimeCheck = False
    g_Player = Player(WindowX / 8 * 2.5, WindowY / 8 * 1, 5, 7, 8)

    #monster
    g_MonsterPool = [Monster(-1, -1, 0, 0) for i in range(0, 100)]
    g_Boss = Boss()


    # effect
    Star_EffectPool = [Effect(0, 0, 50, 0, 0, random.randint(7, 12), random.randint(7, 12)) for i in
                       range(0, 300)]
    for i in range(0, 100):
        Star_EffectPool[i].RandomSetting(random.randint(50, 100), WindowX, WindowY)
    MouseStar = [Effect(0, 0, 15, 0, 0, random.randint(22, 33), random.randint(22, 33)) for i in range(0, 50)]
    ClickStar = [Effect(0, 0, 5, 0, 0, random.randint(7, 10), random.randint(7, 10)) for i in range(0, 50)]
    ClickCnt = 0
    for i in range(0, 50):
        MouseStar[i].live = False

    # serve menu
    pause = False

    # Bullet
    g_BulletArr = [PlayerBullet(i) for i in range(0, 500)]
    g_BulletCnt = 0
    g_BulletDelay = 30

    g_MonsterBulletArr = [MonsterBullet() for i in range(0,1000)]
    g_MonsterBulletCnt = 0


    def SetMonsterBullet(self,x,y,Dx,Dy,speed,w,h,type):
        for i in range(0,len(self.g_MonsterBulletArr)):
            if(self.g_MonsterBulletArr[i].Live == True):
                continue
            else:
                self.g_MonsterBulletArr[i].Set(x,y,Dx,Dy,speed,w,h)
                self.g_MonsterBulletArr[i].Type = type
                self.g_MonsterBulletArr[i].Live = True
                break

    def MonsterAttack(self):
        for Monster in self.g_MonsterPool:
            if Monster.live == True:
                if(Monster.Attack() >= 0):#basic attack
                    Monster.AttackDelay = 0.0
                    #if(self.g_Player.Y < Monster.Y):
                    if(Monster.AttackType == 0):
                        if(abs(self.g_Player.X-Monster.X)>abs(self.g_Player.Y-Monster.Y)):
                            self.SetMonsterBullet(Monster.X, Monster.Y,
                                                  (self.g_Player.X - Monster.X) / abs(self.g_Player.X - Monster.X),
                                                  (self.g_Player.Y - Monster.Y) / abs(self.g_Player.X - Monster.X), 10,
                                                  20, 20,0)
                        else:
                            self.SetMonsterBullet(Monster.X, Monster.Y,
                                                 (self.g_Player.X - Monster.X) / abs(self.g_Player.Y - Monster.Y),
                                                 (self.g_Player.Y - Monster.Y) / abs(self.g_Player.Y - Monster.Y), 10,
                                                 20, 20,0)

                    elif(Monster.AttackType == 1):
                        if (abs(self.g_Player.X - Monster.X) > abs(self.g_Player.Y - Monster.Y)):
                            self.SetMonsterBullet(Monster.X, Monster.Y,
                                                  (self.g_Player.X+25 - Monster.X) / abs(self.g_Player.X - Monster.X),
                                                  (self.g_Player.Y+25 - Monster.Y) / abs(self.g_Player.X - Monster.X), 8+Global.g_Hard,
                                                  20, 20,1)
                            self.SetMonsterBullet(Monster.X, Monster.Y,
                                                  (self.g_Player.X-25 - Monster.X) / abs(self.g_Player.X - Monster.X),
                                                  (self.g_Player.Y+25 - Monster.Y) / abs(self.g_Player.X - Monster.X), 8+Global.g_Hard,
                                                  20, 20,1)
                            self.SetMonsterBullet(Monster.X, Monster.Y,
                                                  (self.g_Player.X - Monster.X) / abs(self.g_Player.X - Monster.X),
                                                  (self.g_Player.Y - Monster.Y) / abs(self.g_Player.X - Monster.X), 8+Global.g_Hard,
                                                  20, 20,1)
                        else:
                            self.SetMonsterBullet(Monster.X, Monster.Y,
                                                  (self.g_Player.X+25 - Monster.X) / abs(self.g_Player.Y - Monster.Y),
                                                  (self.g_Player.Y+25 - Monster.Y) / abs(self.g_Player.Y - Monster.Y), 8+Global.g_Hard,
                                                  20, 20,1)
                            self.SetMonsterBullet(Monster.X, Monster.Y,
                                                  (self.g_Player.X-25 - Monster.X) / abs(self.g_Player.Y - Monster.Y),
                                                  (self.g_Player.Y+25 - Monster.Y) / abs(self.g_Player.Y - Monster.Y), 8+Global.g_Hard,
                                                  20, 20,1)
                            self.SetMonsterBullet(Monster.X, Monster.Y,
                                                  (self.g_Player.X - Monster.X) / abs(self.g_Player.Y - Monster.Y),
                                                  (self.g_Player.Y - Monster.Y) / abs(self.g_Player.Y - Monster.Y), 8+Global.g_Hard,
                                                  20, 20,1)
                    elif (Monster.AttackType == 2):
                        if(random.randint(0,2)==0):
                            for j in range(0,40):
                                self.SetMonsterBullet(Monster.X, Monster.Y, 5*math.sin(math.radians(j*360//40)),-5*math.cos(math.radians(j*360//40)), 1, 14, 14,3)
                        else:
                            for j in range(0,40):
                                self.SetMonsterBullet(Monster.X, Monster.Y, 5.5*math.sin(math.radians(j*360//40)),-5.5*math.cos(math.radians(j*360//40)), 1, 14, 14,3)
                    elif (Monster.AttackType == 3):
                            for j in range(0, 100):
                                self.SetMonsterBullet(Monster.X, Monster.Y, (6+(-5+j%10)*0.5) * math.sin(math.radians(j * 360 // 50)),
                                                      (6 + (-5 + j % 10) * 0.5) * math.cos(math.radians(j * 360 // 50)), 1, 14, 14,3)
                            Monster.AttackType = 4
                    elif (Monster.AttackType == 4):
                            for j in range(0, 100):
                                self.SetMonsterBullet(Monster.X, Monster.Y,
                                                      (6 + (-5 + (100-j) % 10) * 0.5) * math.sin(math.radians(j * 360 // 50)),
                                                      (6 + (-5 + (100 - j) % 10) * 0.5) * math.cos(math.radians(j * 360 // 50)), 1, 14, 14,3)
                            Monster.AttackType = 3
                    elif (Monster.AttackType == 5):
                        if(Monster.Y > 400):
                            if (abs(self.g_Player.X - Monster.X) > abs(self.g_Player.Y - Monster.Y)):
                                self.SetMonsterBullet(Monster.X, Monster.Y,
                                                      (self.g_Player.X - Monster.X) / abs(self.g_Player.X - Monster.X),
                                                      (self.g_Player.Y - Monster.Y) / abs(self.g_Player.X - Monster.X),
                                                      15,14, 14,4)
                            else:
                                self.SetMonsterBullet(Monster.X, Monster.Y,
                                                      (self.g_Player.X - Monster.X) / abs(self.g_Player.Y - Monster.Y),
                                                      (self.g_Player.Y - Monster.Y) / abs(self.g_Player.Y - Monster.Y),
                                                      15,14, 14,4)
                        else:
                            Monster.SetDir(0,Monster.DirY-0.1)

    def MonsterSet(self):
        if(self.g_Level == 0):
            for i in range(0,3):
                self.g_MonsterPool[i].Set(450,820,30+10*self.g_Hard,(i)*0.5+5,0,10-Global.g_Hard)
                self.g_MonsterPool[i].SetDir(-1,-0.5)
                self.g_MonsterPool[i+3].Set(50,820,30+10*self.g_Hard,(i)*0.5+5,0,10-Global.g_Hard)
                self.g_MonsterPool[i+3].SetDir(1,-0.5)
            for i in range(20,23):
                self.g_MonsterPool[i].Set(50 + 50*(i-20),820,30+10*self.g_Hard,10,0,10-Global.g_Hard)
                self.g_MonsterPool[i].SetDir(0,-0.5)

            for i in range(23,26):
                self.g_MonsterPool[i].Set(450 - 50*(i-23),820,30+10*self.g_Hard,10,0,10-Global.g_Hard)
                self.g_MonsterPool[i].SetDir(0,-0.5)
            for i in range(26,29):
                self.g_MonsterPool[i].Set(150 + 100*(26-i),820,50+10*self.g_Hard,15,1,15-Global.g_Hard*2)
                self.g_MonsterPool[i].SetDir(0,-0.5)

            for i in range(30,40):
                self.g_MonsterPool[i].Set(50 + 50*(random.randint(0,9)),820,30+10*self.g_Hard,random.randint(5,20)*0.5+18,0,15-Global.g_Hard*2)
                self.g_MonsterPool[i].SetDir(0,-0.5)


            self.g_MonsterPool[40].Set(350,820,250+100*self.g_Hard,28,2,5.5)
            self.g_MonsterPool[40].SetDir(-0.25,-0.5)
            for i in range(50,55):
                self.g_MonsterPool[i].Set(50 + 50*(random.randint(0,9)),820,30+10*self.g_Hard,random.randint(10,30),0,15-Global.g_Hard*2)
                self.g_MonsterPool[i].SetDir(0,-0.5)
            self.g_MonsterPool[42].Set(250, 820, 250 + 100 * self.g_Hard, 42, 2, 5.5)
            self.g_MonsterPool[42].SetDir(0, -0.5)

            for i in range(60,65):
                self.g_MonsterPool[i].Set(50 + 50 * (random.randint(0, 9)), 820, 40 + 10 * self.g_Hard,
                                          random.randint(30, 45), 1, 15 - Global.g_Hard * 2)
                self.g_MonsterPool[i].SetDir(0, -0.5)
            for i in range(65, 70):
                self.g_MonsterPool[i].Set(100 + 50 * (random.randint(0, 11)), 820, 40 + 10 * self.g_Hard,
                                          random.randint(20, 40), 1, 15 - Global.g_Hard * 2)
                self.g_MonsterPool[i].SetDir(0, -0.5)

                self.g_MonsterPool[70].Set(350, 820, 250 + 100 * self.g_Hard, 45, 3, 8)
                self.g_MonsterPool[70].SetDir(-0.1, -0.5)

            if(Global.g_Hard >= 1):
                self.g_MonsterPool[41].Set(150, 820, 250 + 100 * self.g_Hard, 14, 2, 5.5)
                self.g_MonsterPool[41].SetDir(0.25, -0.5)

                for i in range(55,60):
                    self.g_MonsterPool[i].Set(50 + 50*(random.randint(0,9)),820,20+10*self.g_Hard,random.randint(10,30),0,15-Global.g_Hard*2)
                    self.g_MonsterPool[i].SetDir(0,-0.5)

            if(Global.g_Hard >= 2):
                self.g_MonsterPool[42].Set(150, 820, 250 + 100 * self.g_Hard, 45, 3, 8)
                self.g_MonsterPool[42].SetDir(0, -0.5)
                for i in range(0, 3):
                    self.g_MonsterPool[90 + i].Set(50 + 35 * i, 820, 50 + 25 * self.g_Hard, 40 + i * 0.2, 0, 0.1)
                    self.g_MonsterPool[90 + i].SetDir(-0.1, -1.5)

            self.g_Boss.life = 1000 + 1000 * Global.g_Level + 300 * Global.g_Hard
            self.g_Boss.AttackType = Global.g_Level
            self.g_Boss.X = 250
            self.g_Boss.Y = 820
            self.g_Boss.SetDes(250,600)

    def MonsterActive(self):
        global Timer
        for Monster in self.g_MonsterPool:
            if(Monster.life > 0 and Monster.SetTime != 0):
                if Monster.SetTime < get_time()-Timer.Time_Start:
                    Monster.live = True

        if(Global.g_Boss.life > 0):
            if(get_time() - Timer.Time_Start> 2):
                for Monster in self.g_MonsterPool:
                    Monster.live = False
                Global.g_Boss.live = True

    def MonsterMove(self):
        global Timer
        for Monster in self.g_MonsterPool:
            if(Monster.live == True):
                Monster.Move()

        if(self.g_Boss.live == True):
            if self.g_Boss.ATT == False:
                self.g_Boss.ATT = self.g_Boss.Move()
                if(self.g_Boss.ATT == True):
                    self.g_Boss.AttackCycle = 10
            else:
                if(self.g_Boss.Attack() > 0):
                    self.g_Boss.AttackDelay = 0.0
                    self.g_Boss.SetDes(random.randint(1,4)*100,random.randint(10,15)*50)
                    self.g_Boss.ATT = False
                    #self.g_Boss.AttackType += 1
                else:
                    self.g_Boss.Skill()
                    if(self.g_Boss.AttackType == 0):
                        for i in range(len(self.g_Boss.SkillCycle)):
                            if(self.g_Boss.SkillCycle[i] - (self.g_Hard)/2 < self.g_Boss.SkillDelay[i]):
                                self.g_Boss.SkillDelay[i] = 0
                                if( i == 0):
                                    if (abs(self.g_Player.X - self.g_Boss.X) > abs(self.g_Player.Y - self.g_Boss.Y)):
                                        self.SetMonsterBullet(self.g_Boss.X, self.g_Boss.Y,
                                                              (self.g_Player.X - self.g_Boss.X) / abs(self.g_Player.X - self.g_Boss.X),
                                                              (self.g_Player.Y - self.g_Boss.Y) / abs(self.g_Player.X - self.g_Boss.X), 10,
                                                              20, 20, 0)
                                    else:
                                        self.SetMonsterBullet(self.g_Boss.X, self.g_Boss.Y,
                                                              (self.g_Player.X - self.g_Boss.X) / abs(self.g_Player.Y - self.g_Boss.Y),
                                                              (self.g_Player.Y - self.g_Boss.Y) / abs(self.g_Player.Y - self.g_Boss.Y), 10,
                                                              20, 20, 0)
                                TEMP =random.randint(-10,11)
                                if( i == 1):
                                    for j in range(0, 6):
                                        self.SetMonsterBullet(self.g_Boss.X, self.g_Boss.Y,
                                                              5 * math.sin(math.radians(j * 360 // 6+30+TEMP)),
                                                              -5 * math.cos(math.radians(j * 360 // 6+30+TEMP)), 0.5, 48,48, 3)
                                if (i == 2):
                                    for j in range(0, 18):
                                        self.SetMonsterBullet(self.g_Boss.X, self.g_Boss.Y,
                                                              5 * math.sin(math.radians(j * 360 // 6+TEMP)),
                                                              -5 * math.cos(math.radians(j * 360 // 6+TEMP)), 1, 20, 20, 2)







Global =GLOBAL()

open_canvas(Global.WindowX,Global.WindowY )