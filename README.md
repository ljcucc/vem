# VEM - A Multipass Utils (currently)

> ⚠️ WARNING: unfinished project

this is a very simple tool collection to help you get around your development environments with npm-like, pipenv-style operation.

## Installation

```bash
# 1. pull repo to local machine
git clone https://github.com/ljcucc/vem.git ~/.vem

# 2. add bin to path
echo 'export PATH="$PATH:$HOME/.vem/"' >> ~/.zshrc

# 3. refresh zshrc
source ~/.zshrc
```

## Get Started

usage: `vem [commands] [options]`

> vem stands for **Virtualization Environment Manager**

1. cd to your project workspace folder
2. launch a VM by using command: `vem init`

## Roadmap (TODO)

- [ ] `vem init`: start up automation tool
  - [x] generate `mpconfig.json`
  - [x] auto create instance by using `mpconfig.json`
- [ ]  `vem pkg`: package and solution management tool for dependencies
  - [ ] `vem pkg install`: AKA apt-get install package to instance and add dependency to mpconfig.json
  - [ ] `vem pkg uninstall`: AKA apt-get uninstall package from instance and remove dependency to mpconfig.json
  - [ ] `vem pkg list`: list all dependencies package
- [ ] `vem config`: update, get, set config to a VM instance, everytime config updated, VM will be recreate.
  - [ ] `vem config update`: update `mpconfig.json` settings
  - [ ] `vem config set`: set VM config
  - [ ] `vem config get`: get VM config
- [x] `vem rm`: remove current folder instance totally (delete + purge)
- [ ] `vem exec [command]`: execute command and recored it to config