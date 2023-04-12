from source.manager import img_manager, posi_manager
from source.util import *
from source.manager.img_manager import LOG_WHEN_TRUE, LOG_ALL, LOG_NONE, LOG_WHEN_FALSE, ImgIcon
from path_lib import ASSETS_IMG, ASSETS_COMMON_IMG
from source.manager.button_manager import Button
from source.manager.text_manager import TextTemplate
from source.manager.posi_manager import PosiTemplate

# import scene_manager

LEAVINGIN = TextTemplate(text={'zh_CN': '自动退出',"en_US": 'Leaving in'}, cap_area = f"{ASSETS_IMG}\\common\\area\\LEAVINGIN.jpg")
claim_rewards = TextTemplate(text={'zh_CN': '领取奖励',"en_US": "Claim Rewards"})
use_20x2resin = TextTemplate(text=
{
    'zh_CN': '使用浓缩树脂',
    "en_US": "Use Condensed Resin"
})
use_20resin = TextTemplate(text=
{
    'zh_CN': '使用原粹树脂',
    "en_US": "Use Original Resin"
})
LEYLINEDISORDER = TextTemplate(text=
{
    'zh_CN': '地脉异常',
    "en_US": "Ley Line Disorder"
}, cap_area = f"{ASSETS_IMG}\\common\\area\\LEYLINEDISORDER.jpg")
conti_challenge = TextTemplate(text=
{
    'zh_CN': '继续挑战',
    "en_US": "Continue Challenge"
})
exit_challenge = TextTemplate(text=
{
    'zh_CN': '退出秘境',
    "en_US": "Leave Domain"
})
domain_obtain = TextTemplate(text=
{
    'zh_CN': '获得',
    "en_US": "Obtained"
})
use_revival_item = TextTemplate(text=
{
    'zh_CN': '使用道具',
    "en_US": "Use revival item"
})
revival = TextTemplate(text=
{
    'zh_CN': '复苏',
    "en_US": "Revive"
})

IconCombatCharacterDied = ImgIcon(win_text = use_revival_item.text, threshold=0.98, print_log=LOG_WHEN_TRUE)
ButtonGeneralAllCharacterDied = Button(threshold=0.988, win_text=revival.text, print_log=LOG_WHEN_TRUE)
ButtonUISwitchToTimeMenu = Button(black_offset = 15, print_log=LOG_WHEN_TRUE)
ButtonGeneralExit = Button(print_log=LOG_WHEN_TRUE)
ButtonUICancel = Button(print_log=LOG_WHEN_TRUE)
IconCombatComingOutBySpace = ImgIcon(bbg_posi=[1379,505,1447,568], cap_posi='bbg', threshold=0.8, print_log=LOG_WHEN_TRUE)
IconUIInDomain = ImgIcon(print_log=LOG_WHEN_TRUE)
ButtonGeneralUseOriginResin = ImgIcon(print_log=LOG_WHEN_TRUE)
ButtonGeneralUseCondensedResin = ImgIcon(print_log=LOG_WHEN_TRUE)
IconGeneralFButton = ImgIcon(bbg_posi=[1104,526 , 1128,550 ], cap_posi=[1079,350 ,1162, 751 ],
                   threshold=0.92, print_log=LOG_WHEN_TRUE)
IconBigmapTeleportWaypoint = ImgIcon()
IconBigmapGodStatue = ImgIcon()
IconBigmapDomain = ImgIcon()
IconGeneralMotionSwimming = ImgIcon(bbg_posi=[1808,968,1872,1016], cap_posi='bbg')# 不能删bbg
IconGeneralMotionClimbing = ImgIcon(bbg_posi=[1706,960,1866,1022], cap_posi='bbg')# 不能删bbg
IconGeneralMotionFlying = ImgIcon(bbg_posi=[1706,960,1866,1022], cap_posi='bbg')# 不能删bbg
IconUIEmergencyFood = ImgIcon(print_log=LOG_WHEN_TRUE, threshold=0.98)
IconUIBigmap = ImgIcon(cap_posi=[1300,36,1750, 59 ], print_log=LOG_WHEN_TRUE, threshold=0.95, offset=10)
IconUIEscMenu = ImgIcon(print_log=LOG_WHEN_TRUE, threshold=0.97)
ButtonUISwitchToTimeMenu = ImgIcon(print_log=LOG_WHEN_TRUE)
IconUITimeMenuCore = ImgIcon(print_log=LOG_WHEN_TRUE, threshold=0.89)
BigmapChooseArea = PosiTemplate()
ButtonBigmapTP = ImgIcon()
ButtonDomainStartChallenge = Button(print_log=LOG_WHEN_TRUE, threshold=0.98)
AreaDomainSwitchChallenge = PosiTemplate()
ButtonDomainSoloChallenge = Button(print_log=LOG_WHEN_TRUE, threshold=0.98)
character_q_skills = PosiTemplate(img_path=fr"{ASSETS_PATH}/imgs/Windows/Combat/common/AreaCombatQ1")
character_q_skills.add_posi(img_path=fr"{ASSETS_PATH}/imgs/Windows/Combat/common/AreaCombatQ2")
character_q_skills.add_posi(img_path=fr"{ASSETS_PATH}/imgs/Windows/Combat/common/AreaCombatQ3")
character_q_skills.add_posi(img_path=fr"{ASSETS_PATH}/imgs/Windows/Combat/common/AreaCombatQ4")
ButtonFoodEgg = Button(cap_posi='all', is_bbg = False)
ButtonGeneralConfirm = Button(cap_posi='all', is_bbg = False)
AreaCombatRevivalFoods = PosiTemplate()
ButtonBigmapSwitchDomainModeOn = Button(threshold=0.97)
ButtonBigmapSwitchDomainModeOff = Button(threshold=0.97)
AreaBigmapSwitchMap = PosiTemplate()
ButtonBigmapSwitchMap = Button()
IconBigMapScaling = ImgIcon(threshold=0.98, print_log = LOG_ALL, offset=0)
ButtonBigmapCloseMarkTableInTP = Button()
AreaCombatBloodBar = PosiTemplate()
AreaCombatCharacterName1 = PosiTemplate()
AreaCombatCharacterName2 = PosiTemplate()
AreaCombatCharacterName3 = PosiTemplate()
AreaCombatCharacterName4 = PosiTemplate()
AreaCombatTeamCharactersName = PosiTemplate()
ButtonUIEnterPartySetup = Button()
CombatButtonGoToFight = Button()
ButtonCombatSwitchTeamLeft = Button(threshold=0)
ButtonCombatSwitchTeamRight = Button(threshold=0)
IconUIPartySetup = ImgIcon(threshold=0.96)
AreaCombatPartySetupCharaName1=posi_manager.PosiTemplate()
AreaCombatPartySetupCharaName2=posi_manager.PosiTemplate()
AreaCombatPartySetupCharaName3=posi_manager.PosiTemplate()
AreaCombatPartySetupCharaName4=posi_manager.PosiTemplate()
IconBigmapCommission = ImgIcon(is_bbg=False)
AreaBigmapSidebarCommissionName = PosiTemplate()
IconBigmapSidebarIsCommissionExist = ImgIcon(threshold=0.97)
IconCommissionCommissionIcon = ImgIcon()
IconCommissionInCommission = ImgIcon(is_bbg=False)
AreaClaimRewardAvailableReward = PosiTemplate()

QTSX = TextTemplate(text=
{
    "zh_CN":"七天神像",
    "en_US":"Statues of The Seven"
}, cap_area = BigmapChooseArea.position)
CSMD = TextTemplate(text=
{
    "zh_CN":"传送锚点",
    "en_US": "Teleport Waypoint"
}, cap_area = BigmapChooseArea.position)
ASmallStepForHilichurls = TextTemplate(text={"zh_CN":"丘丘人的一小步", "en_US": "A small step for hilichurls"})
IncreasingDanger = TextTemplate(text={"zh_CN":"攀高危险", "en_US": "Increasing danger"})
Emergency = TextTemplate(text={"zh_CN":"临危受命", "en_US": "Emergency"})
IcyIssues = TextTemplate(text={"zh_CN":"冷冰冰的大麻烦", "en_US": "Icy Issues"})
ForTheHarbingers = TextTemplate(text={"zh_CN":"为了执行官大人", "en_US": "For The Harbingers"})
BigIceColdCrisis = TextTemplate(text={"zh_CN":"冰凉凉的大团危机", "en_US": "Big Ice-Cold Crisis"})
SpreadingEvil = TextTemplate(text={"zh_CN":"邪恶的扩张", "en_US": "Spreading Evil"})
BigPudgyProblem = TextTemplate(text={"zh_CN":"圆滚滚的大团骚乱", "en_US": "Big Pudgy Problem"})
PudgyPyrotechnicians = TextTemplate(text={"zh_CN":"圆滚滚的易爆品", "en_US": "Pudgy Pyrotechnicians"})
MapAreaMD = TextTemplate(text={
    "zh_CN":"蒙德"
}, cap_area = AreaBigmapSwitchMap.position)
MapAreaLY = TextTemplate(text={
    "zh_CN":"璃月"
}, cap_area = AreaBigmapSwitchMap.position)
MapAreaDQ = TextTemplate(text={
    "zh_CN":"稻妻"
}, cap_area = AreaBigmapSwitchMap.position)
MapAreaXM = TextTemplate(text={
    "zh_CN":"须弥"
}, cap_area = AreaBigmapSwitchMap.position)
MapAreaCYJY = TextTemplate(text={
    "zh_CN":"层岩巨渊"
}, cap_area = AreaBigmapSwitchMap.position)

if __name__ == '__main__':
    ButtonUIEnterPartySetup.show_image()