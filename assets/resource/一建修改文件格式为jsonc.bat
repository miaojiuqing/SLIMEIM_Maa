@echo off
setlocal enabledelayedexpansion
cd /d "D:\vscode\SLIMEIM_Maa\assets\resource\pipeline"
for /r %%f in (*.json) do (
    ren "%%f" "%%~nf.jsonc"
)
echo Files renamed successfully.
pause
