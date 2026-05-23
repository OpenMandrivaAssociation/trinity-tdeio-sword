%bcond clang 1

# TDE variables
%define tde_pkg tdeio-sword
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Version:	14.1.6
Release:	1
Summary:	Tdeio-slave for the Sword Bible tool
Group:		Productivity/Networking/Ftp/Clients
URL:		http://lukeplant.me.uk/kio-sword/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/applications/tdeio/%{tarball_name}-%{version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DBUILD_DOC=ON
BuildOption:    -DBUILD_TRANSLATIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-tdebase-devel >= %{version}
BuildRequires:	trinity-tde-cmake >= %{version}

BuildRequires:	desktop-file-utils
BuildRequires:	gettext

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes

# ACL support
BuildRequires:  pkgconfig(libacl)

# IDN support
BuildRequires:	pkgconfig(libidn)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)


# Requires: sword
BuildRequires:	sword-devel
Requires:		sword

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
TDEio-Sword provides access to Bibles, commentaries
and other texts in an easy to use and attractive
interface -- the Konqueror web browser.  It does so
using the SWORD Bible project and implementing a TDE
ioslave, providing the sword:/ protocol.


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
%find_lang tdeio_sword


%files -f tdeio_sword.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README.md TODO
%{tde_prefix}/%{_lib}/trinity/tdeio_sword.la
%{tde_prefix}/%{_lib}/trinity/tdeio_sword.so
%{tde_prefix}/share/apps/tdeio_sword/
%{tde_prefix}/share/doc/tde/HTML/en/tdeioslave/sword/
%{tde_prefix}/share/icons/hicolor/*/apps/tdeio_sword.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/tdeio_sword.svgz
%{tde_prefix}/share/services/sword.protocol

