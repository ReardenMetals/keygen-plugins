@ECHO OFF
setlocal

set KEYGEN_CORE=..\keygen-core-0.2.0\
set PYTHONPATH=%KEYGEN_CORE%;%PYTHONPATH%

echo KEYGEN_CORE = %KEYGEN_CORE%
echo PYTHONPATH = %PYTHONPATH%

python main.py
endlocal
pause