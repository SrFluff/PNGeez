pyinstaller --optimize 2 --noconfirm -w --icon=icon.ico .\pngeez.py
Copy dist\pngeez\pngeez pngeez\
mkdir pngeez\_internal
mkdir pngeez\_internal\pygame
Copy dist\pngeez\_internal\* pngeez\_internal\
Copy dist\pngeez\_internal\pygame\* pngeez\_internal\pygame\
