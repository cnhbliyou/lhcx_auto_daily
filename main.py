import pyautogui
import subprocess
import cv2
import numpy as np
import time


# 获取当前脚本所在目录的路径
# script_dir = sys.path.dirname(os.path.abspath(__file__))

def find_image_on_screen(image_path, threshold=0.8):
    # 获取整个屏幕截图
    try:
        screenshot = pyautogui.screenshot()
    except Exception as e:
        return None
    # 将截图转换为OpenCV格式
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # # 保存屏幕截图
    # cv2.imwrite('screenshot.png', screenshot_cv)

    # 读取要搜索的图像
    image_to_find = cv2.imread(image_path)

    # 读取屏幕截图
    # screenshot = cv2.imread('screenshot.png')

    # 使用cv2.matchTemplate进行图像匹配
    result = cv2.matchTemplate(screenshot, image_to_find, cv2.TM_CCOEFF_NORMED)

    # 获取匹配结果的位置
    locations = np.where(result >= threshold)

    if len(locations[0]) > 0:
        # 返回找到的坐标
        return (locations[1][0], locations[0][0])
    else:
        # 返回None表示未找到
        return None


def click_target(image_path, annotation, times_limit=10):
    app_start_match_location = find_image_on_screen(image_path)
    start = 0
    while app_start_match_location == None and start < times_limit:
        print(annotation)
        time.sleep(1)
        start += 1
        app_start_match_location = find_image_on_screen(image_path)
    if start >= times_limit:
        print('未找到图标, 可能已经进行过, 开始下一项任务')
        return False
    x, y = app_start_match_location

    pyautogui.click(x, y)
    return True


def main():
    android_program_path = 'C:\\Program Files\\BlueStacks_nxt_cn\\HD-Player.exe'

    try:
        # 使用subprocess.run启动程序
        process = subprocess.Popen(android_program_path, shell=True)
        # process.wait()
        # 或者使用subprocess.Popen启动程序并获取进程对象
        # process = subprocess.Popen(program_path, shell=True)
    except Exception as e:
        print(f"启动程序时出错：{e}")

    time.sleep(5)

    click_target('images\\lhcx_start.png', '寻找启动图标中......')

    time.sleep(8)
    click_target('images\\lhcx_gonggao_quedin.png', '寻找确认公告图标中......')
    click_target('images\\lhcx_jinruyouxi.png', '寻找进入游戏图标中......')
    qiandao_ok = click_target('images\\lhcx_qiandao.png', '寻找签到图标中......', 5)
    if qiandao_ok:
        click_target('images\\lhcx_kongbaiquyu.png', '寻找空白区域图标中......', 5)
        click_target('images\\lhcx_qiandao7tian.png', '寻找签到7天领取水晶图标中......', 5)
        click_target('images\\lhcx_kongbaiquyu.png', '寻找空白区域图标中......')
        click_target('images\\lhcx_qiandaoguanbi.png', '寻找关闭签到图标中......')
    click_target('images\\lhcx_gonggaoguanbi.png', '寻找关闭公告图标中......')
    click_target('images\\lhcx_huodong.png', '寻找活动图标中......')
    click_target('images\\lhcx_wucan.png', '寻找午餐体力图标中......', 5)
    click_target('images\\lhcx_wucan.png', '寻找晚餐体力图标中......', 5)
    click_target('images\\lhcx_huodong_tuichu.png', '寻找活动退出图标中......', 5)
    click_target('images\\lhcx_jiayuan.png', '寻找家园图标中......')
    click_target('images\\lhcx_jiayuan_zonglan.png', '寻找家园总览图标中......')
    lingqu_ok = click_target('images\\lhcx_jiayuan_lingqu.png', '寻找家园领取图标中......', 5)
    if lingqu_ok:
        click_target('images\\lhcx_kongbaiquyu.png', '寻找空白区域图标中......')
    lingqu_ok = click_target('images\\lhcx_jiayuan_lingqu.png', '寻找家园领取图标中......', 5)
    if lingqu_ok:
        click_target('images\\lhcx_kongbaiquyu.png', '寻找空白区域图标中......')
    lingqu_ok = click_target('images\\lhcx_jiayuan_lingqu.png', '寻找家园领取图标中......', 5)
    if lingqu_ok:
        click_target('images\\lhcx_kongbaiquyu.png', '寻找空白区域图标中......')
    click_target('images\\lhcx_zhongzhi.png', '寻找种植图标中......')
    for i in range(8):
        click_target('images\\lhcx_zhongzhi_zhongzi.png', '寻找种子图标中......')
        click_target('images\\lhcx_zhongzhi_zhongzhi.png', '寻找种植图标中......', 5)
    click_target('images\\lhcx_zhongzhi_tuichu.png', '寻找种植退出图标中......')
    time.sleep(1)
    click_target('images\\lhcx_jiayuan_zonglan.png', '寻找家园总览图标中......')
    time.sleep(1)
    click_target('images\\lhcx_jiayuan_shiwu.png', '寻找事务板图标中......')
    time.sleep(1)

    click_target('images\\lhcx_jiayuan_shiwu_yijian.png', '寻找一键派遣中......')
    click_target('images\\lhcx_jiayuan_shiwu_tuichu.png', '寻找退出事务板图标中......')
    # click_target('lhcx_jiayuan_baifang.png', '寻找拜访图标中......')
    # click_target('lhcx_jiayuan_baifang_baifang.png', '寻找拜访好友图标中......')

    # baoxiang_number = 0
    # while baoxiang_number < 5:
    #     baoxiang_ok = click_target('lhcx_jiayuan_baifang_baoxiang.png', '寻找宝箱图标中......', 5)
    #     if baoxiang_ok:
    #         baoxiang_number += 1
    #         click_target('lhcx_kongbaiquyu.png', '寻找空白区域图标中......')
    #     else:
    #         baoxiang_ok = click_target('lhcx_jiayuan_baifang_xiayige.png', '寻找下一个好友图标中......', 10)
    #         time.sleep(5)
    click_target('images\\lhcx_jiayuan_tuichu.png', '寻找退出家园图标中......')

    click_target('images\\lhcx_xiangban.png', '寻找相伴图标中......')
    for i in range(5):
        click_target('images\\lhcx_xiangban_motou.png', '寻找摸头图标中......')
        time.sleep(3)
        click_target('images\\lhcx_xiangban_xiayige.png', '寻找下一个图标中......')
    time.sleep(1)
    click_target('images\\lhcx_xiangban_liwu.png', '寻找礼物图标中......')
    songli_ok = click_target('images\\lhcx_xiangban_songli.png', '寻找送礼图标中......', 5)
    if songli_ok:
        click_target('images\\lhcx_xiangban_zengsong.png', '寻找赠送图标中......')
        time.sleep(1)
        if find_image_on_screen('images\\lhcx_xiangban_songli_tishi.png') != None:
            time.sleep(1)
            click_target('images\\lhcx_xiangban_songli_tishi.png', '寻找赠送礼物图标中......')
            time.sleep(1)
    click_target('images\\lhcx_xiangban_tuichu.png', '寻找相伴退出图标中......')

    click_target('images\\lhcx_shangcheng.png', '寻找商城图标中......')
    time.sleep(1)
    click_target('images\\lhcx_shangcheng_shangdian.png', '寻找商店图标中......')
    time.sleep(1)
    click_target('images\\lhcx_shangcheng_shangdian_bujilibao.png', '寻找补给礼包图标中......')
    time.sleep(1)
    click_target('images\\lhcx_shangcheng_shangdian_bujilibao_mianfei.png', '寻找礼包图标中......')
    queren_ok = click_target('images\\lhcx_shangcheng_shangdian_bujilibao_mianfei_queren.png', '寻找确认图标中......', 5)
    if queren_ok:
        click_target('images\\lhcx_kongbaiquyu.png', '寻找空白区域图标中......')
    click_target('images\\lhcx_shangcheng_tuichu.png', '寻找商城退出图标中......')
    time.sleep(1)

    click_target('images\\lhcx_tansuo.png', '寻找探索图标中......')
    time.sleep(1)
    click_target('images\\lhcx_tansuo_shilian.png', '寻找试炼图标中......')
    time.sleep(1)
    click_target('images\\lhcx_tansuo_shilian_jinbi.png', '寻找金币本图标中......')
    time.sleep(1)
    click_target('images\\lhcx_tansuo_shilian_jinbi_saodang.png', '寻找扫荡图标中......')
    time.sleep(1)
    zuida_ok = click_target('images\\lhcx_tansuo_shilian_jinbi_saodang_zuida.png', '寻找最大体力图标中......', 5)
    time.sleep(1)
    if zuida_ok:
        click_target('images\\lhcx_tansuo_shilian_jinbi_saodang_quedin.png', '寻找确定图标中......')
        time.sleep(1)
        click_target('images\\lhcx_jixu.png', '寻找继续图标中......')
        time.sleep(1)
    click_target('images\\lhcx_shangcheng_tuichu.png', '寻找返回图标中......')
    time.sleep(1)
    click_target('images\\lhcx_shangcheng_tuichu.png', '寻找返回图标中......')
    time.sleep(1)

    click_target('images\\lhcx_chouka.png', '寻找抽卡图标中......', 5)
    time.sleep(1)
    click_target('images\\lhcx_chouka_meiri.png', '寻找每日抽卡图标中......', 5)
    time.sleep(1)
    click_target('images\\lhcx_chouka_meiri_kaishi.png', '寻找抽卡一次图标中......', 5)
    time.sleep(1)
    queren_ok = click_target('images\\lhcx_chouka_meiri_kaishi_queren.png', '寻找抽卡确认图标中......', 5)
    time.sleep(1)
    if queren_ok:
        pass
    else:
        queren_ok = click_target('images\\lhcx_chouka_meiri_duihuan.png', '寻找兑换图标中......', 5)
        time.sleep(1)
        click_target('images\\lhcx_kongbaiquyu.png', '寻找空白区域图标中......', 5)
        time.sleep(1)
    click_target('images\\lhcx_chouka_meiri_tiaoguo.png', '寻找跳过图标中......', 5)
    time.sleep(1)
    click_target('images\\lhcx_chouka_meiri_wancheng.png', '寻找离开图标中......', 5)
    time.sleep(1)
    click_target('images\\lhcx_renwu_fanhui.png', '寻找返回图标中......')
    time.sleep(1)

    tongxingzheng_ok = click_target('images\\lhcx_tongxingzheng.png', '寻找通行证图标中......', 5)
    time.sleep(1)
    if tongxingzheng_ok:
        click_target('images\\lhcx_tongxingzheng_yijian.png', '寻找一键领取图标中......', 5)
        time.sleep(1)
        click_target('images\\lhcx_kongbaiquyu.png', '寻找空白区域图标中......', 5)
        time.sleep(1)
        click_target('images\\lhcx_shangcheng_tuichu.png', '寻找返回图标中......', 5)
        time.sleep(1)

    click_target('images\\lhcx_renwu.png', '寻找任务图标中......', 5)
    click_target('images\\lhcx_renwu_yijian.png', '寻找一键图标中......', 5)
    time.sleep(1)
    click_target('images\\lhcx_renwu_yijian.png', '寻找一键图标中......', 5)
    time.sleep(1)
    click_target('images\\lhcx_kongbaiquyu.png', '寻找空白区域图标中......', 5)
    time.sleep(1)
    click_target('images\\lhcx_renwu_zhouchang.png', '寻找周常图标中......')
    time.sleep(1)
    click_target('images\\lhcx_renwu_yijian.png', '寻找一键图标中......', 5)
    time.sleep(1)
    click_target('images\\lhcx_renwu_yijian.png', '寻找一键图标中......', 5)
    time.sleep(1)
    click_target('images\\lhcx_kongbaiquyu.png', '寻找空白区域图标中......', 5)
    time.sleep(1)
    click_target('images\\lhcx_renwu_fanhui.png', '寻找返回图标中......')
    time.sleep(1)

    click_target('images\\lhcx_gonghui.png', '寻找公会图标中......')
    time.sleep(1)
    meiri_ok = click_target('images\\lhcx_gonghui_meiri.png', '寻找每日图标中......', 5)
    time.sleep(1)
    if meiri_ok:
        click_target('images\\lhcx_kongbaiquyu.png', '寻找空白区域图标中......')
        time.sleep(1)
    click_target('images\\lhcx_gonghui_xuanshang.png', '寻找悬赏图标中......')
    time.sleep(1)
    lingqu_ok = click_target('images\\lhcx_gonghui_xuanshang_lingqu.png', '寻找领取图标中......', 5)
    time.sleep(1)
    if lingqu_ok:
        click_target('images\\lhcx_kongbaiquyu.png', '寻找空白区域图标中......')
        time.sleep(1)
    click_target('images\\lhcx_renwu_fanhui.png', '寻找返回图标中......')
    time.sleep(1)
    click_target('images\\lhcx_gonghui_renwu.png', '寻找任务图标中......')
    time.sleep(1)
    click_target('images\\lhcx_gonghui_renwu_yijian.png', '寻找一键图标中......', 5)
    time.sleep(1)
    click_target('images\\lhcx_kongbaiquyu.png', '寻找空白区域图标中......', 5)
    time.sleep(1)
    click_target('images\\lhcx_gonghui_renwu_yijian.png', '寻找一键图标中......', 5)
    time.sleep(1)
    click_target('images\\lhcx_kongbaiquyu.png', '寻找空白区域图标中......', 5)
    time.sleep(1)
    click_target('images\\lhcx_gonghui_renwu_tuichu.png', '寻找退出图标中......')
    time.sleep(1)
    click_target('images\\lhcx_renwu_fanhui.png', '寻找返回图标中......')
    time.sleep(1)

    print('结束')
    time.sleep(10)


if __name__ == '__main__':
    main()
