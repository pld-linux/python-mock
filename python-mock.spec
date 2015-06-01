#
# Conditional build:
%bcond_without	doc		# don't build doc
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	mock
Summary:	A Python Mocking and Patching Library for Testing
Summary(pl.UTF-8):	Biblioteka Pythona do testów przy użyciu techniki "mock" i łatania
Name:		python-%{module}
Version:	1.0.1
Release:	4
License:	BSD-like
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/m/mock/%{module}-%{version}.tar.gz
# Source0-md5:	c3971991738caa55ec7c356bbc154ee2
URL:		http://python-mock.sourceforge.net/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.228
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
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

mock is tested on Python versions 2.4-2.7 and Python 3. mock is also
tested with the latest versions of Jython and pypy.

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

mock jest testowany z Pythonem w wersjach 2.4-2.7 oraz 3, a także z
najnowszymi wersjami Jythona i pypy.

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

mock is tested on Python versions 2.4-2.7 and Python 3. mock is also
tested with the latest versions of Jython and pypy.

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

mock jest testowany z Pythonem w wersjach 2.4-2.7 oraz 3, a także z
najnowszymi wersjami Jythona i pypy.

Moduł mock udostępnia także funkcje/obiekty narzędziowe pomagające
przy testowaniu, w szczególności łataniu.

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%{__python} setup.py build --build-base build-2
%endif

%if %{with python3}
%{__python3} setup.py build --build-base build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt
%{py_sitescriptdir}/mock.py[co]
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt
%{py3_sitescriptdir}/mock.py
%{py3_sitescriptdir}/__pycache__/mock.*
%{py3_sitescriptdir}/%{module}-*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc html/*
%endif
