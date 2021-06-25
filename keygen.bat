@ECHO OFF
setlocal

set KEYGEN_CORE=..\keygen-core\
set PYTHONPATH=%KEYGEN_CORE%;%UI_DEPENDENCIES%;%PYTHONPATH%

echo KEYGEN_CORE = %KEYGEN_CORE%
echo PYTHONPATH = %PYTHONPATH%

python main.py
endlocal
pause