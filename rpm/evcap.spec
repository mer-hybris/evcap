Name:       evcap
Summary:    Evcap is a tool for detecting event device capabilities
Version:    1.0.0
Release:    1
Group:      System/Boot
License:    MIT
Source0:    %{name}-%{version}.tar.gz
BuildArch:  noarch

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%install
install -m 755 -D %{name} %{buildroot}/%{_sbindir}/%{name}

%files
%defattr(-,root,root,-)
%{_sbindir}/%{name}

