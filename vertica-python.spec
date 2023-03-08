Name:           vertica-python
Version:        1.3.1
Release:        1%{?dist}
Summary:        A native Python adapter for the Vertica database

Group:          Development/Languages
License:        MIT
URL:            https://github.com/uber/vertica-python
Source0:        https://github.com/uber/vertica-python/archive/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools


%global _description\
vertica-python is a native Python adapter for the Vertica\
(http://www.vertica.com) database.\


%package -n python3-vertica
Summary: %summary
Requires:       python3-dateutil >= 1.5
Requires:       python3-setuptools
Requires:       python3-pytz
Requires:       python3-future
%{?python_provide:%python_provide python3-vertica}
# Remove before F30
Provides: vertica-python3 = %{version}-%{release}
Obsoletes: vertica-python3 < %{version}-%{release}

%description -n python3-vertica %_description


%prep
%setup -q -n vertica-python-%{version}

%build
%py3_build

%install
%py3_install
%files -n python3-vertica
%license LICENSE
%doc README.md
%{python3_sitelib}/*.egg-info
%dir %{python3_sitelib}/vertica_python
%{python3_sitelib}/vertica_python/*

%changelog
* Web Mar 08 2023 Nghia Le <nghia.le@gooddata.com> - 1.0.0-1
- Build for EL9, No logner python2 support

* Tue Mar 31 2020 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.10.3-1
- Update to version 0.10.3

* Sun Dec 29 2019 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.10.1-1
- Update to version 0.10.1

* Fri Nov 29 2019 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.10.0-1
- Update to version 0.10.0
- support python3 by default

* Sun Jun 23 2019 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.9.3-1
- Update to version 0.9.3

* Fri May 10 2019 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.9.2-1
- Upgrade to version 0.9.2
- Remove of unnecessary requirement (psycopg2)

* Tue Apr 02 2019 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.9.1-1
- Upgrade to version 0.9.1
- Fix bad EPEL dependencies of python2 package

* Tue Apr 02 2019 Troy Dawson <tdawson@redhat.com> - 0.8.2-2
- Rebuilt to change main python from 3.4 to 3.6

* Tue Feb 19 2019 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.8.2-1
- Upgrade to version 0.8.2

* Mon Sep 03 2018 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.7.4-1
- Upgrade to version 0.7.4
- Build python 3 subpackage even on RHEL >= 7

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.3-2
- Rebuilt for Python 3.7

* Tue Mar 27 2018 Jan Beran <jberan@redhat.com> - 0.7.3-1
- Update to version 0.7.3 including Python 3 subpackage

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.14-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.6.14-3
- Python 2 binary package renamed to python2-vertica
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 21 2017 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.6.14-1
- Update to version 0.6.14

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.5.5-1
- update to version 0.5.5

* Tue Dec 01 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.5.4-1
- update to version 0.5.4

* Wed Sep 23 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.5.1-1
- update to version 0.5.1

* Fri Jul 03 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.5.0-1
- update to version 0.5.0

* Mon Jun 22 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.4.6-1
- update to version 0.4.6

* Tue Jun 16 2015 Jakub Jedelsky <jakub.jedelsky@gamil.com> - 0.4.5-1
- update to version 0.4.5

* Wed Apr 15 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.3.6-1
- update to version 0.3.6

* Wed Apr 08 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.3.5-1
- update to version 0.3.5

* Wed Jan 21 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.3.4-1
- update to version 0.3.4

* Wed Oct 15 2014 Jakub Jedelsky <jakub.jedelsky@gooddata.com> - 0.3.0-1
- update to version 0.3.0

* Fri Jun 13 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.2.3-1
- update to new version

* Thu Apr 24 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.2.1-1
- new version update

* Fri Mar 28 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.2.0-4
- remove buildrood tag
- edit dateutil patch for el6

* Wed Mar 26 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.2.0-3
- package is not ready for python3 

* Wed Mar 26 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.2.0-2
- python-setuptools is required only on rhel<=6

* Mon Mar 24 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.2.0-1
- Initial package
