#
# spec file for package python3-warwick-rasa-telescope
#
# Copyright (c) 2016 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           python34-warwick-rasa-telescope
Version:        1.0.0
Release:        0
License:        GPL3
Summary:        Common code for the SuperWASP upgrade prototype mount controller
Url:            https://github.com/warwick-one-metre/
BuildArch:      noarch

%description
Part of the observatory software for the SuperWASP upgrade prototype.

python3-warwick-rasa-telescope holds the common telescope code.

%prep

rsync -av --exclude=build .. .

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
