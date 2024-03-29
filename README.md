# ato

**A**lternative **T**o **O**riginLab (?Maybe)

## Introduction

Try to make a cross-platform CLI to plot charts instead of OriginLab.

## Requirements

Before you build this CLI, you need to install the following requirements.

```
numpy
pandas
matplotlib
pyinstaller
```

## Build

Build from source code.

```shell
pyinstaller -F main.py
```

## Usage

```
Basic Commands:
    'quit' ---- Quit this CLI.
    'help' ---- Show this message.
    'version' ---- Show version.
Plotting Commands:
    'line-chart' ---- Plot a line chart.
    'fitting' ---- Fitting tool.
    'pie-chart' ---- Plot a pie chart.
    'average' ---- Calculate average.
    'standard-deviation' ---- Calculate standard deviation.
```

## Updates

### 2022-06-06

Adjust encoding settings.

### 2022-03-22

Add function.

- Calculate a set of data's standard deviation.

### 2022-03-21

Add function.

- Calculate a set of data's average.
- Fixed some problems.

### 2022-03-16

Released a package.

- Created a `.gitignore` file.
- Build a command line tool.

### 2022-03-15

Fixed some problems.

- Now it can judge your data.

### 2022-03-14

Updated.

- Now you can input and customize your data labels.

### 2022-03-13

New function.

- Add a new function for pie chart

### 2022-03-10

Updated.

- Added legend.
- Added picture's title.

### 2022-03-08

Created the CLI.

- Added line chart function to the CLI.
- Fixed some problems.

## TODO

TODO 01: Explode of the pie chart still need to be fixed.
