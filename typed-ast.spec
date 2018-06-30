#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : typed-ast
Version  : 1.1.0
Release  : 8
URL      : https://pypi.python.org/packages/52/cf/2ebc7d282f026e21eed4987e42e10964a077c13cfc168b42f3573a7f178c/typed-ast-1.1.0.tar.gz
Source0  : https://pypi.python.org/packages/52/cf/2ebc7d282f026e21eed4987e42e10964a077c13cfc168b42f3573a7f178c/typed-ast-1.1.0.tar.gz
Summary  : a fork of Python 2 and 3 ast modules with type comment support
Group    : Development/Tools
License  : Apache-2.0
Requires: typed-ast-python3
Requires: typed-ast-python
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
parser similar to the standard `ast` library.  Unlike `ast`, the parsers in
        `typed_ast` include PEP 484 type comments and are independent of the version of
        Python under which they are run.  The `typed_ast` parsers produce the standard
        Python AST (plus type comments), and are both fast and correct, as they are
        based on the CPython 2.7 and 3.6 parsers.

%package python
Summary: python components for the typed-ast package.
Group: Default
Requires: typed-ast-python3

%description python
python components for the typed-ast package.


%package python3
Summary: python3 components for the typed-ast package.
Group: Default
Requires: python3-core

%description python3
python3 components for the typed-ast package.


%prep
%setup -q -n typed-ast-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513351386
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
