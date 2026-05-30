%define module commonmark

# package is now deprecated by upstream after this v0.9.2 release.
# see notice on https://github.com/readthedocs/commonmark.py
# python-markdown-it-py is recommended as a replacement.

Name:		python-commonmark
Version:	0.9.2
Release:	1
Summary:	Python parser for the CommonMark Markdown spec
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://recommonmark.readthedocs.io
Source0:	https://files.pythonhosted.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:  python%{pyver}dist(setuptools)
Obsoletes:	python2-%{module}

%description
Warning: commonmark.py is now deprecated. We recommend using markdown-it-py
for a commonmark parser going forward.

This package is only provided for backwards compatibility for python packages
yet to move away from using this module.

------

CommonMark-py is a pure Python port of jgm’s commonmark.js,
a Markdown parser and renderer for the CommonMark
specification, using only native modules.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%{_bindir}/cmark
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}-*.egg-info
