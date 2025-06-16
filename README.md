# Stock Market Analysis: NASDAQ Deep Dive

## Table of Contents
- [Overview](#overview)
- [Research Questions](#research-questions)
  - [1. Tariff Impact Analysis](#1-tariff-impact-analysis)
  - [2. Market Correlation Study](#2-market-correlation-study)
  - [3. Institutional Performance Comparison](#3-institutional-performance-comparison)
- [Dataset](#dataset)
- [Methodology](#methodology)
  - [Data Analysis Pipeline](#data-analysis-pipeline)
  - [Key Metrics](#key-metrics)
- [Expected Deliverables](#expected-deliverables)
  - [Analysis Reports](#analysis-reports)
  - [Visualizations](#visualizations)
- [Tools and Technologies](#tools-and-technologies)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Results Summary](#results-summary)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)
- [Contact](#contact)

## Overview
This project analyzes key factors that can provide advantages in stock market trading, with a focus on the NASDAQ exchange. We examine the interplay between tariffs, market correlations, and institutional performance to identify profitable trading opportunities.

## Research Questions

### 1. Tariff Impact Analysis
**How will ongoing tariffs affect stock market prices?**
- Analyze sector-specific impact of trade policies
- Identify which industries benefit vs. suffer from tariff implementations
- Examine historical correlations between tariff announcements and market movements
- Focus on import-dependent vs. export-heavy companies

### 2. Market Correlation Study
**How does the NASDAQ affect S&P 500 and other market indices?**
- Quantify correlation coefficients between major indices
- Identify lead-lag relationships in market movements
- Analyze sector rotation patterns between tech-heavy NASDAQ and broader S&P 500
- Examine divergence opportunities for arbitrage strategies

### 3. Institutional Performance Comparison
**Do hedge funds consistently outperform the S&P 500?**
- Compare risk-adjusted returns of hedge fund strategies vs. index performance
- Analyze alpha generation across different market conditions
- Examine fee impact on net investor returns
- Identify market conditions where active management adds value

## Dataset
**Source:** [Kaggle - Price Volume Data for All US Stocks & ETFs](https://www.kaggle.com/datasets/borismarjanovic/price-volume-data-for-all-us-stocks-etfs)

**Contents:**
- Historical price and volume data for US stocks and ETFs
- Daily OHLC (Open, High, Low, Close) prices
- Trading volume information
- Coverage spans multiple years of market data

## Methodology

### Data Analysis Pipeline
1. **Data Preprocessing**
   - Clean and normalize price data
   - Handle missing values and stock splits
   - Calculate returns and volatility metrics

2. **Feature Engineering**
   - Technical indicators (RSI, MACD, Bollinger Bands)
   - Market correlation metrics
   - Sector classification and weighting

3. **Statistical Analysis**
   - Correlation analysis between indices
   - Regression modeling for tariff impact
   - Risk-adjusted performance metrics (Sharpe ratio, alpha, beta)

4. **Visualization**
   - Time series plots of market movements
   - Correlation heatmaps
   - Performance comparison charts

### Key Metrics
- **Sharpe Ratio**: Risk-adjusted returns
- **Beta**: Market sensitivity
- **Alpha**: Excess returns vs. benchmark
- **Maximum Drawdown**: Worst peak-to-trough decline
- **Correlation Coefficient**: Relationship strength between assets

## Expected Deliverables

### Analysis Reports
1. **Tariff Impact Assessment**
   - Sector vulnerability analysis
   - Trading strategy recommendations
   - Risk management guidelines

2. **Inter-Market Correlation Study**
   - Cross-index relationship mapping
   - Arbitrage opportunity identification
   - Portfolio diversification insights

3. **Institutional vs. Passive Performance**
   - Comprehensive performance comparison
   - Cost-benefit analysis of active management
   - Market timing effectiveness evaluation

### Visualizations
- Interactive dashboards showing real-time correlations
- Historical performance comparisons
- Sector rotation patterns
- Risk-return scatter plots

## Tools and Technologies
- **Python**: Primary analysis language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib/Seaborn**: Data visualization
- **Scikit-learn**: Machine learning models
- **Jupyter Notebooks**: Interactive analysis environment

## Installation and Setup

```bash
# Clone the repository
git clone [repository-url]
cd stock-market-analysis

# Install required packages
pip install -r requirements.txt

# Download dataset from Kaggle
kaggle datasets download -d borismarjanovic/price-volume-data-for-all-us-stocks-etfs

# Extract data
unzip price-volume-data-for-all-us-stocks-etfs.zip -d data/
```

## Usage

```python
# Load and analyze data
from src.data_loader import load_stock_data
from src.analysis import TariffAnalysis, CorrelationAnalysis

# Initialize analysis modules
tariff_analyzer = TariffAnalysis()
correlation_analyzer = CorrelationAnalysis()

# Run analysis
results = tariff_analyzer.analyze_sector_impact()
correlations = correlation_analyzer.calculate_cross_correlations()
```

## Project Structure
```
├── data/                   # Raw and processed data files
├── notebooks/              # Jupyter notebooks for analysis
│   ├── 01_{name}.ipynb
├── src/                    # Source code modules
│   ├── data_loader.py     # Data loading utilities
│   ├── analysis.py        # Core analysis functions
│   ├── visualization.py   # Plotting and charting
│   └── utils.py           # Helper functions
├── results/               # Analysis outputs and reports
│   ├── .html
│   ├── .pdf
│   └── .xlsx
├── requirements.txt       # Python dependencies
└── README.md             # This file
```


## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/analysis-improvement`)
3. Commit your changes (`git commit -am 'Add new analysis feature'`)
4. Push to the branch (`git push origin feature/analysis-improvement`)
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer
This analysis is for educational and research purposes only. It does not constitute financial advice. Always consult with qualified financial professionals before making investment decisions.

## Contact
For questions or collaboration opportunities, please open an issue or contact the project maintainer.
