%define	name	logfinder
%define	version	0.1
%define release	 6

Name:		%{name} 
Summary:	Helps Eliminate Unwanted Logging of Personal Data
Version:	%{version} 
Release:	%{release} 
Source0:	%{name}-%{version}.tar.bz2
URL:		https://www.eff.org/news/archives/2005_02.php#002370
Group:		File tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
Requires:	python
BuildArch:	noarch

%description
By finding unwanted log files, logfinder informs system
administrators when their servers are collecting personal data
and gives them the opportunity to turn logging off if it isn't
gathering information necessary for administering the system.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -m755 logfinder.py -D $RPM_BUILD_ROOT%{_bindir}/logfinder.py

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc README
%{_bindir}/logfinder.py



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-5mdv2011.0
+ Revision: 620251
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1-4mdv2010.0
+ Revision: 429864
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 0.1-3mdv2009.0
+ Revision: 251330
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.1-1mdv2008.1
+ Revision: 129438
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import logfinder


* Wed Feb 09 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1-1mdk
- from Eskild Hustvedt <zerodogg@skolelinux.no> :
	o Initial Mandrakelinux package
