Summary:	The GNU version of the awk text processing utility
Summary(de):	Die GNU-Version des AWK-Textverarbeitungsutilitys
Summary(es):	Utilitarios GNU para manipulaci�n de archivos texto
Summary(fr):	Traitement de texte des utilitaires GNU
Summary(ja):	GNU �С������� awk �ƥ����Ƚ����桼�ƥ���ƥ���
Summary(pl):	Wersja GNU awk - narz�dzia do obr�bki tekst�w
Summary(pt_BR):	Utilit�rios GNU para manipula��o arquivos texto
Summary(ru):	GNU ������ ������� ��������� ������� awk
Summary(tr):	GNU ara�lar� metin d�zenleyici
Summary(uk):	GNU ���Ӧ� ���̦�� ������� ����Ԧ� awk
Name:		gawk
Version:	3.1.3
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	a116eec17e7ba085febb74c7758823bd
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	80753d75be0f469f70e8c90e75121a9c
Source2:	%{name}-pl.po
Patch0:		%{name}-info.patch
Patch1:		%{name}-shutup.patch
Patch2:		%{name}-pmake.patch
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1.7
BuildRequires:	texinfo >= 4.3
BuildRequires:	gettext-devel
Requires:	mktemp
Requires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gawk-doc

%define		_libexecdir	%{_prefix}/lib

%description
The gawk packages contains the GNU version of awk, a text processing
utility. Awk interprets a special-purpose programming language to do
quick and easy text pattern matching and reformatting jobs. Gawk
should be upwardly compatible with the Bell Labs research version of
awk and is almost completely compliant with the 1993 POSIX 1003.2
standard for awk.

%description -l de
Das gawk-Paket enth�lt die GNU-Version von awk, einem
Textverarbeitungs-Utility. Awk interpretiert eine spezielle
Programmiersprache, um Textmuster zu suchen, und neu zu formatieren.
Gawk ist kompatibel zu der Bell Labs research-Version von awk, und ist
fast kompatibel zum 1993 POSIX 1003.2-awk-Standard.

%description -l es
Este es el GNU Awk. Debe ser compatible con la versi�n de pesquisa de
awk del Bell Labs. Es casi completamente vinculado con el padr�n 1993
POSIX 1003.2 para awk. Gawk puede ser usado para procesar archivos
texto y se considera una herramienta padr�n del Linux.

%description -l fr
awk de GNU, compatible vers le haut avec les versions awk des Bell
Labs. Il est presque totalement conforme au standard 1993 POSIX 1003.2
de awk.

%description -l ja
gawk �ѥå������� GNU �С������Ρ��ƥ����Ƚ����桼�ƥ���ƥ���
�Ǥ��� awk ��ޤ�Ǥ��ޤ���awk �����᤯���ưפʥѥ�����ޥå��󥰤�
���������򤹤뤿����ü����Ū�θ���Ǥ���gawk �ϥ٥븦�ΥС�������
awk �Ⱦ�̸ߴ��ǡ�awk �� 1993 POSIX 1003.2 ɸ��˴����˹��פ��ޤ���

%description -l pl
Pakiet zawiera implementacj� GNU interpretera j�zyka awk, kt�ry
powinien by� kompatybilny z aplikacj� o tej samej nazwie zrobion�
przez Bell Labs. GNU awk jest w pe�ni zgodny ze standardem 1993 POSIX
1003.2.

Gawk (GNU awk) jest zaawansowanym j�zykiem skryptowym, doskonale
nadaj�cym si� do obr�bki plik�w tekstowych. Jest to jedno z
podstawowych narz�dzi systemu Linux.

%description -l pt_BR
Este � o GNU Awk. Ele deve ser compat�vel com a vers�o de pesquisa de
awk do Bell Labs. Ele � quase completamente vinculado com o padr�o
1993 POSIX 1003.2 para awk. Gawk pode ser usado para processar
arquivos texto e � considerado uma ferramenta padr�o do Linux.

%description -l ru
����� gawk �������� GNU ������ awk, ������� ��������� �������. awk
�������������� ������������������ ���� ���������������� ��� �������� �
������� ���������� ����� �� ������������� � ��������� �
������������������ �������. Gawk ������ ���� ��������� � ������� awk
�� Bell Labs � ����������� ��������� �������� ��������� 1993 POSIX
1003.2 �� awk.

%description -l tr
Gawk metin dosyalar�n� i�lemek i�in kullan�lan standart Linux
Ara�lar�ndan biridir.

%description -l uk
����� gawk ͦ����� GNU ���Ӧ� awk, ���̦�� ������� ����Ԧ�. awk
���������դ ���æ�̦������ ���� ������������� ��� �������� �� �������
��������� ��¦� �� �Ц���������� � ��������� �� ����������������
����Ԧ�. Gawk ��� ���� ��ͦ���� � ���Ӧ�� awk צ� Bell Labs �
��������� ���Φ��� צ���צ��� ��������� 1993 POSIX 1003.2 �� awk.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

cp %{SOURCE2} po/pl.po
echo 'pl' >> po/LINGUAS

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-nls
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_bindir}/gawk-%{version}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README FUTURES LIMITATIONS NEWS PROBLEMS
%doc README_d/README.linux POSIX.STD
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/*info*
%attr(755,root,root) %{_libdir}/awk
%{_datadir}/awk
