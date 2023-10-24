@echo on

call C:\ProgramData\Anaconda3\Scripts\conda.exe init

REM 激活 Conda 环境
call conda.bat activate autogui

cd C:\Users\yuuri\OneDrive\Documents\shell\lhcx_auto_daily
REM 运行 Python 脚本
python main.py

REM 退出 Conda 环境
call C:\ProgramData\Anaconda3\Scripts\conda.exe deactivate

pause