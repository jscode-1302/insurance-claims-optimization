# Insurance Claims Analysis: Executive Summary

> **Portfolio Project Note:** This is a portfolio project demonstrating end-to-end analysis skills. The company and scenario are fictional, and the dataset is synthetic (generated with `generate_portfolio_data.py`) to mimic realistic claims patterns.

**Prepared for:** VP of Claims Operations  
**Date:** November 7, 2026  
**Analyst:** Jean Salazar

---

## Overview

This analysis examines 1,243 insurance claims to identify opportunities for improving operational efficiency and customer satisfaction. The data reveals clear patterns showing which operational factors drive customer satisfaction and where the company should focus improvement efforts.

---

## Key Findings

### 1. Digital Filing Delivers Better Outcomes

Customers who file claims digitally experience significantly better service across all metrics compared to phone filers:

- **37% faster initial response** (median of 0.9 hours faster)
- **2 days faster settlement** (1.8 to 2.6 days improvement)
- **Higher satisfaction scores** (0.3 to 0.6 points higher on our 10-point scale)

One caveat: customers choose how they file, so part of this gap may come from who chooses digital, not from digital filing itself.

Currently, 60% of claims are filed digitally. The remaining 40% who still call represent an opportunity to improve their experience.

### 2. New Portal Test Was Successful

The new digital claims portal we tested with half our customers delivered a clear win:

- **Treatment group satisfaction:** 7.69 out of 10
- **Control group satisfaction:** 7.17 out of 10
- **Improvement:** +0.53 points (7% increase)

We can be 95% confident the true improvement is between 0.39 and 0.67 points. This is a meaningful gain that should translate to better retention and fewer complaints.

### 3. Response Speed Matters Most

Our analysis identified the factors that most influence customer satisfaction. The top drivers are:

**Largest impact:**
1. **Adjuster experience** – Years of experience handling claims
2. **Response time** – How quickly an adjuster makes first contact
3. **Settlement speed** – Days from filing to resolution

**Moderate impact:**
4. **New portal** – Using the improved digital interface
5. **Digital filing** – Overall benefit through faster processing

Adjuster experience and response time are nearly tied at the top, and response time is the one we can change fastest. Each hour of delay costs us about 0.3 points on our satisfaction scale. For context, cutting average response time from 3 hours to 1 hour would improve satisfaction by roughly 0.6 points—more than any other single intervention.

---

## Recommendations

Based on the data, here's what we should prioritize:

### Immediate Actions (High Impact)

**1. Roll out the new portal to all customers**

The test results are clear. The new portal improves satisfaction by about half a point with minimal downside risk. Before full rollout, confirm that implementation costs are justified by the 0.39 to 0.67 point gain we observed.

**2. Reduce initial response time**

This is our biggest operational lever for improving satisfaction. Focus on:
- Faster adjuster assignment
- Automated acknowledgment when claims are filed
- Clear communication about when customers will hear from us

Even small improvements here (15-30 minutes faster) will have measurable impact on satisfaction.

### Short-Term Improvements (Next Quarter)

**3. Accelerate settlement times**

After response time, this is the next biggest operational factor. Look for bottlenecks in our approval and payment processes. Reducing average settlement time by 2-3 days would improve satisfaction by about 0.15 to 0.2 points.

**4. Promote digital filing more aggressively**

Digital filers get faster service, which drives higher satisfaction. Consider:
- Making the digital option more prominent when customers contact us
- Simplifying the online filing process
- Following up with phone filers to encourage digital filing for future claims

### Long-Term Investments

**5. Invest in adjuster experience**

Experienced adjusters deliver better satisfaction. This means:
- **Retention:** Keep experienced adjusters from leaving
- **Training:** Accelerate skill development for newer adjusters
- **Assignment:** Route complex claims to more experienced adjusters

Each additional year of adjuster experience improves satisfaction by about 0.16 points. An adjuster with 10 years of experience will consistently deliver satisfaction scores about 1.5 points higher than a new adjuster, all else equal.

---

## Expected Impact

If we execute on the top three recommendations (new portal rollout, faster response times, faster settlements), we could realistically improve average satisfaction from 7.4 to somewhere between 8.0 and 8.5 within 6-12 months.

**What this means for the business:**
- Fewer complaints and escalations
- Better customer retention
- Improved reputation and referrals
- Competitive advantage in customer experience

---

## Data Quality & Methodology Notes

The analysis is based on 1,243 claims with complete data across 12 variables. All statistical tests were validated for appropriate use, and confidence intervals were calculated to quantify uncertainty.

The findings represent associations in our data. While we can't prove causation from this analysis alone, the patterns are strong and consistent across multiple tests. The new portal result comes from a properly randomized test, which gives us the highest confidence in that finding.

---

## Next Steps

1. **Decision on portal rollout** – Review costs and make go/no-go decision
2. **Response time initiative** – Identify specific process improvements to test
3. **Quarterly tracking** – Monitor these metrics to measure progress

I'm available to discuss these findings, dive deeper into any area, or help design the implementation of these recommendations.

---

**Questions or feedback?** Contact Jean Salazar