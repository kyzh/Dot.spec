#
# spec file for package pdfspec (Version 0.9.0)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
# norootforbuild


Name:           pdfmod
License:        GPL v2.0 or later
Group:          Productivity/Office/Other
Version:        0.9.0
Release:        1%{?dist}
Summary:        PDF Modifier
Url:            http://live.gnome.org/PdfMod

Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  hyena >= 0.2

# Construction tools
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  intltool

# Fix for:: checking for GCONF_SHARP_20... no
#BuildRequires:  gnome-sharp2-devel

BuildRequires:  gmime-sharp
BuildRequires:  gnome-doc-utils
BuildRequires:  gnome-sharp
BuildRequires:  gtk-sharp2
BuildRequires:  gtk-sharp2-gapi
BuildRequires:  mono-basic
BuildRequires:  mono-data-sqlite
BuildRequires:  mono-devel
BuildRequires:  mono-nunit
BuildRequires:  ndesk-dbus
BuildRequires:  ndesk-dbus-glib-devel
BuildRequires:  perl-XML-Parser

BuildRequires:  scrollkeeper
BuildRequires:  tango-icon-theme
BuildRequires:  docbook-dtds

# Legacy
#  BuildRequires:  docbook_4
#  BuildRequires:  glib-sharp2
#  BuildRequires:  gnome-doc-utils-devel
#  BuildRequires:  gnome-sharp2
#  BuildRequires:  update-desktop-files


# Mono and gtk depencies
Requires:       mono-core
Requires:       gtk-sharp2

#Requires:       libpoppler-glib4

%description
PDF Mod is a simple tool for modifying your PDFs; moving, removing, extracting, and rotating pages.

Authors:
--------
    Gabriel Burt <gabriel.burt@gmail.com>

%lang_package
%prep
%setup

%build
%configure 
make

%install
make install DESTDIR=%{buildroot}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
gtk-update-icon-cache %{_datadir}/icons/hicolor/

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS NEWS README COPYING
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gnome/help/pdfmod/*/pdfmod.xml


%changelog
* Wed Sep 16 2009 <ismael@olea.org> 0.2-1.olea
- minor changes for compiling

* Wed Sep  9 2009 gburt@suse.de
- Version 0.7
  * View Fullscreen option
  * User docs translated into ca
  * Build fixes for *bsd
  * Update recent files list after opening a document
  * libdir expansion issue fixed in Hyena, depend on 0.2
* Tue Aug 18 2009 gburt@suse.de
- Version 0.6
* Fri Aug  7 2009 gburt@suse.de
- Version 0.5
* Tue Aug  4 2009 gburt@suse.de
- Version 0.4
* Mon Jul 27 2009 gburt@suse.de
- Version 0.3
* Fri Jul 24 2009 gburt@suse.de
- Version 0.2 (bundling Mono.Data.Sqlite)
* Thu Jul 23 2009 gburt@suse.de
- Initial version (0.1)
