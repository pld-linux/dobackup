%include        /usr/lib/rpm/macros.perl
Summary:	A Perl script for performing unattended incremental backups.
Name:		dobackup
Version:	4.22
Release:	1
License:	GPL
Vendor:		Webcon, Inc.
Group:		Applications/Archiving
URL:		http://www.webcon.ca/opensource/dobackup/
Source0:	http://www.webcon.ca/opensource/dobackup/%{name}-%{version}.tar.gz
Requires:	perl >= 5.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
A flexible Perl script to handle unattended incremental backups of
multiple servers. Handles multiple media sets with automatic media
preparation and rotation, configurable 'what-to-backup', global
exclusion patterns, user settable 'don't-backup-this-directory'
metafiles. Design goal: zero-maintenance, nothing to do except change
the media when told.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -D dobackup.conf.sample ${RPM_BUILD_ROOT}%{_sysconfdir}/dobackup.conf
install -D dobackup.pl ${RPM_BUILD_ROOT}%{_sbindir}/dobackup
install -D dobackup.8  ${RPM_BUILD_ROOT}%{_mandir}/man8/dobackup.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr( 644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dobackup.conf
%doc README* CHANGELOG BUGS TODO dobackup.conf.sample dobackup.cron
%attr(755,root,root) %{_sbindir}/dobackup
%{_mandir}/man8/*
