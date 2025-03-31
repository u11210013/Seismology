/*--------------------------------------------------------------------
 *
 *  Copyright (c) 1991-2024 by the GMT Team (https://www.generic-mapping-tools.org/team.html)
 *  See LICENSE.TXT file for copying and redistribution conditions.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU Lesser General Public License as published by
 *  the Free Software Foundation; version 3 or any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU Lesser General Public License for more details.
 *
 *  Contact info: www.generic-mapping-tools.org
 *--------------------------------------------------------------------*/

#pragma once
#ifndef _CONFIG_H
#define _CONFIG_H

/* configured options and settings for GMT */
#define GMT_PACKAGE_VERSION_MAJOR 6
#define GMT_PACKAGE_VERSION_MINOR 5
#define GMT_PACKAGE_VERSION_PATCH 0

#define GMT_PACKAGE_VERSION "6.5.0"
#define GMT_PACKAGE_VERSION_WITH_GIT_REVISION "6.5.0"
#define GMT_BUILD_DATE "2024.01.07"

/* URL to the docs on the GMT web server */
#define GMT_DOC_URL "https://docs.generic-mapping-tools.org/6.5"

/* path to executables/libs */
#define GMT_BINDIR_RELATIVE "bin"
#ifndef WIN32
    #define GMT_LIBDIR_RELATIVE "lib"
#else
    #define GMT_LIBDIR_RELATIVE "bin"
#endif

/* path to shared files */
#define GMT_SHARE_DIR "C:/progs_cygw/GMTdev/gmt5/compileds/gmt6/VC14_64/share"
#define GMT_SHARE_DIR_RELATIVE "share"

/* URL to remote files */
#define GMT_DATA_SERVER "oceania"

/* for running and debugging in C:/v/build */
#define SUPPORT_EXEC_IN_BINARY_DIR
#define GMT_SHARE_DIR_DEBUG "C:/progs_cygw/GMTdev/gmt5/master/share"
#define GMT_USER_DIR_DEBUG "C:/v/build/share"
#define GMT_BINARY_DIR_SRC_DEBUG "C:/v/build/src"

/* path to documentation */
#define GMT_DOC_DIR "C:/progs_cygw/GMTdev/gmt5/compileds/gmt6/VC14_64/share/doc"

/* min required GSHHG version and its netCDF extension */
#define GSHHG_MIN_REQUIRED_VERSION {2, 2, 0}

/* Name of core library */
#define GMT_CORE_LIB_NAME "gmt_w64.dll"

/* Name of gs executable */
#define GMT_GS_EXECUTABLE "gswin64c"

/* Name of supplemental library */
#define GMT_SUPPL_LIBRARY "supplements_w64.dll"

/* Name of PSL library */
#define PSL_LIB_NAME "postscriptlight_w64.dll"

/* Name of DCW path */
#define DCW_INSTALL_PATH "C:/progs_cygw/GMTdev/gmt5/master/share/dcw"

/* Name of GSHHG path */
#define GSHHG_INSTALL_PATH "C:/progs_cygw/GMTdev/gmt5/master/share/coast"

/* Default units (SI vs US) */
#define GMT_DEF_UNITS "SI"

/* Suffix of gmt executable, include dir, data dir, and plugin dir */
#define GMT_INSTALL_NAME_SUFFIX ""

#endif /* !_CONFIG_H */

/* vim: set ft=c: */
