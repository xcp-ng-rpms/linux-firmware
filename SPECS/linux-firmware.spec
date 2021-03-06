Name: linux-firmware
Version: 20190314
Release: 1%{?dist}
Summary: Firmware files used by the Linux kernel

Group: System Environment/Kernel
License: GPL, GPLv2, GPLv2+, GPLv3, MIT and Redistributable, no modification permitted
URL: http://www.kernel.org/

Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/linux-firmware/archive?at=7bc246451318b3536d9bfd3c4e46d541a9831b33&format=tar.gz&prefix=linux-firmware-20190314#/linux-firmware.tar.gz



BuildArch: noarch
Requires: udev
BuildRequires:  kernel-devel

%description
Firmware files required for some devices to operate.

%prep
%autosetup -p1

%build
# Remove wifi and other firmware
%{__rm} iwlwifi*
%{__rm} v4l*
%{__rm} *.sbcf
%{__rm} -rf ar3k
%{__rm} -rf ath10k
%{__rm} -rf ath6k
%{__rm} -rf ath9k_htc
%{__rm} -rf brcm
%{__rm} -rf carl9170fw
%{__rm} -rf dabusb
%{__rm} -rf libertas
%{__rm} -rf liquidio
%{__rm} -rf mrvl
%{__rm} -rf mwlwifi
%{__rm} -rf rtlwifi
%{__rm} -rf ti-connectivity
%{__rm} -rf ueagle-atm
%{__rm} -rf qcom
%{__rm} -rf netronome

# Remove source files we don't need to install
%{__rm} -f usbdux/*dux */*.asm Makefile configure check_whence.py

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}/lib/firmware
%{__cp} -rp * %{buildroot}/lib/firmware
%{__rm} %{buildroot}/lib/firmware/{GPL-*,README,WHENCE,LICENCE.*,LICENSE.*}

%post
%{regenerate_initrd_post}

%postun
%{regenerate_initrd_postun}

%posttrans
%{regenerate_initrd_posttrans}

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc GPL-* README WHENCE LICENCE.* LICENSE.*
/lib/firmware/*

%changelog
* Thu Mar 21 2019 Ross Lagerwall <ross.lagerwall@citrix.com> - 20190314-1
- Update to latest version
- Drop extra chelsio firmware

* Thu Mar 07 2019 Thomas Mckelvey <thomas.mckelvey@citrix.com> - 20180606-2
- Update chelsio firmware version to 1.22.9.0

* Wed Jun 27 2018 Ross Lagerwall <ross.lagerwall@citrix.com> - 20180606-1
- Update to latest version.
- Drop extra AMD family 17h microcode

* Wed Dec 20 2017 Simon Rowe <simon.rowe@citrix.com> 20170622-3
- Add AMD family 17h microcode
* Tue Sep 05 2017 Sergey Dyasly <sergey.dyasli@citrix.com> 20170622-2
- Add initrd regeneration

* Mon Nov 18 2013 Malcolm Crossley <malcolm.crossley@citrix.com>
- Remove wifi firmware to reduce package size
* Fri May 04 2012 David Vrabel <david.vrabel@citrix.com>
- Remove firmware file included in firmware-chelsio-cxgb3 package.
* Tue Mar 06 2012 David Vrabel <david.vrabel@citrix.com>
- New package derived from fedora 17 package.
