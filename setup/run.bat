@echo off
echo   ------------------------------------------------
echo   *                                              *
echo   *     PUREMSOUND PYTHON PACKAGES INSTALLER     *                              
echo   *                                              *
echo   ------------------------------------------------
echo,
echo,
echo * python version must be like 35 or 36 or ... not 3.5,3.6 ....
echo,

set /p user="Enter pc user name: "
set /p python_version="Enter python version: "

echo user name = %user%
echo python version = %python_version%
echo installing required python packages

set "python=C:\Users\%user%\AppData\Local\Programs\Python\Python%python_version%\python.exe"
"%python%" setup.py

pause