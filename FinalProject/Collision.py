from  globalParamiter import*

def MonsterCol():
    global Global

    for Monster in Global.g_MonsterPool:
        if Monster.live == True:
            if(-20< Monster.X< 520)==False:
                Monster.live = False
                Monster.life = 0
            if(-50< Monster.Y< 850)==False:
                Monster.live = False
                Monster.life = 0
            for Bullet in Global.g_BulletArr:
                if (Bullet.Draw == True):
                    if (Monster.X - Monster.W // 2 < Bullet.X < Monster.X + Monster.W // 2):
                        if (Monster.Y - Monster.H // 2 < Bullet.Y < Monster.Y + Monster.H // 2):
                            Monster.Hit(Bullet.Damage)
                            Bullet.Draw = False

    if(Global.g_Boss.live == True):
        for Bullet in Global.g_BulletArr:
            if (Bullet.Draw == True):
                if (Global.g_Boss.X - Global.g_Boss.W // 2 < Bullet.X < Global.g_Boss.X + Global.g_Boss.W // 2):
                    if (Global.g_Boss.Y - Global.g_Boss.H // 2 < Bullet.Y < Global.g_Boss.Y + Global.g_Boss.H // 2):
                        Global.g_Boss.Hit(Bullet.Damage)
                        Bullet.Draw = False

def MonsterBulletCol():
    global Global
    for Arr in Global.g_MonsterBulletArr:
        if Arr.Live == True:
            if(0< Arr.X < 500) == False:
                Arr.Live = False
            if(0< Arr.Y < Global.WindowY) == False:
                Arr.Live = False
            if(Arr.X - Arr.W/2 < Global.g_Player.X <Arr.X + Arr.W/2):
                if(Arr.Y - Arr.H/2 < Global.g_Player.Y <Arr.Y + Arr.H/2):
                    Arr.Live = False
                    if(Global.g_Player.invincibility == False):
                        Global.g_Player.Life -= 1
                        Global.g_Player.invincibility = True
