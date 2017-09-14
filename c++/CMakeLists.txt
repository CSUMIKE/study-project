cmake_minimum_required(VERSION 2.8)
 
PROJECT(Visualize)
 
find_package(VTK REQUIRED)
include(${VTK_USE_FILE})
 
add_executable(Visualize MACOSX_BUNDLE main.cxx)
 
if(VTK_LIBRARIES)
  target_link_libraries(Visualize ${VTK_LIBRARIES})
else()
  target_link_libraries(Visualize vtkHybrid vtkWidgets)
endif()