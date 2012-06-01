Summary:	EFL-based psplash replacement
Summary(pl.UTF-8):	Zamiennik psplasha oparty na EFL
Name:		exquisite
Version:	1.0.0
Release:	1
License:	BSD
Group:		Applications/Graphics
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	5d939d267d97230f0f772b17938ad2ab
URL:		http://trac.enlightenment.org/e/wiki/
BuildRequires:	ecore-devel >= 1.0.0
BuildRequires:	ecore-con-devel >= 1.0.0
BuildRequires:	ecore-evas-devel >= 1.0.0
BuildRequires:	ecore-fb-devel >= 1.0.0
BuildRequires:	edje >= 1.0.0
BuildRequires:	edje-devel >= 1.0.0
BuildRequires:	eina-devel >= 1.0.0
BuildRequires:	eet-devel >= 1.4.0
BuildRequires:	evas-devel >= 1.0.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Exquisite is a psplash replacement that is very simple and uses EFL
(Evas, Edje, Ecore etc.) for display - thus having immensely powerful
theme abilities without needing any platform-specific compiled themes
or modules. It is compatible with psplash with the same message
commands (and more). The difference is that it requires libraries like
evas, edje, ecore, eet... These also have loadable modules of their
own - thus this isn't perfect for systems that can't have these
libraries available and working at boot, but if you can, it's a lot
more capable than other splash engines, while still running in the
framebuffer.

%description -l pl.UTF-8
Exquisite to bardzo prosty zamiennik psplasha, wykorzystujący do
wyświetlania biblioteki EFL (Evas, Edje, Ecore itp.) - dzięki temu
mający ogromne możliwości dostosowywania motywów bez potrzeby
kompilowania motywów czy modułów w sposób zależny od platformy. Jest
kompatybilny z psplashem, ma te same polecenia. Różnica polega na tym,
że wymaga bibliotek takich jak evas, edje, ecore, eet... Te także mają
swoje moduły - więc nie jest to ideał dla systemów nie mających tych
bibliotek dostępnych w trakcie rozruchu, ale ma większe możliwości niż
inne silniki ekranów startowych, a nadal działa na framebufferze.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/exquisite
%attr(755,root,root) %{_bindir}/exquisite-write
%{_datadir}/exquisite
