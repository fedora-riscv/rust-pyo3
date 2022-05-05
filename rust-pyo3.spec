# Generated by rust2rpm 21
%bcond_without check
%global debug_package %{nil}

%global crate pyo3

Name:           rust-%{crate}
Version:        0.15.2
Release:        %autorelease
Summary:        Bindings to Python interpreter

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/pyo3
Source:         %{crates_source}
# Initial patched metadata
# * bump dependencies (MSRV 1.41 is not relevant for Fedora):
#   - bump indoc from 0.3.6 to 1.0.3
#   - bump paste from 0.1.18 to 1.0
# * relax exact versions for optional indexmap dependency
# * relax exact versions for bitflags, clap, and half dev-dependencies
# * drop unused, benchmark-only criterion dev-dependency to speed up builds
# * drop unused benchmark definitions from Cargo.toml
Patch0:         pyo3-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Bindings to Python interpreter.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       python3-devel >= 3.6

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+abi3-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+abi3-devel %{_description}

This package contains library source intended for building other packages which
use the "abi3" feature of the "%{crate}" crate.

%files       -n %{name}+abi3-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+abi3-py310-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+abi3-py310-devel %{_description}

This package contains library source intended for building other packages which
use the "abi3-py310" feature of the "%{crate}" crate.

%files       -n %{name}+abi3-py310-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+abi3-py36-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       python3-devel >= 3.6

%description -n %{name}+abi3-py36-devel %{_description}

This package contains library source intended for building other packages which
use the "abi3-py36" feature of the "%{crate}" crate.

%files       -n %{name}+abi3-py36-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+abi3-py37-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       python3-devel >= 3.7

%description -n %{name}+abi3-py37-devel %{_description}

This package contains library source intended for building other packages which
use the "abi3-py37" feature of the "%{crate}" crate.

%files       -n %{name}+abi3-py37-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+abi3-py38-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       python3-devel >= 3.8

%description -n %{name}+abi3-py38-devel %{_description}

This package contains library source intended for building other packages which
use the "abi3-py38" feature of the "%{crate}" crate.

%files       -n %{name}+abi3-py38-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+abi3-py39-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       python3-devel >= 3.9

%description -n %{name}+abi3-py39-devel %{_description}

This package contains library source intended for building other packages which
use the "abi3-py39" feature of the "%{crate}" crate.

%files       -n %{name}+abi3-py39-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+anyhow-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+anyhow-devel %{_description}

This package contains library source intended for building other packages which
use the "anyhow" feature of the "%{crate}" crate.

%files       -n %{name}+anyhow-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+auto-initialize-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+auto-initialize-devel %{_description}

This package contains library source intended for building other packages which
use the "auto-initialize" feature of the "%{crate}" crate.

%files       -n %{name}+auto-initialize-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+extension-module-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+extension-module-devel %{_description}

This package contains library source intended for building other packages which
use the "extension-module" feature of the "%{crate}" crate.

%files       -n %{name}+extension-module-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+eyre-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+eyre-devel %{_description}

This package contains library source intended for building other packages which
use the "eyre" feature of the "%{crate}" crate.

%files       -n %{name}+eyre-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+hashbrown-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hashbrown-devel %{_description}

This package contains library source intended for building other packages which
use the "hashbrown" feature of the "%{crate}" crate.

%files       -n %{name}+hashbrown-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+indexmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+indexmap-devel %{_description}

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%files       -n %{name}+indexmap-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+indoc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+indoc-devel %{_description}

This package contains library source intended for building other packages which
use the "indoc" feature of the "%{crate}" crate.

%files       -n %{name}+indoc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+inventory-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+inventory-devel %{_description}

This package contains library source intended for building other packages which
use the "inventory" feature of the "%{crate}" crate.

%files       -n %{name}+inventory-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+macros-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+macros-devel %{_description}

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%files       -n %{name}+macros-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+multiple-pymethods-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+multiple-pymethods-devel %{_description}

This package contains library source intended for building other packages which
use the "multiple-pymethods" feature of the "%{crate}" crate.

%files       -n %{name}+multiple-pymethods-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+num-bigint-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+num-bigint-devel %{_description}

This package contains library source intended for building other packages which
use the "num-bigint" feature of the "%{crate}" crate.

%files       -n %{name}+num-bigint-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+num-complex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+num-complex-devel %{_description}

This package contains library source intended for building other packages which
use the "num-complex" feature of the "%{crate}" crate.

%files       -n %{name}+num-complex-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+paste-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+paste-devel %{_description}

This package contains library source intended for building other packages which
use the "paste" feature of the "%{crate}" crate.

%files       -n %{name}+paste-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pyo3-macros-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pyo3-macros-devel %{_description}

This package contains library source intended for building other packages which
use the "pyo3-macros" feature of the "%{crate}" crate.

%files       -n %{name}+pyo3-macros-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unindent-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unindent-devel %{_description}

This package contains library source intended for building other packages which
use the "unindent" feature of the "%{crate}" crate.

%files       -n %{name}+unindent-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
# drop broken trybuild ui tests
rm tests/test_compile_error.rs
%cargo_prep

%generate_buildrequires
# unit tests require optional dependencies
%cargo_generate_buildrequires -a
echo 'python3-devel >= 3.6'

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
# unit tests require an UTF-8 locale
export LANG=C.utf8
# unit tests require the "auto-initialize" feature
%cargo_test -f auto-initialize
%endif

%changelog
%autochangelog
