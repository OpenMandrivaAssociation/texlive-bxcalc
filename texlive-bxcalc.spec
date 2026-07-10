%global tl_name bxcalc
%global tl_revision 78793

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Extend the functionality of the calc package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bxcalc
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxcalc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxcalc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package bundle consists of the following packages: bxcalcize: To
make calc expressions available in more places. bxcalcux: To add user-
defined units to the calc syntax. In addition, this bundle provides the
bxcalc package, which simply loads the above-mentioned packages
internally.

