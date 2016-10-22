%{?scl:%scl_package perl-Business-ISBN}

Name:           %{?scl_prefix}perl-Business-ISBN
%global cpan_version 2.011
Version:        %(echo '%{cpan_version}' | tr '_' '.'})
Release:        2%{?dist}
Summary:        Perl module to work with International Standard Book Numbers

Group:          Development/Libraries
License:        Artistic 2.0
URL:            http://search.cpan.org/dist/Business-ISBN/
Source0:        http://search.cpan.org/CPAN/authors/id/B/BD/BDFOY/Business-ISBN-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(File::Spec::Functions)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Test::Manifest 1.21 is optional
# Run-time:
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Business::ISBN::Data) >= 20140910.002
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(subs)
BuildRequires:  %{?scl_prefix}perl(vars)
# Optinonal run-time
%if !%{defined perl_small}
BuildRequires:  %{?scl_prefix}perl(GD::Barcode::EAN13)
BuildRequires:  %{?scl_prefix}perl(Mojo::DOM)
BuildRequires:  %{?scl_prefix}perl(Mojo::UserAgent)
%endif
# Tests:
BuildRequires:  %{?scl_prefix}perl(IO::Socket)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.95
# Optional tests:
%if !%{defined perl_small}
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 1.00
BuildRequires:  %{?scl_prefix}perl(Test::Pod::Coverage)
%endif
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
%if !%{defined perl_small}
Requires:       %{?scl_prefix}perl(GD::Barcode::EAN13)
Requires:       %{?scl_prefix}perl(Mojo::DOM)
Requires:       %{?scl_prefix}perl(Mojo::UserAgent)
%endif

%description
This modules handles International Standard Book Numbers, including
ISBN-10 and ISBN-13.

%prep
%setup -q -n Business-ISBN-%{cpan_version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
%doc Changes README.pod
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Tue Jul 19 2016 Petr Pisar <ppisar@redhat.com> - 2.011-2
- SCL

* Thu Jun 09 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.011-1
- 2.011 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.010-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.010-1
- 2.010 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.09-6
- Perl 5.22 re-rebuild of bootstrapped packages

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.09-5
- Perl 5.22 rebuild

* Tue Sep 23 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.09-1
- 2.09 bump

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-4
- Perl 5.20 re-rebuild of bootstrapped packages

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 06 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-1
- 2.07 bump

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.06-4
- Perl 5.18 re-rebuild of bootstrapped packages

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 2.06-2
- Perl 5.18 rebuild

* Mon Jun 03 2013 Petr Pisar <ppisar@redhat.com> - 2.06-1
- 2.06 bump

* Wed Feb 27 2013 Paul Howarth <paul@city-fan.org> - 2.05.03-3
- Don't BR: perl(LWP::Simple) for optional tests when bootstrapping; this is a
  cleaner fix than nobbling perl-URI's runtime dependencies

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.05.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 09 2012 Jitka Plesnikova <jplesnik@redhat.com> - 2.05.03-1
- 2.05_03 bump. Fix failing tests (RT#78671, RT#75686)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.05-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 2.05-8
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 2.05-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.05-4
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.05-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.05-2
- rebuild against perl 5.10.1

* Mon Oct  5 2009 Stepan Kasal <skasal@redhat.com> - 2.05-1
- new upstream version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04_01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04_01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 24 2008 Stepan Kasal <skasal@redhat.com> - 2.04_01-1
- new upstream version
- drop integrated patch

* Thu Feb  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.03-4
- rebuild for new perl

* Fri Oct 26 2007 Robin Norwood <rnorwood@redhat.com> - 2.03-3
- Apply patch to fix barcode test

* Thu Oct 25 2007 Robin Norwood <rnorwood@redhat.com> - 2.03-2
- Fix buildrequires and doc list

* Thu Oct 25 2007 Robin Norwood <rnorwood@redhat.com> - 2.03-1
- Initial build
