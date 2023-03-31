%define oname   commonmark

# Workaround for the Requires: generator coming up with
# bogus ideas
%global __requires_exclude python[0-9\.]*dist\\(future\\)

Name:           python-%{oname}
Version:	0.9.1
Release:	4
Summary:        Python parser for the CommonMark Markdown spec

Source0:	https://files.pythonhosted.org/packages/60/48/a60f593447e8f0894ebb7f6e6c1f25dafc5e89c5879fdc9360ae93ff83f0/%{oname}-%{version}.tar.gz
License:        Python
Group:          Development/Python
Url:            https://recommonmark.readthedocs.io/en/latest/
BuildRequires:  pkgconfig(python)
BuildRequires:  python-setuptools
BuildArch:	noarch
Obsoletes:	python2-%{oname}

%description
CommonMark-py is a pure Python port of jgm’s commonmark.js,
a Markdown parser and renderer for the CommonMark
specification, using only native modules.

%prep
%autosetup -n %{oname}-%{version}

%build
%py3_build

%install
%py3_install

%files
%dir %{py_puresitedir}/%{oname}
%{_bindir}/cmark
%{py_puresitedir}/%{oname}-%{version}-*.egg-info
%{py_puresitedir}/%{oname}/*
