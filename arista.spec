%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:			arista
Summary:		Easy to use multimedia transcoder for the GNOME Desktop
Version:		0.9.6
Release:		1%{dist}
License:		LGPLv2+
Group:			Applications/Multimedia
URL:			http://www.transcoder.org
Source:			http://programmer-art.org/media/releases/arista-transcoder/%{name}-%{version}.tar.gz
Source1:		%{name}.png
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	python-gudev
Requires:	pycairo
Requires:	pygtk2
Requires:	gstreamer-python
Requires:	gstreamer-plugins-good
Requires:	gstreamer-plugins-base
Requires:	pygobject2
Requires:	gnome-python2-gconf

BuildRequires:	python-devel
BuildRequires:	desktop-file-utils
BuildRequires:	python-setuptools-devel
BuildRequires:	gettext
BuildArch:	noarch

%description
A easy to use multimedia transcoder for the GNOME Desktop. Arista focuses on 
beingeasy to use by making the complex task of encoding for various devices 
simple. Pick your input, pick your target device, choose a file to save to and 
go. Features include automatic discovery of DVD media and V4L devices, ripping 
from DVD, V4L devices, or files, a live quality preview, and included presets
for the most popular devices currently in use.

%prep
%setup -q -n %{name}-%{version}

sed -i -e 's|Icon=/usr/share/arista/ui/icon.svg|Icon=%{name}|g' \
	%{name}.desktop
%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install \
	--skip-build \
	--root=%{buildroot} \

install -dm 755 %{buildroot}%{_datadir}/pixmaps
install -m 644 %{SOURCE1} \
	%{buildroot}%{_datadir}/pixmaps

rm -r %{buildroot}%{_datadir}/locale/templates %{buildroot}%{_datadir}/doc/

chmod 755 %{buildroot}%{python_sitelib}/%{name}/*.py
chmod 644 %{buildroot}%{python_sitelib}/%{name}/discoverer.py

desktop-file-validate %{buildroot}/%{_datadir}/applications/arista.desktop

# Until there's a nautilus-python for GNOME 3
rm -r %{buildroot}/usr/lib/nautilus/

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS LICENSE README.md
%{_bindir}/arista-gtk
%{_bindir}/arista-transcode
%dir %{python_sitelib}/%{name}
%{python_sitelib}/%{name}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/presets
%{_datadir}/%{name}/presets/*.*
%dir %{_datadir}/%{name}/ui
%{_datadir}/%{name}/ui/*.svg
%{_datadir}/%{name}/ui/*.ui
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{python_sitelib}/%{name}-%{version}-*.egg-info

%changelog
* Wed Mar 21 2011 Florentin Raud <florentin.raud@gmail.com> - 0.9.6-1
- New version 0.9.6

* Wed May 27 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.9.1-2
- Fix review issues
* Mon May 25 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.9.1-1
- initial release 
