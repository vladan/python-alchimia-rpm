# python3 support isn't added because twisted isn't ported yet

%global srcname alchimia

Name:       python-%{srcname}
Version:    0.4
Release:    3%{?dist}
Summary:    A Python library that integrates Twisted with SqlAlchemy

Group:      Development/Libraries
License:    MIT
URL:        https://github.com/alex/%{srcname}
Source0:    https://pypi.python.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz


BuildArch: noarch


BuildRequires: python-setuptools
BuildRequires: pytest
BuildRequires: python-twisted
BuildRequires: python-sqlalchemy
BuildRequires: python-pbr
BuildRequires: python2-devel


Requires: python-sqlalchemy
Requires: python-twisted


%description
alchimia lets you use most of the SQLAlchemy-core API with Twisted,
it does not allow you to use the ORM.


%prep
%setup -q -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info
rm -f {test-,}requirements.txt


%check
%{__python2} setup.py test


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%doc README.rst AUTHORS CONTRIBUTING.rst LICENSE ChangeLog
%{python2_sitelib}/%{srcname}/
%{python2_sitelib}/%{srcname}-%{version}-py*.egg-info/


%changelog
* Wed Oct 16 2013 0.4-3
- Add build requirements python-pbr and python-devel
- Move the deletion of unneeded files in the prep section
- Remove requirements.txt and test-requirements.txt

* Wed Oct 16 2013 Vladan Popovic <vpopovic@redhat.com> - 0.4-2
- Remove prebuilt package egg
- Remove EPEL5 parts
- Shorten the licence name (only MIT)
- Change the summary
- Add files to %%doc
- Fix typo Buildarch -> BuildArch

* Thu Oct 10 2013 Vladan Popovic <vpopovic@redhat.com> - 0.4-1
- Initial package.
