%define modname gnutls
%define dirname %{modname}
%define soname %{modname}.so
%define inifile A67_%{modname}.ini

Summary:	GnuTLS PHP Module
Name:		php-%{modname}
Version:	0.3
Release:	%mkrel 0.rc1.1
Group:		Development/PHP
License:	GPL
URL:		http://openvcp.org/
Source0:	http://files.openvcp.org/modphp-%{modname}-%{version}-rc1.tar.gz
BuildRequires:	php-devel >= 3:5.2.0
BuildRequires:	pkgconfig
BuildRequires:	gnutls-devel
BuildRoot:	%{_tmppath}/%{name}-root

%description
This is a dynamic shared object (DSO) that adds GnuTLS support to PHP.

%prep

%setup -q -n modphp-%{modname}-%{version}-rc1

%build

%{_usrsrc}/php-devel/buildext %{modname} "%{modname}.c" "-DCOMPILE_DL=1 -DHAVE_SOCKETS -L%{_libdir} `pkg-config --libs gnutls`"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_sysconfdir}/php.d

cat > README.%{modname} << EOF
The %{name} package contains a dynamic shared object (DSO) for PHP. 
EOF

install -m755 %{soname} %{buildroot}%{_libdir}/php/extensions/

cat > %{buildroot}%{_sysconfdir}/php.d/%{inifile} << EOF
extension = %{soname}
EOF

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README*
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}

