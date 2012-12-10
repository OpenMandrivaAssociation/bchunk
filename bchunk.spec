%define name bchunk
%define version 1.2.0
%define release %mkrel 7

Summary: CD image format conversion from bin/cue to iso/cdr
Name: %{name}
Version: %{version}
Release: %{release}
Group: Archiving/Other
License: GPL
Url: http://hes.iki.fi/bchunk
Source: %{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot

%description
This is a Unix/C rewrite of the fine BinChunker software for
some non-Unix system. The non-Unix version of BinChunker
can be found at http://home.ptd.net/~redline/binchunker.html .
Thanks go to Bob Marietta <marietrg@SLU.EDU>, the author of
BinChunker, for the extensive help, documentation and letting me
look at his Pascal/Delphi source code!

binchunker converts a CD image in a ".bin / .cue" format
(sometimes ".raw / .cue") to a set of .iso and .cdr tracks.

The bin/cue format is used by some non-Unix cd-writing
software, but is not supported on most other cd-writing
programs.

The .iso track contains an ISO file system, which can be
mounted through a loop device on Linux systems, or
written on a CD-R using cdrecord.

The .cdr tracks are in the native CD audio format. They can
be either written on a CD-R using cdrecord -audio, or converted
to WAV (or any other sound format for that matter) using
sox.

%prep

%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" make

%install
rm -rf $RPM_BUILD_ROOT

install -m 755 -d  $RPM_BUILD_ROOT%{_bindir}
install -m 755 bchunk $RPM_BUILD_ROOT%{_bindir}

%files
%defattr (-,root,root)
%doc COPYING README bchunk-%{version}.lsm
%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-7mdv2011.0
+ Revision: 616744
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 1.2.0-6mdv2010.0
+ Revision: 424024
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.2.0-5mdv2009.0
+ Revision: 243207
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.2.0-3mdv2008.1
+ Revision: 135828
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import bchunk


* Tue Aug 01 2006 Lenny Cartier <lenny@mandriva.com> 1.2.0-3mdv2007.0
- rebuild

* Wed Jul 06 2005 Lenny Cartier <lenny@mandriva.com> 1.2.0-2mdk
- rebuild

* Wed Jun 30 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2.0-1mdk
- 1.2.0

* Fri Feb 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.1.1-4mdk
- rebuild

* Fri Jan 24 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.1.1-3mdk
- rebuild

* Thu Aug 29 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.1.1-2mdk
- rebuild

* Sat Aug 25 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.1.1-1mdk
- updated to  1.1.1

* Wed Jun 27 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-5mdk
- rebuild

* Fri Jan 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-4mdk 
- rebuild

* Fri Jul 28 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.0-3mdk
- BM

* Tue Apr 20 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-2mdk
- fix group


* Mon Feb 07 2000 Lenny Cartier <lenny@mandrakesoft.com>
- mandrake build

* Thu Nov  5 1998 Fryguy_ <fryguy@falsehope.com>
  [bchunk-1.0.0-1]
- Initial Release    
