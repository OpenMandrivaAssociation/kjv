%global debug_package %{nil}

Name:       kjv
Version:    1.0.0
Release:	1
Source0:	https://github.com/StudebakerGuy/kjv_source/archive/refs/tags/%{version}.tar.gz
Summary:	Read the Bible from your terminal 
URL:		https://github.com/layeh/kjv/
License:    Unlicense
Group:      Text tools

BuildRequires:  slibtool
BuildRequires:  pkgconfig(readline)

Requires:  readline

%description
Read and search the KJV Bible in your your terminal.

This is a fork of https://github.com/layeh/kjv/ to add semantic versioning. 

%prep
%setup -n kjv_source-%{version} 

%build
%make_build

%install
install -D -p -m 0755 %{name}   %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license	LICENSE
%doc		README.md
