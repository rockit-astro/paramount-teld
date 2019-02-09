Name:           python36-warwick-rasa-telescope
Version:        1.0.0
Release:        0
License:        GPL3
Summary:        Common code for the SuperWASP upgrade prototype mount controller
Url:            https://github.com/warwick-one-metre/
BuildArch:      noarch

%description
Part of the observatory software for the SuperWASP upgrade prototype.

python36-warwick-rasa-telescope holds the common telescope code.

%prep

rsync -av --exclude=build .. .

%build
%{__python3_other} setup.py build

%install
%{__python3_other} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_other_sitelib}/*

%changelog
