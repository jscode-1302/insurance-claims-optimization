# Insurance Claims Analysis

A complete end-to-end data analysis project demonstrating statistical analysis, hypothesis testing, A/B testing, and regression modeling to identify opportunities for improving operational efficiency and customer satisfaction in insurance claims processing.

## Project Overview

This project analyzes 1,243 insurance claims to answer key business questions:

1. **What patterns exist in our claims data?** - Exploratory data analysis to understand distributions, claim types, and baseline metrics
2. **Does digital filing improve operational metrics?** - Hypothesis testing comparing digital vs. phone filing across multiple outcomes
3. **Should we roll out the new claims portal?** - A/B test evaluation with treatment vs. control groups
4. **What drives customer satisfaction?** - Multiple regression analysis identifying key satisfaction drivers and their relative impact

## Key Findings

- **Digital filing** improves response time by 37%, settlement time by ~2 days, and satisfaction by 0.3-0.6 points
- **New portal A/B test** shows +0.53 point satisfaction increase (95% CI: 0.39-0.67), supporting full rollout
- **Response time** is the strongest satisfaction driver (~0.52 points per standard deviation)
- **Adjuster experience** and **settlement speed** are also major satisfaction factors

## Files

```
project/
├── analysis.ipynb              # Main analysis notebook with all code and findings
├── executive_summary.md        # Non-technical summary for business stakeholders
├── claims_data.csv            # Dataset (1,243 claims, 12 variables)
├── generate_portfolio_data.py # Data generation script
└── README.md                  # This file
```

## Technologies Used

- **Python 3.12**
- **pandas** - Data manipulation and analysis
- **DuckDB** - SQL queries for aggregation
- **matplotlib & seaborn** - Data visualization
- **scipy** - Statistical tests (t-tests, Mann-Whitney U)
- **pingouin** - Additional statistical analysis
- **statsmodels** - Regression modeling and diagnostics
- **Jupyter Notebook** - Interactive analysis environment

## Dataset

The dataset contains 1,243 insurance claims with the following variables:

| Variable | Description |
|----------|-------------|
| `claim_id` | Unique identifier |
| `claim_type` | Auto, Home, or Renters |
| `claim_amount` | Total payout in dollars |
| `customer_age` | Policyholder age |
| `customer_tenure_years` | Years as customer |
| `claim_complexity` | Simple, Moderate, or Complex |
| `adjuster_experience` | Years of adjuster experience |
| `digital_filing` | True = filed online, False = filed by phone |
| `response_time_hours` | Hours until first adjuster contact |
| `settlement_days` | Days from filing to resolution |
| `satisfaction_score` | Customer rating (1-10 scale) |
| `new_portal` | True = used new portal (test group), False = control |

**Data characteristics:**
- 1,243 observations
- 12 variables (mix of numeric, boolean, and categorical)
- No missing values
- Right-skewed claim amounts (expected for insurance data)

## Methodology

### 1. Exploratory Data Analysis
- Distribution analysis with histograms and box plots
- Summary statistics for all numeric variables
- Breakdown by categorical variables (claim type, complexity, filing method)
- Correlation analysis via heatmap

### 2. Hypothesis Testing (Digital Filing Impact)
- **Satisfaction score:** Welch's t-test (normal distribution, large samples)
- **Settlement days:** Welch's t-test (normal distribution, large samples)
- **Response time:** Mann-Whitney U test (right-skewed distribution)
- Calculated effect sizes (Cohen's d, rank-biserial correlation)
- Reported 95% confidence intervals for all estimates

### 3. A/B Test Evaluation (New Portal)
- Compared treatment (n=605) vs. control (n=638) groups
- Primary test: Welch's t-test
- Validation: Mann-Whitney U test as secondary check
- Calculated absolute and relative lift
- Assessed practical significance alongside statistical significance

### 4. Regression Analysis (Satisfaction Drivers)
- **Model 1:** Full model with all predictors to identify direct effects
- **Model 2:** Reduced model to capture total effect of digital filing (removing mediators)
- Validated assumptions:
  - Checked for multicollinearity (VIF < 2 for all predictors)
  - Residual plot (homoscedasticity check)
  - Q-Q plot (normality of residuals)
- Standardized effects to compare variable importance
- Generated predictions for hypothetical claims

## Key Statistical Results

### Digital Filing Impact

| Metric | Digital | Phone | Difference | p-value | Effect Size |
|--------|---------|-------|------------|---------|-------------|
| Response time (median, hours) | Lower | Higher | -0.865 hrs (-37%) | <0.0001 | RBC = -0.36 |
| Settlement days (mean) | Lower | Higher | -2.20 days | <0.0001 | Cohen's d = 0.57 |
| Satisfaction (mean) | 7.90 | 7.42 | +0.48 points | <0.0001 | Cohen's d = 0.38 |

### A/B Test Results

- **Control group:** Mean satisfaction = 7.17 (95% CI: 7.07-7.27)
- **Treatment group:** Mean satisfaction = 7.69 (95% CI: 7.60-7.79)
- **Absolute lift:** +0.53 points (95% CI: 0.39-0.67)
- **Relative lift:** +7.34%
- **Recommendation:** Roll out new portal

### Regression Model Performance

- **R² = 0.58** (model explains 58% of satisfaction variance)
- All predictors statistically significant (p < 0.05)
- No multicollinearity concerns (VIF < 2)
- Residuals approximately normal with constant variance

**Top satisfaction drivers (by standardized effect):**
1. Response time hours: -0.52
2. Adjuster experience: +0.51
3. Settlement days: -0.44
4. New portal: +0.24

## Installation & Usage

### Prerequisites

- Python 3.12+
- Jupyter Notebook or JupyterLab

### Setup

1. Clone this repository
2. Install required packages:

```bash
pip install pandas duckdb matplotlib seaborn scipy pingouin statsmodels jupyter
```

3. Launch Jupyter:

```bash
jupyter notebook analysis.ipynb
```

4. Run all cells to reproduce the analysis

### Alternative: Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install packages
pip install pandas duckdb matplotlib seaborn scipy pingouin statsmodels jupyter

# Launch notebook
jupyter notebook analysis.ipynb
```

## Project Structure

The analysis follows a clear progression:

1. **Data Loading & Exploration** - Understanding the dataset
2. **Question 1: Understanding Our Data** - Comprehensive EDA
3. **Question 2: Digital Filing Impact** - Hypothesis testing on three metrics
4. **Question 3: New Portal Evaluation** - A/B test analysis
5. **Question 4: Satisfaction Drivers** - Multiple regression modeling

Each section includes:
- Clear business question
- Appropriate statistical methods
- Visualizations
- Interpretation of results
- Business recommendations

## Skills Demonstrated

- **Exploratory Data Analysis:** Distribution analysis, summary statistics, visualization
- **Statistical Testing:** t-tests, Mann-Whitney U, effect sizes, confidence intervals
- **A/B Testing:** Experimental design evaluation, treatment effect estimation
- **Regression Modeling:** Multiple regression, assumption checking, variable selection
- **Data Visualization:** matplotlib, seaborn, appropriate chart selection
- **SQL:** DuckDB for data aggregation
- **Business Communication:** Translating technical findings to actionable recommendations
- **Reproducible Research:** Clean, documented, executable notebook

## Recommendations Summary

Based on the analysis, the top priorities are:

1. **Roll out the new portal** - Clear positive impact on satisfaction
2. **Reduce response time** - Largest satisfaction driver
3. **Reduce settlement days** - Second-highest operational priority
4. **Promote digital filing** - Improves all operational metrics
5. **Invest in adjuster experience** - Training and retention programs

Full details in [executive_summary.md](executive_summary.md).

## Future Work

Potential extensions to this analysis:

- **Predictive modeling:** Build a model to predict satisfaction scores for new claims
- **Segmentation analysis:** Identify customer segments with different satisfaction drivers
- **Time series analysis:** Track metrics over time to measure improvement
- **Cost-benefit analysis:** Quantify ROI of recommended interventions
- **Causal inference:** Use propensity score matching or other methods to strengthen causal claims

## License

This is a portfolio project for educational and demonstration purposes.

## Contact

**Jean Salazar**  
[jeansalazar135@gmail.com](mailto:jeansalazar135@gmail.com)

---

*This project was completed as part of a data analysis portfolio to demonstrate end-to-end analytical skills for job applications.*
