Name:      rasa-telescope-client
Version:   1.0.0
Release:   0
Url:       https://github.com/warwick-one-metre/rasa-teld
Summary:   Telescope control client for the RASA prototype telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python34, python34-Pyro4, python34-warwick-observatory-common, python34-warwick-rasa-telescope

%description
Part of the observatory software for the RASA prototype telescope.

tel is a commandline utility for controlling the mount.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/tel %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/tel %{buildroot}/etc/bash_completion.d/tel

%files
%defattr(0755,root,root,-)
%{_bindir}/tel
/etc/bash_completion.d/tel

%changelog
