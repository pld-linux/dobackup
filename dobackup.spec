%include	/usr/lib/rpm/macros.perl
Summary:	A Perl script for performing unattended incremental backups
Summary(pl):	Skrypt Perla do bezobs�ugowego tworzenia przyrostowych kopii zapasowych
Name:		dobackup
Version:	4.35
Release:	1
License:	GPL
Vendor:		Webcon, Inc.
Group:		Applications/Archiving
Source0:	http://www.webcon.ca/opensource/dobackup/%{name}-%{version}.tar.gz
# Source0-md5:	b6460ef562248afdf85b4db20095e59f
Patch0:		%{name}-perl.patch
URL:		http://www.webcon.ca/opensource/dobackup/
BuildRequires:	perl-devel >= 1:5.6.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A flexible Perl script to handle unattended incremental backups of
multiple servers. Handles multiple media sets with automatic media
preparation and rotation, configurable 'what-to-backup', global
exclusion patterns, user settable 'don't-backup-this-directory'
metafiles. Design goal: zero-maintenance, nothing to do except change
the media when told.

%description -l pl
Elastyczny skrypt Perla maj�cy za zadanie bezobs�ugowe tworzenie
przyrostowych kopii zapasowych z wielu serwer�w. Obs�uguje wiele
zestaw�w no�nik�w z automatycznym przygotowywaniem i rotacj� no�nik�w,
konfigurowalnym wyborem danych do kopiowania, globalnymi wzorcami
wyklucze� oraz ustawianymi przez u�ytkownika metaplikami
zabraniaj�cymi kopiowania danego katalogu. Cel projektu: zerowy
nadz�r, jedyne co trzeba robi�, to wymiana no�nik�w na ��danie.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -D dobackup.conf.sample $RPM_BUILD_ROOT%{_sysconfdir}/dobackup.conf
install -D dobackup.pl	$RPM_BUILD_ROOT%{_sbindir}/dobackup
install -D dobackup.8	$RPM_BUILD_ROOT%{_mandir}/man8/dobackup.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* CHANGELOG BUGS TODO dobackup.conf.sample dobackup.cron
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dobackup.conf
%attr(755,root,root) %{_sbindir}/dobackup
%{_mandir}/man8/*
