# lhcx_auto_daily
灵魂潮汐日常自动化脚本，不包括深渊，每日五个事件，公会对战等
## 注意
- 需要主页设置live2D，相伴界面设置初始背景。
- 需要自行更改bat文件中的conda路径，conda环境名称，项目所在目录绝对路径。

## 使用教程
1. 使用anaconda创建新的环境，默认为autogui。

```bash
conda create -n autogui python=3.9
```

2. 切换到项目目录，安装需要的包。

```bash
cd the/place/to/lhcx_auto_daily
pip install -r requirements.txt
```

3. 更改bat文件的conda路径，conda环境名称，项目所在目录绝对路径。

4. 以管理员权限运行bat文件。

5. （可选）给bat文件创建快捷方式，放到方便的地方双击运行，并调节成必须管理员权限，可选择项目中的icon作图标。