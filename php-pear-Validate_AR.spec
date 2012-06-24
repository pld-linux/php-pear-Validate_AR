%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	AR
%define		_status		alpha
%define		_pearname	Validate_AR

Summary:	%{_pearname} - Validation class for Argentina
Summary(pl):	%{_pearname} - Klasa sprawdzaj�ca poprawno�� dla Argentyny
Name:		php-pear-%{_pearname}
Version:	0.0.1
Release:	1
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7c9e8bdd002cbb611fece3ddc4a697f7
URL:		http://pear.php.net/package/Validate_AR/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package contains locale validation for Argentina such as:
- Postal Code
- Region (provinces)

In PEAR status of this package is: %{_status}.

%description -l pl
Pakiet do sprawdzania poprawno�ci danych dla Argentyny:
- kod pocztowy
- region (prowincje)

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
