Name:		kjv
Version:    0^2025012806efb21a7
Release:	1
Source0:	https://github.com/layeh/kjv/archive/06efb21a76ee0ab0030210c5abe3d72c84320aa9.tar.gz
Summary:	Read the Bible from your terminal 
URL:		https://github.com/layeh/kjv/
License:	Unlicense
Group:	    Text tools  	

Buildrequires: slibtool
Buildrequires: pkgconfig(readline)

Requires: readline


%description
Read the KJV Bible from your terminal

%prep
%autosetup -C 0 

%build
%set_build_flags \
%make_build

%install
mkdir -p %{buildroot}/usr/bin
cp kjv %{buildroot}/usr/bin

%files
/usr/bin/*
