%global package_speccommit 6688ab11280d1c0fe6644c212794c627dfcd8f70
%global usver 20190314
%global xsver 11
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global package_srccommit 7bc246451318b3536d9bfd3c4e46d541a9831b33
Name: linux-firmware
Version: 20190314
Release: %{?xsrel}.1%{?dist}
Summary: Firmware files used by the Linux kernel

Group: System Environment/Kernel
License: GPL, GPLv2, GPLv2+, GPLv3, MIT and Redistributable, no modification permitted
URL: http://www.kernel.org/
Source0: linux-firmware.tar.gz
BuildArch: noarch
Requires: udev
BuildRequires:  kernel-devel
Source1: microcode_amd_fam17h.bin
Source2: microcode_amd_fam19h.bin

# XCP-ng
Source10: rtl8125a-3.fw
Source11: rtl8125b-1.fw
Source12: rtl8125b-2.fw

%description
Firmware files required for some devices to operate.

%prep
%autosetup -p1
cp %{SOURCE1} %{SOURCE2} amd-ucode/

# XCP-ng
cp %{SOURCE10} %{SOURCE11} %{SOURCE12} rtl_nic/

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
* Wed May 15 2024 Gael Duperrey <gduperrey@vates.tech> - 20190314-11.1
- Synced from hotfix XS82ECU1067
- *** Upstream changelog ***
- * Fri May 10 2024 Andrew Cooper <andrew.cooper3@citrix.com> - 20190314-11
- - Update to the 2024-05-03 drop.
-   Updated CPUs:
-     ZP-B2 00800f12: 2021-11-11, rev 0800126e -> 2023-12-19, rev 0800126f
-    SSP-B0 00830f10: 2023-08-16, rev 0830107b -> 2023-12-18, rev 0830107c
-     GN-B0 00a00f10: 2023-06-09, rev 0a001079 -> 2024-02-26, rev 0a00107a
-     GN-B1 00a00f11: 2023-08-23, rev 0a0011d3 -> 2024-02-23, rev 0a0011d5
-     GN-B2 00a00f12: 2023-08-31, rev 0a001236 -> 2024-02-26, rev 0a001238
-     RS-B1 00a10f11: 2023-09-06, rev 0a101144 -> 2024-02-23, rev 0a101148
-     RS-B2 00a10f12: 2023-09-11, rev 0a101244 -> 2024-02-26, rev 0a101248
-   RSDN-A2 00aa0f02: 2023-09-11, rev 0aa00213 -> 2024-02-28, rev 0aa00215

* Fri Nov 24 2023 Samuel Verschelde <stormi-xcp@ylix.fr> - 20190314-10.2
- Add firmware for rtl8125

* Thu Nov 16 2023 Gael Duperrey <gduperrey@vates.tech> - 20190314-10.1
- Synced from hotfix XS82ECU1057
- *** Upstream changelog ***
- * Mon Nov 6 2023 Andrew Cooper <andrew.cooper3@citrix.com> - 20190314-10
- - Update to the 2023-10-19 AMD microcode drop
-   Updated CPUs:
-     RS-B1 00a10f11: 2023-06-20, rev 0a10113e -> 2023-09-06, rev 0a101144
-     RS-B2 00a10f12: 2023-06-20, rev 0a10123e -> 2023-09-11, rev 0a101244
-   RSDN-A2 00aa0f02: 2023-06-19, rev 0aa00212 -> 2023-09-11, rev 0aa00213

* Tue Aug 08 2023 Gael Duperrey <gduperrey@vates.fr> - 20190314-9.1
- Synced from hotfix XS82ECU1045
- *** Upstream changelog ***
- * Wed Jul 26 2023 Alejandro Vallejo <alejandro.vallejo@cloud.com> 20190314-9
- - Add new CPUs to the microcode blob:
- - RS-B1 00a10f11: 2023-06-20, rev 0a10113e
- - RS-B2 00a10f12: 2023-06-20, rev 0a10123e
- - RSDN-A1 00aa0f01: 2023-06-19, rev 0aa00116
- - RSDN-A2 00aa0f02: 2023-06-19, rev 0aa00212
- * Fri Jul 21 2023 Alejandro Vallejo <alejandro.vallejo@cloud.com> 20190314-8
- - Update to the 2023-07-19 drop.

* Mon Jul 24 2023 Gael Duperrey <gduperrey@vates.fr> - 20190314-8.1
- Synced from hotfix XS82ECU1041
- Fixes for XSA-433 CVE-2023-20593

* Thu May 11 2023 Samuel Verschelde <stormi-xcp@ylix.fr> - 20190314-7.1
- Synced from hotfix XS82ECU1030
- *** Upstream changelog ***
- * Tue Apr 18 2023 Andrew Cooper <andrew.cooper3@citrix.com> - 20190314-7
- - Update to the 2023-04-13 drop.  Manually fix up the SSP-B0 date.

* Thu Feb 23 2023 Gael Duperrey <gduperrey@vates.fr> - 20190314-6.1
- Synced from hotfix XS82ECU1026
- *** Upstream changelog ***
- * Tue Feb 7 2023 Andrew Cooper <andrew.cooper3@citrix.com> - 20190314-6
- - Update AMD microcode to the 2023-01-31 drop

* Thu Feb 16 2023 Samuel Verschelde <stormi-xcp@ylix.fr> - 20190314-5.1
- Update AMD microcode to the 2023-02-10 drop

* Fri Sep 30 2022 Andrew Cooper <andrew.cooper3@citrix.com> - 20190314-5
* Update AMD microcode to the 2022-09-30 drop

* Fri May 6 2022 Andrew Cooper <andrew.cooper3@citrix.com> - 20190314-4
* Update AMD microcode to the 2022-04-11 drop

* Tue Mar 1 2022 Andrew Cooper <andrew.cooper3@citrix.com> - 20190314-3
- Update AMD microcode for Fam17h and Fam19h

* Fri Nov 19 2021 Igor Druzhinin <igor.druzhinin@citrix.com> - 20190314-2
- CP-38643: Update AMD microcode for Fam17h and Fam19h

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
