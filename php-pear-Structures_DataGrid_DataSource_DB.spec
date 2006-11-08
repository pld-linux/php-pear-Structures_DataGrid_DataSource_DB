%include	/usr/lib/rpm/macros.php
%define		_class		Structures
%define		_subclass	DataGrid_DataSource_DB
%define		_status		beta
%define		_pearname	Structures_DataGrid_DataSource_DB
Summary:	%{_pearname} - DataSource driver using PEAR::DB result objects
Summary(pl):	%{_pearname} - sterownik DataSource dla obiekt�w PEAR::DB
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	381af1c616ce5b354c724c627b8fcab1
URL:		http://pear.php.net/package/Structures_DataGrid_DataSource_DB/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-DB >= 1.7.6
Requires:	php-pear-PEAR-core >= 1:1.4.9
Requires:	php-pear-Structures_DataGrid >= 0.7.0
Requires:	php-pear-Structures_DataGrid_DataSource_Array >= 0.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a DataSource driver for Structures_DataGrid using PEAR::DB
result objects.

Please note that this driver is deprecated. Consider using DBQuery or
MDB2 DataSource drivers instead.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet dostarcza sterownik DataSource do obiekt�w wynik�w PEAR::DB
dla Structures_DataGrid.

Prosze wzi�� pod uwag�, i� ten sterownik jest uznany jako niepolecany.
Zamiast niego lepiej u�y� sterownik�w DataSource DBQuery lub MDB2.

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
%{php_pear_dir}/Structures/DataGrid/DataSource/DB.php
