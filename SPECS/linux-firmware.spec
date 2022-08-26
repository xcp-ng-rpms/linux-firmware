%global package_speccommit e2db0a7fa1dfba4496c26861070edecb6a544b1b
%global usver 20211027
%global xsver 2
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global package_srccommit f5d519563ac9d2d1f382a817aae5ec5473811ac8
Name: linux-firmware
Version: 20211027
Release: %{?xsrel}%{?dist}
Summary: Firmware files used by the Linux kernel

Group: System Environment/Kernel
License: GPL, GPLv2, GPLv2+, GPLv3, MIT and Redistributable, no modification permitted
URL: http://www.kernel.org/
Source0: linux-firmware.tar.gz
BuildArch: noarch
Requires: udev
BuildRequires:  kernel-devel

%description
Firmware files required for some devices to operate.

%prep
%autosetup -p1

%build
# Remove AMD Microcode (packaged separately)
%{__rm} -rf amd-ucode LICENSE.amd-ucode

# Remove wifi and other firmware
%{__rm} dvb*
%{__rm} iwlwifi*
%{__rm} v4l*
%{__rm} *.sbcf
%{__rm} -rf ar3k
%{__rm} -rf ath10k
%{__rm} -rf ath11k
%{__rm} -rf ath6k
%{__rm} -rf ath9k_htc
%{__rm} -rf brcm
%{__rm} -rf carl9170fw
%{__rm} -rf cypress
%{__rm} -rf dabusb
%{__rm} -rf dpaa2
%{__rm} -rf libertas
%{__rm} -rf liquidio
%{__rm} -rf mediatek
%{__rm} -rf mellanox/mlxsw_spectrum*
%{__rm} -rf meson
%{__rm} -rf mrvl
%{__rm} -rf mwlwifi
%{__rm} -rf netronome
%{__rm} -rf qca
%{__rm} -rf qcom
%{__rm} -rf rtl_bt
%{__rm} -rf rtlwifi
%{__rm} -rf ti-connectivity
%{__rm} -rf ueagle-atm

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
* Fri Apr 8 2022 Andrew Cooper <andrew.cooper3@citrix.com> 20211027-2
- Exclude AMD microcode.  Moved to new package.

* Wed Nov 17 2021 Igor Druzhinin <igor.druzhinin> - 20211027-1
- CP-38643: Update to latest version

* Wed Dec 02 2020 Ross Lagerwall <ross.lagerwall@citrix.com> - 20190314-2
- CP-35517: Build for koji

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
