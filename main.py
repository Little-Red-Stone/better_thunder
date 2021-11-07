import pygame,sys,time,os
SCREEN_W,SCREEN_H=400,720
ICON_REA = "AppIcon.png"
ICON = pygame.image.load(ICON_REA)
CL = [
    [(0, 0, 0), (244,245,245)],  # black 0
    [(255, 0, 0), (255, 0, 0)],  # red 1
    [(255, 165, 0), (255, 165, 0)],  # orange 2
    [(255, 255, 0), (255, 255, 0)],  # yellow 3
    [(0, 255, 0), (0, 255, 0)],  # lime 4
    [(86, 188, 133), (86, 188, 133)],  # forest green 5
    [(0, 255, 255), (0, 255, 255)],  # cyan 6
    [(0, 0, 255), (0, 0, 255)],  # blue 7
    [(70, 130, 180), (44, 124, 246)],  # steel blue 8
    [(128, 0, 128), (128, 0, 128)],  # purple 9
    [(199, 21, 133), (199, 21, 133)],  # medium violet red 10
    [(255, 255, 255), (0, 0, 0)],  # white 11

    [(40, 36, 35), (255, 255, 255)],  # dark gray 12
    [(49, 45, 44), (234, 233, 232)],  # gray 13
    [(105, 105, 105), (209, 207, 206)],  # dim gray 14
    [(50, 46, 45), (50, 46, 45)],  # white gray 15
    [(45, 105, 155), (45, 105, 155)],  # selected blue 16
    [(70, 67, 65), (244, 245, 245)],  # Windows gray 17

    [(64, 156, 231), (64, 156, 231)]  # good blue 18
]
def disfonten(big, word, x, y, color=11):
    font = pygame.font.Font("JetBrainsMono.ttf", big)
    screen.blit(font.render(word, True, CL[color][0]), (x, y))
def disfontch(big, word, x, y, color=11):
    font = pygame.font.Font("WeiRuanYaHei.ttf", big)
    screen.blit(font.render(word, True, CL[color][0]), (x, y))
def drect(x, y, w, h, color=11):
    pygame.draw.rect(screen, CL[color][0], (x, y, w, h))
class better_thunder(object):
    def __init__(self):
        self.pList=[
            ["applications","应用页面（删除后顶部无应用 Tab，打不开设置，不建议删除）"],
            ["cloudspace","迅雷云盘"],
            ["browserhelper","浏览器支持"],
            ["diagnostic","网络诊断（可以不删除）"],
            ["featuredpage","精选页面（删除后顶部无精选 Tab ）"],
            ["feedback","意见反馈"],
            ["livestream","直播相关"],
            ["liveupdate","直播相关"],
            ["myvip","会员中心"],
            ["onethingcloud","玩客云"],
            ["preferences","偏好设置（不建议删除）"],
            ["softmanager","应用管理（卸载）"],
            ["subtitle","内置字幕下载"],
            ["thunderword","迅雷世界"],
            ["userlogin","用户登录"],
            ["viprenew","会员相关（需要会员功能的不要删除，同时也不要删除用户登录插件）"],
            ["viptips","会员相关（需要会员功能的不要删除，同时也不要删除用户登录插件）"],
            ["webgame","网络游戏"],
            ["xlbrowser","内置浏览器（可以不删除）"],
            ["xlplayer","迅雷影音"],
        ]
        self.pFlag=[1 for _ in range(len(self.pList))]
        self.pFlag[0],self.pFlag[10]=0,0
        self.window=0
        self.sccsim=0
        self.usrpList=[0 for _ in range(len(self.pList))]
        self.usrpList[0], self.usrpList[10] = 1, 1
        self.shdt=False
    def reload(self):
        screen.fill(CL[13][0])
        disfonten(30,"Better Thunder",10,5)
    def draw(self):
        self.reload()
        if self.window==0:
            drect(10,60,300,30,17)
            disfontch(20,"一键精简（推荐设置）",20,60)
            drect(10, 100, 300, 30,17)
            disfontch(20, "自己设置精简（!! 先看详情 !!）", 20, 100)
            drect(0, SCREEN_H-200, SCREEN_W,300, 12)
            if self.sccsim==1:
                disfontch(20,"成功精简",5,SCREEN_H-195)
            elif self.sccsim==2:
                disfontch(20, "未成功精简，错误模块：", 5, SCREEN_H - 195)
                for i in range(len(nsList)):
                    if i<=4:
                        disfontch(14, self.pList[nsList[i]][0], 5, SCREEN_H - 195+16*i)
                    if i<=9:
                        disfontch(14, self.pList[nsList[i]][0], SCREEN_W//2+5, SCREEN_H - 195+16*i)
            drect(10, 140, 300, 30, 17)
            disfontch(20, "精简内容详情", 20, 140)
            drect(10, 180, 300, 30, 17)
            disfontch(20, "关于Better Thunder", 20, 180)
        if self.window==1:
            drect(10, 60, 100, 30, 17)
            disfontch(20, "<-返回", 20, 60)
            disfontch(20, "操作可能略有延迟", 230, 60)
            drect(120, 60, 100, 30, 17)
            disfontch(20, "点我精简", 130, 60)
            for i in range(len(self.pList)):
                disfonten(15,self.pList[i][0], 10, 80+26*(i+1))
                drect(160, 80 + 26 * (i + 1),80,20,12)
                if self.usrpList[i]:
                    disfontch(15,"关闭", 185, 80 + 26 * (i + 1))
                else:
                    disfontch(15,"需要", 185, 80 + 26 * (i + 1))
        if self.window==2:
            drect(10, 60, 100, 30, 17)
            disfontch(20, "<-返回", 20, 60)
            disfontch(20, "Better Thunder 是基于Pygame开发的一", 10, 100)
            disfontch(20, """个"破解"迅雷的应用（小软件），你可以""", 10, 130)
            disfontch(20, "在这里面选择你想要删除的迅雷模块，比", 10, 160)
            disfontch(20, "如：广告模块（advertising.xlplugin），", 10, 190)
            disfontch(20, "我提供了图形界面，方便快捷。", 10, 220)
            disfontch(20, "! 注意 !", 10, 260, 1)
            disfontch(20, "本软件为Mac用户设计，Windows用户请", 10, 290)
            disfontch(20, "自行百度：迅雷破解版", 10, 320)
            disfontch(20, "! 声明 !", 10, 360, 1)
            disfontch(20, "本软件仅用于学习研究使用, 请于下载后24", 10, 390)
            disfontch(20, "小时内自行删除", 10, 420)

#----main----
pygame.init()
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
pygame.display.set_icon(ICON)
pygame.display.set_caption("Better Thunder")
clock=pygame.time.Clock()
BT=better_thunder()
while 1:
    BT.draw()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if 10 <= mx <= 310 and 60 <= my < 90 and BT.window==0:
                nsList=[]
                c=0
                for i in BT.pList:
                    if BT.pFlag[c]:
                        tmp = os.system('rm -rf //Applications//Thunder.app//Contents//PlugIns//'+i[0]+'.xlplugin')
                        if tmp:
                            nsList.append(i[0])
                    c+=1
                if nsList==[]:
                    BT.sccsim=1
                else:
                    BT.sccsim=2
            if 10 <= mx <= 310 and 100 <= my < 130 and BT.window == 0:
                BT.window=1
            if 10 <= mx <= 310 and 140 <= my < 170 and BT.window == 0:
                os.system("open /Users/xzh/Desktop/better_thunder/Details.txt")
            if 10 <= mx <= 310 and 180 <= my < 210 and BT.window == 0:
                BT.window=2
            if 10 <= mx <= 110 and 60 <= my < 90 and BT.window != 0:
                BT.window=0
            if 160 <= mx <= 240 and 80+26 <= my < 100 + 26 * (len(BT.pList) + 1) and BT.window == 1:
                for i in range(len(BT.pList)):
                    if 160 <= mx <= 240 and  80 + 26 * (i + 1)<= my < 100 + 26 * (i + 1) and BT.window == 1:
                        if BT.usrpList[i]==1:
                            BT.usrpList[i]=0
                        else:
                            BT.usrpList[i]=1
            if 120 <= mx <= 220 and 60 <= my < 90 and BT.window == 1:
                nsList = []
                c = 0
                for i in BT.pList:
                    if not BT.usrpList[c]:
                        tmp = os.system('rm -rf //Applications//Thunder.app//Contents//PlugIns//' + i[0] + '.xlplugin')
                        if tmp:
                            nsList.append(i[0])
                    c += 1
                if nsList == []:
                    BT.sccsim = 1
                else:
                    BT.sccsim = 2
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    # time.sleep(0)