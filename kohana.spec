Summary: KohanaPHP
Name: kohana3.1
Version: 3.1.2
Release: 3
Group: Web/Frameworks
License: BSD
URL: http://kohanaframework.org/
Source0: kohana-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: php >= 5.2.3, webserver
Packager: Kohana Team <team@kohanaframework.org>
BuildArch: noarch
Requires: kohana3.1-core = %{version}-%{release}
Requires: kohana3.1-mod-auth = %{version}-%{release}
Requires: kohana3.1-mod-cache = %{version}-%{release}
Requires: kohana3.1-mod-codebench = %{version}-%{release}
Requires: kohana3.1-mod-database = %{version}-%{release}
Requires: kohana3.1-mod-image = %{version}-%{release}
Requires: kohana3.1-mod-orm = %{version}-%{release}
Requires: kohana3.1-mod-unittest = %{version}-%{release}
Requires: kohana3.1-mod-userguide = %{version}-%{release}

%description
Kohana is an elegant HMVC PHP5 framework that provides 
a rich set of components for building web applications.

%package core
Summary: Kohana Core
Group: Web/Frameworks

%description core
Kohana is an elegant HMVC PHP5 framework that provides 
a rich set of components for building web applications.

Core Classes

%package mod-auth
Summary: Kohana Auth Module
Group: Web/Frameworks
Requires: kohana3.1-core = %{version}-%{release}

%description mod-auth
Kohana is an elegant HMVC PHP5 framework that provides 
a rich set of components for building web applications.

Auth Module

%package mod-cache
Summary: Kohana Cache Module
Group: Web/Frameworks
Requires: kohana3.1-core = %{version}-%{release}

%description mod-cache
Kohana is an elegant HMVC PHP5 framework that provides 
a rich set of components for building web applications.

Cache Module

%package mod-codebench
Summary: Kohana Codebench Module
Group: Web/Frameworks
Requires: kohana3.1-core = %{version}-%{release}

%description mod-codebench
Kohana is an elegant HMVC PHP5 framework that provides 
a rich set of components for building web applications.

Codebench Module

%package mod-database
Summary: Kohana Database Module
Group: Web/Frameworks
<<<<<<< HEAD
Requires: kohana3.1-core = %{version}-%{release}
=======
Requires: kohana3.0-core = %{version}-%{release}
>>>>>>> 3.0/master
Requires: php-mysql

%description mod-database
Kohana is an elegant HMVC PHP5 framework that provides 
a rich set of components for building web applications.

Database Module

%package mod-image
Summary: Kohana Image Module
Group: Web/Frameworks
<<<<<<< HEAD
Requires: kohana3.1-core = %{version}-%{release}, php-mysql
=======
Requires: kohana3.0-core = %{version}-%{release}, php-mysql
>>>>>>> 3.0/master
Requires: php-gd

%description mod-image
Kohana is an elegant HMVC PHP5 framework that provides 
a rich set of components for building web applications.

Image Module

%package mod-orm
Summary: Kohana ORM Module
Group: Web/Frameworks
Requires: kohana3.1-core = %{version}-%{release}
Requires: kohana3.1-mod-database = %{version}-%{release}

%description mod-orm
Kohana is an elegant HMVC PHP5 framework that provides 
a rich set of components for building web applications.

ORM Module

%package mod-unittest
Summary: Kohana Unittest Module
Group: Web/Frameworks
Requires: kohana3.1-core = %{version}-%{release}

%description mod-unittest
Kohana is an elegant HMVC PHP5 framework that provides 
a rich set of components for building web applications.

Unittest Module

%package mod-userguide
Summary: Kohana Userguide Module
Group: Web/Frameworks
<<<<<<< HEAD
Requires: kohana3.1-core = %{version}-%{release}, php-pear-PHPUnit
=======
Requires: kohana3.0-core = %{version}-%{release}, php-pear-PHPUnit
>>>>>>> 3.0/master

%description mod-userguide
Kohana is an elegant HMVC PHP5 framework that provides 
a rich set of components for building web applications.

Userguide Module

%prep
%setup -q -n kohana-%{version}

%install
rm -rf %{buildroot}
%{__install} -d -m0755  %{buildroot}/usr/share/php/kohana3.1
%{__install} -d -m0755  %{buildroot}/usr/share/php/kohana3.1/modules/
cp -R system %{buildroot}/usr/share/php/kohana3.1/system
cp -R modules/* %{buildroot}/usr/share/php/kohana3.1/modules/

%clean
rm -rf %{buildroot}

%files
%dir /usr/share/php/kohana3.1

%files core
/usr/share/php/kohana3.1/system

%files mod-auth
/usr/share/php/kohana3.1/modules/auth

%files mod-cache
/usr/share/php/kohana3.1/modules/cache

%files mod-codebench
/usr/share/php/kohana3.1/modules/codebench

%files mod-database
/usr/share/php/kohana3.1/modules/database

%files mod-image
/usr/share/php/kohana3.1/modules/image

%files mod-orm
/usr/share/php/kohana3.1/modules/orm

%files mod-unittest
/usr/share/php/kohana3.1/modules/unittest

%files mod-userguide
/usr/share/php/kohana3.1/modules/userguide

%changelog
* Thu Apr 28 2011 Kohana Team <team@kohanaframework.org>
- First packaging

