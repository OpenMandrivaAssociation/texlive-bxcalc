Name:		texlive-bxcalc
Version:	56431
Release:	1
Summary:	Extend the functionality of the calc package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bxcalc
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxcalc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxcalc.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package bundle consists of the following packages:
bxcalcize: To make calc expressions available in more places.
bxcalcux: To add user-defined units to the calc syntax. In
addition, this bundle provides the bxcalc package, which simply
loads the above-mentioned packages internally.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bxcalc
%doc %{_texmfdistdir}/doc/latex/bxcalc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
