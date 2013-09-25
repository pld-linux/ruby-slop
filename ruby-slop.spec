#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	slop
Summary:	Option gathering made easy
Name:		ruby-%{pkgname}
Version:	3.4.3
Release:	1
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	-
URL:		http://github.com/injekt/slop
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	ruby-minitest
BuildRequires:	ruby-rake
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple DSL for gathering options and parsing the command line.

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%if %{with tests}
# if running via testrb, modify the check for invoked testing binary
sed -i 's|Usage: rake_test_loader \[options\]|Usage: testrb: SlopTest#test_printing_help_with__help____true [options]|' test/slop_test.rb
testrb test/*_test.rb
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGES.md LICENSE
%{ruby_vendorlibdir}/slop.rb
%{ruby_vendorlibdir}/slop
