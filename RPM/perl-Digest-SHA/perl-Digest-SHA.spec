Name:           perl-Digest-SHA
Epoch:		1
Version:        5.95
Release:        1.efa%{?dist}
Summary:        Perl extension for SHA-1/224/256/384/512
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Digest-SHA/
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSHELOR/Digest-SHA-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl >= 0:5.003
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Digest::SHA is written in C for speed. If your platform lacks a C compiler,
you can install the functionally equivalent (but much slower)
Digest::SHA::PurePerl module.

%prep
%setup -q -n Digest-SHA-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

find %{buildroot} -name .packlist -exec %{__rm} {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
%{__make} test

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README shasum
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Digest*
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Thu Feb 19 2016 Shawn Iverson <shawniverson@gmail.com> - 5.95-1
- Updated for EFA https://efa-project.org

* Tue Sep 02 2014 Dave Cross <dave@mag-sol.com> 5.92-1
- Specfile autogenerated by cpanspec 1.78.
