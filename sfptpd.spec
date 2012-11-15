Name: sfptpd
Summary: Solarflare Enhanced PTPD (Precision Time Protocol) daemon
License: Unknown (BSD-like?)
Group: System Environment/Daemons
Version: 2.0.0
Release: 2
# Spec file largely inspired by http://jwboyer.fedorapeople.org/pub/ptpd-phc.spec
# author twitter.com/jwboyer19
# Init fil largely inspired by http://serverfault.com/questions/329127/ptp-time-synchronization-on-centos6-rhel
# Author serverfault.com/users/89768/sashka-b
# I centralise it all there:
# https://gist.github.com/4078197

URL: https://support.solarflare.com/index.php?view=categories&id=165&option=com_cognidox&Itemid=2
Source0: sfptpd-2.0.0.2-64bit.tgz
Source1: sfptpd.init
Source2: sfptpd.sysconfig


%description
This package contains a "sptpd" binary compiled for 64bit linux platforms
with support for Solarflare SFN5322F and SFN6322F PTP adapters .
PTP provides precise time coordination of Ethernet LAN connected computers.

%setup -q -n %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}%{_bindir} ${RPM_BUILD_ROOT}%{_sysconfdir}/init.d ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig ${RPM_BUILD_ROOT}%{_sysconfdir}/sfptpd
echo `pwd`
echo `ls -l`
cp sfptpd ${RPM_BUILD_ROOT}%{_bindir}
cp config/* ${RPM_BUILD_ROOT}%{_sysconfdir}/sfptpd/
install -m 755 -p %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/init.d/sfptpd
install -m 755 -p %{SOURCE2} ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/sfptpd


%postun
/sbin/chkconfig --add sfptpd

ptrace
%files
%defattr(-,root,root)
%doc RELEASE_NOTES COPYRIGHT
%{_bindir}/sfptpd
%{_sysconfdir}/init.d/sfptpd
%{_sysconfdir}/sysconfig/sfptpd
%{_sysconfdir}/sfptpd/ptp_master.cfg
%{_sysconfdir}/sfptpd/ptp_master_ntp.cfg
%{_sysconfdir}/sfptpd/ptp_slave.cfg

%changelog
* Thu Nov 15 2012 Florentin Raud <florentin.raud@tradition.com>
- Update to use sfptpd

* Tue Oct 9 2012 Florentin Raud <florentin.raud@tradition.com>
- Put random file from the interweb together

* Tue Oct 9 2012 Solarflare <support@solarflare.com> - 1_0_15
- Added support to handle leap seconds signalled by master clocks

* Tue Oct 9 2012 Solarflare <support@solarflare.com> - 1_0_14
- option '-L' to ignore the lock file
- fix for daemon mode where an error can occur if the child process attempts
 to get the lock before the parent process releases it.

 * Tue Oct 9 2012 Solarflare <support@solarflare.com> - 1_0_13
 - Set the transport to zero for all packets
 - Only set the two-step flag for Sync and Peer Delay Response packets

 * Tue Oct 9 2012 Solarflare <support@solarflare.com> - 1_0_12
 - change to column headings of stats type output
 - addition of -T option to set TTL

 * Tue Oct 9 2012 Solarflare <support@solarflare.com> - 1_0_10
 - initial release
