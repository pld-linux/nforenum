%define		_rc	RC1
Summary:	Tool to create add-ons for TTDPatch and OpenTTD
Summary(pl.UTF-8):	Narzędzie do tworzenia dodatków dla TTDPatch oraz OpenTTD
Name:		nforenum
Version:	4.0.0
Release:	0.%{_rc}.1
License:	GPL v2+
Group:		Applications
Source0:	http://binaries.openttd.org/extra/nforenum/%{version}-%{_rc}/%{name}-%{version}-%{_rc}-source.tar.gz
# Source0-md5:	be1b49850c8cb13febb247611bbb8309
Patch0:		%{name}-cflags.patch
URL:		http://www.openttd.org/en/download-nforenum
BuildRequires:	boost-devel
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NFORenum is a format correcter, linter, and pretty-printer for NFO,
used to create add-ons for TTDPatch and OpenTTD.

%description -l pl.UTF-8
NFORenum jest narzędziem poprawiającym formatowanie, linie i ogólny
wygląd plików NFO. Jest używany do tworzenia dodatków dla TTDPatch
oraz OpenTTD.

%prep
%setup -q -n %{name}-%{version}-%{_rc}-source
%patch0 -p1

%build
%{__make} \
	SVNVERSION="echo %{rev}" \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGAPP="%{rpmcxxflags}" \
	LDOPT="%{rpmldflags}" \
	V="1"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install nforenum $RPM_BUILD_ROOT%{_bindir}
install docs/nforenum.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip $RPM_BUILD_ROOT%{_mandir}/man1/nforenum.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog.txt docs/*.txt
%attr(755,root,root) %{_bindir}/nforenum
%{_mandir}/man1/nforenum.1*
