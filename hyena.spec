#
# spec file for package hyena (Version 0.2)
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


Name:           hyena
License:        X11/MIT
Group:          Development/Libraries/GNOME
Version:        0.2.0
Release:        1%{?dist}
Summary:        Library for .NET applications
Url:            http://banshee-project.org/
Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#BuildRequires:  glib-sharp2
BuildRequires:  gtk-sharp2
BuildRequires:  gtk-sharp2-devel
BuildRequires:  mono-basic
BuildRequires:  mono-devel
BuildRequires:  mono-nunit
BuildRequires:  perl-XML-Parser
BuildRequires:  make autoconf automake libtool pkgconfig
Requires:       mono-core
Requires:       gtk-sharp2

%description
Hyena is a .NET library that powers Banshee and PDF Mod, among others.

Authors:
--------
    Aaron Bockover <abockover@novell.com>
    Gabriel Burt <gabriel.burt@gmail.com>

%prep
%setup
%build
%configure 
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc NEWS README COPYING
%{_libdir}/%{name}
%{_libdir}/pkgconfig/*.pc

%changelog
* Wed Sep 16 2009 <ismael@olea.org> 0.2-1.olea
- minor changes for compiling in Fedora

* Wed Sep  9 2009 gburt@suse.de
- Version 0.2
  * Fixes libdir expansion issue
  * Fixes dll mappings for *bsd
* Tue Aug 18 2009 gburt@suse.de
- Version 0.1
* Thu Aug 13 2009 gburt@suse.de
- Initial release
