# python3 support isn't added because twisted isn't ported yet

%global srcname alchimia

Name:       python-%{srcname}
Version:    0.4
Release:    1%{?dist}
Summary:    (SQLAlchemy - ORM) + Twisted = win

Group:      Development/Libraries
License:    The MIT License (MIT)
URL:        https://github.com/alex/%{srcname}
Source0:    https://pypi.python.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz


Buildarch: noarch


BuildRequires: python-setuptools
BuildRequires: pytest
BuildRequires: python-twisted
BuildRequires: python-sqlalchemy


Requires: python-sqlalchemy
Requires: python-twisted




%description
alchimia lets you use most of the SQLAlchemy-core API with Twisted,
it does not allow you to use the ORM.


%prep
%setup -q -n %{srcname}-%{version}


%check
%{__python} setup.py test


%build
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc README.rst
%{python_sitelib}/%{srcname}/
%{python_sitelib}/%{srcname}-%{version}-py*.egg-info/


%changelog
* Thu Oct 10 2013 Vladan Popovic - 0.4
- Initial package.
