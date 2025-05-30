# OpenCortex for Brain-Computer Interfaces
OpenCortex is a fully-featured EEG streamer that includes a classifier and a GUI to visualize the data in real-time.  
Via the LabStreamingLayer (LSL) protocol, it can receive and send data to any compatible device or software and be used
to build real-time neural applications (BCI, neurofeedback, etc.).

![OpenCortex StreamerGUI](https://github.com/BRomans/OpenCortex/blob/main/img/interface.png?raw=true)

## Features
- GUI to plot EEG in real-time
- Signal real-time filtering (bandpass, notch) 
- Signal quality estimators
- Save custom markers on the data
- Inlet stream to mark the data with external triggers
- Outlet stream that can send raw EEG to an external receiver
- General-purpose classifier interface that can be initialized with any model from Scikit-Learn
- Cross-validation plots with ROC curve and Confusion Matrix

## Table of Contents

- [Supported Devices](#supported-devices)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Issues](#issues)
- [Usage](#usage)
- [Examples](#examples)
- [Notebooks](#notebooks)
- [Building](#building)
    - [Wheel Distribution](#wheel-distribution)
    - [Source Distribution](#source-distribution)
- [Contributing](#contributing)
- [License](#license)

## Supported Devices
- Any EEG board listed on [Brainflow documentation](https://brainflow.readthedocs.io/en/stable/SupportedBoards.html)
- (Coming Soon) Emotiv Epoc and other consumer EEG devices

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

List any software or dependencies that need to be installed before setting up the project.

- Python 3.8 or higher (earlier versions might work, but they are not tested)
- [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

```bash
# Example: 
# Python 3
sudo apt-get install python3
```
### Installation and Usage with pip
You can install the package using command:
```bash
pip install opencortex
```

To run the OpenCortex Streamer:
```bash
python -m opencortex
```
or even just:
```bash 
opencortex
```
>[!Important]
>The package is still in development, so it is recommended to install it in a virtual environment.


### Local Installation
If you want to install the package locally, for example to modify the source code, follow these steps:
1. Clone the repository
```bash
git clone https://github.com/BRomans/OpenCortex.git
cd OpenCortex
```
2. Create a virtual environment
```bash
# Using venv
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

```
3. Install the required packages
```bash
pip install -r requirements.txt
```

4. Solve issues with PyBluez

The base requirement for bluetooth scanning is `pybluez2`, which is a Python wrapper for the BlueZ Linux Bluetooth stack.
There might be [issues](https://stackoverflow.com/questions/74196428/pip-install-pybluez2-package-directory-bluetooth-macos-does-not-exist) installing the package from pip, so it is recommended to install it from the source.
```bash
pip install git+https://github.com/airgproducts/pybluez2.git@0.46
```
Alternatively, you can install `pybluez`, which should silently be called instead of `pybluez2`.
If you encounter issues installing PyBluez, please refer to the latest comments on the project [issues page](https://github.com/pybluez/pybluez/issues/431).

## Usage
To run any example, use the following command:
```bash
cd examples
python <example_name>.py
```
To run the EEG Streamer app, use the following command:
```bash
python opencortex/__main__.py
```

## Examples
The [examples](examples) folder contains single runnable scripts that demonstrate how to handle data collected
using g.tec hardware.

## Notebooks
The [notebooks](notebooks) folder contains some examples on how to use the utilities provided in this repository. You 
can run the notebooks using Jupyter, Jupyter Lab or Google Colab.

## Building
This project can be built as pip package using the following commands

### Source Distribution
If you want to build a source distribution, run the following command:
```bash
python setup.py sdist
```
Copy the content of the `dist` folder to the desired location and install the package using pip:
```bash
pip install <package_name>.tar.gz
```

### Wheel Distribution
Afterwards, to build a wheel distribution, run the following command:
```bash
python setup.py sdist bdist_wheel
```
Copy the content of the `dist` folder to the desired location and install the package using pip:
```bash
pip install <package_name>.whl
``` 





## Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome. 
1. Fork the project.
2. Create a new branch.
3. Make your changes and commit them.
4. Push to the branch and create a pull request.


## Credits
This project is freely available to anyone and is not intended for commercial use. If you use this project for academic 
purposes, please cite the original authors.

## License
This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details.
Packages used in this project are licensed under their respective licenses, as stated in the [Acknowledgments](#acknowledgments) 
section.

## Authors
- [Michele Romani](https://bromans.github.io/)

Please make sure to update the [AUTHORS](AUTHORS) file if you are contributing to the project.


## Acknowledgments
- [Brainflow](https://brainflow.readthedocs.io/en/stable/index.html), distributed under the MIT License.
- [LabStreamingLayer](https://labstreaminglayer.org/) distributed under the MIT License.
- [MNE](https://mne.tools/stable/index.html) distributed under the BSD 3-Clause License.
- [Scikit-learn](https://scikit-learn.org/stable/) distributed under the BSD 3-Clause License.

