@echo off

REM arg 1- folder z plikami wejsciowymi, arg 2- folder docelowy
REM utworzyc foldery backup i output
if not exist "%2\backup\" (
	mkdir "%2\backup"
)

if not exist "%2\output\" (
	mkdir "%2\output"
)

REM pobrac obecna date i czas
set "d=%date:~-4%%date:~3,2%%date:~0,2%%time:~0,2%%time:~3,2%%time:~6,2%"
set /A "n=0"

SETLOCAL EnableDelayedExpansion 

REM dla wszystkich plikow wejsciowych .txt utworzyc backup i wykonac rozklad
if exist "%1\" (
	cd /D "%~dp0"
	type nul>"%2\report_%d%.txt"
	for %%i in ("%1\*.txt") do (
		set /A "n+=1"
		py "backup.py" "%%i" "%2\backup" "!d!"
		py "fib_decomp.py" "%%i" "%2\output\out_!d!_!n!.txt" "%2\report_!d!.txt"
	)
	REM utworzyc raport
	py "report.py" "%2\report_%d%.txt" "%2"
) else (echo Folder nie istnieje)

echo Zakonczono dzialanie
endlocal
pause