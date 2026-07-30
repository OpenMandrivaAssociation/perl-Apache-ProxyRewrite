%define upstream_name	 Apache-ProxyRewrite
%define upstream_version 0.17
Name:		perl-%{upstream_name}
Version:	0.17
Release:	2

Summary:	Apache::ProxyRewrite - mod_perl URL-rewriting proxy
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Apache-ProxyRewrite
Source0:	https://cpan.metacpan.org/authors/id/C/CG/CGILMORE/Apache-ProxyRewrite-0.17.tar.gz
Patch0:		Apache-ProxyRewrite-mpb.diff
Patch1:		Apache-ProxyRewrite-0.17-mod_perl2.diff

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}
%patch -P0 -p1
%patch -P1 -p1
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


