%global tl_name skrapport
%global tl_revision 79121

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.12k
Release:	%{tl_revision}.1
Summary:	Simple class for reports, etc.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/skrapport
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/skrapport.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/skrapport.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/skrapport.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class is intended for simple documents (e.g., reports handed in as
coursework and the like). The class is small and straightforward; its
design was inspired by that of the PracTeX journal style.

