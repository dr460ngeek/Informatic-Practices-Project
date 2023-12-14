@echo off

REM Check Windows architecture
set arch=AMD64
IF EXIST "C:\Windows\SysWOW64" set arch=x86

REM Download and install Python
IF "%arch%"=="AMD64" (
  curl -L https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe -o python.exe
  IF EXIST python.exe (
    python.exe /quiet InstallAllUsers
  ) ELSE (
    echo Error downloading Python!
    exit 1
  )
) ELSE (
  curl -L https://www.python.org/ftp/python/3.11.2/python-3.11.2-embed-amd64.exe -o python.exe
  IF EXIST python.exe (
    python.exe /quiet InstallAllUsers
  ) ELSE (
    echo Error downloading Python!
    exit 1
  )
)

REM Install pip and Python libraries
pip install --upgrade pip
pip install matplotlib numpy pandas

REM Verify installations
git --version
python --version
pip list | findstr /i "matplotlib|numpy|pandas"

echo Git, Python, and libraries installed successfully!

pause