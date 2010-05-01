%define		rev	2309
Summary:	Tool to create add-ons for TTDPatch and OpenTTD
Summary(pl.UTF-8):	Narzędzie do tworzenia dodatków dla TTDPatch oraz OpenTTD
Name:		nforenum
Version:	3.4.6
Release:	0.%{rev}.1
License:	GPL v2+
Group:		Applications
Source0:	http://binaries.openttd.org/extra/nforenum/%{version}/%{name}-r%{rev}-source.tar.bz2
# Source0-md5:	cab21665a9a14339c590a8f9981787c3
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
%setup -q -n %{name}-r%{rev}
%patch0 -p1

VER=$(awk '/VER /{print $3}' version.def)
if [ "$VER" != "%{version}" ]; then
	: Current version is $VER, not %{version}
	exit 1
fi

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
install -d $RPM_BUILD_ROOT%{_bindir}

install renum $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.txt TODO.txt
%attr(755,root,root) %{_bindir}/renum
