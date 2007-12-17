%define module	Apache-ProxyRewrite

Summary:	Apache::ProxyRewrite - mod_perl URL-rewriting proxy
Name:		perl-%{module}
Version:	0.17
Release:	%mkrel 5
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Apache/%{module}-%{version}.tar.bz2
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

%setup -q -n %{module}-%{version}
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



