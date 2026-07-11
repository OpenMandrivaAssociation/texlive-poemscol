%global tl_name poemscol
%global tl_revision 56082

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.1415926
Release:	%{tl_revision}.1
Summary:	Typesetting Critical Editions of Poetry
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/poemscol
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/poemscol.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/poemscol.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/poemscol.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers LaTeX macros for typesetting critical editions of
poetry. Its features include automatic linenumbering, generation of
separate endnotes sections for emendations, textual collations, and
explanatory notes, special marking for cases in which page breaks occur
during stanza breaks, running headers of the form 'Notes to pp. xx-yy'
for the notes sections, index of titles and first lines, and automatic
generation of a table of contents.

