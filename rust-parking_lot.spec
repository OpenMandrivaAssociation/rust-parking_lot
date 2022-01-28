%bcond_without check
%global debug_package %{nil}

%global crate parking_lot

Name:           rust-%{crate}
Version:        0.11.2
Release:        1
Summary:        More compact and efficient implementations of the standard synchronization primitives

# Upstream license specification: Apache-2.0/MIT
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/parking_lot
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(instant/default) >= 0.1.9 with crate(instant/default) < 0.2.0)
BuildRequires:  (crate(lock_api/default) >= 0.4.5 with crate(lock_api/default) < 0.5.0)
BuildRequires:  (crate(parking_lot_core/default) >= 0.8.4 with crate(parking_lot_core/default) < 0.9.0)
%if %{with check}
BuildRequires:  (crate(bincode/default) >= 1.3.3 with crate(bincode/default) < 2.0.0)
BuildRequires:  (crate(rand/default) >= 0.8.3 with crate(rand/default) < 0.9.0)
%endif
%endif

%global _description %{expand:
More compact and efficient implementations of the standard synchronization
primitives.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(parking_lot) = 0.11.2
Requires:       cargo
Requires:       (crate(instant/default) >= 0.1.9 with crate(instant/default) < 0.2.0)
Requires:       (crate(lock_api/default) >= 0.4.5 with crate(lock_api/default) < 0.5.0)
Requires:       (crate(parking_lot_core/default) >= 0.8.4 with crate(parking_lot_core/default) < 0.9.0)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(parking_lot/default) = 0.11.2
Requires:       cargo
Requires:       crate(parking_lot) = 0.11.2

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+arc_lock-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(parking_lot/arc_lock) = 0.11.2
Requires:       cargo
Requires:       (crate(lock_api/arc_lock) >= 0.4.5 with crate(lock_api/arc_lock) < 0.5.0)
Requires:       crate(parking_lot) = 0.11.2

%description -n %{name}+arc_lock-devel %{_description}

This package contains library source intended for building other packages
which use "arc_lock" feature of "%{crate}" crate.

%files       -n %{name}+arc_lock-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+deadlock_detection-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(parking_lot/deadlock_detection) = 0.11.2
Requires:       cargo
Requires:       (crate(parking_lot_core/deadlock_detection) >= 0.8.4 with crate(parking_lot_core/deadlock_detection) < 0.9.0)
Requires:       crate(parking_lot) = 0.11.2

%description -n %{name}+deadlock_detection-devel %{_description}

This package contains library source intended for building other packages
which use "deadlock_detection" feature of "%{crate}" crate.

%files       -n %{name}+deadlock_detection-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(parking_lot/nightly) = 0.11.2
Requires:       cargo
Requires:       (crate(lock_api/nightly) >= 0.4.5 with crate(lock_api/nightly) < 0.5.0)
Requires:       (crate(parking_lot_core/nightly) >= 0.8.4 with crate(parking_lot_core/nightly) < 0.9.0)
Requires:       crate(parking_lot) = 0.11.2

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages
which use "nightly" feature of "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+owning_ref-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(parking_lot/owning_ref) = 0.11.2
Requires:       cargo
Requires:       (crate(lock_api/owning_ref) >= 0.4.5 with crate(lock_api/owning_ref) < 0.5.0)
Requires:       crate(parking_lot) = 0.11.2

%description -n %{name}+owning_ref-devel %{_description}

This package contains library source intended for building other packages
which use "owning_ref" feature of "%{crate}" crate.

%files       -n %{name}+owning_ref-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+send_guard-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(parking_lot/send_guard) = 0.11.2
Requires:       cargo
Requires:       crate(parking_lot) = 0.11.2

%description -n %{name}+send_guard-devel %{_description}

This package contains library source intended for building other packages
which use "send_guard" feature of "%{crate}" crate.

%files       -n %{name}+send_guard-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(parking_lot/serde) = 0.11.2
Requires:       cargo
Requires:       (crate(lock_api/serde) >= 0.4.5 with crate(lock_api/serde) < 0.5.0)
Requires:       crate(parking_lot) = 0.11.2

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+stdweb-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(parking_lot/stdweb) = 0.11.2
Requires:       cargo
Requires:       (crate(instant/stdweb) >= 0.1.9 with crate(instant/stdweb) < 0.2.0)
Requires:       crate(parking_lot) = 0.11.2

%description -n %{name}+stdweb-devel %{_description}

This package contains library source intended for building other packages
which use "stdweb" feature of "%{crate}" crate.

%files       -n %{name}+stdweb-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+wasm-bindgen-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(parking_lot/wasm-bindgen) = 0.11.2
Requires:       cargo
Requires:       (crate(instant/wasm-bindgen) >= 0.1.9 with crate(instant/wasm-bindgen) < 0.2.0)
Requires:       crate(parking_lot) = 0.11.2

%description -n %{name}+wasm-bindgen-devel %{_description}

This package contains library source intended for building other packages
which use "wasm-bindgen" feature of "%{crate}" crate.

%files       -n %{name}+wasm-bindgen-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
