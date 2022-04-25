# VEM - A Multipass Utils (currently)

> ⚠️ WARNING: unfinished project - anytime, anywhen the source code may changes several times, currently unstable, tasks on roadmap currently implementing.

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
  * if `mpconfig.json` exists, then `vem` will auto setup VM and install all packages
  * if not, `vem` will ask to setup config (just like `npm init`)
3. if you want to stop current VM (maybe saving space on hard drive or abort VM), type `vem rm` to remove all stuff
4. copy your project to someone else, and run (1) to start your environment again

## Roadmap (TODO)

- [ ] `vem init`: start up automation tool
  - [x] generate `mpconfig.json`
  - [x] auto create instance by using `mpconfig.json`
  - [x] auto install packages when init from a exist `mpconfig.json`
  - [ ] auto mount Workspace folder to VM
- [ ]  `vem pkg`: package and solution management tool for dependencies
  - [ ] `vem pkg install`: AKA apt-get install package to instance and add dependency to `mpconfig.json`
    - [x] supprt `apt-get install`
    - [x] support other PM and optional sudo
    - [ ] implements for other PM
  - [ ] `vem pkg uninstall`: AKA apt-get uninstall package from instance and remove dependency to `mpconfig.json`
    - [x] supprt `apt-get uninstall`
    - [x] support other PM and optional sudo
    - [ ] implements for other PM
  - [ ] `vem pkg list`: list all dependencies package
- [ ] `vem config`: update, get, set config to a VM instance, everytime config updated, VM will be recreate.
  - [ ] `vem config update`: update `mpconfig.json` settings
  - [ ] `vem config set`: set VM config
  - [ ] `vem config get`: get VM config
- [x] `vem rm`: remove current folder instance totally (delete + purge)
- [ ] `vem exec [command]`: execute command and recored it to config
- [ ] `vem shell [command]`: enter instance shell to execute command (not recommended to do that)
- [ ] `vem doctor`: A command tool to help you setup and diagnosis vem
- [ ] `vem build`: build a docker image for current developement

## Configuration design

`mpconfig.json` is the config file of `vem`, here's a template of a regular config file looks like:
```js
{
  "version": 1,                      // current version
  "name": "aabbCC-helloworld",       // instance name
  "disk": "10G",                     // instance disk size
  "dir": "/Users/ITWolf/Workspace/", // dir path to workspace
  "packages": [                      // packages to install at the first time
    "nodejs",
    "build-essential"
  ]

}
```