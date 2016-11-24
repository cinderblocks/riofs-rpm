%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

Summary: RioFS is a nice time for fuse and S3
Name: riofs
Version: pre0.7
Release: 1
License: GPL
Group: System
SOURCE0: %{name}-%{version}.tar.gz
URL: https://github.com/skoobe/riofs/

Requires: fuse >= 2.8.4
Requires: curl >= 7.0
Requires: libxml2 >= 2.6
Requires: openssl >= 0.9

BuildRequires:  fuse-devel, libxml2-devel
BuildRequires:  openssl-devel, mailcap

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}

%prep
%setup -q

%build
# Empty section.

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}

# in builddir
cp -a * %{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf.xml
%{_bindir}/*

%changelog
* Mon Nov 21 2016  Cinder Roxley <cinder@sdf.org> 1.0-1
- First Build

