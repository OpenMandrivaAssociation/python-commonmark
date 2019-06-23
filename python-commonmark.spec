%define oname   commonmark

# Workaround for the Requires: generator coming up with
# bogus ideas
%global __requires_exclude python[0-9\.]*dist\\(future\\)

Name:           python-%{oname}
Version:	0.9.0
Release:        1
Summary:        Python parser for the CommonMark Markdown spec

Source0:	https://files.pythonhosted.org/packages/ac/9d/a9ff7efaf06fb2b6fcc7a035760ba0971250832e37f0c554c335d86c160b/commonmark-0.9.0.tar.gz
License:        Python
Group:          Development/Python
Url:            https://recommonmark.readthedocs.io/en/latest/
BuildRequires:  python2-devel
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  python2-setuptools
BuildArch:	noarch

%description
CommonMark-py is a pure Python port of jgm’s commonmark.js,
a Markdown parser and renderer for the CommonMark
specification, using only native modules.

%package -n python2-commonmark
Summary: %{summary}
BuildRequires: python2-devel

%description -n python2-commonmark
CommonMark-py is a pure Python port of jgm’s commonmark.js,
a Markdown parser and renderer for the CommonMark
specification, using only native modules.

%prep
%setup -qc 
mv %{oname}-%{version} python2
cp -a python2 python3

%build
pushd python2
%{__python2} setup.py build
popd

pushd python3
python3 setup.py build
popd

%install
pushd python2
%{__python2} setup.py install --root=%{buildroot}
popd

pushd python3
%{__python} setup.py install --root=%{buildroot}
popd

%files
%{_bindir}/cmark
%{py_puresitedir}/commonmark-%{version}-*.egg-info
%{py_puresitedir}/commonmark*

%files -n python2-commonmark
%{py2_puresitedir}/commonmark-%{version}-*.egg-info
%{py2_puresitedir}/commonmark*
