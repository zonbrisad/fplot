
<p align="center">
  <img width="150" height="150" src="icon/fplot_128x128.png">
</p>

<div style="text-align: center">

<h1>fplot</h1>

</div>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
  - [Runtime](#runtime)
  - [Development](#development)
- [Install](#install)
  - [Download](#download)
  - [Installation](#installation)
- [Freqlenty asked Questions](#freqlenty-asked-questions)
- [Links](#links)
- [Contribute](#contribute)
- [License](#license)
- [Some examples, remove after creation](#some-examples-remove-after-creation)
- [The largest heading](#the-largest-heading)
  - [The second largest heading](#the-second-largest-heading)
          - [The smallest heading](#the-smallest-heading)
  - [Tables](#tables)
  - [List](#list)
  - [Task list](#task-list)
  - [Colapsed section](#colapsed-section)
    - [We can hide anything, even code!](#we-can-hide-anything-even-code)
  - [Links](#links-1)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## About

Fplot is a program for quick and easy visualization of realtime data from files in procfs and sysfs.

## Features

- Realtime graphical plots of data from files in procfs and sysfs.
- Realtime plot of CPU load (--cpu)
- Realtime plot of process cpu usage (--pid)
- Average function
- Config file

## Requirements

Python 3
PyQt6
pyqtgraph

## Install

### Download

```bash
git clone https://github.com/zonbrisad/fplot.git
```

### Installation

```bash
>apt install python3-pyqtgraph
```

or

```bash
>pip install pyqtgraph 
```

### Configuration

Add to directory to PATH or run:

```bash
>source fplot_init 
```

## Usage

### Option "--plot"

### Option "--plotrc"

### Option "--cpu"

### Option "--pid"

### Option "--conf"

Fplot supports plot configurations in json files.

```json
{
    "title": "Memory",
    "columns": 1,
    "interval": 1000,
    "datapoints": 1000,
    "plots": [
        {
            "file": "/proc/meminfo",
            "cmd": "",
            "row": "MemFree",
            "col": 2,
            "title": "MemFree (MB)",
            "divider": 1024
        },
        {
            "file": "/proc/meminfo",
            "cmd": "",
            "row": "MemAvailable",
            "col": 2,
            "title": "MemAvailable (MB)",
            "divider": 1024
        },
        {
            "file": "/proc/meminfo",
            "cmd": "",
            "row": "Cached",
            "col": 2,
            "title": "Cached (MB)",
            "divider": 1024
        },
        {
            "file": "/proc/meminfo",
            "cmd": "",
            "row": "Buffers",
            "col": 2,
            "title": "Buffers (MB)",
            "divider": 1024
        },
        {
            "file": "/proc/meminfo",
            "cmd": "",
            "row": "Active",
            "col": 2,
            "title": "Active (MB)",
            "divider": 1024
        }
    ]
}
```

![alt text](images/mem_json.png)

## History

[HISTORY.md](/HISTORY.md)

## ToDo

- [x] icon
- [ ] Support gpio
- [ ] Colors
- [ ] guide lines in graphs
- [ ] multiple plots in graphs
- [x] averaging
- [ ] save/recover data
- [ ] screenshot button
- [ ] pause button
- [ ] change to timestamps as x axis
- [ ] arithmetics
- [ ] counting
- [ ] integrating
- [ ] finding min/max
- [ ] Add: option to generate template config file
- [ ] Add: Local directory for storage of userdefined config scripts ~/.config/fplot
- [ ] Automatic detection of file type
- [ ] Individual timer for all plots
- [ ] Derived plots, plots based on other plots, downsampling, average, derivation
- [x] Invividual plot Title

## License
