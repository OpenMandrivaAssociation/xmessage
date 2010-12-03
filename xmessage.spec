Name: xmessage
Version: 1.0.3
Release: %mkrel 2
Summary: Display a message or query in a window 
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xmessage
%{_datadir}/X11/app-defaults/Xmessage-color
%{_datadir}/X11/app-defaults/Xmessage
%{_mandir}/man1/xmessage.1*
