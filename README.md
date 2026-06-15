# Equation Visualizer

## Overview

Equation Visualizer is an interactive mathematical analysis platform developed using Python, Streamlit, SymPy, NumPy, and Plotly. The application enables users to visualize mathematical functions, perform symbolic calculus operations, analyze critical points and roots, compute integrals, and explore three-dimensional surfaces through an intuitive web interface.

The project combines symbolic mathematics and interactive visualization to create a powerful educational and analytical tool for students, researchers, and mathematics enthusiasts.

---

## Features

### 2D Function Visualization

* Plot mathematical functions interactively.
* Zoom, pan, and inspect coordinates.
* Support for common mathematical expressions.

Examples:

```text
x^2
x^3 - 3*x
sin(x)
cos(x)
exp(x)
log(x)
```

### Symbolic Differentiation

* Compute first derivatives automatically.
* Display derivative expressions.
* Plot original and derivative functions simultaneously.

### Critical Point Analysis

* Detect stationary points.
* Identify local maxima and local minima using the second derivative test.
* Display critical point coordinates.

### Root Finding

* Compute real roots of equations.
* Highlight roots directly on the graph.
* Display numerical root values.

### Integration

* Compute indefinite integrals symbolically.
* Compute definite integrals over user-defined intervals.
* Visualize the area under the curve.

### Interactive 3D Surface Visualization

* Plot functions of two variables.
* Rotate, zoom, and inspect surfaces interactively.

Examples:

```text
x^2 + y^2
x*y
x^2 - y^2
sin(sqrt(x^2+y^2))
```

---

## Technologies Used

* Python
* Streamlit
* SymPy
* NumPy
* Plotly

---

## Mathematical Capabilities

The platform currently supports:

* Function plotting
* Symbolic differentiation
* Critical point detection
* Root finding
* Definite and indefinite integration
* Area under curve visualization
* Interactive 3D surface rendering

---

## Project Structure

```text
EquationVisualizer/
│
├── app.py
├── requirements.txt
├── README.md
└── venv/
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd EquationVisualizer
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Windows:

```bash
.\venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

The application will launch in your browser at:

```text
http://localhost:8501
```

---

## Example Applications

* Calculus education
* Mathematical visualization
* Engineering analysis
* Scientific computing
* Function exploration
* Interactive learning

---

## Future Enhancements

Planned improvements include:

* Tangent and normal line visualization
* Inflection point analysis
* Differential equation solving
* Exporting graphs as images
* PDF report generation
* Multiple function comparison
* Enhanced user interface

---

## Author

Developed as a mathematical visualization and analysis project demonstrating symbolic computation, numerical methods, calculus, and scientific visualization using Python.
