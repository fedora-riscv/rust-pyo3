# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate pyo3

Name:           rust-%{crate}
Version:        0.13.1
Release:        2%{?dist}
Summary:        Bindings to Python interpreter

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/pyo3
Source:         %{crates_source}
# Initial patched metadata
# * exclude Makefile, pyproject.toml, and tox.ini:
#   https://github.com/PyO3/pyo3/pull/1380
Patch0:         pyo3-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Bindings to Python interpreter.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md CHANGELOG.md Code-of-Conduct.md Contributing.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       python3-devel >= 3.6

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+abi3-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+abi3-devel %{_description}

This package contains library source intended for building other packages
which use "abi3" feature of "%{crate}" crate.

%files       -n %{name}+abi3-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+abi3-py36-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       python3-devel >= 3.6

%description -n %{name}+abi3-py36-devel %{_description}

This package contains library source intended for building other packages
which use "abi3-py36" feature of "%{crate}" crate.

%files       -n %{name}+abi3-py36-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+abi3-py37-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       python3-devel >= 3.7

%description -n %{name}+abi3-py37-devel %{_description}

This package contains library source intended for building other packages
which use "abi3-py37" feature of "%{crate}" crate.

%files       -n %{name}+abi3-py37-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+abi3-py38-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       python3-devel >= 3.8

%description -n %{name}+abi3-py38-devel %{_description}

This package contains library source intended for building other packages
which use "abi3-py38" feature of "%{crate}" crate.

%files       -n %{name}+abi3-py38-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+abi3-py39-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       python3-devel >= 3.9

%description -n %{name}+abi3-py39-devel %{_description}

This package contains library source intended for building other packages
which use "abi3-py39" feature of "%{crate}" crate.

%files       -n %{name}+abi3-py39-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+auto-initialize-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+auto-initialize-devel %{_description}

This package contains library source intended for building other packages
which use "auto-initialize" feature of "%{crate}" crate.

%files       -n %{name}+auto-initialize-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+ctor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ctor-devel %{_description}

This package contains library source intended for building other packages
which use "ctor" feature of "%{crate}" crate.

%files       -n %{name}+ctor-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+extension-module-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+extension-module-devel %{_description}

This package contains library source intended for building other packages
which use "extension-module" feature of "%{crate}" crate.

%files       -n %{name}+extension-module-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+hashbrown-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hashbrown-devel %{_description}

This package contains library source intended for building other packages
which use "hashbrown" feature of "%{crate}" crate.

%files       -n %{name}+hashbrown-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+indoc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+indoc-devel %{_description}

This package contains library source intended for building other packages
which use "indoc" feature of "%{crate}" crate.

%files       -n %{name}+indoc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+inventory-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+inventory-devel %{_description}

This package contains library source intended for building other packages
which use "inventory" feature of "%{crate}" crate.

%files       -n %{name}+inventory-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+macros-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+macros-devel %{_description}

This package contains library source intended for building other packages
which use "macros" feature of "%{crate}" crate.

%files       -n %{name}+macros-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages
which use "nightly" feature of "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+num-bigint-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+num-bigint-devel %{_description}

This package contains library source intended for building other packages
which use "num-bigint" feature of "%{crate}" crate.

%files       -n %{name}+num-bigint-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+num-complex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+num-complex-devel %{_description}

This package contains library source intended for building other packages
which use "num-complex" feature of "%{crate}" crate.

%files       -n %{name}+num-complex-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+paste-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+paste-devel %{_description}

This package contains library source intended for building other packages
which use "paste" feature of "%{crate}" crate.

%files       -n %{name}+paste-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pyo3-macros-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pyo3-macros-devel %{_description}

This package contains library source intended for building other packages
which use "pyo3-macros" feature of "%{crate}" crate.

%files       -n %{name}+pyo3-macros-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unindent-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unindent-devel %{_description}

This package contains library source intended for building other packages
which use "unindent" feature of "%{crate}" crate.

%files       -n %{name}+unindent-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'python3-devel >= 3.6'

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
# skip a test that fails in the wrong way
%cargo_test -- -- --skip test_compile_errors
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Fabio Valentini <decathorpe@gmail.com> - 0.13.1-1
- Update to version 0.13.1.

* Thu Jan 07 2021 Fabio Valentini <decathorpe@gmail.com> - 0.13.0-1
- Initial package
