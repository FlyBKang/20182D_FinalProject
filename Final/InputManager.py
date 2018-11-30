from pico2d import*
from  globalParamiter import*

def handle_events(events):
    global Global,Texture,Timer
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            Global.MyMouse[0] = event.x
            Global.MyMouse[1] = Global.WindowY - event.y
            num = (int)(Global.g_Time) % 50
            Global.MouseStar[num].X = event.x + random.randint(-5, 6)
            Global.MouseStar[num].Y = Global.WindowY - event.y + random.randint(-5, 6)
            Global.MouseStar[num].dirX = Global.MouseStar[num].dirY = 0
            Global.MouseStar[num].Life = random.randint(12, 20)
            Global.MouseStar[num].live = True
            if(Global.stage == "level"):
                for i in range(0,8):
                    if(180-25+60*i < Global.MyMouse[0] <180+25+60*i):
                        if (250-25 < Global.MyMouse[1] < 250+25):
                            Global.Itemshow = i
                            break
                        else:
                            Global.Itemshow = -1
                    else:
                        Global.Itemshow = -1

        if event.type == SDL_MOUSEBUTTONDOWN:
            for i in range(0,50):
                Global.ClickStar[i].live = True
                Global.ClickStar[i].Life = 5
                Global.ClickStar[i].X = event.x
                Global.ClickStar[i].Y = Global.WindowY -event.y
                Global.ClickStar[i].dirX = Global.ClickStar[i].dirY = 0
            Global.ClickCnt = 0

        if(Global.stage == "main"):
            if event.type == SDL_MOUSEBUTTONDOWN:
                if (100 < Global.MyMouse[0] < 700):
                    if (400 < Global.MyMouse[1] < 500):
                        Timer.TimeReset()
                        Global.stage = "level"

                if (100 < Global.MyMouse[0] < 700):
                    if (250 < Global.MyMouse[1] < 350):
                        close_canvas()
                        exit(1);

        elif(Global.stage == "level"):
            if event.type == SDL_MOUSEBUTTONDOWN:
                if ( 620 < Global.MyMouse[0] < 780):
                    if (40 < Global.MyMouse[1] < 120):
                        #reset
                        Timer.TimeReset()
                        Global.stage = "stage"
                        Global.g_Level = Global.g_Level + 1
                        Global.g_Player.X,Global.g_Player.Y = Global.WindowX / 8 * 2.5, Global.WindowY / 8 * 1
                        Global.g_Player.Life = Global.g_Player.MaxLife
                        Global.g_Clear = False
                        for arr in Global.g_BulletArr:
                            arr.Draw = False
                        for arr in Global.g_MonsterBulletArr:
                            arr.Live = False
                        Global.MonsterSet()


                if ( 490 < Global.MyMouse[0] < 610):
                    if (40 < Global.MyMouse[1] < 120):
                        Timer.TimeReset()
                        Global.stage = "main"
                        Global.g_Level = -1

                if(330-70 < Global.MyMouse[0] <330+70):
                    if (470-65 < Global.MyMouse[1] < 470+65):
                        Global.g_Hard = 0

                if(450-70 < Global.MyMouse[0] <450+70):
                    if (470-65 < Global.MyMouse[1] < 470+65):
                        Global.g_Hard = 1

                if(570-70 < Global.MyMouse[0] <570+70):
                    if (470-65 < Global.MyMouse[1] < 470+65):
                        Global.g_Hard = 2

                if(330-70 < Global.MyMouse[0] <330+70):
                    if (670-65 < Global.MyMouse[1] < 670+65):
                        Global.g_Type = 0

                if(450-70 < Global.MyMouse[0] <450+70):
                    if (670-65 < Global.MyMouse[1] < 670+65):
                        Global.g_Type = 1

                if(570-70 < Global.MyMouse[0] <570+70):
                    if (670-65 < Global.MyMouse[1] < 670+65):
                        Global.g_Type = 2



                if(Global.g_Level == -1):
                    pass

        elif(Global.stage == "stage"):
            if event.type == SDL_KEYDOWN:  # key down
                if event.key == SDLK_LSHIFT:
                    Global.g_Player.slow = True
                if event.key == SDLK_RIGHT:
                    Global.g_Player.forceX = 1
                elif event.key == SDLK_LEFT:
                    Global.g_Player.forceX = -1
                elif event.key == SDLK_UP:
                    Global.g_Player.forceY = 1
                elif event.key == SDLK_DOWN:
                    Global.g_Player.forceY = -1

                if event.key == SDLK_a:
                    Global.g_ATT = True

                if event.key == SDLK_TAB:#치트
                    Global.g_Type = (Global.g_Type+1) % 3
                if event.key == SDLK_n:
                    Global.g_Player.BulletNum += 1
                if event.key == SDLK_m:
                    if(Global.g_Player.BulletNum>3):
                        Global.g_Player.BulletNum -= 1





            if event.type == SDL_KEYUP:  # key up
                if event.key == SDLK_LSHIFT:
                    Global.g_Player.slow = False
                if event.key == SDLK_RIGHT:
                    if(Global.g_Player.forceX == 1):
                        Global.g_Player.forceX = 0
                if event.key == SDLK_LEFT:
                    if(Global.g_Player.forceX == -1):
                        Global.g_Player.forceX = 0

                if event.key == SDLK_DOWN:
                    if(Global.g_Player.forceY == -1):
                        Global.g_Player.forceY = 0
                if event.key == SDLK_UP:
                    if(Global.g_Player.forceY == 1):
                        Global.g_Player.forceY = 0

                if event.key == SDLK_a:
                    Global.g_ATT = False
                    Global.g_BulletCnt = Global.g_BulletDelay

                if event.key == SDLK_ESCAPE:
                    if(Global.pause == True):
                        Global.pause = False
                    else:
                        Global.pause = True
                if event.key == SDLK_F1:
                    Global.g_Boss.live = True

        else:
            pass
