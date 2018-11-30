import math
import random
from pico2d import *

class TIME:
    Time_Frame = 0.0
    Time_Start = 0.0
    Sec_Per_Frame = 0.0
    IntTime = 0
    MapCompensatorSpeed = 20
    CompensatorSpeed = 30
    def __init__(self):
        self.Time_Start = get_time()

    def TimeReset(self):
        self.Time_Start = get_time()

Timer = TIME()
class Boss:
    live = False
    W = 80
    H = 80
    life = 0
    frame = 0
    Speed = 4
    X = 0
    Y = 0
    DirX = 0
    DirY = 0
    Degree = 0
    SkillCycle = [0.0,0.0,0.0,0.0 ,0.0,0.0,0.0]
    SkillDelay = [0.0,0.0,0.0,0.0 ,0.0,0.0,0.0]
    AttackType = 0
    AttackDelay = 0.0
    AttackCycle = 2.5
    DesX = 0
    DesY = 0
    ATT = False
    def SetDes(self, x, y):
        self.DesX = x
        self.DesY = y
        self.DirX = (x - self.X)/200
        self.DirY = (y - self.Y)/200
        print((x,y))

    def Rotate(self, degree):
        self.Degree = degree

    def Move(self):
        self.X += self.DirX * self.Speed * Timer.Time_Frame * Timer.CompensatorSpeed
        self.Y += self.DirY * self.Speed * Timer.Time_Frame * Timer.CompensatorSpeed
        if(self.DesX - 10 < self.X < self.DesX +10 ):
            if(self.DesY - 10 < self.Y < self.DesY +10 ):
                self.DirX = 0.0
                self.DirY = 0.0
                return True
        return False


    def Attack(self):
        if (self.AttackDelay > self.AttackCycle):
            return 1
        else:
            self.AttackDelay += Timer.Time_Frame*3
            return -1
    def Skill(self):
        for i in range(len(self.SkillCycle)):
            self.SkillDelay[i] += Timer.Time_Frame * 3

    def Hit(self,power):
        self.life -= power
        if(self.life < 0):
            self.live = False


class Monster:
    live = False
    frame = 0
    W = 40
    H = 40
    life = 10
    DirX = 0
    DirY = 0
    Speed = 5
    SetTime = 0
    queue = [(-1,SetTime),]
    AttackType = 0
    AttackDelay = 0.0
    AttackCycle = 2.5

    def __init__(self, x,y,degree,framesize):
        self.X = x
        self.Y = y
        self.Degree = degree
        self.frame = 0
        self.framesize = framesize
    def Set(self, x,y,l,time,type,cycle):
        self.X = x
        self.Y = y
        self.life =l
        self.SetTime = time
        self.AttackType = type
        if(type == 2 or type == 3):
            self.W = 100
            self.H = 100
            self.AttackDelay = 0.0
        elif(type == 1):
            self.W = 50
            self.H = 50
            self.AttackDelay = cycle - 1.5
        elif(type == 0):
            self.W = 40
            self.H = 40
            self.AttackDelay = cycle - 1.5
        elif(type == 5):
            self.W = 40
            self.H = 40
            self.AttackDelay = 0


        self.AttackCycle = cycle
    def SetDir(self,x,y):
        self.DirX = x
        self.DirY = y
    def Rotate(self, degree):
        self.Degree = degree
    def Move(self):
        self.X += self.DirX*self.Speed*Timer.Time_Frame*Timer.CompensatorSpeed
        self.Y += self.DirY*self.Speed*Timer.Time_Frame*Timer.CompensatorSpeed
    def Attack(self):
        if(self.AttackDelay > self.AttackCycle):
            return self.AttackType
        else:
            self.AttackDelay += Timer.Time_Frame*3
            return -1

    def Draw(self):
        self.frame = self.frame = 4 + (int)((Timer.Sec_Per_Frame*8)-(Timer.Sec_Per_Frame*8 % 1))%4
    def Hit(self,power):
        self.life -= power
        if(self.life < 0):
            self.live = False

class Map:
    HightLight = (200,200)
    Size = (0,0)
    def __init__(self,x,y,w,h):
        self.HightLight = (x,y)
        self.Size = (w,h)

class Player:
    live = True
    frame = 0
    slow = False
    BulletSpeed = 15
    BulletNum = 5
    BulletPower = 10
    invincibility = False
    invincibilityTime = 0.0
    invincibilityDelay = 1.0
    MaxLife = 5
    def Invin(self):
        if(self.invincibility == True):
            if(self.invincibilityDelay < self.invincibilityTime):
                self.invincibility = False
                self.invincibilityTime = 0.0
            else:
                self.invincibilityTime += Timer.Time_Frame

    def __init__(self,x,y,life,speed,framesize):
        self.X = x
        self.Y = y
        self.Life = life
        self.Speed = speed
        self.forceX = 0
        self.forceY = 0
        self.framesize = framesize
        self.AttCnt = 0
        self.AttDelay = 5
    def Move(self):
        if(self.slow == True):
            self.X = self.X + self.forceX*self.Speed*0.5*Timer.Time_Frame* Timer.CompensatorSpeed
            self.Y = self.Y + self.forceY*self.Speed*0.5*Timer.Time_Frame* Timer.CompensatorSpeed
        else:
            self.X = self.X + self.forceX*self.Speed*Timer.Time_Frame* Timer.CompensatorSpeed
            self.Y = self.Y + self.forceY*self.Speed*Timer.Time_Frame* Timer.CompensatorSpeed

        if((10 < self.X < 490) == False):
            if(self.slow == True):
                self.X = self.X - self.forceX*self.Speed*0.5*Timer.Time_Frame* Timer.CompensatorSpeed
            else:
                self.X = self.X - self.forceX * self.Speed*Timer.Time_Frame* Timer.CompensatorSpeed

        if((20 < self.Y < 780) == False):
            if(self.slow == True):
                self.Y = self.Y - self.forceY*self.Speed*0.5*Timer.Time_Frame* Timer.CompensatorSpeed
            else:
                self.Y = self.Y - self.forceY * self.Speed*Timer.Time_Frame* Timer.CompensatorSpeed
    def Draw(self):
        if (self.forceX != 0):
            self.frame = 4 + (int)((Timer.Sec_Per_Frame*8)-(Timer.Sec_Per_Frame*8 % 1))%4
        else:
            self.frame = (int)((Timer.Sec_Per_Frame*8)-(Timer.Sec_Per_Frame*8 % 1))%self.framesize



class Effect:
    live = False
    def __init__(self,x,y,Lifetime,desX,desY,w,h):
        self.X = x
        self.Y = y
        self.Life = Lifetime
        self.desx = desX
        self.desy = desY
        self.Wsize = w
        self.Hsize = h
        self.dirX = (self.desx - self.X) // self.Life
        self.dirY = (self.desy - self.Y) // self.Life
    def Move(self):
        if(self.live == True):
            self.X = self.X + self.dirX
            self.Y = self.Y + self.dirY
            self.Life= self.Life-1*Timer.Time_Frame*Timer.CompensatorSpeed
            if(self.Life <= 0):
                self.live = False
    def RandomSetting(self,life,MaxX,MaxY):
        self.X = random.randint(0,MaxX)
        self.Y = random.randint(0,MaxY)
        self.dirX = 0
        self.dirY = 0
        self.Life = life

class Item:
    IsHave = False
    def __init__(self,num):
        self.ID = num

class PlayerBullet:
    Draw = False
    Damage = 0
    def __init__(self,id):
        self.ID = id
        self.Type = 0
        self.Speed = 0
        self.X = 800
        self.Y = 800
        self.Num = -1
    def Shoot(self,DirX,DirY):
        if(self.Draw == True):
            if(self.Type == 0 ):
                if(-10 > self.X or 510 < self.X):
                    self.Draw = False
                elif(-10 > self.Y or 810 < self.Y):
                    self.Draw = False
                else:
                    self.Y = self.Y + self.Speed*Timer.Time_Frame* Timer.CompensatorSpeed

            elif(self.Type == 1):
                if(-10  > self.X or 510 < self.X):
                    self.Draw = False
                elif(-10 > self.Y or 810 < self.Y):
                    self.Draw = False
                else:
                    self.Y = self.Y + self.Speed*Timer.Time_Frame* Timer.CompensatorSpeed
                    self.X = self.X + DirX*Timer.Time_Frame* Timer.CompensatorSpeed

    def AutoShoot(self,TargetX,TargetY):
        self.Fin = False
        if(self.Draw == True):
            if(self.Type == 2):
                if(-10 > self.X or 510 < self.X):
                    self.Draw = False
                elif(-10 > self.Y or 810 <  self.Y):
                    self.Draw = False
                else:
                    if(TargetX-5 > self.X):
                        self.X = self.X + (TargetX - self.X)* 0.19*Timer.Time_Frame* Timer.CompensatorSpeed
                    if(self.X > TargetX+5):
                        self.X = self.X + (TargetX - self.X) * 0.19*Timer.Time_Frame* Timer.CompensatorSpeed

                    self.Y = self.Y + self.Speed*Timer.Time_Frame* Timer.CompensatorSpeed

    def Set(self,x,y,type,speed,dirX,dirY,damage):
        self.Damage = damage
        self.Draw = True
        self.X = x
        self.Y = y
        self.Type = type
        self.Speed = speed
        self.DirX = dirX
        self.DirY = dirY
        self.Num = -1

class MonsterBullet:
    Live = False
    Type = 0
    X = 0
    Y = 0
    DirX = 0.00
    DirY = 0.00
    Speed = 0
    W = 20
    H = 20
    def Set(self,x,y,Dx,Dy,speed,w,h):
        self.X = x
        self.Y = y
        self.DirX = Dx
        self.DirY = Dy
        self.Speed = speed
        self.W = w
        self.H = h
    def ChangeDir(self,x,y):
        self.X = x
        self.Y = y
    def Move(self):
        self.X += self.DirX*Timer.Time_Frame*Timer.CompensatorSpeed*self.Speed
        self.Y += self.DirY*Timer.Time_Frame*Timer.CompensatorSpeed*self.Speed










