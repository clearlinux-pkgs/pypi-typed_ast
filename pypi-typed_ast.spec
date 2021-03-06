#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-typed_ast
Version  : 1.5.4
Release  : 56
URL      : https://files.pythonhosted.org/packages/07/d2/d55702e8deba2c80282fea0df53130790d8f398648be589750954c2dcce4/typed_ast-1.5.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/07/d2/d55702e8deba2c80282fea0df53130790d8f398648be589750954c2dcce4/typed_ast-1.5.4.tar.gz
Summary  : a fork of Python 2 and 3 ast modules with type comment support
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-typed_ast-filemap = %{version}-%{release}
Requires: pypi-typed_ast-lib = %{version}-%{release}
Requires: pypi-typed_ast-license = %{version}-%{release}
Requires: pypi-typed_ast-python = %{version}-%{release}
Requires: pypi-typed_ast-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# Typed AST
[![Build Status](https://travis-ci.org/python/typed_ast.svg?branch=master)](https://travis-ci.org/python/typed_ast)
[![Chat at https://gitter.im/python/typed_ast](https://badges.gitter.im/python/typed_ast.svg)](https://gitter.im/python/typed_ast)

%package filemap
Summary: filemap components for the pypi-typed_ast package.
Group: Default

%description filemap
filemap components for the pypi-typed_ast package.


%package lib
Summary: lib components for the pypi-typed_ast package.
Group: Libraries
Requires: pypi-typed_ast-license = %{version}-%{release}
Requires: pypi-typed_ast-filemap = %{version}-%{release}

%description lib
lib components for the pypi-typed_ast package.


%package license
Summary: license components for the pypi-typed_ast package.
Group: Default

%description license
license components for the pypi-typed_ast package.


%package python
Summary: python components for the pypi-typed_ast package.
Group: Default
Requires: pypi-typed_ast-python3 = %{version}-%{release}

%description python
python components for the pypi-typed_ast package.


%package python3
Summary: python3 components for the pypi-typed_ast package.
Group: Default
Requires: pypi-typed_ast-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(typed_ast)

%description python3
python3 components for the pypi-typed_ast package.


%prep
%setup -q -n typed_ast-1.5.4
cd %{_builddir}/typed_ast-1.5.4
pushd ..
cp -a typed_ast-1.5.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656366646
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-typed_ast
cp %{_builddir}/typed_ast-1.5.4/LICENSE %{buildroot}/usr/share/package-licenses/pypi-typed_ast/5cba2695438a74e1f7a057b4fe6ec39bc444a0fc
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-typed_ast

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-typed_ast/5cba2695438a74e1f7a057b4fe6ec39bc444a0fc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
