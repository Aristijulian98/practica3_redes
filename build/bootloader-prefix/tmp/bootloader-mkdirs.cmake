# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "C:/Users/JulianAristi/esp-idf/components/bootloader/subproject"
  "C:/Users/JulianAristi/coap_server_julian_aristizabal/build/bootloader"
  "C:/Users/JulianAristi/coap_server_julian_aristizabal/build/bootloader-prefix"
  "C:/Users/JulianAristi/coap_server_julian_aristizabal/build/bootloader-prefix/tmp"
  "C:/Users/JulianAristi/coap_server_julian_aristizabal/build/bootloader-prefix/src/bootloader-stamp"
  "C:/Users/JulianAristi/coap_server_julian_aristizabal/build/bootloader-prefix/src"
  "C:/Users/JulianAristi/coap_server_julian_aristizabal/build/bootloader-prefix/src/bootloader-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "C:/Users/JulianAristi/coap_server_julian_aristizabal/build/bootloader-prefix/src/bootloader-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "C:/Users/JulianAristi/coap_server_julian_aristizabal/build/bootloader-prefix/src/bootloader-stamp${cfgdir}") # cfgdir has leading slash
endif()
