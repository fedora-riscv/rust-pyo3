# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate pyo3

Name:           rust-pyo3
Version:        0.18.1
Release:        %autorelease
Summary:        Bindings to Python interpreter

License:        Apache-2.0
URL:            https://crates.io/crates/pyo3
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop unused, benchmark-only criterion dev-dependency to speed up builds
# * drop unused benchmark definitions from Cargo.toml
# * drop send_wrapper and widestring dev-dependencies (not packaged yet)
# * drop MSVC- and MinGW-only features
Patch:          pyo3-fix-metadata.diff
# * skip the single doctest that depends on send_wrapper
Patch:          0001-ignore-doctest-with-missing-send_wrapper-dependency.patch
# * skip a little-endian-specific test on big-endian arches
Patch:          0002-Ensure-to-skip-tests-for-little-endian-things-on-big.patch

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
%doc %{crate_instdir}/Architecture.md
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/Code-of-Conduct.md
%doc %{crate_instdir}/Contributing.md
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/Releasing.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

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

%package     -n %{name}+abi3-py311-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+abi3-py311-devel %{_description}

This package contains library source intended for building other packages which
use the "abi3-py311" feature of the "%{crate}" crate.

%files       -n %{name}+abi3-py311-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+abi3-py37-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+abi3-py37-devel %{_description}

This package contains library source intended for building other packages which
use the "abi3-py37" feature of the "%{crate}" crate.

%files       -n %{name}+abi3-py37-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+abi3-py38-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+abi3-py38-devel %{_description}

This package contains library source intended for building other packages which
use the "abi3-py38" feature of the "%{crate}" crate.

%files       -n %{name}+abi3-py38-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+abi3-py39-devel
Summary:        %{summary}
BuildArch:      noarch

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

%package     -n %{name}+chrono-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+chrono-devel %{_description}

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%files       -n %{name}+chrono-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+experimental-inspect-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+experimental-inspect-devel %{_description}

This package contains library source intended for building other packages which
use the "experimental-inspect" feature of the "%{crate}" crate.

%files       -n %{name}+experimental-inspect-devel
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

%package     -n %{name}+full-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+full-devel %{_description}

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%files       -n %{name}+full-devel
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
# drop files that are not useful
rm -r emscripten/ newsfragments/
# drop broken trybuild ui tests
rm tests/test_compile_error.rs
# drop the tests for which dependencies were removed
rm tests/test_pep_587.rs
rm tests/ui/send_wrapper.rs
%cargo_prep

%generate_buildrequires
# unit tests require optional dependencies
%cargo_generate_buildrequires -a

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
