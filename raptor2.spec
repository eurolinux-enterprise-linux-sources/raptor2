
Summary: RDF Parser Toolkit for Redland
Name:    raptor2
Version: 2.0.9
Release: 1%{?dist}

License: GPLv2+ or LGPLv2+ or ASL 2.0
Source:  http://download.librdf.org/source/raptor2-%{version}.tar.gz
URL:     http://librdf.org/raptor/

## upstreamable patches

BuildRequires: curl-devel
BuildRequires: gtk-doc
BuildRequires: libicu-devel
BuildRequires: pkgconfig(libxslt)
BuildRequires: yajl-devel

# when /usr/bin/rappor moved here  -- rex
Conflicts: raptor < 1.4.21-10

%description
Raptor is the RDF Parser Toolkit for Redland that provides
a set of standalone RDF parsers, generating triples from RDF/XML
or N-Triples.

%package devel
Summary: Development files for %{name} 
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
%setup -q

# hack to nuke rpaths
%if "%{_libdir}" != "/usr/lib"
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure
%endif


%build
%configure \
  --disable-static --enable-release \
  --with-icu-config=/usr/bin/icu-config

make %{?_smp_mflags}


%install
rm -rf %{buildroot} 

make DESTDIR=%{buildroot} install

## unpackaged files
rm -fv %{buildroot}%{_libdir}/lib*.la


%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion raptor2)" = "%{version}"
make check 


%clean
rm -rf %{buildroot} 


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog NEWS README
%doc COPYING* LICENSE.txt LICENSE-2.0.txt
%{_libdir}/libraptor2.so.0*
%{_bindir}/rapper
%{_mandir}/man1/rapper*

%files devel
%doc UPGRADING.html
%{_includedir}/raptor2/
%{_libdir}/libraptor2.so
%{_libdir}/pkgconfig/raptor2.pc
%{_mandir}/man3/libraptor2*
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/raptor2/


%changelog
* Tue Mar 26 2013 Rex Dieter <rdieter@fedoraproject.org> 2.0.9-1
- 2.0.9
- BR: libicu-devel

* Tue Feb 19 2013 Rex Dieter <rdieter@fedoraproject.org> 2.0.8-1
- 2.0.8

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 23 2012 Rex Dieter <rdieter@fedoraproject.org> 2.0.7-1
- 2.0.7

* Mon Mar 05 2012 Rex Dieter <rdieter@fedoraproject.org> 2.0.6-1
- 2.0.6

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.4-3
- rebuild (yajl)
- pkgconfig-style deps

* Sun Jul 31 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.4-2
- include rapper here

* Fri Jul 29 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.4-1
- 2.0.4

* Fri Jul 29 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.3-3
- upstream patch to fix build against newer libcurl

* Tue Jul 26 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.3-2
- -devel: drop Group: tag
- add lot's of %%doc's
- License: GPLv2+ or LGPLv2+ or ASL 2.0 (or newer)

* Sat Jul 23 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.3-1
- first try


