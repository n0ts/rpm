%define prefix_dir      /opt
%define revision        A00
%define install_dir     %{prefix_dir}/%{name}

Name:		dell-omsa
Version:	6.1.0
Release:	1%{?dist}
License:	DELL SOFTWARE LICENSE AGREEMENT - see license.txt
URL:		http://linux.dell.com/wiki/index.php/Repository/OMSA
Source:		http://ftp.us.dell.com/sysman/OM_%{version}_ManNode_%{revision}.tar.gz
Buildroot:	/tmp/%{name}-%{version}-buildroot

Summary:	OpenManage Server Administrator
Group:		Development/Languages

Requires: compat-libstdc++-33
Requires: curl-devel
Requires: libxml2-devel
Requires: smbios-utils


%description
Dell OpenManage Server Administrator (OMSA) helps administrators manage the hardware and software resources of Dell(tm) PowerEdge(tm) servers running Microsoft(r) Windows(r) or Linux operating systems.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
%__mkdir -p $RPM_BUILD_ROOT%{install_dir}
cp %{_sourcedir}/OM_%{version}_ManNode_%{revision}.tar.gz $RPM_BUILD_ROOT%{install_dir}/%{name}.tar.gz

%files 
%defattr(-, root, root)
%dir %{install_dir}
%{install_dir}/*

%post

%clean
%{__rm} -fr %{install_dir}

%changelog
* Sat Sep 19 2009 Naoya NAKAZAWA <naoya.n@gmail.com> - 6.1-A00
- Initial version

