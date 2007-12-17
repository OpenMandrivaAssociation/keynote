%define	major 0
%define libname	%mklibname keynote %{major}

Summary:	Decentralized Trust-Management system
Name:		keynote
Version:	2.3
Release:	%mkrel 2
License:	BSD
Group:		System/Libraries
URL:		http://www.cis.upenn.edu/~keynote/
Source0:	http://www.cis.upenn.edu/~keynote/Code/keynote-%{version}.tar.bz2
Patch0:		keynote_2.3-11.diff.bz2
BuildRequires:	openssl-devel
BuildRequires:	flex
BuildRequires:	bison

%description
The KeyNote architecture and language are useful as building blocks for the
trust management aspects of a variety of Internet protocols and services.

This package contains the keynote binary used to generate and verify
KeyNote assertions.

%package -n	%{libname}
Summary:	Decentralized Trust-Management system, shared library
Group:          System/Libraries

%description -n	%{libname}
The KeyNote architecture and language are useful as building blocks for the
trust management aspects of a variety of Internet protocols and services.

%package -n	%{libname}-devel
Summary:	Decentralized Trust-Management system, development files
Group:		Development/C
Obsoletes:	lib%{name}-devel %{name}-devel
Provides:	lib%{name}-devel %{name}-devel
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
The KeyNote architecture and language are useful as building blocks for the
trust management aspects of a variety of Internet protocols and services.

This Package contains all the files and documentation needed to use the
KeyNote library in own applications.

%prep

%setup -q
%patch0 -p1

%build

%configure2_5x

make CFLAGS="%{optflags} -Wall"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING HOWTO.add.crypto LICENSE README TODO doc/rfc*.txt
%attr(0755,root,root) %{_bindir}/keynote
%{_mandir}/man1/*
%{_mandir}/man4/*
%{_mandir}/man5/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_includedir}/*.*
%{_mandir}/man3/*

