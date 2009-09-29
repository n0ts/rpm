%define bindir /usr/local/bin

Summary: /usr/local/bin/ruby dummy package
Name: rubylocal
Version: 0.0.1
Release: 1%{?dist}
Group: Development/Languages
License: GPL
URL: http://example.com
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby
BuildArch: noarch

%description
/usr/local/bin/ruby dummy package

%prep
%build
%install
rm -fr %{buildroot}
mkdir -p %{buildroot}%{bindir}
ln -s `which ruby` %{buildroot}/%{bindir}/ruby

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{bindir}/ruby


%changelog
* Sun Jun 28 2008  <naoya.n@gmail.com> - 0.0.1-1
- Initial package
