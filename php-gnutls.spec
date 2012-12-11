%define modname gnutls
%define dirname %{modname}
%define soname %{modname}.so
%define inifile A67_%{modname}.ini

Summary:	GnuTLS PHP Module
Name:		php-%{modname}
Version:	0.3
Release:	%mkrel 0.rc1.24
Group:		Development/PHP
License:	GPLv2+
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

%post
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
	%{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README*
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}


%changelog
* Thu May 03 2012 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.24mdv2012.0
+ Revision: 795444
- rebuild for php-5.4.x

* Sun Jan 15 2012 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.23
+ Revision: 761251
- rebuild

* Wed Aug 24 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.22
+ Revision: 696427
- rebuilt for php-5.3.8

* Fri Aug 19 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.21
+ Revision: 695402
- rebuilt for php-5.3.7

* Sat Mar 19 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.20
+ Revision: 646643
- rebuilt for php-5.3.6

* Sat Jan 08 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.19mdv2011.0
+ Revision: 629802
- rebuilt for php-5.3.5

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.18mdv2011.0
+ Revision: 628107
- ensure it's built without automake1.7

* Wed Nov 24 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.17mdv2011.0
+ Revision: 600493
- rebuild

* Sun Oct 24 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.16mdv2011.0
+ Revision: 588824
- rebuild

* Fri Mar 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.15mdv2010.1
+ Revision: 514550
- rebuilt for php-5.3.2

* Sat Jan 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.14mdv2010.1
+ Revision: 485366
- rebuilt for php-5.3.2RC1

* Sat Nov 21 2009 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.13mdv2010.1
+ Revision: 468171
- rebuilt against php-5.3.1

* Wed Sep 30 2009 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.12mdv2010.0
+ Revision: 451275
- rebuild

* Sun Jul 19 2009 Raphaël Gertz <rapsys@mandriva.org> 0.3-0.rc1.11mdv2010.0
+ Revision: 397533
- Rebuild

* Mon May 18 2009 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.10mdv2010.0
+ Revision: 376995
- rebuilt for php-5.3.0RC2

* Sun Mar 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.9mdv2009.1
+ Revision: 346453
- rebuilt for php-5.2.9

* Tue Feb 17 2009 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.8mdv2009.1
+ Revision: 341750
- rebuilt against php-5.2.9RC2

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.7mdv2009.1
+ Revision: 321739
- rebuild

* Fri Dec 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.6mdv2009.1
+ Revision: 310271
- rebuilt against php-5.2.7

* Fri Jul 18 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.5mdv2009.0
+ Revision: 238398
- rebuild

* Mon Feb 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.4mdv2008.1
+ Revision: 162225
- rebuild

* Sun Jan 13 2008 Funda Wang <fwang@mandriva.org> 0.3-0.rc1.3mdv2008.1
+ Revision: 150856
- rebuild against latest gnutls

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 11 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.2mdv2008.1
+ Revision: 107639
- restart apache if needed

* Fri Oct 12 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.1mdv2008.1
+ Revision: 97779
- import php-gnutls


* Fri Oct 12 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.rc1.1mdv2008.1
- initial Mandriva package
