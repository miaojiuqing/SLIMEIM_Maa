@echo off
setlocal enabledelayedexpansion
cd /d "D:\vscode\SLIMEIM_Maa\assets\resource\pipeline"
for /r %%f in (*.jsonc) do (
    ren "%%f" "%%~nf.json"
)
echo Files renamed successfully.
pause
