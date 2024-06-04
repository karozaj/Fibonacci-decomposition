@echo off
cd /D "%~dp0"

:menu
echo Rozklad Fibonacciego
echo 1. Rozpocznij
echo 2. Zakoncz
set /p option="wybor: "
if %option%==1 goto start
if %option%==2 goto end

:start
set /p l1="sciezka do plikow wejsciowych: "
set /p l2="sciezka docelowa: "
call "fib_decomp.bat" %l1% %l2%
goto menu

:end
pause