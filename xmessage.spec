Name: xmessage
Version: 1.0.4
Release: 5
Summary: Display a message or query in a window 
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: libxaw-devel >= 1.0.1
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The xmessage program displays a window containing a message from the command
line, a file, or standard input

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/xmessage
%{_datadir}/X11/app-defaults/Xmessage-color
%{_datadir}/X11/app-defaults/Xmessage
%{_mandir}/man1/xmessage.1*


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-3mdv2011.0
+ Revision: 671343
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdv2011.0
+ Revision: 608220
- rebuild

* Sat Jan 30 2010 Frederik Himpe <fhimpe@mandriva.org> 1.0.3-1mdv2010.1
+ Revision: 498509
- update to new version 1.0.3

* Mon Apr 13 2009 Funda Wang <fwang@mandriva.org> 1.0.2-4mdv2009.1
+ Revision: 366742
- no more autoconf

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-3mdv2009.0
+ Revision: 226064
- rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-2mdv2008.1
+ Revision: 154404
- Updated BuildRequires and resubmit package.
- Choose default Xaw from xaw.m4 unless configure explicitly told otherwise.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 10 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.2-1mdv2008.0
+ Revision: 61366
- new upstream release: 1.0.4


* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 20:58:33 (59486)
- rebuild to fix libXaw.so.8 dependency

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-30 21:31:16 (31770)
- better description

* Tue May 30 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-30 21:11:11 (31759)
- rebuild against new libXaw package\n- fixed description

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

