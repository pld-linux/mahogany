Summary:	The Email Client
Summary(pl.UTF-8):	Klient poczty
Name:		mahogany
Version:	0.66
Release:	2
License:	Mahogany Artistic or GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/mahogany/%{name}-%{version}.tar.bz2
# Source0-md5:	1e0a7a6dfcc8e35bdf570e1fe198d7bb
Patch0:		%{name}-confmake.patch
URL:		http://mahogany.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	glib-devel
BuildRequires:	latex2html >= 99.2beta8
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	wxGTK-devel >= 2.2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This package contains Mahogany, a powerful, scriptable GUI mail and
news client using GTK+ toolkit. Mahogany supports remote POP3, IMAP4,
NNTP servers as well as local MBOX and news spool folders and sending
mail using SMTP or local MTA.

%description -l pl.UTF-8
Klient poczty i wiadomości USENET o ogromnych możliwościach używający
GTK+. Mahogany obsługuje protokoły POP3, IMAP3, NNTP jak również
lokalne spoole poczty i wiadomości USENET oraz wysyłanie poprzez
zdalny serwer SMTP lub lokalny.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I ./
%{__autoconf}
%configure \
	--with-threads \
	--without-debug \
	--with-modules=dynamic \
	--with-ssl=/usr

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGES CREDITS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_applnkdir}/*/*/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man*/*
