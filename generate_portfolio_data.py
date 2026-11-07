"""
Generate comprehensive insurance claims dataset for portfolio project.
This creates realistic claims data with embedded patterns for analysis.
"""

import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(789)
n = 1243

print("Generating insurance claims dataset...")

# Generate claim IDs
claim_ids = [f'CLM-2024-{i:04d}' for i in range(1, n+1)]

# Generate claim types (60% auto, 30% home, 10% renters)
claim_types = np.random.choice(['Auto', 'Home', 'Renters'], n, p=[0.6, 0.3, 0.1])

# Generate customer characteristics
customer_ages = np.random.normal(45, 15, n).clip(22, 85).astype(int)
customer_tenure = np.random.gamma(3, 2, n).clip(0.5, 30).round(1)

# Generate claim characteristics
claim_complexity = np.random.choice(['Simple', 'Moderate', 'Complex'], n, p=[0.5, 0.35, 0.15])
complexity_numeric = pd.Series(claim_complexity).map({'Simple': 1, 'Moderate': 2, 'Complex': 3}).values

# Claim amounts (varies by type and complexity)
# Using lognormal distribution for more realistic claim amounts with heavy tail
claim_amounts = []
for claim_type, complexity in zip(claim_types, complexity_numeric):
    if claim_type == 'Auto':
        # Auto claims: median ~$3500, with long tail for severe accidents
        mu, sigma = 8.0, 0.9
    elif claim_type == 'Home':
        # Home claims: median ~$8000, wider variation
        mu, sigma = 8.8, 1.1
    else:  # Renters
        # Renters claims: median ~$2000, less variation
        mu, sigma = 7.5, 0.7

    # Complexity increases claim amount
    complexity_multiplier = 1 + (complexity - 1) * 0.3
    amount = np.random.lognormal(mu, sigma) * complexity_multiplier

    # Add realistic noise: adjustments, manual entries, partial payments
    noise_factor = np.random.uniform(0.85, 1.15)
    amount = amount * noise_factor

    # Sometimes add/subtract arbitrary amounts (adjustments, deductibles applied inconsistently)
    if np.random.random() < 0.3:
        adjustment = np.random.uniform(-500, 500)
        amount = max(100, amount + adjustment)

    claim_amounts.append(round(amount, 2))

# Adjuster experience (years)
adjuster_experience = np.random.gamma(3, 2, n).clip(0.5, 20).round(1)

# Digital filing (60% digital, 40% phone)
digital_filing = np.random.choice([True, False], n, p=[0.6, 0.4])

# New portal (experimental rollout - 50% of sample)
new_portal = np.random.choice([True, False], n, p=[0.5, 0.5])

# Response time (hours) - affected by digital filing and complexity
# Digital filing → faster response
# Higher complexity → slower response
response_time = []
for digital, complexity in zip(digital_filing, complexity_numeric):
    base_time = 1.5 if digital else 2.5
    time = np.random.gamma(2, base_time/2) * (0.8 + 0.2 * complexity)
    response_time.append(max(0.1, round(time, 2)))

# Settlement days - affected by complexity, digital filing, adjuster experience
# Digital filing → faster settlement (-2 days)
# More experience → faster settlement (-0.3 days per year)
# Higher complexity → slower settlement (+3 days per level)
settlement_days = []
for digital, complexity, exp in zip(digital_filing, complexity_numeric, adjuster_experience):
    base_days = 10
    complexity_effect = complexity * 3
    digital_effect = -2 if digital else 0
    exp_effect = -0.3 * exp
    days = base_days + complexity_effect + digital_effect + exp_effect + np.random.normal(0, 3)
    settlement_days.append(max(1, round(days, 1)))

# Satisfaction score (1-10) - affected by multiple factors
# Response time → -0.28 per hour (slower = less satisfied)
# Settlement days → -0.08 per day (longer = less satisfied)
# Adjuster experience → +0.15 per year (more experience = higher satisfaction)
# New portal → +0.5 points (portal improves satisfaction)
# Complexity → -0.3 per level (complex claims = lower satisfaction)
satisfaction_scores = []
for resp_time, settle_days, exp, portal, complexity in zip(
    response_time, settlement_days, adjuster_experience, new_portal, complexity_numeric):

    base_score = 8.0
    response_effect = -0.28 * resp_time
    settlement_effect = -0.08 * settle_days
    exp_effect = 0.15 * exp
    portal_effect = 0.5 if portal else 0
    complexity_effect = -0.3 * (complexity - 1)
    noise = np.random.normal(0, 0.8)

    score = base_score + response_effect + settlement_effect + exp_effect + portal_effect + complexity_effect + noise
    satisfaction_scores.append(round(max(1, min(10, score)), 1))

# Create DataFrame
df = pd.DataFrame({
    'claim_id': claim_ids,
    'claim_type': claim_types,
    'claim_amount': claim_amounts,
    'customer_age': customer_ages,
    'customer_tenure_years': customer_tenure,
    'claim_complexity': claim_complexity,
    'adjuster_experience': adjuster_experience,
    'digital_filing': digital_filing,
    'response_time_hours': response_time,
    'settlement_days': settlement_days,
    'satisfaction_score': satisfaction_scores,
    'new_portal': new_portal
})

# Save to CSV
output_path = 'claims_portfolio_data.csv'
df.to_csv(output_path, index=False)

print(f"\n✓ Dataset created: {len(df)} claims")
print(f"✓ Saved to: {output_path}")
print("\nDataset preview:")
print(df.head(10))
print("\nSummary statistics:")
print(df.describe())
print("\nClaim type distribution:")
print(df['claim_type'].value_counts())
print("\nClaim complexity distribution:")
print(df['claim_complexity'].value_counts())
print(f"\nDigital filing rate: {df['digital_filing'].mean():.1%}")
print(f"New portal rollout rate: {df['new_portal'].mean():.1%}")
print("\n✓ Dataset ready for analysis!")
