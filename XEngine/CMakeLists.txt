CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

OPTION(DEFINE_MACRO "Option description" ON)

project("XEngine")

ADD_SUBDIRECTORY(3rd)
ADD_SUBDIRECTORY(source)

execute_process(COMMAND python ./tools/prebuild.py
    OUTPUT_VARIABLE OUT_MSG
    WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR})

message(STATUS ${OUT_MSG})