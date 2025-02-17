Name:		texlive-poemscol
Version:	56082
Release:	2
Summary:	Typesetting Critical Editions of Poetry
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/poemscol
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poemscol.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poemscol.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poemscol.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers LaTeX macros for typesetting critical
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
%{_texmfdistdir}/tex/latex/poemscol
%doc %{_texmfdistdir}/doc/latex/poemscol
#- source
%doc %{_texmfdistdir}/source/latex/poemscol

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
