Summary:	Colorful X solitaire Mah Jongg game
Summary(pl):	Komputerowy Mad�ong
Name:		xmahjongg
Version:	3.6.1
Release:	1
License:	GPL
Vendor:		Little Cambridgeport Design Factory
Group:		X11/Applications/Games
URL:		http://www.lcdf.org/xmahjongg/
Source0:	http://www.lcdf.org/xmahjongg/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	XFree86-devel


%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Real Mah Jongg is a social game that originated in China thousands of
years ago. Four players, named after the four winds, take tiles from a
wall in turn. The best tiles are made of ivory and wood; they click
pleasantly when you knock them together. Computer Solitaire Mah Jongg
(xmahjongg being one of the sillier examples) is nothing like that but
it's fun, or it must be, since there are like 300 shareware versions
available for Windows. This is for X11 and it's free.

%description -l pl
Stara, chi�ska gra logiczna. Powsta�a ona w staro�ytnym Pa�stwie
�rodka, a jej historia si�ga chi�skiej dynastii Zachodniego Chou,
czyli ok. 720 roku n.e. Podobnie jak wi�kszo�� gier karcianych tak i
mad�ong rozwija� si� niezale�nie w r�nych okr�gach i prowincjach
dawnych Chin, zyskuj�c niezliczone odmiany dla r�nej liczby
graj�cych. Ta wersja przeznaczona jest dla jednej osoby i zawiera
kilka r�nych zestaw�w klock�w (dorothys, gnome, gnome2, real, thick,
dorwhite, small, thin). Wywo�uje si� je za pomoc� parametru '-t'.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags}" ./configure --datadir=%{_datadir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_mandir}/man6
install -c -s xmahjongg $RPM_BUILD_ROOT%{_bindir}/xmahjongg
install -c xmahjongg.6 $RPM_BUILD_ROOT%{_mandir}/man6/xmahjongg.6
%{__make} pkgdatadir="$RPM_BUILD_ROOT%{_datadir}/%{name}" install-share

%clean
rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/xmahjongg
%{_mandir}/man6/xmahjongg.6*
%{_datadir}/%{name}
