Name: xmessage
Version: 1.0.4
Release: 9
Summary: Display a message or query in a window 
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: pkgconfig(xaw7) >= 1.0.1
BuildRequires: pkgconfig(xt) >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The xmessage program displays a window containing a message from the command
line, a file, or standard input

%prep
%setup -q

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
