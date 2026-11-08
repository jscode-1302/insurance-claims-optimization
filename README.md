# Insurance Claims Analysis

End-to-end statistical analysis of 1,243 insurance claims to identify opportunities for improving operational efficiency and customer satisfaction.

> **Note:** The dataset is synthetic. I generated it with [`generate_portfolio_data.py`](generate_portfolio_data.py) to mimic realistic claims patterns, so I could practice the full analysis workflow end to end.

## What I Did

Analyzed insurance claims data to answer four business questions:

1. What patterns exist in the data?
2. Does digital filing improve operational metrics?
3. Should we roll out the new claims portal?
4. What drives customer satisfaction?

## Key Findings

### Digital Filing Delivers Better Outcomes

![Digital filing impact on key metrics](images/digital_filing_impact.png)

Digital filers get a **37%** faster response, settlement **~2 days** sooner, and satisfaction **0.3-0.6 points** higher than phone filers. Since customers choose how they file, this is an association, not a proven cause.

### New Portal A/B Test: Clear Win

![A/B test results](images/ab_test_results.png)

The new portal increased satisfaction by **+0.53 points** (95% CI: 0.39-0.67), a **7.3% improvement**. This supports full rollout.

### Adjuster Experience and Response Time Drive Satisfaction

![Satisfaction drivers analysis](images/satisfaction_drivers.png)

Adjuster experience and response time have the largest impact on satisfaction (nearly tied), followed by settlement speed.

## Files

```
├── analysis.ipynb           # Main analysis with all code and findings
├── executive_summary.md     # Non-technical summary for stakeholders
├── claims_data.csv         # Dataset (1,243 claims)
├── generate_portfolio_data.py  # Script that generates the synthetic dataset
├── requirements.txt        # Python dependencies
├── images/                 # Visualizations
└── README.md               # This file
```

## Tech Stack

- **Python:** pandas, scipy, statsmodels, pingouin
- **SQL:** DuckDB for aggregations
- **Visualization:** matplotlib, seaborn
- **Analysis:** Jupyter Notebook

## Methodology

### 1. Exploratory Data Analysis

![Correlation heatmap](images/correlation_heatmap.png)

Distribution analysis, summary stats, and correlation heatmap to identify relationships between variables.

### 2. Hypothesis Testing

- Welch's t-tests (two-sided) for satisfaction and settlement days
- Mann-Whitney U test for response time (right-skewed data)
- Calculated effect sizes and 95% confidence intervals

### 3. A/B Test Evaluation

Compared treatment (n=605) vs. control (n=638) groups using a two-sided Welch's t-test with secondary Mann-Whitney validation.

### 4. Regression Analysis

Built two models:
- **Model 1:** Full model to identify direct effects (controlling for claim complexity)
- **Model 2:** Reduced model to capture total effect of digital filing

Validated assumptions with VIF checks, residual plots, and Q-Q plots.

## Results Summary

**Digital Filing Impact:**

| Metric | Digital | Phone | Difference | Effect Size |
|--------|---------|-------|------------|-------------|
| Response time (median) | Lower | Higher | -37% | RBC = -0.36 |
| Settlement days | Lower | Higher | -2.20 days | Cohen's d = 0.57 |
| Satisfaction | 7.90 | 7.42 | +0.48 points | Cohen's d = 0.38 |

**A/B Test:**
- Control: 7.17 (95% CI: 7.07-7.27)
- Treatment: 7.69 (95% CI: 7.60-7.79)
- Lift: +0.53 points (+7.3%)

**Regression Model:**
- R² = 0.60 (explains 60% of satisfaction variance)
- Top drivers (per standard deviation): adjuster experience (+0.54), response time (-0.50), settlement days (-0.29)

## Recommendations

1. **Roll out the new portal** - Clear positive impact
2. **Reduce response time** - Biggest operational lever
3. **Invest in adjuster experience** - Largest driver; training and retention
4. **Reduce settlement days** - Next priority
5. **Promote digital filing** - Associated with better results on all metrics

Full details: [executive_summary.md](executive_summary.md)

## How to Run

```bash
# Clone repo
git clone https://github.com/jscode-1302/insurance-claims-optimization.git
cd insurance-claims-optimization

# Install dependencies
pip install -r requirements.txt

# Run notebook
jupyter notebook analysis.ipynb
```

## Skills Demonstrated

- Exploratory data analysis
- Hypothesis testing (t-tests, Mann-Whitney U)
- A/B testing and experiment evaluation
- Multiple regression modeling
- Statistical assumption validation
- Data visualization
- SQL for data aggregation
- Business communication

---

**Portfolio project demonstrating end-to-end data analysis skills.**

**Contact:** [jeansalazar135@gmail.com](mailto:jeansalazar135@gmail.com)
