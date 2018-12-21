#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : okular
Version  : 18.12.0
Release  : 4
URL      : https://download.kde.org/stable/applications/18.12.0/src/okular-18.12.0.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.0/src/okular-18.12.0.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.0/src/okular-18.12.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: okular-bin = %{version}-%{release}
Requires: okular-data = %{version}-%{release}
Requires: okular-lib = %{version}-%{release}
Requires: okular-license = %{version}-%{release}
Requires: okular-locales = %{version}-%{release}
Requires: okular-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(poppler)
BuildRequires : freetype-dev
BuildRequires : kactivities-dev
BuildRequires : khtml-dev
BuildRequires : kirigami2-dev
BuildRequires : kjs-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : phonon-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libspectre)
BuildRequires : poppler-extras
BuildRequires : qca-qt5-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : threadweaver-dev
BuildRequires : tiff-dev
BuildRequires : zlib-dev

%description
This is a libepub based backend to watch epub books using okular
The epub library can be obtained using:

%package bin
Summary: bin components for the okular package.
Group: Binaries
Requires: okular-data = %{version}-%{release}
Requires: okular-license = %{version}-%{release}
Requires: okular-man = %{version}-%{release}

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
%setup -q -n okular-18.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545363048
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1545363048
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/okular
cp COPYING %{buildroot}/usr/share/package-licenses/okular/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/okular/COPYING.DOC
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/okular/COPYING.LIB
cp cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/okular/cmake_modules_COPYING-CMAKE-SCRIPTS
pushd clr-build
%make_install
popd
%find_lang okular
%find_lang okular_chm
%find_lang okular_comicbook
%find_lang okular_djvu
%find_lang okular_dvi
%find_lang okular_epub
%find_lang okular_fax
%find_lang okular_fictionbook
%find_lang okular_ghostview
%find_lang okular_kimgio
%find_lang okular_mobi
%find_lang okular_ooo
%find_lang okular_plucker
%find_lang okular_poppler
%find_lang okular_txt
%find_lang okular_xps
%find_lang org.kde.active.documentviewer
%find_lang okular_markdown

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/okular
/usr/bin/okularkirigami

%files data
%defattr(-,root,root,-)
/usr/share/applications/okularApplication_comicbook.desktop
/usr/share/applications/okularApplication_dvi.desktop
/usr/share/applications/okularApplication_fax.desktop
/usr/share/applications/okularApplication_fb.desktop
/usr/share/applications/okularApplication_ghostview.desktop
/usr/share/applications/okularApplication_ooo.desktop
/usr/share/applications/okularApplication_pdf.desktop
/usr/share/applications/okularApplication_plucker.desktop
/usr/share/applications/okularApplication_tiff.desktop
/usr/share/applications/okularApplication_txt.desktop
/usr/share/applications/okularApplication_xps.desktop
/usr/share/applications/org.kde.mobile.okular_comicbook.desktop
/usr/share/applications/org.kde.mobile.okular_dvi.desktop
/usr/share/applications/org.kde.mobile.okular_fax.desktop
/usr/share/applications/org.kde.mobile.okular_fb.desktop
/usr/share/applications/org.kde.mobile.okular_ghostview.desktop
/usr/share/applications/org.kde.mobile.okular_ooo.desktop
/usr/share/applications/org.kde.mobile.okular_pdf.desktop
/usr/share/applications/org.kde.mobile.okular_plucker.desktop
/usr/share/applications/org.kde.mobile.okular_tiff.desktop
/usr/share/applications/org.kde.mobile.okular_txt.desktop
/usr/share/applications/org.kde.mobile.okular_xps.desktop
/usr/share/applications/org.kde.okular.desktop
/usr/share/applications/org.kde.okular.kirigami.desktop
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
/usr/share/kconf_update/okular.upd
/usr/share/kservices5/okularComicbook.desktop
/usr/share/kservices5/okularDvi.desktop
/usr/share/kservices5/okularFax.desktop
/usr/share/kservices5/okularFb.desktop
/usr/share/kservices5/okularGhostview.desktop
/usr/share/kservices5/okularOoo.desktop
/usr/share/kservices5/okularPlucker.desktop
/usr/share/kservices5/okularPoppler.desktop
/usr/share/kservices5/okularTiff.desktop
/usr/share/kservices5/okularTxt.desktop
/usr/share/kservices5/okularXps.desktop
/usr/share/kservices5/okular_part.desktop
/usr/share/kservicetypes5/okularGenerator.desktop
/usr/share/kxmlgui5/okular/part-viewermode.rc
/usr/share/kxmlgui5/okular/part.rc
/usr/share/kxmlgui5/okular/shell.rc
/usr/share/metainfo/org.kde.okular-comicbook.metainfo.xml
/usr/share/metainfo/org.kde.okular-dvi.metainfo.xml
/usr/share/metainfo/org.kde.okular-fax.metainfo.xml
/usr/share/metainfo/org.kde.okular-fb.metainfo.xml
/usr/share/metainfo/org.kde.okular-ooo.metainfo.xml
/usr/share/metainfo/org.kde.okular-plucker.metainfo.xml
/usr/share/metainfo/org.kde.okular-poppler.metainfo.xml
/usr/share/metainfo/org.kde.okular-spectre.metainfo.xml
/usr/share/metainfo/org.kde.okular-tiff.metainfo.xml
/usr/share/metainfo/org.kde.okular-txt.metainfo.xml
/usr/share/metainfo/org.kde.okular-xps.metainfo.xml
/usr/share/metainfo/org.kde.okular.appdata.xml
/usr/share/metainfo/org.kde.okular.kirigami.appdata.xml
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
/usr/share/xdg/okular.categories

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
/usr/include/okular/core/settings_core.h
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
/usr/lib64/cmake/Okular5/Okular5Config.cmake
/usr/lib64/cmake/Okular5/Okular5ConfigVersion.cmake
/usr/lib64/cmake/Okular5/Okular5Targets-relwithdebinfo.cmake
/usr/lib64/cmake/Okular5/Okular5Targets.cmake
/usr/lib64/libOkular5Core.so

%files doc
%defattr(0644,root,root,0755)
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
/usr/share/doc/HTML/en/okular/tool-ellipse-okular.png
/usr/share/doc/HTML/en/okular/tool-highlighter-okular.png
/usr/share/doc/HTML/en/okular/tool-ink-okular.png
/usr/share/doc/HTML/en/okular/tool-line-okular.png
/usr/share/doc/HTML/en/okular/tool-note-inline-okular.png
/usr/share/doc/HTML/en/okular/tool-note-okular.png
/usr/share/doc/HTML/en/okular/tool-polygon-okular.png
/usr/share/doc/HTML/en/okular/tool-stamp-okular.png
/usr/share/doc/HTML/en/okular/tool-typewriter-okular.png
/usr/share/doc/HTML/en/okular/tool-underline-okular.png
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
/usr/share/doc/HTML/it/okular/index.cache.bz2
/usr/share/doc/HTML/it/okular/index.docbook
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
/usr/share/doc/HTML/pl/okular/enhance-lowcontrast.png
/usr/share/doc/HTML/pl/okular/enhance-shape.png
/usr/share/doc/HTML/pl/okular/enhance-solid.png
/usr/share/doc/HTML/pl/okular/enhance-thinline.png
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
/usr/share/doc/HTML/pt_BR/okular/configure.png
/usr/share/doc/HTML/pt_BR/okular/embedded-files-bar.png
/usr/share/doc/HTML/pt_BR/okular/forms-bar.png
/usr/share/doc/HTML/pt_BR/okular/index.cache.bz2
/usr/share/doc/HTML/pt_BR/okular/index.docbook
/usr/share/doc/HTML/pt_BR/okular/mainwindow.png
/usr/share/doc/HTML/pt_BR/okular/presentation.png
/usr/share/doc/HTML/sv/okular/configure.png
/usr/share/doc/HTML/sv/okular/index.cache.bz2
/usr/share/doc/HTML/sv/okular/index.docbook
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/libOkular5Core.so.9
/usr/lib64/libOkular5Core.so.9.0.0
/usr/lib64/qt5/plugins/okular/generators/okularGenerator_comicbook.so
/usr/lib64/qt5/plugins/okular/generators/okularGenerator_dvi.so
/usr/lib64/qt5/plugins/okular/generators/okularGenerator_fax.so
/usr/lib64/qt5/plugins/okular/generators/okularGenerator_fb.so
/usr/lib64/qt5/plugins/okular/generators/okularGenerator_ghostview.so
/usr/lib64/qt5/plugins/okular/generators/okularGenerator_ooo.so
/usr/lib64/qt5/plugins/okular/generators/okularGenerator_plucker.so
/usr/lib64/qt5/plugins/okular/generators/okularGenerator_poppler.so
/usr/lib64/qt5/plugins/okular/generators/okularGenerator_tiff.so
/usr/lib64/qt5/plugins/okular/generators/okularGenerator_txt.so
/usr/lib64/qt5/plugins/okular/generators/okularGenerator_xps.so
/usr/lib64/qt5/plugins/okularpart.so
/usr/lib64/qt5/qml/org/kde/okular/DocumentView.qml
/usr/lib64/qt5/qml/org/kde/okular/libokularplugin.so
/usr/lib64/qt5/qml/org/kde/okular/private/PageView.qml
/usr/lib64/qt5/qml/org/kde/okular/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/okular/COPYING
/usr/share/package-licenses/okular/COPYING.DOC
/usr/share/package-licenses/okular/COPYING.LIB
/usr/share/package-licenses/okular/cmake_modules_COPYING-CMAKE-SCRIPTS

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
/usr/share/man/sv/man1/okular.1
/usr/share/man/uk/man1/okular.1

%files locales -f okular.lang -f okular_chm.lang -f okular_comicbook.lang -f okular_djvu.lang -f okular_dvi.lang -f okular_epub.lang -f okular_fax.lang -f okular_fictionbook.lang -f okular_ghostview.lang -f okular_kimgio.lang -f okular_mobi.lang -f okular_ooo.lang -f okular_plucker.lang -f okular_poppler.lang -f okular_txt.lang -f okular_xps.lang -f org.kde.active.documentviewer.lang -f okular_markdown.lang
%defattr(-,root,root,-)

