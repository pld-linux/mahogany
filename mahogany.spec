Summary:	The Email Client
Summary(pl):	Klient poczty
Name:		mahogany
Version:	0.62
Release:	2
License:	Mahogany Artistic or GPL
Group:		Applications/Mail
Source0:	http://ftp1.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-confmake.patch
URL:		http://mahogany.sourceforge.net/
Icon:		mahogany.gif
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	openssl-devel
BuildRequires:	wxGTK-devel >= 2.2.6
BuildRequires:	latex2html >= 99.2beta8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This package contains Mahogany, a powerful, scriptable GUI mail and
news client using GTK+ toolkit. Mahogany supports remote POP3, IMAP4,
NNTP servers as well as local MBOX and news spool folders and sending
mail using SMTP or local MTA.

%description -l pl
Klient poczty i wiadomo¶ci USENET o ogromnych mo¿liwo¶ciach u¿ywaj±cy
GTK+. Mahogany obs³uguje protoko³u POP3, IMAP3, NNTP jak równie¿
lokalne spoole poczty i wiadomo¶ci USENET oraz wysy³anie poprzez
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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
