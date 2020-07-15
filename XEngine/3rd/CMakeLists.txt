#header
include_directories(assimp/include/)
include_directories(imgui/)

file(GLOB_RECURSE assimp_headers  assimp/include/*.h assimp/include/*.hpp)
source_group("Include" FILES ${assimp_headers})

file(GLOB imgui_headers  imgui/*.h imgui/*.hpp)
source_group("include/imgui" FILES ${imgui_headers})

set_property(GLOBAL PROPERTY 3RD_HEADS ${assimp_headers}  ${imgui_headers})


#lib
file(GLOB_RECURSE CURRENT_LIBS  lib/release/*.lib lib/release/*.a lib/release/*.so)
set(libs)
foreach(v ${CURRENT_LIBS})
	string(REGEX MATCH "lib/release/.*" relative_path ${v})
	string(REGEX REPLACE ".*lib/release/" "" target_name ${relative_path})
	list(APPEND libs ${target_name})
endforeach()

string(REGEX REPLACE "\;" " " target_ls "${libs}")
set_property(GLOBAL PROPERTY 3RD_LIBS ${target_ls})

#get_property(HEADERS_LIST GLOBAL PROPERTY "3RD_LIBS" )
#message(STATUS "${HEADERS_LIST}")