#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : typed_ast
Version  : 1.4.1
Release  : 33
URL      : https://files.pythonhosted.org/packages/18/09/b6a6b14bb8c5ec4a24fe0cf0160aa0b784fd55a6fd7f8da602197c5c461e/typed_ast-1.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/18/09/b6a6b14bb8c5ec4a24fe0cf0160aa0b784fd55a6fd7f8da602197c5c461e/typed_ast-1.4.1.tar.gz
Summary  : a fork of Python 2 and 3 ast modules with type comment support
Group    : Development/Tools
License  : Apache-2.0
Requires: typed_ast-license = %{version}-%{release}
Requires: typed_ast-python = %{version}-%{release}
Requires: typed_ast-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
parser similar to the standard `ast` library.  Unlike `ast`, the parsers in
        `typed_ast` include PEP 484 type comments and are independent of the version of
        Python under which they are run.  The `typed_ast` parsers produce the standard
        Python AST (plus type comments), and are both fast and correct, as they are
        based on the CPython 2.7 and 3.6 parsers.

%package license
Summary: license components for the typed_ast package.
Group: Default

%description license
license components for the typed_ast package.


%package python
Summary: python components for the typed_ast package.
Group: Default
Requires: typed_ast-python3 = %{version}-%{release}

%description python
python components for the typed_ast package.


%package python3
Summary: python3 components for the typed_ast package.
Group: Default
Requires: python3-core
Provides: pypi(typed_ast)

%description python3
python3 components for the typed_ast package.


%prep
%setup -q -n typed_ast-1.4.1
cd %{_builddir}/typed_ast-1.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603406660
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/typed_ast
cp %{_builddir}/typed_ast-1.4.1/LICENSE %{buildroot}/usr/share/package-licenses/typed_ast/5cba2695438a74e1f7a057b4fe6ec39bc444a0fc
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/typed_ast/5cba2695438a74e1f7a057b4fe6ec39bc444a0fc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
