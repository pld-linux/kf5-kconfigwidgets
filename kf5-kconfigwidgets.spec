#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	5.97
%define		qtver		5.15.2
%define		kfname		kconfigwidgets

Summary:	Widgets for configuration dialogs
Name:		kf5-%{kfname}
Version:	5.97.0
Release:	2
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	1c150ec6adaf8685af8bc80256560a86
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	gettext-tools
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-kauth-devel >= %{version}
BuildRequires:	kf5-kcodecs-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kdoctools-devel >= %{version}
BuildRequires:	kf5-kguiaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5DBus >= %{qtver}
Requires:	Qt5Widgets >= %{qtver}
Requires:	kf5-dirs
Requires:	kf5-kauth >= %{version}
Requires:	kf5-kcodecs >= %{version}
Requires:	kf5-kconfig >= %{version}
Requires:	kf5-kcoreaddons >= %{version}
Requires:	kf5-kguiaddons >= %{version}
Requires:	kf5-ki18n >= %{version}
Requires:	kf5-kwidgetsaddons >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KConfigWidgets provides easy-to-use classes to create configuration
dialogs, as well as a set of widgets which uses KConfig to store their
settings.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cmake >= 3.16
Requires:	kf5-kauth-devel >= %{version}
Requires:	kf5-kcodecs-devel >= %{version}
Requires:	kf5-kconfig-devel >= %{version}
Requires:	kf5-kwidgetsaddons-devel >= %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}5

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/preparetips5
%ghost %{_libdir}/libKF5ConfigWidgets.so.5
%attr(755,root,root) %{_libdir}/libKF5ConfigWidgets.so.*.*
%{_mandir}/man1/preparetips5.1*
%lang(ca) %{_mandir}/ca/man1/preparetips5.1*
%lang(de) %{_mandir}/de/man1/preparetips5.1*
%lang(es) %{_mandir}/es/man1/preparetips5.1*
%lang(it) %{_mandir}/it/man1/preparetips5.1*
%lang(nl) %{_mandir}/nl/man1/preparetips5.1*
%lang(pt) %{_mandir}/pt/man1/preparetips5.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/preparetips5.1*
%lang(ru) %{_mandir}/ru/man1/preparetips5.1*
%lang(sv) %{_mandir}/sv/man1/preparetips5.1*
%lang(uk) %{_mandir}/uk/man1/preparetips5.1*
%{_datadir}/qlogging-categories5/kconfigwidgets.categories
%attr(755,root,root) %{qt5dir}/plugins/designer/kconfigwidgets5widgets.so
%lang(fr) %{_mandir}/fr/man1/preparetips5.1*
%{_datadir}/qlogging-categories5/kconfigwidgets.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KConfigWidgets
%{_libdir}/cmake/KF5ConfigWidgets
%{_libdir}/libKF5ConfigWidgets.so
%{qt5dir}/mkspecs/modules/qt_KConfigWidgets.pri
