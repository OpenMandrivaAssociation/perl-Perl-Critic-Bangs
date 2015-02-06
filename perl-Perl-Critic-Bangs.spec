%define upstream_name    Perl-Critic-Bangs
%define upstream_version 1.10
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.10
Release:	3

Summary:	Adding modifiers to a regular expression
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Perl/Perl-Critic-Bangs-1.10.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Perl::Critic)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Perl::Critic)

BuildArch:	noarch

%description
This is a test diagnostic.

Adding modifiers to a regular expression made up entirely of
a variable created with qr() is usually not doing what you expect.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Wed Jun 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.80.0-1mdv2011.0
+ Revision: 686678
- update to new version 1.08

* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 1.60.0-2
+ Revision: 653612
- rebuild for updated spec-helper

* Thu Aug 26 2010 Jérôme Quelin <jquelin@mandriva.org> 1.60.0-1mdv2011.0
+ Revision: 573436
- adding missing buildrequires:
- import perl-Perl-Critic-Bangs


