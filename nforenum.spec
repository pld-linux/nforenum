Summary:	Tool to create add-ons for TTDPatch and OpenTTD
Summary(pl.UTF-8):	Narzędzie do tworzenia dodatków dla TTDPatch oraz OpenTTD
Name:		nforenum
Version:	4.0.0
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://binaries.openttd.org/extra/nforenum/%{version}/%{name}-%{version}-source.tar.gz
# Source0-md5:	9dd7ec02f14256ca65e648b5de415eea
Patch0:		%{name}-flags.patch
URL:		http://www.openttd.org/en/download-nforenum
BuildRequires:	boost-devel
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NFORenum is a format correcter, linter, and pretty-printer for NFO,
used to create add-ons for TTDPatch and OpenTTD.

%description -l pl.UTF-8
NFORenum jest narzędziem poprawiającym formatowanie, linie i ogólny
wygląd plików NFO. Jest używany do tworzenia dodatków dla TTDPatch
oraz OpenTTD.

%prep
%setup -q -n %{name}-%{version}-source
%patch0 -p1

%build
%{__make} \
	SVNVERSION="echo %{rev}" \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags}" \
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
