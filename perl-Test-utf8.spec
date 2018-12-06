#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-utf8
Version  : 1.01
Release  : 5
URL      : http://search.cpan.org/CPAN/authors/id/M/MA/MARKF/Test-utf8-1.01.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/M/MA/MARKF/Test-utf8-1.01.tar.gz
Summary  : 'handy utf8 tests'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Install)

%description
NAME
Test::utf8 - handy utf8 tests
SYNOPSIS
# check the string is good
is_valid_string($string);   # check the string is valid
is_sane_utf8($string);      # check not double encoded

%package dev
Summary: dev components for the perl-Test-utf8 package.
Group: Development
Provides: perl-Test-utf8-devel = %{version}-%{release}

%description dev
dev components for the perl-Test-utf8 package.


%prep
%setup -q -n Test-utf8-1.01

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Test/utf8.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::utf8.3
