Name: xmessage
Version: 1.0.2
Release: %mkrel 2
Summary: Display a message or query in a window 
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros	>= 1.1.5
BuildRequires: libxaw-devel	>= 1.0.4

%description
The xmessage program displays a window containing a message from the command
line, a file, or standard input

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -ifs
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

#

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xmessage
%{_datadir}/X11/app-defaults/Xmessage-color
%{_datadir}/X11/app-defaults/Xmessage
%{_mandir}/man1/xmessage.1*
