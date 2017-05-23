#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : golang-github-docker-go-units
Version  : 5d2041e26a699eaca682e2ea41c8f891e1060444
Release  : 6
URL      : https://github.com/docker/go-units/archive/5d2041e26a699eaca682e2ea41c8f891e1060444.tar.gz
Source0  : https://github.com/docker/go-units/archive/5d2041e26a699eaca682e2ea41c8f891e1060444.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 CC-BY-SA-4.0
BuildRequires : go

%description
[![GoDoc](https://godoc.org/github.com/docker/go-units?status.svg)](https://godoc.org/github.com/docker/go-units)

%prep
%setup -q -n go-units-5d2041e26a699eaca682e2ea41c8f891e1060444

%build

%install
gopath="/usr/lib/golang"
library_path="github.com/docker/go-units"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done

%check
gopath="/usr/lib/golang"
export GOPATH="%{buildroot}${gopath}"
go test -v -x github.com/docker/go-units

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/docker/go-units/duration.go
/usr/lib/golang/src/github.com/docker/go-units/duration_test.go
/usr/lib/golang/src/github.com/docker/go-units/size.go
/usr/lib/golang/src/github.com/docker/go-units/size_test.go
/usr/lib/golang/src/github.com/docker/go-units/ulimit.go
/usr/lib/golang/src/github.com/docker/go-units/ulimit_test.go
