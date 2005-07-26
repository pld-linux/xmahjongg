Summary:	Colorful X solitaire Mah Jongg game
Summary(pl):	Komputerowy Mad¿ong
Name:		xmahjongg
Version:	3.7
Release:	1
License:	GPL
Vendor:		Little Cambridgeport Design Factory
Group:		X11/Applications/Games
Source0:	http://www.lcdf.org/xmahjongg/%{name}-%{version}.tar.gz
# Source0-md5:	9db5bf1b329b410220b7976cd9b3d374
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.lcdf.org/xmahjongg/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Real Mah Jongg is a social game that originated in China thousands of
years ago. Four players, named after the four winds, take tiles from a
wall in turn. The best tiles are made of ivory and wood; they click
pleasantly when you knock them together. Computer Solitaire Mah Jongg
(xmahjongg being one of the sillier examples) is nothing like that but
it's fun, or it must be, since there are like 300 shareware versions
available for Windows. This is for X11 and it's free.

%description -l pl
Stara, chiñska gra logiczna. Powsta³a ona w staro¿ytnym Pañstwie
¦rodka, a jej historia siêga chiñskiej dynastii Zachodniego Chou,
czyli ok. 720 roku n.e. Podobnie jak wiêkszo¶æ gier karcianych tak i
mad¿ong rozwija³ siê niezale¿nie w ró¿nych okrêgach i prowincjach
dawnych Chin, zyskuj±c niezliczone odmiany dla ró¿nej liczby
graj±cych. Ta wersja przeznaczona jest dla jednej osoby i zawiera
kilka ró¿nych zestawów klocków (dorothys, gnome, gnome2, real, thick,
dorwhite, small, thin). Wywo³uje siê je za pomoc± parametru '-t'.

%prep
%setup -q

%build
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/xmahjongg
%{_pixmapsdir}/*
%{_desktopdir}/*
%{_mandir}/man6/xmahjongg.6*
%{_datadir}/%{name}
