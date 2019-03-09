# TODO: enable building python libs

Name:           libmonome
Version:        1.4.2
Release:        1%{?dist}
Summary:        libmonome

License:        As-is
URL:            https://github.com/monome/libmonome
Source0:        https://github.com/monome/libmonome/archive/v1.4.2/libmonome-v1.4.2.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  liblo-devel
BuildRequires:  python
BuildRequires:  systemd-devel

Requires:       liblo
Requires:       systemd-libs

%description
libmonome is a library for controlling the monome

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
%set_build_flags
./waf configure --prefix=%{_prefix} --libdir=%{_libdir}
./waf build %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
./waf install --destdir=%{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc README
%{_libdir}/*.so.*
%{_libdir}/monome/protocol*
%{_bindir}/monomeserial
%{_mandir}/man1/*.gz

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/monome/protocol*

%changelog
* Sat Mar  9 2019 Evan Klitzke <evan@eklitzke.org>
- Initial packaging work
