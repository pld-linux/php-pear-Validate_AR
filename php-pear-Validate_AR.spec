%define		_status		alpha
%define		_pearname	Validate_AR
Summary:	%{_pearname} - Validation class for Argentina
Summary(pl.UTF-8):	%{_pearname} - Klasa sprawdzająca poprawność dla Argentyny
Name:		php-pear-%{_pearname}
Version:	0.1.2
Release:	2
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7a0ddf48d20338580319274cc57a06b6
URL:		http://pear.php.net/package/Validate_AR/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.2.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package contains locale validation for Argentina such as:
- Postal Code
- Region (provinces)

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet do sprawdzania poprawności dla Argentyny danych takich jak:
- kod pocztowy
- region (prowincje)

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/AR.php
