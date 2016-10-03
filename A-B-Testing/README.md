# DAN-A/B-Testing
A/B Testing for Udacity's Data Analyst Nanodegree

**1. Exiperiment Design:**<br/>
*List which metrics you will use as invariant metrics and evaluation metrics here. (These should be the same metrics you chose in the "Choosing Invariant Metrics" and "Choosing Evaluation Metrics" quizzes.)*
<br/>
* Invariant Metrics: Number of cookies, Number of clicks, Click-through-probability<br/>
* Evaluation Metrics: Gross conversion, Retention, Net conversion<br/>
<br/>
*For each metric, explain both why you did or did not use it as an invariant metric and why you did or did not use it as an evaluation metric. Also, state what results you will look for in your evaluation metrics in order to launch the experiment.*
* Number of cookies: This is an invariant metric because users are independent of this as it happens before the experiment begins.
* Number of user-ids: Not a good invariant metric because the number of users enrolling in the free trial are dependent on the experiment. Since number of users can fluctuate among the Experimental and Control groups, this is not a good evaluation metric.
* Number of clicks: Just like Number of cookies, this is a good invariant metric as it happens before the user sees the experiment.
* Click-through-probability: Good invariant metric because the clicks happen before the user sees the experiment, and are thus independent from it.
* Gross Conversion: It is a good evaluation metric as it has direct dependency on the experiment and we can decide on the hypothesis that this would decrease the cost of enrollments that aren’t likely to become paying customers.
* Retention: Not a good invariant metric because the number of users who enroll in the free trial is dependent on the experiment. Good evaluation metric because it is directly dependent on the effect of the experiment. 
* Net Conversion: Again, dependency on the experiment makes it a bad invariant metric. It is a good evaluation metric because being dependent on the metric, it can help us hypothesise a positive financial outcome for the change.
<br/>
The experiment could be designed in a way that the **Gross Conversion** *will* have a decrease in practical significance and **Net Conversion** *will not* decrease in practical significance.
<br/>
<br/>
**Standard Deviation:**<br/>
*List the standard deviation of each of your evaluation metrics. (These should be the answers from the "Calculating standard deviation" quiz.)*<br/>

```
Gross conversion: 0.0202
Retention: 0.0549
Net conversion: 0.0156
```
*For each of your evaluation metrics, indicate whether you think the analytic estimate would be comparable to the the empirical variability, or whether you expect them to be different (in which case it might be worth doing an empirical estimate if there is time). Briefly give your reasoning in each case.*
<br/>
Since the unit of diversion (number of cookies) is in the denominator of both Gross Conversion and Net Conversion, we can use the analytic estimate of variance. For Retention, the unit of analysis and the unit of diversion are different and therefore the analytical an the empirical estimates are different.
<br/>
<br/>
**Sizing:**<br/>
*Number of Samples vs. Power:*<br/>
*Indicate whether you will use the Bonferroni correction during your analysis phase, and give the number of pageviews you will need to power you experiment appropriately. (These should be the answers from the "Calculating Number of Pageviews" quiz.)*
<br/>
No, I did not use Bonferroni correction in my calculations because of the metrics being highly correalted. I chose Gross Concersion and Net Conversion as my evaluation metric.<br/>
Using the <a href=http://www.evanmiller.org/ab-testing/sample-size.html>Evan's Awesome A/B Tools</a>, I came to the final conclusion that Net Conversion has the higher number of Samples that were needed, 27413 tio be precise. Now, for pageviews:
```
pageview/group = 27413/0.08 = 342662.5
Total pageview = 342662.5*2 = 685325
```
The total pageview has a factor of 2 because we need them for both control and experimental group.<br/>
*Duration vs. Exposure:*<br/>
*Indicate what fraction of traffic you would divert to this experiment and, given this, how many days you would need to run the experiment. (These should be the answers from the "Choosing Duration and Exposure" quiz.). Give your reasoning for the fraction you chose to divert. How risky do you think this experiment would be for Udacity?*<br/>
If I choose 70% of traffic to be directed towards the experiment, it would be 25 days long.((685325/(0.7*40000))=25). This wouldn't be risky as it does not affect existing customers that have paid. Now since it could have an impact on the new enrollments, it is advisable that we do not direct 100% of traffic to the experiment.<br/>
<br/>
**2. Experimental Analysis:** <br/>
*Sanity Checks:* <br/>
*For each of your invariant metrics, give the 95% confidence interval for the value you expect to observe, the actual observed value, and whether the metric passes your sanity check. (These should be the answers from the "Sanity Checks" quiz.)*
<br/>
Number of Cookies:
```
Observed value  = 344660/690203 = 0.5006
SE = sqrt(0.5*(1-0.5)*(1/345543+1/344660) = 0.0006018
Margin of error (m) = SE * 1.96 = 0.0011796
Confidence Interval =  [0.4988,0.5012]
Pass Sanity Check
```
Number of clicks on 'Start free trial':
```
Observed value  = 28378/56703 = 0.50046
SE = sqrt(0.5*(1-0.5)*(1/28378+1/28325) = 0.0021
Margin of error (m) = SE * 1.96 = 0.0041
Confidence Interval =  [0.4959,0.5041]
Pass Sanity Check
```
<br/>
**Effect Size Tests:**<br/>
*For each of your evaluation metrics, give a 95% confidence interval around the difference between the experiment and control groups. Indicate whether each metric is statistically and practically significant. (These should be the answers from the "Effect Size Tests" quiz.)*
<br/>
Gross Conversion:
```
Confidence Interval =  [-.0291, -.0120]
1. Statistically significant 
2. Practically significant 
```
Net Conversion:
```
Confidence Interval =  [-0.0116, 0.0018]
1. Not statistically significant
2. Not practically significant
```
**Sign Tests:**<br/>
*For each of your evaluation metrics, do a sign test using the day-by-day data, and report the p-value of the sign test and whether the result is statistically significant. (These should be the answers from the "Sign Tests" quiz.)*<br/>
Below are the results:
```
p-value for Gross Conversion = .0026
p-value for Net Conversion = .6776
alpha = 0.05/2 = 0.025
Gross Conversion : Statistically significant
Net Conversion : Statistically insignificant
```
<br/>
**Summary:**<br/>
*State whether you used the Bonferroni correction, and explain why or why not. If there are any discrepancies between the effect size hypothesis tests and the sign tests, describe the discrepancy and why you think it arose.*<br/>
Three invariant metrics were chosen for purposes of validation and sanity checking while Gross Conversion and Net Conversion were used as evaluation metrics. The null hypothesis is that there is no difference in the evaluation metrics between the groups. Because our acceptance criteria requires statiscally signifcant differences for all evaluation metrics, the use of the Bonferonni correction is not appropriate. The Bonferonni correction is a method for controlling for type I errors (false positives) when using multiple metrics in which relevance of any of the metrics matches the hypothesis. In this case the risk of type I errors increases as the number of metrics increases (signifcance by random chance). In our case in which all metrics must be relevant to launch, the risk of type II errors (false negatives) increases as the number of metrics increases and thus it is not consistent with our criteria.
<br/>
**Recommendation:**<br/>
*Make a recommendation and briefly describe your reasoning.*
<br/>
Gross conversion turned out to be practically significant and is in sync with our hypothesis. This is a good outcome because we lower our costs by discouraging trial signups that are unlikely to convert. Net conversion was statistically and practically insignificant and the confidence interval also includes negative numbers.This is reasonable with the fact that we are prone to risk of decrease in revenue by introducing the trial screener.
This is why we **cannot launch** the experiment because we risk a decline in revenue by the introduction of the screen. 
<br/>
**Follow-Up Experiment:**<br/>
*Give a high-level description of the follow up experiment you would run, what your hypothesis would be, what metrics you would want to measure, what your unit of diversion would be, and your reasoning for these choices.*<br/>
Personal help and one-on-one converstaions usually always helps. I propose that we Udacity can add a personal touch to their students by providing a mentor/academic advisor when a user signs up for the free trial. This way the student feels that he/she is being valued and encouragement from the mentors can go a long way for helping a student subscribe!
In this case my NulL Hypothesis would be that provisioning a mentor new student signups will not increase Retention by a practically significant amount.
<br/>
New free trial signups will randomly be assigned to either a  Control or an Experiment group. The experience for users in the Control group will remain unchanged. Users in the Experiment group will be assigned a random mentor of the Udacity team who can provide personal feedback once the user starts a course.
<br/>
The unit of diversion will be the user-id, as this will only impact when a free trial is created.<br/>
The invariant metric will be the Number of user-ids, because the users sign up for the free trial before they are assigned a point of contact and are exposed to the new feeback system.<br/>
The evaluation metric will be Retention, which can result in an increase in revenue if proven to be practically significant.<br/>
**Resources:**
* Introduction to A/B Testing (Udacity)
* Evan Miller


