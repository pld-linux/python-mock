# TODO
# - better group
%define 	module	mock
Summary:	A Python Mocking and Patching Library for Testing
Name:		python-%{module}
Version:	0.7.2
Release:	0.1
License:	BSD-like
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/m/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	0e63747b20e67f7d3e563bc6fd5b88d3
URL:		http://python-mock.sourceforge.net/
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.228
Requires(post,preun):	/sbin/chkconfig
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mock is a Python module that provides a core Mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set
needed attributes in the normal way.

mock is tested on Python versions 2.4-2.7 and Python 3.

The mock module also provides utility functions / objects to assist with
testing, particularly monkey patching.

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
%doc README* docs

%{py_sitescriptdir}/%{module}.*
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-infoock
%endif
