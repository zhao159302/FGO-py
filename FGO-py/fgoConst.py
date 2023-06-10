VERSION='v18.3.0'
CONFIG={
'runOnce':'',
'device':'',
'teamIndex':0,
'farming':False,
'stopOnDefeated':True,
'stopOnKizunaReisou':True,
'stayOnTop':False,
'closeToTray':False,
'notifyEnable':False,
'notifyParam':[],
}
# F1-F10        选取编队
# 12345         选卡,234指向技能的目标,铜银苹果
# 678           宝具卡,选取剧情选项,8选取第一个关卡
# 9             下一个挖掘池
# QWER          御主技能,W剧情选项/金苹果
# TYUIOP        换人礼装
# <BackSpace>   跳过/商店
# =             无响应区域
# ASDFGHJKL     从者技能,F取消,K确认/铜苹果
# ;             刷新助战列表
# \\            下一个无限池
# Z             确认换人/关闭
# X             对战结束时不发送好友申请
# C             战败撤退
# V             下拉苹果列表
# N             补充体力
# M             再次进行十连召唤
# ,.            左右
# <Space>       选卡/下一步/菜单
# NUM4-9        选取敌人,NUM7返回/关闭
KEYMAP={
'\x70':(527,47),'\x71':(552,49),'\x72':(577,49),'\x73':(602,49),'\x74':(627,49),'\x75':(652,49),'\x76':(677,49),'\x77':(702,49),'\x78':(727,49),'\x79':(752,49), # VK_F1..10
'1':(185,440),'2':(399,440),'3':(649,440),'4':(875,440),'5':(1101,440),'6':(431,203),'7':(651,203),'8':(845,203),'9':(1068,203),'\xBB':(876,46),'\x08':(1253,46), # = VK_OEM_PLUS VK_BACK
'Q':(1200,317),'W':(907,317),'E':(995,317),'R':(1084,317),'T':(140,360),'Y':(340,360),'U':(540,360),'I':(740,360),'O':(940,360),'P':(1140,360),'\xDC':(1213,245), # \ VK_OEM_5
'A':(73,573),'S':(163,573),'D':(257,573),'F':(388,573),'G':(483,573),'H':(574,573),'J':(704,573),'K':(801,573),'L':(891,573),'\xBA':(927,131), # ; VK_OEM_1
'Z':(640,629),'X':(173,621),'C':(330,320),'V':(1014,500),'N':(165,694),'M':(800,667),'\xBC':(45,360),'\xBE':(1235,360), # , VK_OEM_COMMA . VK_OEM_PERIOD
'\x1B':(40,40),' ':(1231,687), # VK_ESCAPE
'\x64':(45,142),'\x65':(295,142),'\x66':(545,142),'\x67':(142,40),'\x68':(342,40),'\x69':(542,40), # VK_NUMPAD4..9
}
PACKAGE_TO_REGION={
'com.bilibili.fatego':'CN',
'com.aniplex.fategrandorder':'JP',
'com.aniplex.fategrandorder.en':'NA',
'com.aniplex.fategrandorder.tw':'TW',
'com.aniplex.fategrandorder.kr':'KR',
}