# revision 23762
# category Package
# catalog-ctan /macros/latex/contrib/poemscol
# catalog-date 2011-08-31 08:15:30 +0200
# catalog-license lppl
# catalog-version 2.54
Name:		texlive-poemscol
Version:	2.54
Release:	1
Summary:	Typesetting Critical Editions of Poetry
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/poemscol
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poemscol.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poemscol.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poemscol.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Poemscol is a package of LaTeX macros for typesetting critical
editions of poetry. Its features include automatic
linenumbering, generation of separate endnotes sections for
emendations, textual collations, and explanatory notes, special
marking for cases in which page breaks occur during stanza
breaks, running headers of the form 'Notes to pp. xx-yy' for
the notes sections, index of titles and first lines, and
automatic generation of a table of contents.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/poemscol/poemscol.sty
%doc %{_texmfdistdir}/doc/latex/poemscol/README
%doc %{_texmfdistdir}/doc/latex/poemscol/poemscol.pdf
%doc %{_texmfdistdir}/doc/latex/poemscol/poemscolcheatsheet.pdf
#- source
%doc %{_texmfdistdir}/source/latex/poemscol/poemscol.dtx
%doc %{_texmfdistdir}/source/latex/poemscol/poemscol.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
