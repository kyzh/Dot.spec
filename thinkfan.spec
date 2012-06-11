Name:		thinkfan
Version:        0.7.1
Summary:        A minimalist fan control program
License:        Creative Commons Attribution-Share Alike 3.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.gz
Release:	14.1
Group:		Productivity/Other
%description
A minimalist fan control program. Supports any hardware through the sysfs hwmon
interface and most Thinkpads through /proc/acpi/ibm. Please check out the new
config extensions that support sensor correction values to protect your hard
disk! 

%prep
%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS"

%clean 
rm -rf $RPM_BUILD_ROOT

%install
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
mkdir -p ${RPM_BUILD_ROOT}/etc
mkdir -p ${RPM_BUILD_ROOT}/etc/modprobe.d/
mkdir -p ${RPM_BUILD_ROOT}/usr/share/man/man1
cp thinkfan ${RPM_BUILD_ROOT}/usr/bin/thinkfan
cp thinkfan.conf* ${RPM_BUILD_ROOT}/etc/
cp thinkfan.1 ${RPM_BUILD_ROOT}/usr/share/man/man1/thinkfan.1
cat > ${RPM_BUILD_ROOT}/etc/modprobe.d/%{name}.conf << EOF
options thinkpad_acpi fan_control=1
EOF

%files 
%defattr(-,root,root)
/usr/bin/thinkfan
/usr/share/man/man1/thinkfan.1.gz
/etc/thinkfan.conf*
/etc/modprobe.d/thinkfan.conf
%doc README NEWS

%changelog

