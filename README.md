# 🌡️ HeatHaiku

> Transform your CPU temperature into beautiful poetry

HeatHaiku monitors your CPU temperature and generates personalized haikus based on thermal states. From icy cool
processors to blazing hot cores, every temperature tells a story in 5-7-5 syllables.

## 📋 Requirements

- **Python 3.8+**
- **Linux** (with CPU temperature sensors)
- **psutil** library for system monitoring

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/GarySkywalker-droid/HeatHaiku.git
cd HeatHaiku

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode
make install
# or manually:
pip install -e .
```

## 🛠️ Development

### Setup Development Environment

``` bash
# Install with development dependencies
make install-dev
# or manually:
pip install -e .[dev]
```

### Available Make Commands

``` bash
make install      # Install package in development mode
make install-dev  # Install with development dependencies
make run          # Run the application
make lint         # Run linting (ruff + pyright)
make format       # Format code with black
make clean        # Clean build artifacts
```
