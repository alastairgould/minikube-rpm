Name:          minikube
Version:       0.28.2
Release:       1%{?dist}
Summary:       Run Kubernetes locally

Group:         Development Tools
URL:           https://github.com/kubernetes/minikube
License:       ASL 2.0
Source0:       https://storage.googleapis.com/minikube/releases/v%{version}/%{name}-linux-amd64
ExclusiveArch: x86_64
Requires:      kubernetes-client

%description
Minikube is a tool that makes it easy to run Kubernetes locally.
Minikube runs a single-node Kubernetes cluster inside a VM on your
laptop for users looking to try out Kubernetes or develop with it 
day-to-day.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
