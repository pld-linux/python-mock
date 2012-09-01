%define 	module	mock
Summary:	A Python Mocking and Patching Library for Testing
Summary(pl.UTF-8):	Biblioteka Pythona do testów przy użyciu techniki "mock" i łatania
Name:		python-%{module}
Version:	0.8.0
Release:	1
License:	BSD-like
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/m/mock/%{module}-%{version}.tar.gz
# Source0-md5:	b1ac87a1ceab295aef11dcfc104a7a4a
URL:		http://python-mock.sourceforge.net/
BuildRequires:	python-devel >= 2.4
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.228
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

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt html
%{py_sitescriptdir}/mock.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
