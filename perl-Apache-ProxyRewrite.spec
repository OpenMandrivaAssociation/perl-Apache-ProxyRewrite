%define upstream_name	 Apache-ProxyRewrite
%define upstream_version 0.17

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Apache::ProxyRewrite - mod_perl URL-rewriting proxy
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Apache/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		Apache-ProxyRewrite-mpb.diff
Patch1:		Apache-ProxyRewrite-0.17-mod_perl2.diff

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Apache::ProxyRewrite acts as a reverse-proxy that will rewrite
URLs embedded in HTML documents per apache configuration
directives.

This module was written to allow multiple backend services with
discrete URLs to be presented as one service and to allow the
proxy to do authentication on the client's behalf.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1
%patch1 -p1
find . -type f -exec chmod 644 {} \;

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc ChangeLog README SUPPORT
%{perl_vendorlib}/Apache/ProxyRewrite.pm
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.170.0-2mdv2011.0
+ Revision: 680456
- mass rebuild

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.170.0-1mdv2011.0
+ Revision: 402966
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.17-7mdv2009.0
+ Revision: 255277
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.17-5mdv2008.1
+ Revision: 136658
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Oct 27 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.17-5mdv2007.0
+ Revision: 73201
- import perl-Apache-ProxyRewrite-0.17-5mdk

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.17-5mdk
- Fix SPEC according to Perl Policy
	- URL && Source URL

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.17-4mdk
- rebuild

* Fri Jan 27 2006 Oden Eriksson <oeriksson@mandriva.com> 0.17-3mdk
- use mod_perl2 (P1)

* Sat Sep 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.17-2mdk
- rebuild

* Fri Aug 27 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.17-1mdk
- initial mandrake package
- added P0

