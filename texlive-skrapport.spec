# revision 31718
# category Package
# catalog-ctan /macros/latex/contrib/skrapport
# catalog-date 2013-09-21 11:27:06 +0200
# catalog-license lppl1.3
# catalog-version 0.12d
Name:		texlive-skrapport
Version:	0.12d
Release:	2
Summary:	'Simple' class for reports, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/skrapport
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skrapport.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skrapport.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skrapport.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class is intended for simple documents (e.g., reports
handed in as coursework and the like). The class is small and
straightforward; its design was inspired by that of the PracTeX
journal style.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/skrapport/skrapport-colortheme-cruelwater.sty
%{_texmfdistdir}/tex/latex/skrapport/skrapport-colortheme-default.sty
%{_texmfdistdir}/tex/latex/skrapport/skrapport-colortheme-skdoc.sty
%{_texmfdistdir}/tex/latex/skrapport/skrapport-colortheme-unscathed.sty
%{_texmfdistdir}/tex/latex/skrapport/skrapport-colortheme-violet.sty
%{_texmfdistdir}/tex/latex/skrapport/skrapport-size-common.sty
%{_texmfdistdir}/tex/latex/skrapport/skrapport-size10pt.clo
%{_texmfdistdir}/tex/latex/skrapport/skrapport-size11pt.clo
%{_texmfdistdir}/tex/latex/skrapport/skrapport-size12pt.clo
%{_texmfdistdir}/tex/latex/skrapport/skrapport.cls
%doc %{_texmfdistdir}/doc/latex/skrapport/README
%doc %{_texmfdistdir}/doc/latex/skrapport/skrapport.pdf
#- source
%doc %{_texmfdistdir}/source/latex/skrapport/skrapport.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
