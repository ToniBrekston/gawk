Summary:	The GNU version of the awk text processing utility
Summary(de.UTF-8):	Die GNU-Version des AWK-Textverarbeitungsutilitys
Summary(es.UTF-8):	Utilitarios GNU para manipulación de archivos texto
Summary(fr.UTF-8):	Traitement de texte des utilitaires GNU
Summary(ja.UTF-8):	GNU バージョンの awk テキスト処理ユーティリティー
Summary(pl.UTF-8):	Wersja GNU awk - narzędzia do obróbki tekstów
Summary(pt_BR.UTF-8):	Utilitários GNU para manipulação arquivos texto
Summary(ru.UTF-8):	GNU версия утилиты обработки текстов awk
Summary(tr.UTF-8):	GNU araçları metin düzenleyici
Summary(uk.UTF-8):	GNU версія утиліти обробки текстів awk
Name:		gawk
Version:	4.0.0
Release:	1
License:	GPL v3+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/gawk/%{name}-%{version}.tar.bz2
# Source0-md5:	7cdc48e99b885a4bbe0e98dcf1706b22
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	80753d75be0f469f70e8c90e75121a9c
Patch0:		%{name}-info.patch
Patch1:		%{name}-shutup.patch
Patch2:		%{name}-pl.po-update.patch
URL:		http://www.gnu.org/software/gawk/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-devel >= 0.18.1
BuildRequires:	libsigsegv
BuildRequires:	readline-devel
BuildRequires:	texinfo >= 4.3
Requires:	mktemp
Requires:	sed
Obsoletes:	gawk-doc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	%{_prefix}/include/awk

%description
The gawk packages contains the GNU version of awk, a text processing
utility. Awk interprets a special-purpose programming language to do
quick and easy text pattern matching and reformatting jobs. Gawk
should be upwardly compatible with the Bell Labs research version of
awk and is almost completely compliant with the 1993 POSIX 1003.2
standard for awk.

%description -l de.UTF-8
Das gawk-Paket enthält die GNU-Version von awk, einem
Textverarbeitungs-Utility. Awk interpretiert eine spezielle
Programmiersprache, um Textmuster zu suchen, und neu zu formatieren.
Gawk ist kompatibel zu der Bell Labs research-Version von awk, und ist
fast kompatibel zum 1993 POSIX 1003.2-awk-Standard.

%description -l es.UTF-8
Este es el GNU Awk. Debe ser compatible con la versión de pesquisa de
awk del Bell Labs. Es casi completamente vinculado con el padrón 1993
POSIX 1003.2 para awk. Gawk puede ser usado para procesar archivos
texto y se considera una herramienta padrón del Linux.

%description -l fr.UTF-8
awk de GNU, compatible vers le haut avec les versions awk des Bell
Labs. Il est presque totalement conforme au standard 1993 POSIX 1003.2
de awk.

%description -l ja.UTF-8
gawk パッケージは GNU バージョンの、テキスト処理ユーティリティー
である awk を含んでいます。awk は素早く、容易なパターンマッチングと
整形処理をするための特殊な目的の言語です。gawk はベル研のバージョンの
awk と上位互換で、awk の 1993 POSIX 1003.2 標準に完全に合致します。

%description -l pl.UTF-8
Pakiet zawiera implementację GNU interpretera języka awk, który
powinien być kompatybilny z aplikacją o tej samej nazwie zrobioną
przez Bell Labs. GNU awk jest w pełni zgodny ze standardem 1993 POSIX
1003.2.

Gawk (GNU awk) jest zaawansowanym językiem skryptowym, doskonale
nadającym się do obróbki plików tekstowych. Jest to jedno z
podstawowych narzędzi systemu Linux.

%description -l pt_BR.UTF-8
Este é o GNU Awk. Ele deve ser compatível com a versão de pesquisa de
awk do Bell Labs. Ele é quase completamente vinculado com o padrão
1993 POSIX 1003.2 para awk. Gawk pode ser usado para processar
arquivos texto e é considerado uma ferramenta padrão do Linux.

%description -l ru.UTF-8
Пакет gawk содержит GNU версию awk, утилиты обработки текстов. awk
интерпретирует специализированный язык программирования для быстрого и
легкого выполнения работ по сопоставлению с шаблонами и
переформатированию текстов. Gawk должен быть совместим с версией awk
от Bell Labs и практически полностью отвечает стандарту 1993 POSIX
1003.2 на awk.

%description -l tr.UTF-8
Gawk metin dosyalarını işlemek için kullanılan standart Linux
Araçlarından biridir.

%description -l uk.UTF-8
Пакет gawk містить GNU версію awk, утиліти обробки текстів. awk
інтерпретує спеціалізовану мову програмування для швидкого та легкого
виконання робіт по співставленню з шаблонами та переформатуванню
текстів. Gawk має бути сумісним з версією awk від Bell Labs і
практично повністю відповідає стандарту 1993 POSIX 1003.2 на awk.

%package devel
Summary:	Header files for gawk
Summary(pl.UTF-8):	Pliki nagłówkowe dla gawka
Group:		Development/Libraries

%description devel
This is the package containing the header files for gawk.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe dla gawka.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%{__rm} po/stamp-po

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

%configure

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_includedir}
install *.h $RPM_BUILD_ROOT%{_includedir}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__rm} $RPM_BUILD_ROOT%{_bindir}/gawk-%{version}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/README.gawk-non-english-man-pages
rm -f $RPM_BUILD_ROOT%{_datadir}/info/dir

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FUTURES LIMITATIONS NEWS POSIX.STD PROBLEMS README TODO
%attr(755,root,root) %{_bindir}/dgawk
%attr(755,root,root) %{_bindir}/gawk
%attr(755,root,root) %{_bindir}/igawk
%attr(755,root,root) %{_bindir}/pgawk*
%attr(755,root,root) %{_libdir}/awk
%{_datadir}/awk
%{_mandir}/man1/gawk.1*
%{_mandir}/man1/igawk.1*
%{_mandir}/man1/pgawk.1*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/gawk*.info*

%files devel
%defattr(644,root,root,755)
%{_includedir}
