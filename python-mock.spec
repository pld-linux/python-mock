#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module
%bcond_with	tests	# test target

%define		module	mock
Summary:	A Python Mocking and Patching Library for Testing
Summary(pl.UTF-8):	Biblioteka Pythona do testów przy użyciu techniki "mock" i łatania
Name:		python-%{module}
Version:	2.0.0
Release:	4
License:	BSD-like
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/mock/
Source0:	https://files.pythonhosted.org/packages/source/m/mock/%{module}-%{version}.tar.gz
# Source0-md5:	0febfafd14330c9dcaa40de2d82d40ad
URL:		http://python-mock.sourceforge.net/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-pbr >= 1.3
BuildRequires:	python-setuptools >= 17.1
%if %{with tests}
BuildRequires:	python-funcsigs >= 1
BuildRequires:	python-six >= 1.9
BuildRequires:	python-unittest2 >= 1.1.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-pbr >= 1.3
BuildRequires:	python3-setuptools >= 17.1
%if %{with doc} || %{with tests}
%if "%{py3_ver}" < "3.3"
BuildRequires:	python3-funcsigs >= 1
%endif
BuildRequires:	python3-six >= 1.9
%endif
%{?with_tests:BuildRequires:	python3-unittest2 >= 1.1.0}
%endif
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mock is a library for testing in Python. It allows you to replace
parts of your system under test with mock objects and make assertions
about how they have been used.

mock provides a core `MagicMock` class removing the need to create a
host of stubs throughout your test suite. After performing an action,
you can make assertions about which methods/attributes were used and
arguments they were called with. You can also specify return values
and set needed attributes in the normal way.

The mock module also provides utility functions/objects to assist with
testing, particularly monkey patching.

%description -l pl.UTF-8
mock to biblioteka do testowania w Pythonie. Pozwala na zastępowanie
części testowanego systemu obiektami "mock" oraz sprawdzania zapewnień
(assert) o tym, jak zostały użyte.

mock udostępnia klasę główną "MagicMock", dzięki której nie trzeba
tworzyć systemu zaślepek do testów. W czasie wykonywania akcji można
kontrolować, czy odpowiednie metody/atrybuty zostały użyte i z jakimi
argumentami. Można określić zwracane wartości i w zwykły sposób
ustawiać potrzebne atrybuty.

Moduł mock udostępnia także funkcje/obiekty narzędziowe pomagające
przy testowaniu, w szczególności łataniu.

%package -n python3-%{module}
Summary:	A Python Mocking and Patching Library for Testing
Summary(pl.UTF-8):	Biblioteka Pythona do testów przy użyciu techniki "mock" i łatania
Group:		Development/Languages/Python

%description -n python3-%{module}
mock is a library for testing in Python. It allows you to replace
parts of your system under test with mock objects and make assertions
about how they have been used.

mock provides a core `MagicMock` class removing the need to create a
host of stubs throughout your test suite. After performing an action,
you can make assertions about which methods/attributes were used and
arguments they were called with. You can also specify return values
and set needed attributes in the normal way.

The mock module also provides utility functions/objects to assist with
testing, particularly monkey patching.

%description -n python3-%{module} -l pl.UTF-8
mock to biblioteka do testowania w Pythonie. Pozwala na zastępowanie
części testowanego systemu obiektami "mock" oraz sprawdzania zapewnień
(assert) o tym, jak zostały użyte.

mock udostępnia klasę główną "MagicMock", dzięki której nie trzeba
tworzyć systemu zaślepek do testów. W czasie wykonywania akcji można
kontrolować, czy odpowiednie metody/atrybuty zostały użyte i z jakimi
argumentami. Można określić zwracane wartości i w zwykły sposób
ustawiać potrzebne atrybuty.

Moduł mock udostępnia także funkcje/obiekty narzędziowe pomagające
przy testowaniu, w szczególności łataniu.

%package apidocs
Summary:	API documentation for mock module
Summary(pl.UTF-8):	Dokumentacja API modułu mock
Group:		Documentation

%description apidocs
API documentation for mock module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu mock.

%prep
%setup -q -n %{module}-%{version}

# avoid rewriting by pbr
chmod a-w AUTHORS ChangeLog

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
PYTHONPATH=. sphinx-build-3 -b html docs html
%{__rm} -r html/{_sources,.doctrees,.buildinfo}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install

# pythonegg dependency generator resolves conditionals for requires() based on
# python version that runs the generator, not the version egg is targeted;
# avoid generation of python3egg(funcsigs) dependency for python >= 3.3
%{__sed} -i -e '/^\[:(python_version<"3.3")]/,/^$/d' $RPM_BUILD_ROOT%{py3_sitescriptdir}/mock-%{version}-py*.egg-info/requires.txt
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE.txt NEWS README.rst
%{py_sitescriptdir}/mock
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE.txt NEWS README.rst
%{py3_sitescriptdir}/mock
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc html/*
%endif
