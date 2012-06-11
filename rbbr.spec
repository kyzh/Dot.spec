%{!?ruby_sitelib: %define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")}

Name:             rbbr
Version:          0.6.0
Release:          1%{?dist}
Summary:          RuBy BRowser

Group:            Development/Languages
License:          GPL
URL:              http://ruby-gnome2.sourceforge.jp/hiki.cgi?rbbr
Source0:          %{name}-%{version}-withapi.tar.gz

BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
BuildRequires:    ruby
BuildRequires:    gettext
Requires:         ruby(abi) = 1.8
Requires:         rubygem-gtk2
Requires:         ruby-gnome2
Provides:         rbbr = %{version}-%{release}

%description
rbbr is a ruby application to browse modules/classes hierarchy and their
constants and methods.

%prep
%setup -q -n %{name}-%{version}-withapi

%build
ruby install.rb config
ruby install.rb setup

%install
rm -rf %buildroot
ruby install.rb install --prefix=%buildroot

%find_lang %{name}
# --all-name 

# Make icons available at the right place 
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp -p $RPM_BUILD_ROOT%{_datadir}/%{name}/icon.png $RPM_BUILD_ROOT%{_datadir}/icons/rbbr.png
cp -p $RPM_BUILD_ROOT%{_datadir}/%{name}/icon.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/rbbr.png


# Make .desktop file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=rbbr
GenericName=Documentation Browser
Comment=RuBy BRowser
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
Categories=GTK;Development;
EOF

# Verification of desktop file
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{_bindir}/*
%{ruby_sitelib}/*
%{_datadir}/icons/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*
%{_datadir}/%{name}/*
%{_datadir}/locale/*

%doc AUTHORS README README.ja ChangeLog COPYING COPYING.ja

%changelog

* Tue Mar 22 2011 Someone <someone@dev.null> - 0.6.0
- First build 0.6.0
