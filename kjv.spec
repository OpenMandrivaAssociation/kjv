Name:		kjv
Version:    1.0.0
Release:	1
Source0:	https://github.com/StudebakerGuy/kjv/archive/refs/tags/1.0.0.tar.gz
Summary:	Read the Bible from your terminal 
URL:		https://github.com/layeh/kjv/
License:	Unlicense
Group:	    Text tools  	

BuildRequires: slibtool
BuildRequires: pkgconfig(readline)

Requires: readline


%description
Read the KJV Bible from your terminal.

This is a fork of https://github.com/layeh/kjv/ 

%prep
%autosetup -C 0 

%build
%set_build_flags \
%make_build

%install
install -D -p -m 0755 %{name}     %{buildroot}%{_bindir}/%{name}
install -D -p -m 0644 LICENSE %{buildroot}%{_defaultlicensedir}/%{name}/LICENSE

%files
%{_bindir}/%{name}
%{_defaultlicensedir}/%{name}/LICENSE
