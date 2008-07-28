%define	name	logfinder
%define	version	0.1
%define	release	 %mkrel 3 

Name:		%{name} 
Summary:	Helps Eliminate Unwanted Logging of Personal Data
Version:	%{version} 
Release:	%{release} 
Source0:	%{name}-%{version}.tar.bz2
URL:		http://www.eff.org/news/archives/2005_02.php#002370
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

