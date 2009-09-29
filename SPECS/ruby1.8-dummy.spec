%define bindir /usr/bin

Summary: /usr/bin/ruby1.8 dummy package
Name: ruby1.8-dummy
Version: 0.0.1
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://example.com
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby
BuildArch: noarch

%description
/usr/bin/ruby1.8 dummy package

%prep
%build
%install
rm -fr %{buildroot}
mkdir -p %{buildroot}%{bindir}
ln -s `which ruby` %{buildroot}/%{bindir}/ruby1.8

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{bindir}/ruby1.8


%changelog
* Sun Jun 28 2008  <naoya.n@gmail.com> - 0.0.1-1
- Initial package
