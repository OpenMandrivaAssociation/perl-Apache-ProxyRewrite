%define upstream_name	 Apache-ProxyRewrite
%define upstream_version 0.17

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Apache::ProxyRewrite - mod_perl URL-rewriting proxy
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Apache/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		Apache-ProxyRewrite-mpb.diff
Patch1:		Apache-ProxyRewrite-0.17-mod_perl2.diff

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
#%make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

%clean 
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README SUPPORT
%{perl_vendorlib}/Apache/ProxyRewrite.pm
%{_mandir}/*/*
