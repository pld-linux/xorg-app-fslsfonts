Summary:	fslsfonts application - list fonts served by X font server
Summary(pl.UTF-8):	Aplikacja fslsfonts - lista fontów udostępnianych przez serwer fontów X
Name:		xorg-app-fslsfonts
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/fslsfonts-%{version}.tar.bz2
# Source0-md5:	9b50d967ac6d4bae9bffb62a5e527a50
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libFS-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros >= 1.8
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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/fslsfonts
%{_mandir}/man1/fslsfonts.1x*
