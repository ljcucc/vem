# Multipass Utils

> ⚠️ WARNING: unfinished project

this is a very simple tool collection to help you get around your development environments with npm-like, pipenv-style operation.

## Get Started

usage: `vem [commands] [options]`

> vem stands for **Virtualization Environment Manager**

1. cd to your project workspace folder
2. launch a VM by using command: `vem init`

## Progress (TODO)

- [ ] `vem init`: start up automation tool
  - [x] generate `mpconfig.json`
  - [ ] auto create instance by using `mpconfig.json`
- [ ]  `vem pkg`: package and solution management tool
  - [ ] `vem pkg install`: AKA apt-get install but record installed on mpconfig.json
  - [ ] `vem pkg uninstall`: AKA apt-get uninstall but remove uninstalled from mpconfig.json