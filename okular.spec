#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v27
# autospec commit: 65cf152
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : okular
Version  : 25.04.2
Release  : 90
URL      : https://download.kde.org/stable/release-service/25.04.2/src/okular-25.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/25.04.2/src/okular-25.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/25.04.2/src/okular-25.04.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause GFDL-1.2 GPL-2.0 GPL-3.0 LGPL-2.0 MIT X11
Requires: okular-bin = %{version}-%{release}
Requires: okular-data = %{version}-%{release}
Requires: okular-lib = %{version}-%{release}
Requires: okular-license = %{version}-%{release}
Requires: okular-locales = %{version}-%{release}
Requires: okular-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules-data
BuildRequires : freetype-dev
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : kwallet-dev
BuildRequires : libkexiv2-dev
BuildRequires : phonon-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libspectre)
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(poppler)
BuildRequires : plasma-activities-dev
BuildRequires : poppler-dev
BuildRequires : poppler-extras
BuildRequires : purpose-dev
BuildRequires : qt6base-dev
BuildRequires : threadweaver-dev
BuildRequires : tiff-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This is a libepub based backend to watch epub books using okular
The epub library can be obtained using:

%package bin
Summary: bin components for the okular package.
Group: Binaries
Requires: okular-data = %{version}-%{release}
Requires: okular-license = %{version}-%{release}

%description bin
bin components for the okular package.


%package data
Summary: data components for the okular package.
Group: Data

%description data
data components for the okular package.


%package dev
Summary: dev components for the okular package.
Group: Development
Requires: okular-lib = %{version}-%{release}
Requires: okular-bin = %{version}-%{release}
Requires: okular-data = %{version}-%{release}
Provides: okular-devel = %{version}-%{release}
Requires: okular = %{version}-%{release}

%description dev
dev components for the okular package.


%package doc
Summary: doc components for the okular package.
Group: Documentation
Requires: okular-man = %{version}-%{release}

%description doc
doc components for the okular package.


%package lib
Summary: lib components for the okular package.
Group: Libraries
Requires: okular-data = %{version}-%{release}
Requires: okular-license = %{version}-%{release}

%description lib
lib components for the okular package.


%package license
Summary: license components for the okular package.
Group: Default

%description license
license components for the okular package.


%package locales
Summary: locales components for the okular package.
Group: Default

%description locales
locales components for the okular package.


%package man
Summary: man components for the okular package.
Group: Default

%description man
man components for the okular package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n okular-25.04.2
cd %{_builddir}/okular-25.04.2
pushd ..
cp -a okular-25.04.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1749565712
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DFORCE_NOT_REQUIRED_DEPENDENCIES="CHM;LibZip;DjVuLibre;EPub;Discount"  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DFORCE_NOT_REQUIRED_DEPENDENCIES="CHM;LibZip;DjVuLibre;EPub;Discount"  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1749565712
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/okular
cp %{_builddir}/okular-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/okular/52039e5c19c950d4c7d6ec5da42ebba2c6def7ee || :
cp %{_builddir}/okular-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/okular/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe || :
cp %{_builddir}/okular-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/okular/ee03d68f6be20b170e5ea5d114d6acafb3f2d1dc || :
cp %{_builddir}/okular-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/okular/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/okular-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/okular/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/okular-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/okular/2123756e0b1fc8243547235a33c0fcabfe3b9a51 || :
cp %{_builddir}/okular-%{version}/LICENSES/GPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/okular/2123756e0b1fc8243547235a33c0fcabfe3b9a51 || :
cp %{_builddir}/okular-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/okular/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/okular-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/okular/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/okular-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/okular/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/okular-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/okular/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/okular-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/okular/adadb67a9875aeeac285309f1eab6e47d9ee08a7 || :
cp %{_builddir}/okular-%{version}/LICENSES/X11.txt %{buildroot}/usr/share/package-licenses/okular/f6cdf05df7acdde7587a632d418465e3547fe498 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang okular
%find_lang okular_comicbook
%find_lang okular_djvu
%find_lang okular_dvi
%find_lang okular_epub
%find_lang okular_fax
%find_lang okular_fictionbook
%find_lang okular_ghostview
%find_lang okular_kimgio
%find_lang okular_markdown
%find_lang okular_mobi
%find_lang okular_poppler
%find_lang okular_tiff
%find_lang okular_txt
%find_lang okular_xps
%find_lang org.kde.active.documentviewer
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/okular
/usr/bin/okular

%files data
%defattr(-,root,root,-)
/usr/share/applications/okularApplication_comicbook.desktop
/usr/share/applications/okularApplication_dvi.desktop
/usr/share/applications/okularApplication_fax.desktop
/usr/share/applications/okularApplication_fb.desktop
/usr/share/applications/okularApplication_ghostview.desktop
/usr/share/applications/okularApplication_kimgio.desktop
/usr/share/applications/okularApplication_pdf.desktop
/usr/share/applications/okularApplication_tiff.desktop
/usr/share/applications/okularApplication_txt.desktop
/usr/share/applications/okularApplication_xps.desktop
/usr/share/applications/org.kde.okular.desktop
/usr/share/config.kcfg/gssettings.kcfg
/usr/share/config.kcfg/okular.kcfg
/usr/share/config.kcfg/okular_core.kcfg
/usr/share/config.kcfg/pdfsettings.kcfg
/usr/share/icons/hicolor/128x128/apps/okular.png
/usr/share/icons/hicolor/16x16/apps/okular.png
/usr/share/icons/hicolor/22x22/apps/okular.png
/usr/share/icons/hicolor/32x32/apps/okular.png
/usr/share/icons/hicolor/48x48/apps/okular.png
/usr/share/icons/hicolor/64x64/apps/okular.png
/usr/share/metainfo/org.kde.okular-comicbook.metainfo.xml
/usr/share/metainfo/org.kde.okular-dvi.metainfo.xml
/usr/share/metainfo/org.kde.okular-fax.metainfo.xml
/usr/share/metainfo/org.kde.okular-fb.metainfo.xml
/usr/share/metainfo/org.kde.okular-kimgio.metainfo.xml
/usr/share/metainfo/org.kde.okular-poppler.metainfo.xml
/usr/share/metainfo/org.kde.okular-spectre.metainfo.xml
/usr/share/metainfo/org.kde.okular-tiff.metainfo.xml
/usr/share/metainfo/org.kde.okular-txt.metainfo.xml
/usr/share/metainfo/org.kde.okular-xps.metainfo.xml
/usr/share/metainfo/org.kde.okular.appdata.xml
/usr/share/okular/drawingtools.xml
/usr/share/okular/icons/hicolor/16x16/apps/okular-fb2.png
/usr/share/okular/icons/hicolor/16x16/apps/okular-gv.png
/usr/share/okular/icons/hicolor/32x32/apps/okular-fb2.png
/usr/share/okular/icons/hicolor/32x32/apps/okular-gv.png
/usr/share/okular/icons/hicolor/48x48/apps/okular-fb2.png
/usr/share/okular/pics/checkmark.png
/usr/share/okular/pics/circle.png
/usr/share/okular/pics/comment.png
/usr/share/okular/pics/cross.png
/usr/share/okular/pics/help.png
/usr/share/okular/pics/insert.png
/usr/share/okular/pics/key.png
/usr/share/okular/pics/newparagraph.png
/usr/share/okular/pics/note.png
/usr/share/okular/pics/paperclip.png
/usr/share/okular/pics/paragraph.png
/usr/share/okular/pics/pushpin.png
/usr/share/okular/pics/rightarrow.png
/usr/share/okular/pics/rightpointer.png
/usr/share/okular/pics/stamps.svg
/usr/share/okular/pics/star.png
/usr/share/okular/pics/tool-base-okular.png
/usr/share/okular/pics/tool-base-okular@2x.png
/usr/share/okular/pics/tool-highlighter-okular-colorizable.png
/usr/share/okular/pics/tool-highlighter-okular-colorizable@2x.png
/usr/share/okular/pics/tool-ink-okular-colorizable.png
/usr/share/okular/pics/tool-ink-okular-colorizable@2x.png
/usr/share/okular/pics/tool-note-inline-okular-colorizable.png
/usr/share/okular/pics/tool-note-inline-okular-colorizable@2x.png
/usr/share/okular/pics/tool-note-inline.png
/usr/share/okular/pics/tool-note-okular-colorizable.png
/usr/share/okular/pics/tool-note-okular-colorizable@2x.png
/usr/share/okular/pics/tool-note.png
/usr/share/okular/pics/tool-typewriter-okular-colorizable.png
/usr/share/okular/pics/tool-typewriter-okular-colorizable@2x.png
/usr/share/okular/pics/uparrow.png
/usr/share/okular/pics/upleftarrow.png
/usr/share/okular/tools.xml
/usr/share/okular/toolsQuick.xml
/usr/share/qlogging-categories6/okular.categories

%files dev
%defattr(-,root,root,-)
/usr/include/okular/core/action.h
/usr/include/okular/core/annotations.h
/usr/include/okular/core/area.h
/usr/include/okular/core/document.h
/usr/include/okular/core/fileprinter.h
/usr/include/okular/core/fontinfo.h
/usr/include/okular/core/form.h
/usr/include/okular/core/generator.h
/usr/include/okular/core/global.h
/usr/include/okular/core/observer.h
/usr/include/okular/core/okularcore_export.h
/usr/include/okular/core/page.h
/usr/include/okular/core/pagesize.h
/usr/include/okular/core/pagetransition.h
/usr/include/okular/core/printoptionswidget.h
/usr/include/okular/core/settings_core.h
/usr/include/okular/core/signatureutils.h
/usr/include/okular/core/sound.h
/usr/include/okular/core/sourcereference.h
/usr/include/okular/core/textdocumentgenerator.h
/usr/include/okular/core/textdocumentsettings.h
/usr/include/okular/core/textpage.h
/usr/include/okular/core/tile.h
/usr/include/okular/core/utils.h
/usr/include/okular/core/version.h
/usr/include/okular/interfaces/configinterface.h
/usr/include/okular/interfaces/guiinterface.h
/usr/include/okular/interfaces/printinterface.h
/usr/include/okular/interfaces/saveinterface.h
/usr/include/okular/interfaces/viewerinterface.h
/usr/lib64/cmake/Okular6/Okular6Config.cmake
/usr/lib64/cmake/Okular6/Okular6ConfigVersion.cmake
/usr/lib64/cmake/Okular6/Okular6Targets-relwithdebinfo.cmake
/usr/lib64/cmake/Okular6/Okular6Targets.cmake
/usr/lib64/libOkular6Core.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/okular/bookmark-management.png
/usr/share/doc/HTML/ca/okular/configure-annotations.png
/usr/share/doc/HTML/ca/okular/configure-backends.png
/usr/share/doc/HTML/ca/okular/configure-editor.png
/usr/share/doc/HTML/ca/okular/configure.png
/usr/share/doc/HTML/ca/okular/index.cache.bz2
/usr/share/doc/HTML/ca/okular/index.docbook
/usr/share/doc/HTML/ca/okular/mainwindow.png
/usr/share/doc/HTML/ca/okular/presentation.png
/usr/share/doc/HTML/de/okular/annotation-properties.png
/usr/share/doc/HTML/de/okular/configure-annotations.png
/usr/share/doc/HTML/de/okular/configure-editor.png
/usr/share/doc/HTML/de/okular/configure.png
/usr/share/doc/HTML/de/okular/embedded-files-bar.png
/usr/share/doc/HTML/de/okular/index.cache.bz2
/usr/share/doc/HTML/de/okular/index.docbook
/usr/share/doc/HTML/de/okular/mainwindow.png
/usr/share/doc/HTML/en/okular/annotation-properties.png
/usr/share/doc/HTML/en/okular/annotations.png
/usr/share/doc/HTML/en/okular/bookmark-management.png
/usr/share/doc/HTML/en/okular/bookmarks.png
/usr/share/doc/HTML/en/okular/config-pdf-digital-signatures.png
/usr/share/doc/HTML/en/okular/configure-annotations.png
/usr/share/doc/HTML/en/okular/configure-backends.png
/usr/share/doc/HTML/en/okular/configure-editor.png
/usr/share/doc/HTML/en/okular/configure.png
/usr/share/doc/HTML/en/okular/embedded-files-bar.png
/usr/share/doc/HTML/en/okular/enhance-lowcontrast.png
/usr/share/doc/HTML/en/okular/enhance-shape.png
/usr/share/doc/HTML/en/okular/enhance-solid.png
/usr/share/doc/HTML/en/okular/enhance-thinline.png
/usr/share/doc/HTML/en/okular/forms-bar.png
/usr/share/doc/HTML/en/okular/index.cache.bz2
/usr/share/doc/HTML/en/okular/index.docbook
/usr/share/doc/HTML/en/okular/mainwindow.png
/usr/share/doc/HTML/en/okular/presentation.png
/usr/share/doc/HTML/en/okular/signatures-bar.png
/usr/share/doc/HTML/en/okular/signatures-panel.png
/usr/share/doc/HTML/en/okular/tool-draw-arrow.png
/usr/share/doc/HTML/en/okular/tool-draw-ellipse.png
/usr/share/doc/HTML/en/okular/tool-draw-freehand.png
/usr/share/doc/HTML/en/okular/tool-draw-highlight.png
/usr/share/doc/HTML/en/okular/tool-draw-line.png
/usr/share/doc/HTML/en/okular/tool-draw-polyline.png
/usr/share/doc/HTML/en/okular/tool-draw-rectangle.png
/usr/share/doc/HTML/en/okular/tool-edit-comment.png
/usr/share/doc/HTML/en/okular/tool-edit-line-width.png
/usr/share/doc/HTML/en/okular/tool-edit-opacity.png
/usr/share/doc/HTML/en/okular/tool-favorite.png
/usr/share/doc/HTML/en/okular/tool-fill-color.png
/usr/share/doc/HTML/en/okular/tool-font-face.png
/usr/share/doc/HTML/en/okular/tool-format-text-color.png
/usr/share/doc/HTML/en/okular/tool-format-text-strikethrough.png
/usr/share/doc/HTML/en/okular/tool-format-text-underline-squiggle.png
/usr/share/doc/HTML/en/okular/tool-format-text-underline.png
/usr/share/doc/HTML/en/okular/tool-note.png
/usr/share/doc/HTML/en/okular/tool-pin.png
/usr/share/doc/HTML/en/okular/tool-settings-configure.png
/usr/share/doc/HTML/en/okular/tool-tag.png
/usr/share/doc/HTML/en/okular/tool-tool-text.png
/usr/share/doc/HTML/en/okular/tool-window-pin.png
/usr/share/doc/HTML/es/okular/configure.png
/usr/share/doc/HTML/es/okular/embedded-files-bar.png
/usr/share/doc/HTML/es/okular/index.cache.bz2
/usr/share/doc/HTML/es/okular/index.docbook
/usr/share/doc/HTML/fr/okular/annotation-properties.png
/usr/share/doc/HTML/fr/okular/annotations.png
/usr/share/doc/HTML/fr/okular/bookmark-management.png
/usr/share/doc/HTML/fr/okular/configure-annotations.png
/usr/share/doc/HTML/fr/okular/configure-backends.png
/usr/share/doc/HTML/fr/okular/configure-editor.png
/usr/share/doc/HTML/fr/okular/configure.png
/usr/share/doc/HTML/fr/okular/forms-bar.png
/usr/share/doc/HTML/fr/okular/index.cache.bz2
/usr/share/doc/HTML/fr/okular/index.docbook
/usr/share/doc/HTML/fr/okular/mainwindow.png
/usr/share/doc/HTML/fr/okular/presentation.png
/usr/share/doc/HTML/gl/okular/index.cache.bz2
/usr/share/doc/HTML/gl/okular/index.docbook
/usr/share/doc/HTML/it/okular/annotation-properties.png
/usr/share/doc/HTML/it/okular/annotations.png
/usr/share/doc/HTML/it/okular/bookmark-management.png
/usr/share/doc/HTML/it/okular/configure-annotations.png
/usr/share/doc/HTML/it/okular/configure-backends.png
/usr/share/doc/HTML/it/okular/configure-editor.png
/usr/share/doc/HTML/it/okular/configure.png
/usr/share/doc/HTML/it/okular/embedded-files-bar.png
/usr/share/doc/HTML/it/okular/forms-bar.png
/usr/share/doc/HTML/it/okular/index.cache.bz2
/usr/share/doc/HTML/it/okular/index.docbook
/usr/share/doc/HTML/it/okular/mainwindow.png
/usr/share/doc/HTML/it/okular/presentation.png
/usr/share/doc/HTML/it/okular/signatures-bar.png
/usr/share/doc/HTML/it/okular/signatures-panel.png
/usr/share/doc/HTML/ja/okular/configure.png
/usr/share/doc/HTML/ja/okular/embedded-files-bar.png
/usr/share/doc/HTML/ja/okular/index.cache.bz2
/usr/share/doc/HTML/ja/okular/index.docbook
/usr/share/doc/HTML/nl/okular/index.cache.bz2
/usr/share/doc/HTML/nl/okular/index.docbook
/usr/share/doc/HTML/pl/okular/annotation-properties.png
/usr/share/doc/HTML/pl/okular/annotations.png
/usr/share/doc/HTML/pl/okular/bookmark-management.png
/usr/share/doc/HTML/pl/okular/configure-annotations.png
/usr/share/doc/HTML/pl/okular/configure-backends.png
/usr/share/doc/HTML/pl/okular/configure-editor.png
/usr/share/doc/HTML/pl/okular/configure.png
/usr/share/doc/HTML/pl/okular/embedded-files-bar.png
/usr/share/doc/HTML/pl/okular/forms-bar.png
/usr/share/doc/HTML/pl/okular/index.cache.bz2
/usr/share/doc/HTML/pl/okular/index.docbook
/usr/share/doc/HTML/pl/okular/mainwindow.png
/usr/share/doc/HTML/pl/okular/presentation.png
/usr/share/doc/HTML/pl/okular/rating.png
/usr/share/doc/HTML/pl/okular/tool-ellipse-okular.png
/usr/share/doc/HTML/pl/okular/tool-highlighter-okular.png
/usr/share/doc/HTML/pl/okular/tool-ink-okular.png
/usr/share/doc/HTML/pl/okular/tool-line-okular.png
/usr/share/doc/HTML/pl/okular/tool-note-inline-okular.png
/usr/share/doc/HTML/pl/okular/tool-note-okular.png
/usr/share/doc/HTML/pl/okular/tool-polygon-okular.png
/usr/share/doc/HTML/pl/okular/tool-stamp-okular.png
/usr/share/doc/HTML/pl/okular/tool-underline-okular.png
/usr/share/doc/HTML/pt/okular/index.cache.bz2
/usr/share/doc/HTML/pt/okular/index.docbook
/usr/share/doc/HTML/pt_BR/okular/annotation-properties.png
/usr/share/doc/HTML/pt_BR/okular/annotations.png
/usr/share/doc/HTML/pt_BR/okular/bookmark-management.png
/usr/share/doc/HTML/pt_BR/okular/configure-annotations.png
/usr/share/doc/HTML/pt_BR/okular/configure-backends.png
/usr/share/doc/HTML/pt_BR/okular/configure-editor.png
/usr/share/doc/HTML/pt_BR/okular/configure.png
/usr/share/doc/HTML/pt_BR/okular/embedded-files-bar.png
/usr/share/doc/HTML/pt_BR/okular/forms-bar.png
/usr/share/doc/HTML/pt_BR/okular/index.cache.bz2
/usr/share/doc/HTML/pt_BR/okular/index.docbook
/usr/share/doc/HTML/pt_BR/okular/mainwindow.png
/usr/share/doc/HTML/pt_BR/okular/presentation.png
/usr/share/doc/HTML/pt_BR/okular/signatures-bar.png
/usr/share/doc/HTML/pt_BR/okular/signatures-panel.png
/usr/share/doc/HTML/ru/okular/annotation-properties.png
/usr/share/doc/HTML/ru/okular/annotations.png
/usr/share/doc/HTML/ru/okular/bookmark-management.png
/usr/share/doc/HTML/ru/okular/configure-annotations.png
/usr/share/doc/HTML/ru/okular/configure-backends.png
/usr/share/doc/HTML/ru/okular/configure-editor.png
/usr/share/doc/HTML/ru/okular/configure.png
/usr/share/doc/HTML/ru/okular/embedded-files-bar.png
/usr/share/doc/HTML/ru/okular/enhance-lowcontrast.png
/usr/share/doc/HTML/ru/okular/enhance-shape.png
/usr/share/doc/HTML/ru/okular/enhance-solid.png
/usr/share/doc/HTML/ru/okular/enhance-thinline.png
/usr/share/doc/HTML/ru/okular/forms-bar.png
/usr/share/doc/HTML/ru/okular/index.cache.bz2
/usr/share/doc/HTML/ru/okular/index.docbook
/usr/share/doc/HTML/ru/okular/mainwindow.png
/usr/share/doc/HTML/ru/okular/presentation.png
/usr/share/doc/HTML/ru/okular/rating.png
/usr/share/doc/HTML/ru/okular/tool-ellipse-okular.png
/usr/share/doc/HTML/ru/okular/tool-highlighter-okular.png
/usr/share/doc/HTML/ru/okular/tool-ink-okular.png
/usr/share/doc/HTML/ru/okular/tool-line-okular.png
/usr/share/doc/HTML/ru/okular/tool-note-inline-okular.png
/usr/share/doc/HTML/ru/okular/tool-note-okular.png
/usr/share/doc/HTML/ru/okular/tool-polygon-okular.png
/usr/share/doc/HTML/ru/okular/tool-stamp-okular.png
/usr/share/doc/HTML/ru/okular/tool-underline-okular.png
/usr/share/doc/HTML/sl/okular/index.cache.bz2
/usr/share/doc/HTML/sl/okular/index.docbook
/usr/share/doc/HTML/sv/okular/configure.png
/usr/share/doc/HTML/sv/okular/index.cache.bz2
/usr/share/doc/HTML/sv/okular/index.docbook
/usr/share/doc/HTML/tr/okular/index.cache.bz2
/usr/share/doc/HTML/tr/okular/index.docbook
/usr/share/doc/HTML/uk/okular/annotation-properties.png
/usr/share/doc/HTML/uk/okular/annotations.png
/usr/share/doc/HTML/uk/okular/bookmark-management.png
/usr/share/doc/HTML/uk/okular/configure-annotations.png
/usr/share/doc/HTML/uk/okular/configure-backends.png
/usr/share/doc/HTML/uk/okular/configure-editor.png
/usr/share/doc/HTML/uk/okular/configure.png
/usr/share/doc/HTML/uk/okular/embedded-files-bar.png
/usr/share/doc/HTML/uk/okular/forms-bar.png
/usr/share/doc/HTML/uk/okular/index.cache.bz2
/usr/share/doc/HTML/uk/okular/index.docbook
/usr/share/doc/HTML/uk/okular/mainwindow.png
/usr/share/doc/HTML/uk/okular/signatures-bar.png
/usr/share/doc/HTML/uk/okular/signatures-panel.png

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libOkular6Core.so.3.0.0
/V3/usr/lib64/qt6/plugins/kf6/parts/okularpart.so
/V3/usr/lib64/qt6/plugins/okular_generators/okularGenerator_comicbook.so
/V3/usr/lib64/qt6/plugins/okular_generators/okularGenerator_dvi.so
/V3/usr/lib64/qt6/plugins/okular_generators/okularGenerator_fax.so
/V3/usr/lib64/qt6/plugins/okular_generators/okularGenerator_fb.so
/V3/usr/lib64/qt6/plugins/okular_generators/okularGenerator_ghostview.so
/V3/usr/lib64/qt6/plugins/okular_generators/okularGenerator_kimgio.so
/V3/usr/lib64/qt6/plugins/okular_generators/okularGenerator_poppler.so
/V3/usr/lib64/qt6/plugins/okular_generators/okularGenerator_tiff.so
/V3/usr/lib64/qt6/plugins/okular_generators/okularGenerator_txt.so
/V3/usr/lib64/qt6/plugins/okular_generators/okularGenerator_xps.so
/usr/lib64/libOkular6Core.so.3
/usr/lib64/libOkular6Core.so.3.0.0
/usr/lib64/qt6/plugins/kf6/parts/okularpart.so
/usr/lib64/qt6/plugins/okular_generators/okularGenerator_comicbook.so
/usr/lib64/qt6/plugins/okular_generators/okularGenerator_dvi.so
/usr/lib64/qt6/plugins/okular_generators/okularGenerator_fax.so
/usr/lib64/qt6/plugins/okular_generators/okularGenerator_fb.so
/usr/lib64/qt6/plugins/okular_generators/okularGenerator_ghostview.so
/usr/lib64/qt6/plugins/okular_generators/okularGenerator_kimgio.so
/usr/lib64/qt6/plugins/okular_generators/okularGenerator_poppler.so
/usr/lib64/qt6/plugins/okular_generators/okularGenerator_tiff.so
/usr/lib64/qt6/plugins/okular_generators/okularGenerator_txt.so
/usr/lib64/qt6/plugins/okular_generators/okularGenerator_xps.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/okular/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/okular/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/okular/52039e5c19c950d4c7d6ec5da42ebba2c6def7ee
/usr/share/package-licenses/okular/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/okular/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/okular/adadb67a9875aeeac285309f1eab6e47d9ee08a7
/usr/share/package-licenses/okular/ee03d68f6be20b170e5ea5d114d6acafb3f2d1dc
/usr/share/package-licenses/okular/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe
/usr/share/package-licenses/okular/f6cdf05df7acdde7587a632d418465e3547fe498

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/okular.1
/usr/share/man/de/man1/okular.1
/usr/share/man/es/man1/okular.1
/usr/share/man/et/man1/okular.1
/usr/share/man/fr/man1/okular.1
/usr/share/man/it/man1/okular.1
/usr/share/man/man1/okular.1
/usr/share/man/nl/man1/okular.1
/usr/share/man/pt/man1/okular.1
/usr/share/man/pt_BR/man1/okular.1
/usr/share/man/ru/man1/okular.1
/usr/share/man/sl/man1/okular.1
/usr/share/man/sv/man1/okular.1
/usr/share/man/tr/man1/okular.1
/usr/share/man/uk/man1/okular.1

%files locales -f okular.lang -f okular_comicbook.lang -f okular_djvu.lang -f okular_dvi.lang -f okular_epub.lang -f okular_fax.lang -f okular_fictionbook.lang -f okular_ghostview.lang -f okular_kimgio.lang -f okular_markdown.lang -f okular_mobi.lang -f okular_poppler.lang -f okular_tiff.lang -f okular_txt.lang -f okular_xps.lang -f org.kde.active.documentviewer.lang
%defattr(-,root,root,-)

