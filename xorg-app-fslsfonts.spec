# $Rev: 3342 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	fslsfonts application
Summary(pl):	Aplikacja fslsfonts
Name:		xorg-app-fslsfonts
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/fslsfonts-%{version}.tar.bz2
# Source0-md5:	85446bdd92d56da6c53d9c187e48aba2
Patch0:		fslsfonts-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libFS-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/fslsfonts-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
fslsfonts application.

%description -l pl
Aplikacja fslsfonts.


%prep
%setup -q -n fslsfonts-%{version}
%patch0 -p1


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
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*