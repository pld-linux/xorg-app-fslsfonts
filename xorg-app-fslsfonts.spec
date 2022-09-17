Summary:	fslsfonts application - list fonts served by X font server
Summary(pl.UTF-8):	Aplikacja fslsfonts - lista fontów udostępnianych przez serwer fontów X
Name:		xorg-app-fslsfonts
Version:	1.0.6
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/fslsfonts-%{version}.tar.xz
# Source0-md5:	7bbde137769c15fd9ada97150720076d
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libFS-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.25
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fslsfonts application lists the fonts served by X font server and
matching given pattern.

%description -l pl.UTF-8
Aplikacja fslsfonts wypisuje listę fontów udostępnianych przez serwer
fontów X i pasujących do zadanego wzorca.

%prep
%setup -q -n fslsfonts-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/fslsfonts
%{_mandir}/man1/fslsfonts.1*
