CAPS: Characterization, Analysis, Prediction, and Suggestion of The Opioid Crisis
====================================================================================

Drug abuse negatively impacts the society and infiltrates into every corner of the society, due to
its high tendency to spread and strong addiction. The five states of Ohio, Kentucky, West Virginia,
and Pennsylvania are currently confronted with the opioid crisis (which is a kind of drug crisis) and
hope to constrain the epidemic. Therefore, we conduct an insightful study of the drug crisis in five
states and formulate a concrete strategy to counter the problem.


We propose a framework named CAPS to characterize the crisis, analyze the spread, predict the
future situation, and suggest the governors. First, we use the Collaborative Filter to characterize
each countys drug use preference and each drugs features by a three-dimensional vector, with each
couple of vectors determining a corresponding drug use situation. Then we use the Gradient descent
to obtain the numerical solution and cluster the 69 types of the drug into 3 categories. Second,
considering cars as the carrier of drugs, we build a geography-based Complex Network to further
characterize the crisis by its tendency of spread. We identify the sources and the threshold level of
spread, based on the idea of reciprocal influence of a county and its neighbors. After identifying the
spread pattern, we predict the future drug use situation based on the NFLIS data.


Moreover, we fill and filter the linearly dependent socio-economic data, using the Pearson Correlation
Coefficient. After data processing, we use the processed 25-column data to construct the
Decision Tree. Specifically, we use the Information Entropy and the Information Gain to select the
best feature for each node of it. The tree extracts the most influential factors, which facilitates further
analysis of their mechanism. Finally, we formulate a detailed strategy targeted on the top five influential
factors (immigrants, English proficiency, state, and family) to counter the problem, including
drug flow control, interstate cooperation, and social support. We set both short-term and long-term
goals accordingly. The test of our strategy gives us the satisfying result of an average 1.1% yearly
improvement for 1% modification of the factors.


In addition we carry out the sensitivity, stability, and reliability analyses, discuss the strengths
and weaknesses of our models and present a memo to the Chief Administrator and the DEA/NFLIS
Database.


Keywords: data mining, collaborative filter, complex network, decision tree, opioid spread
