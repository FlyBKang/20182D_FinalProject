from pico2d import*
from  globalParamiter import*
from InputManager import *
from Collision import *

class TEXTURE:
    P_main = load_image("resource\\main.jpg")
    P_player = load_image("resource\\character.png")
    P_player_alpha = load_image("resource\\character.png")
    P_player_alpha.opacify(0.5)
    P_light1 = load_image("resource\\Eff_Glitter.png")
    P_light2 = load_image("resource\\Eff_Glitter2.png")
    P_light3 = load_image("resource\\Eff_Glitter3.png")
    P_light4 = load_image("resource\\Eff_Glitter4.png")
    P_startbutton = load_image("resource\\startbutton.png")
    P_exitbutton = load_image("resource\\exitbutton.png")
    P_bullet = load_image("resource\\bullet.png")
    P_menuback = load_image("resource\\edge.png")
    P_menuside = load_image("resource\\side.png")
    P_mouse = load_image("resource\\pointer.png")
    P_okbutton = load_image("resource\\okbutton.png")
    P_cancelbutton = load_image("resource\\cancelbutton.png")
    P_levelselect = load_image("resource\\edge2.png")
    P_item = load_image("resource\\item.png")
    P_effectlevel = load_image("resource\\effect_background.png")
    P_leveltype = load_image("resource\\level_type.png")
    P_stage = [load_image("resource\\stage1.jpg")]
    P_level = [load_image("resource\\level_easy.png"), load_image("resource\\level_normal.png"), load_image("resource\\level_hard.png")]
    P_textlevel = [load_image("resource\\menu_stage.png"), load_image("resource\\menu_level.png"), load_image("resource\\menu_attack.png"),
                   load_image("resource\\menu_item.png")]
    # 텍스쳐를 불러옵니다.
    P_Monster = load_image("resource\\Unit.png")
    P_Boss1 = load_image("resource\\boss1.png")
    stage_arr = [Map(0, 0, 500, 800)]

Texture = TEXTURE()
def Collision():
    global Global
    if(Global.stage == "stage"):
        MonsterCol()
        MonsterBulletCol()
        Global.g_Player.Invin()

def Draw():
    global Global
    if (Global.stage == "main"):
        TitleDraw()
    elif(Global.stage == "stage"):
        CreateBullet()
        StageDraw()
        shoot()
        Global.MonsterActive()
        Global.MonsterMove()
        Global.MonsterAttack()
        BulletDraw()
        MonsterDraw()
        Collision()
        UI_Draw()#임시
    elif(Global.stage == "level"):
        LevelDraw()

    if(Global.stage != "stage"):
        EffectDraw()

    #mouse cursor
    Texture.P_mouse.draw(Global.MyMouse[0],Global.MyMouse[1],100,100)

def UI_Draw():
    global Global,Texture,Timer
    font = load_font('ENCR10B.TTF', 16)
    font.draw(400,760, '(Life: %d)' %Global.g_Player.Life, (255, 255, 0))


def EffectDraw():
    global Global
    ##main Effect
    if(Global.stage != "stage"):
        if (Global.g_TimeCheck == False):
            Global.g_Time = Global.g_Time + 2 * Timer.Time_Frame * Timer.CompensatorSpeed
            if (Global.g_Time > Texture.P_main.w - Global.WindowX):
                Global.g_TimeCheck = True
        else:
            Global.g_Time = Global.g_Time - 2 * Timer.Time_Frame * Timer.CompensatorSpeed
            if (Global.g_Time < Global.WindowY):
                Global.g_TimeCheck = False
        for i in range(0,100):
            if(Global.Star_EffectPool[i].live == True):
                if( (i % 2) == 0):
                    Texture.P_light1.composite_draw(math.radians(random.randint(0,360)),'',Global.Star_EffectPool[i].X,Global.Star_EffectPool[i].Y,Global.Star_EffectPool[i].Wsize,Global.Star_EffectPool[i].Hsize)
                else:
                    Texture.P_light2.composite_draw(math.radians(random.randint(0,360)),'',Global.Star_EffectPool[i].X,Global.Star_EffectPool[i].Y,Global.Star_EffectPool[i].Wsize,Global.Star_EffectPool[i].Hsize)
                Global.Star_EffectPool[i].Move()
            else:
                Global.Star_EffectPool[i].RandomSetting(random.randint(50, 100), Global.WindowX, Global.WindowY)
                Global.Star_EffectPool[i].live = True
        for i in range(0,50):
            if(Global.MouseStar[i].live == True):
                if(i%2 == 0):
                    Texture.P_light3.composite_draw(math.radians(random.randint(0, 360)), '', Global.MouseStar[i].X,Global.MouseStar[i].Y, Global.MouseStar[i].Life*2, Global.MouseStar[i].Life*2)
                else:
                    Texture.P_light4.composite_draw(math.radians(random.randint(0, 360)), '', Global.MouseStar[i].X,Global.MouseStar[i].Y, Global.MouseStar[i].Life*2, Global.MouseStar[i].Life*2)
                Global.MouseStar[i].Move()
        angle = float(math.radians(1))
        if(Global.ClickCnt < 50):
            Global.ClickCnt = Global.ClickCnt+1*Timer.Time_Frame*Timer.CompensatorSpeed
            for i in range(0,50):
                if Global.ClickStar[i].live == True:
                    if(i%2==0):
                        Texture.P_light3.composite_draw(math.radians(random.randint(0, 1)), '',
                                                Global.ClickStar[i].X + Global.ClickCnt/2*random.randint(20,100)*0.02 * math.sin(angle * float(360 / 50 * i)),
                                                Global.ClickStar[i].Y + Global.ClickCnt/2*random.randint(20,100)*0.02 * math.cos(angle * float(360 / 50 * i)),
                                                Global.ClickStar[i].Wsize, Global.ClickStar[i].Hsize)
                    else:
                        Texture.P_light4.composite_draw(math.radians(random.randint(0, 1)), '',
                                                Global.ClickStar[i].X + Global.ClickCnt/2*random.randint(20,100)*0.02 * math.sin(angle * float(360 / 50 * i)),
                                                Global.ClickStar[i].Y + Global.ClickCnt/2*random.randint(20,100)*0.02 * math.cos(angle * float(360 / 50 * i)),
                                                Global.ClickStar[i].Wsize, Global.ClickStar[i].Hsize)

                    if(i%2==0):
                        Texture.P_light3.composite_draw(math.radians(random.randint(0, 1)), '',
                                                Global.ClickStar[i].X + Global.ClickCnt/2*random.randint(20,100)*0.02 * math.sin(angle * float(360 / 50 * i)),
                                                Global.ClickStar[i].Y + Global.ClickCnt/2*random.randint(20,100)*0.02 * math.cos(angle * float(360 / 50 * i)),
                                                Global.ClickStar[i].Wsize//0.75, Global.ClickStar[i].Hsize//0.75)
                    else:
                        Texture.P_light4.composite_draw(math.radians(random.randint(0, 1)), '',
                                                Global.ClickStar[i].X + Global.ClickCnt/2*random.randint(20,100)*0.02 * math.sin(angle * float(360 / 50 * i)),
                                                Global.ClickStar[i].Y + Global.ClickCnt/2*random.randint(20,100)*0.02 * math.cos(angle * float(360 / 50 * i)),
                                                Global.ClickStar[i].Wsize//0.75, Global.ClickStar[i].Hsize//0.75)

    ##main Effect

def TitleDraw():
    global Global, Texture, Timer
    ##main menu
    Texture.P_main.clip_draw(0 + (int)(Global.g_Time), 0, Global.WindowX, Global.WindowY, Global.WindowX // 2,Global.WindowY // 2)
    ##main menu
    if (100 < Global.MyMouse[0] < 700):
        if (400 < Global.MyMouse[1] < 500):
            Texture.P_startbutton.draw(Global.WindowX / 2, Global.WindowY - 350, 620, 110)
        else:
            Texture.P_startbutton.draw(Global.WindowX / 2, Global.WindowY - 350, 600, 100)
    else:
        Texture.P_startbutton.draw(Global.WindowX / 2, Global.WindowY - 350, 600, 100)

    if (100 < Global.MyMouse[0] < 700):
        if (250 < Global.MyMouse[1] < 350):
            Texture.P_exitbutton.draw(Global.WindowX / 2, Global.WindowY - 500, 620, 110)
        else:
            Texture.P_exitbutton.draw(Global.WindowX / 2, Global.WindowY - 500, 600, 100)
    else:
        Texture.P_exitbutton.draw(Global.WindowX / 2, Global.WindowY - 500, 600, 100)



def StageDraw():
    global Global, Timer
    if (Global.stage == "stage"):
        if (Global.g_Level == 0):
            if (Global.stageback == 1):
                Texture.P_stage[0].clip_composite_draw(0 + (int)(Global.g_StageTime / 3 * 2),
                                                       0 + (int)(Global.g_StageTime), (int)(Texture.P_stage[0].w // 3),
                                                       (int)(Texture.P_stage[0].h // 2), 0, "", 250, 400, 500, 800)
                #if (Global.serve == False):
                Global.g_StageTime = Global.g_StageTime + 1.25*Timer.Time_Frame* Timer.MapCompensatorSpeed
                if (Texture.P_stage[0].h > Global.g_StageTime >= Texture.P_stage[0].h // 2):
                    Global.stageback = -1
            elif (Global.stageback == -1):
                if (Global.g_StageTime >= Texture.P_stage[0].h):
                    pass
                else:
                    Global.g_StageTime = Global.g_StageTime + 1.25*Timer.Time_Frame* Timer.MapCompensatorSpeed
                Texture.P_stage[0].clip_composite_draw(0 + (int)(Global.g_StageTime / 3 * 2),
                                                       0 + (int)(Texture.P_stage[0].h - Global.g_StageTime),
                                                       (int)(Texture.P_stage[0].w // 3),
                                                       (int)(Texture.P_stage[0].h // 2), 0, "", 250, 400, 500, 800)


        if (Global.g_Player.live == True):
            Global.g_Player.Move()
            if (Global.g_Player.forceX > 0):
                Texture.P_player.clip_draw(Global.g_Player.frame * 32, 60 + 50 * 0, 32, 50, Global.g_Player.X,
                                           Global.g_Player.Y)
            elif (Global.g_Player.forceX < 0):
                Texture.P_player.clip_draw(Global.g_Player.frame * 32, 60 + 50 * 1, 32, 50, Global.g_Player.X,
                                           Global.g_Player.Y)
            else:
                Texture.P_player.clip_draw(Global.g_Player.frame * 32, 60 + 50 * 2, 32, 50, Global.g_Player.X,
                                           Global.g_Player.Y)
            Global.g_Player.Draw()
            if (Global.g_Player.slow == True):
                Texture.P_player.clip_draw(0, 0, 65, 65, Global.g_Player.X, Global.g_Player.Y)
            else:
                Texture.P_player.clip_draw(28, 28, 7, 7, Global.g_Player.X, Global.g_Player.Y)


def MonsterDraw():
    angle = math.radians(1)

    for monster in Global.g_MonsterPool:
        if (monster.live == True):
            if (monster.AttackType == 0):
                Texture.P_Monster.clip_composite_draw(0, 300, 80, 70, monster.Degree * angle, "", monster.X, monster.Y,
                                                      monster.W, monster.H)
            elif (monster.AttackType == 1):
                Texture.P_Monster.clip_composite_draw(80, 300, 75, 69, monster.Degree * angle, "", monster.X, monster.Y,
                                                      monster.W, monster.H)
            elif (monster.AttackType == 2):
                Texture.P_Monster.clip_composite_draw(0, 1350, 80, 75, monster.Degree * angle, "", monster.X, monster.Y,
                                                      monster.W, monster.H)
            elif (monster.AttackType == 3 or monster.AttackType == 4):
                Texture.P_Monster.clip_composite_draw(0, 1350, 80, 75, monster.Degree * angle, "", monster.X, monster.Y,
                                                      monster.W, monster.H)
            elif (monster.AttackType == 5):
                monster.Rotate(monster.Degree + 3)
                Texture.P_player_alpha.clip_composite_draw(65, 0, 65, 65, monster.Degree * angle, "", monster.X,
                                                           monster.Y, monster.W, monster.H)
            else:
                draw_rectangle(monster.X - 50, monster.Y - 50, monster.X + 50, monster.Y + 50)
    if (Global.g_Boss.live == True):
        Texture.P_Boss1.clip_composite_draw(0, 220, 75, 60, Global.g_Boss.Degree * angle, "", Global.g_Boss.X,
                                            Global.g_Boss.Y, Global.g_Boss.W, Global.g_Boss.H)


def LevelDraw():
    global Texture, Global,Timer
    if(Global.stage == "level"):#
        Texture.P_menuback.draw(Global.WindowX/2,Global.WindowY/2,Global.WindowX,Global.WindowY)
        Texture.P_effectlevel.draw(Global.WindowX/2,Global.WindowY/2,Global.WindowX-80,Global.WindowY-80)
        Texture.P_levelselect.draw(390,660,610,170)
        Texture.P_levelselect.draw(390,460,610,170)
        Texture.P_levelselect.draw(390,260,610,170)
        Texture.P_menuside.draw(Global.WindowX/2,Global.WindowY/10*9-50,900,200)
        Texture.P_menuside.draw(Global.WindowX/2,Global.WindowY/10*9-250,900,200)
        Texture.P_menuside.draw(Global.WindowX/2,Global.WindowY/10*9-450,900,200)
        if (640 < Global.MyMouse[0] < 760):
            if (40 < Global.MyMouse[1] < 120):
                Texture.P_okbutton.draw(700,80,130,90)
            else:
                Texture.P_okbutton.draw(700,80,120,80)
        else:
            Texture.P_okbutton.draw(700,80,120,80)

        if (490 < Global.MyMouse[0] < 610):
            if (40 < Global.MyMouse[1] < 120):
                Texture.P_cancelbutton.draw(550, 80, 130, 90)
            else:
                Texture.P_cancelbutton.draw(550, 80, 120, 80)
        else:
            Texture.P_cancelbutton.draw(550, 80, 120, 80)


        if(Timer.IntTime % 2 == 0):
            Texture.P_bullet.clip_draw(625,000, 60, 61, 330, 662, 70, 70)
            Texture.P_bullet.clip_draw(625,000, 60, 61, 450, 662, 70, 70)
            Texture.P_bullet.clip_draw(625,000, 60, 61, 570, 662, 70, 70)
            Texture.P_bullet.clip_draw(625,000, 60, 61, 330, 455, 70, 70)
            Texture.P_bullet.clip_draw(625,000, 60, 61, 450, 455, 70, 70)
            Texture.P_bullet.clip_draw(625,000, 60, 61, 570, 455, 70, 70)

        if(Global.g_Type== 0):
            Texture.P_item.clip_draw(46*3,3+47*1, 45, 46, 330, 662, 70, 70)
        elif(Global.g_Type == 1):
            Texture.P_item.clip_draw(46*3,3+47*1, 45, 46, 450, 662, 70, 70)
        else:
            Texture.P_item.clip_draw(46*3,3+47*1, 45, 46, 570, 662, 70, 70)

        if(Global.g_Hard == 0):
            Texture.P_item.clip_draw(46*3,3+47*1, 45, 46, 330, 455, 70, 70)
        elif(Global.g_Hard == 1):
            Texture.P_item.clip_draw(46*3,3+47*1, 45, 46, 450, 455, 70, 70)
        else:
            Texture.P_item.clip_draw(46*3,3+47*1, 45, 46, 570, 455, 70, 70)
        Texture.P_bullet.clip_composite_draw(150, 190, 30, 85, math.radians(0), "", 340, 655, 15, 55)
        Texture.P_bullet.clip_composite_draw(150, 190, 30, 85, math.radians(0), "", 320, 655, 15, 55)
        Texture.P_bullet.clip_composite_draw(150, 190, 30, 85, math.radians(0), "", 330, 662, 20, 70)

        Texture.P_bullet.clip_composite_draw(120, 190, 30, 85, math.radians(15), "", 435, 655, 15, 55)
        Texture.P_bullet.clip_composite_draw(120, 190, 30, 85, math.radians(-15), "", 465, 655, 15, 55)
        Texture.P_bullet.clip_composite_draw(120, 190, 30, 85, math.radians(0), "", 450, 662, 20, 70)

        Texture.P_bullet.clip_composite_draw(90, 190, 30, 40, math.radians(-25), "", 585, 645, 15, 25)
        Texture.P_bullet.clip_composite_draw(90, 190, 30, 40, math.radians(25), "", 555, 645, 15, 25)
        Texture.P_bullet.clip_composite_draw(90, 230, 30, 40, math.radians(25), "", 585, 675, 15, 25)
        Texture.P_bullet.clip_composite_draw(90, 230, 30, 40, math.radians(-25), "", 555, 675, 15, 25)
        Texture.P_bullet.clip_composite_draw(0, 190, 30, 85, math.radians(0), "", 570, 662, 20, 70)


        Texture.P_bullet.clip_composite_draw(0, 190, 30, 85, math.radians(-45), "", 190, 640, 40, 100)
        Texture.P_bullet.clip_composite_draw(30, 190, 30, 85, math.radians(45), "", 190, 640, 40, 100)
        Texture.P_leveltype.clip_draw(0,50,200,50,450,707,120,30)
        Texture.P_leveltype.clip_draw(0,0,40,50,330,607,50,25)
        Texture.P_leveltype.clip_draw(40,0,40,50,450,607,30,30)
        Texture.P_leveltype.clip_draw(80,0, 40,50,570,607,30,30)
        Texture.P_textlevel[0].draw(190,490,120,60)
        Texture.P_textlevel[1].draw(450,490,120,60)
        Texture.P_textlevel[2].draw(190,690,120,60)
        Texture.P_textlevel[3].draw(190,290,120,60)
        Texture.P_level[0].draw(330, 390, 100, 50)
        Texture.P_level[1].draw(450, 390, 100, 50)
        Texture.P_level[2].draw(570, 390, 100, 50)
        if (Global.g_Level == -1):
            Texture.P_stage[0].clip_draw(Texture.stage_arr[0].HightLight[0],Texture.stage_arr[0].HightLight[1],Texture.stage_arr[0].Size[0],Texture.stage_arr[0].Size[1],190,440,120,100)
            #P_stage[1].clip_draw(stage_arr[0].HightLight[0],stage_arr[0].HightLight[1],stage_arr[0].Size[0],stage_arr[0].Size[1],330,470,100,100)
            #P_stage[2].clip_draw(stage_arr[0].HightLight[0],stage_arr[0].HightLight[1],stage_arr[0].Size[0],stage_arr[0].Size[1],450,470,100,100)
            #P_stage[3].clip_draw(stage_arr[0].HightLight[0],stage_arr[0].HightLight[1],stage_arr[0].Size[0],stage_arr[0].Size[1],570,470,100,100)
        #ITEM
        draw_rectangle(150,200,175+60*8,300)

def shoot():
    global Global
    for Arr in Global.g_BulletArr:
        if (Arr.Draw == True):
            if (Arr.Type == 2):
                TargetTemp = (Global.g_Player.X, 850)
                for Monster in Global.g_MonsterPool:
                    if Monster.live == True:
                        if Global.g_Player.Y + 125 < Monster.Y :
                            if Arr.Y < Global.g_Player.Y +255:
                                TargetTemp = (Monster.X, Monster.Y)
                                break

                if (TargetTemp[1] == 850):
                    Arr.AutoShoot(Arr.X, TargetTemp[1])
                else:
                    Arr.AutoShoot(TargetTemp[0], TargetTemp[1])

            elif (Arr.Type == 0):
                Arr.Shoot(0, 0)
            else:
                (Arr.Shoot(Arr.DirX, Arr.DirY))

def CreateBullet():
    global Global,Timer
    if (Global.g_Level >= 0):
        if (Global.g_ATT == True):
            Global.g_BulletCnt = Global.g_BulletCnt + 1
            if (Global.g_BulletCnt > Global.g_BulletDelay):
                Bulletlenth = 50 // Global.g_Player.BulletNum
                BulletTemp = 1
                PosTemp = -1
                for Arr in Global.g_BulletArr:
                    if (Arr.Draw == False):
                        if (Global.g_Type != 2):
                            Arr.Set(
                                Global.g_Player.X + Bulletlenth * (-Global.g_Player.BulletNum // 2 + BulletTemp),
                                Global.g_Player.Y + 8 * (PosTemp), Global.g_Type, Global.g_Player.BulletSpeed,
                                Bulletlenth * (-Global.g_Player.BulletNum // 2 + BulletTemp) // 10, 800,
                                Global.g_Player.BulletPower)
                        else:
                            if BulletTemp == 1 or BulletTemp == Global.g_Player.BulletNum:
                                Arr.Set(Global.g_Player.X + Bulletlenth * (
                                        -Global.g_Player.BulletNum // 2 + BulletTemp),
                                        Global.g_Player.Y + 8 * (PosTemp), Global.g_Type,
                                        Global.g_Player.BulletSpeed,
                                        Bulletlenth * (-Global.g_Player.BulletNum // 2 + BulletTemp) // 10, 800,
                                        Global.g_Player.BulletPower / 2)
                            else:
                                Arr.Set(Global.g_Player.X + Bulletlenth * (
                                        -Global.g_Player.BulletNum // 2 + BulletTemp),
                                        Global.g_Player.Y + 8 * (PosTemp), 0, Global.g_Player.BulletSpeed,
                                        Bulletlenth * (-Global.g_Player.BulletNum // 2 + BulletTemp) // 10, 800,
                                        Global.g_Player.BulletPower)

                        BulletTemp = BulletTemp + 1
                        PosTemp = PosTemp * (-1)
                    if (BulletTemp == Global.g_Player.BulletNum + 1):
                        Global.g_BulletCnt = 0
                        break

def BulletDraw():
    global Global,Texture
    # draw Bullet
    for Arr in Global.g_BulletArr:
        if (Arr.Draw == True):
            if (Arr.Type == 1):
                Texture.P_bullet.clip_draw(363, 137, 22, 22, Arr.X, Arr.Y, 17, 17)
            elif (Arr.Type == 0):
                Texture.P_bullet.clip_draw(533, 220, 17, 27, Arr.X, Arr.Y, 12, 22)
            else:
                Texture.P_bullet.clip_draw(425, 160, 25, 20, Arr.X, Arr.Y, 14, 14)

    for Arr in Global.g_MonsterBulletArr:
        if(Arr.Live == True):
            Arr.Move()
            if(Arr.Type == 0):
                Texture.P_bullet.clip_draw(Arr.Type * 63, 0, 62, 64, Arr.X, Arr.Y, Arr.W, Arr.H)
            elif(Arr.Type == 1):
                Texture.P_bullet.clip_draw(Arr.Type * 63, 0, 62, 64, Arr.X, Arr.Y, Arr.W, Arr.H)
            elif(Arr.Type == 2):
                Texture.P_bullet.clip_draw(Arr.Type * 63, 0, 62, 64, Arr.X, Arr.Y, Arr.W, Arr.H)
            elif(Arr.Type == 3):
                Texture.P_bullet.clip_draw(Arr.Type * 63, 0, 62, 64, Arr.X, Arr.Y, Arr.W, Arr.H)
            elif(Arr.Type == 4):
                Texture.P_bullet.clip_draw(Arr.Type * 63, 0, 62, 64, Arr.X, Arr.Y, Arr.W, Arr.H)
            elif(Arr.Type == 5):
                Texture.P_bullet.clip_draw(5 * 63, 0, 62, 64, Arr.X, Arr.Y, Arr.W, Arr.H)
            elif (Arr.Type == 6):
                Texture.P_bullet.clip_draw(5 * 63, 0, 62, 64, Arr.X, Arr.Y, Arr.W, Arr.H)


def Input():
    events = get_events()
    handle_events(events)


