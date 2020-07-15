::assimp lib
@set stage="assimp"
@mkdir .\assimp\build
cd .\assimp\build

cmake -T host=x64  .. 1>log.log
@if %errorlevel% neq 0 goto err

cmake --build . --parallel 12 --config Release --target assimp 1>log.log
@if %errorlevel% neq 0 goto err
@copy .\bin\Release\*.dll ..\..\lib\Release
@copy .\lib\Release\*.lib ..\..\lib\Release

cmake --build . --parallel 12 --config Debug  --target assimp 1>log.log
@if %errorlevel% neq 0 goto err
@copy .\bin\Debug\*.dll ..\..\lib\Debug
@copy .\lib\Debug\*.lib ..\..\lib\Debug


::imgui lib
@set stage="imgui"
cd ../../
@mkdir .\imgui\build
cd ./imgui/build
::cl /I:../ /O2 /D WIN32 /D _DEBUG /D _UNICODE /D UNICODE /Z7 /GS- imgui.cpp imgui_demo.cpp imgui_draw.cpp imgui_widgets.cpp

:err
@echo.  build 3rd err!  %stage% check log.log
exit -1