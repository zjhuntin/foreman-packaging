%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name invariant

Name: %{?scl_prefix}nodejs-invariant
Version: 2.2.4
Release: 4%{?dist}
Summary: invariant
License: MIT
Group: Development/Libraries
URL: https://github.com/zertosh/invariant#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
BuildRequires: npm
%endif
Requires: %{?scl_prefix}npm(loose-envify) >= 1.0.0
Requires: %{?scl_prefix}npm(loose-envify) < 2.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr browser.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr invariant.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr invariant.js.flow %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.2.4-4
- Bump packages to build for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 2.2.4-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 2.2.4-2
- Update specs to handle SCL

* Wed Oct 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.2.4-1
- Add nodejs-invariant generated by npm2rpm using the single strategy
