%define release_date    20090520
%define prefix_dir      /opt
%define install_dir     %{prefix_dir}/%{name}-%{version}-%{release_date}

Name:		ruby-enterprise
Version:	1.8.6
Release:	%{release_date}%{?dist}.1
License:	Ruby License/GPL - see COPYING
URL:		http://www.rubyenterpriseedition.com/
BuildRequires:	readline readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel tk-devel libX11-devel autoconf gcc unzip openssl-devel db4-devel byacc
%ifnarch ppc64
BuildRequires:	emacs
%endif

Source0:	http://rubyforge.org/frs/download.php/41040/%{name}-%{version}-%{release_date}.tar.gz

Summary:	An interpreter of object-oriented scripting language customized by Phusion
Group:		Development/Languages

Requires: rubylocal
Requires: ruby1.8-dummy


%description
Ruby Enterprise Edition is a drop-in, transparent solution for improving your Ruby on Rails website's scalability and performance, while decreasing memory usage.


%prep
%setup -q -n %{name}-%{version}-%{release_date}
sudo chown -R $USER %{prefix_dir}

%build

%install
rm -rf %{install_dir}
%{_builddir}/%{name}-%{version}-%{release_date}/installer --auto %{install_dir} 

%files 
%defattr(-, root, root)
%dir %{install_dir}
%{install_dir}/*

%post
if test -h %{prefix_dir}/ruby; then
  rm -f %{prefix_dir}/ruby
fi

ln -fs %{install_dir} %{prefix_dir}/ruby

%clean
%{__rm} -fr %{buildroot}
%{__rm} -fr %{install_dir}


%changelog
* Mon Jan 19 2009 Naoya NAKAZAWA <naoya.n@gmail.com> - 1.8.6-20090113
- Updated version 1.8.6-20090113

* Sun Sep 21 2008 Naoya NAKAZAWA <naoya.n@gmail.com> - 1.8.6-20080810
- Initial version

