######################################################################################################################
#
# JeVois Neuromorphic Embedded Vision Toolkit - Copyright (C) 2016 by Laurent Itti, the University of Southern
# California (USC), and iLab at USC. See http://iLab.usc.edu and http://jevois.org for information about this project.
#
# This file is part of the JeVois Neuromorphic Embedded Vision Toolkit.  This program is free software; you can
# redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software
# Foundation, version 2.  This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
# License for more details.  You should have received a copy of the GNU General Public License along with this program;
# if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# Contact information: Laurent Itti - 3641 Watt Way, HNB-07A - Los Angeles, CA 90089-2520 - USA.
# Tel: +1 213 740 3527 - itti@pollux.usc.edu - http://iLab.usc.edu - http://jevois.org
######################################################################################################################

# CMake configuration variables inherited from compiling the core JeVois library and to be used when compiling modules

set(JEVOIS_VERSION_MAJOR 1)
set(JEVOIS_VERSION_MINOR 5)
set(JEVOIS_VERSION_PATCH 2)
set(JEVOIS_SOVERSION "1.5.2")

set(JEVOIS_SRC_ROOT "")

set(JEVOIS_BUILDROOT_BASE "/lab/itti/jevois/software/jevois-sdk/out/sun8iw5p1/linux/common/buildroot")

set(JEVOIS_HOST_INSTALL_PREFIX "/usr")
set(JEVOIS_PLATFORM_INSTALL_PREFIX "/var/lib/jevois-build/usr")

set(JEVOIS_HOST_ARCH_FLAGS "-msse4 -Ofast")
set(JEVOIS_PLATFORM_ARCH_FLAGS "-mcpu=cortex-a7 -mfpu=neon-vfpv4 -mfloat-abi=hard -ftree-vectorize -Ofast -funsafe-math-optimizations -mfp16-format=ieee")

set(JEVOIS_PLATFORM_C_COMPILER "/lab/itti/jevois/software/jevois-sdk/out/sun8iw5p1/linux/common/buildroot/host/usr/bin/arm-buildroot-linux-gnueabihf-gcc")
set(JEVOIS_PLATFORM_CXX_COMPILER "/lab/itti/jevois/software/jevois-sdk/out/sun8iw5p1/linux/common/buildroot/host/usr/bin/arm-buildroot-linux-gnueabihf-g++")

set(JEVOIS_HOST_CFLAGS "-msse4 -Ofast -W -Wall -Wextra -g -O4 -I/jevois/include -I/usr/share/jevois-opencv-3.3.0/include -I/usr/include/python3.5m -fPIC -Wno-deprecated-declarations")
set(JEVOIS_PLATFORM_CFLAGS "-mcpu=cortex-a7 -mfpu=neon-vfpv4 -mfloat-abi=hard -ftree-vectorize -Ofast -funsafe-math-optimizations -mfp16-format=ieee -W -Wall -Wextra -g -O4 -I/jevois/include -I/lab/itti/jevois/software/jevois-sdk/out/sun8iw5p1/linux/common/buildroot/build/linux-headers-3.4.113/usr/include -I/lab/itti/jevois/software/jevois-sdk/out/sun8iw5p1/linux/common/buildroot/build/opencv3-3.3.0/buildroot-build/3rdparty/tbb/tbb-4.4.3/include -I/lab/itti/jevois/software/jevois-sdk/out/sun8iw5p1/linux/common/buildroot/host/usr/arm-buildroot-linux-gnueabihf/sysroot/usr/include/python3.6m -I/lab/itti/jevois/software/jevois-sdk/out/sun8iw5p1/linux/common/buildroot/target/usr/lib/python3.6/site-packages/numpy/core/include/ -fPIC -Wno-deprecated-declarations -Wno-psabi")

set(JEVOIS_HOST_OPENCV_LIBS "-L/usr/share/jevois-opencv-3.3.0/lib -lopencv_core -lopencv_imgproc -lopencv_features2d -lopencv_flann -lopencv_ml -lopencv_objdetect -lopencv_imgcodecs -lopencv_tracking -lopencv_video -lopencv_videoio -lopencv_highgui")
set(JEVOIS_PLATFORM_OPENCV_LIBS "-lopencv_core -lopencv_imgproc -lopencv_features2d -lopencv_flann -lopencv_ml -lopencv_objdetect -lopencv_imgcodecs -lopencv_tracking -lopencv_video -lopencv_videoio")

set(JEVOIS_HOST_PYTHON_LIBS "-lpython3.5m -lboost_python-py35")
set(JEVOIS_PLATFORM_PYTHON_LIBS "-lpython3.6m -lboost_python3")

set(JEVOIS_PLATFORM_INCLUDE "-I/lab/itti/jevois/software/jevois-sdk/out/sun8iw5p1/linux/common/buildroot/build/linux-headers-3.4.113/usr/include -I/lab/itti/jevois/software/jevois-sdk/out/sun8iw5p1/linux/common/buildroot/build/opencv3-3.3.0/buildroot-build/3rdparty/tbb/tbb-4.4.3/include -I/lab/itti/jevois/software/jevois-sdk/out/sun8iw5p1/linux/common/buildroot/host/usr/arm-buildroot-linux-gnueabihf/sysroot/usr/include/python3.6m -I/lab/itti/jevois/software/jevois-sdk/out/sun8iw5p1/linux/common/buildroot/target/usr/lib/python3.6/site-packages/numpy/core/include/")
set(JEVOIS_HOST_INCLUDE "-I/usr/share/jevois-opencv-3.3.0/include -I/usr/include/python3.5m")

set(JEVOIS_HOST_MODULES_ROOT "/jevois")
set(JEVOIS_PLATFORM_MODULES_ROOT "/var/lib/jevois-microsd")
