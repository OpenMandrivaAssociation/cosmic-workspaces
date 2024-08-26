%undefine _debugsource_packages

%define         appname com.system76.CosmicWorkspaces
Name:           cosmic-workspaces
Version:        1.0.0
Release:        0.alpha1.0
Summary:        COSMIC workspaces
Group:          Desktop/COSMIC
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-workspaces-epoch
Source0:        https://github.com/pop-os/cosmic-workspaces-epoch/archive/epoch-%{version}-alpha.1/%{name}-epoch-epoch-%{version}-alpha.1.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  rust-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.

%prep
%autosetup -n %{name}-epoch-epoch-%{version}-alpha.1 -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%make_build

%install
%make_install DESTDIR=%{buildroot} prefix=%{_prefix}

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}.svg