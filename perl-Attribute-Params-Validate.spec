#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Attribute
%define		pnam	Params-Validate
%include	/usr/lib/rpm/macros.perl
Summary:	Attribute::Params::Validate - Define validation through subroutine attributes
Summary(pl.UTF-8):	Attribute::Params::Validate - określanie poprawności poprzez atrybuty funkcji
Name:		perl-Attribute-Params-Validate
Version:	1.21
Release:	2
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Attribute/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a769581e3f2131392a14e8a858063a19
URL:		http://search.cpan.org/dist/Attribute-Params-Validate/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Exporter) >= 5.60
BuildRequires:	perl-Attribute-Handlers >= 0.79
BuildRequires:	perl-Params-Validate >= 1.21
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Simple >= 0.96
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is currently unmaintained. I do not recommend using it. It
is a failed experiment. If you would like to take over maintenance of
this module, please contact the author.

The Attribute::Params::Validate module allows you to validate method
or function call parameters just like Params::Validate does. However,
this module allows you to specify your validation spec as an
attribute, rather than by calling the validate routine.

Please see Params::Validate for more information on how you can
specify what validation is performed.

%description -l pl.UTF-8
Ten moduł nie jest obecnie utrzymywany. Jego użycie nie jest zalecane,
jest to nieudany eksperyment. Aby przejąć utrzymywanie tego modułu,
można skontaktować się z autorem.

Moduł Attribute::Params::Validate pozwala sprawdzać poprawność
parametrów wywołania metody lub funkcji podobnie do Params::Validate.
Jednak moduł ten pozwala na zdefiniowanie poprawności jako atrybutów
zamiast poprzez wywołanie funkcji sprawdzającej poprawność.

Więcej informacji o sposobie sprawdzania poprawności można uzyskać w
dokumentacji do modułu Params::Validate.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL
%dir %{perl_vendorlib}/Attribute/Params
%{perl_vendorlib}/Attribute/Params/Validate.pm
%{_mandir}/man3/Attribute::Params::Validate.3pm*
