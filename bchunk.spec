Summary: CD image format conversion from bin/cue to iso/cdr
Name: bchunk
Version: 1.2.2
Release: 1
Group: Archiving/Other
License: GPL
Url: http://hes.iki.fi/bchunk
Source0: https://github.com/hessu/bchunk/archive/release/%{version}.tar.gz

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

%autosetup -p1 -n %{name}-release-%{version}

%build
%make_build

%install
rm -rf $RPM_BUILD_ROOT

install -m 755 -d  $RPM_BUILD_ROOT%{_bindir}
install -m 755 bchunk $RPM_BUILD_ROOT%{_bindir}

%files
%defattr (-,root,root)
%license COPYING
%doc README
%{_bindir}/*
