#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "MaaFramework::MaaUtils" for configuration "RelWithDebInfo"
set_property(TARGET MaaFramework::MaaUtils APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(MaaFramework::MaaUtils PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELWITHDEBINFO "opencv_core;opencv_imgproc;opencv_imgcodecs"
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/bin/MaaUtils.dll"
  )

list(APPEND _cmake_import_check_targets MaaFramework::MaaUtils )
list(APPEND _cmake_import_check_files_for_MaaFramework::MaaUtils "${_IMPORT_PREFIX}/bin/MaaUtils.dll" )

# Import target "MaaFramework::MaaFramework" for configuration "RelWithDebInfo"
set_property(TARGET MaaFramework::MaaFramework APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(MaaFramework::MaaFramework PROPERTIES
  IMPORTED_IMPLIB_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/MaaFramework.lib"
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELWITHDEBINFO "MaaFramework::MaaUtils;opencv_core;opencv_imgproc;opencv_imgcodecs;fastdeploy_ppocr;ONNXRuntime::ONNXRuntime"
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/bin/MaaFramework.dll"
  )

list(APPEND _cmake_import_check_targets MaaFramework::MaaFramework )
list(APPEND _cmake_import_check_files_for_MaaFramework::MaaFramework "${_IMPORT_PREFIX}/lib/MaaFramework.lib" "${_IMPORT_PREFIX}/bin/MaaFramework.dll" )

# Import target "MaaFramework::MaaToolkit" for configuration "RelWithDebInfo"
set_property(TARGET MaaFramework::MaaToolkit APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(MaaFramework::MaaToolkit PROPERTIES
  IMPORTED_IMPLIB_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/MaaToolkit.lib"
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELWITHDEBINFO "MaaFramework::MaaUtils;opencv_core;opencv_imgproc;opencv_imgcodecs"
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/bin/MaaToolkit.dll"
  )

list(APPEND _cmake_import_check_targets MaaFramework::MaaToolkit )
list(APPEND _cmake_import_check_files_for_MaaFramework::MaaToolkit "${_IMPORT_PREFIX}/lib/MaaToolkit.lib" "${_IMPORT_PREFIX}/bin/MaaToolkit.dll" )

# Import target "MaaFramework::MaaAgentClient" for configuration "RelWithDebInfo"
set_property(TARGET MaaFramework::MaaAgentClient APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(MaaFramework::MaaAgentClient PROPERTIES
  IMPORTED_IMPLIB_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/MaaAgentClient.lib"
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELWITHDEBINFO "opencv_core;opencv_imgproc;opencv_imgcodecs;MaaFramework::MaaUtils;MaaFramework::MaaFramework"
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/bin/MaaAgentClient.dll"
  )

list(APPEND _cmake_import_check_targets MaaFramework::MaaAgentClient )
list(APPEND _cmake_import_check_files_for_MaaFramework::MaaAgentClient "${_IMPORT_PREFIX}/lib/MaaAgentClient.lib" "${_IMPORT_PREFIX}/bin/MaaAgentClient.dll" )

# Import target "MaaFramework::MaaFrameworkModule" for configuration "RelWithDebInfo"
set_property(TARGET MaaFramework::MaaFrameworkModule APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(MaaFramework::MaaFrameworkModule PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELWITHDEBINFO "CXX"
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/MaaFrameworkModule.lib"
  )

list(APPEND _cmake_import_check_targets MaaFramework::MaaFrameworkModule )
list(APPEND _cmake_import_check_files_for_MaaFramework::MaaFrameworkModule "${_IMPORT_PREFIX}/lib/MaaFrameworkModule.lib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
