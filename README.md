---
title: 'Project documentation template'
disqus: hackmd
---
Patchfork Hypothesis Testing
===

## Table of Contents

[TOC]

## Intro
This jupyter notebook shows the process of the music review hypothesis analysis, including creating the data frame, addressing the question for analyzing, stating the null hypothesis and alternative hypothesis for each question, calculating the p value of each hypothesis, comparing each p value with the alpha threshold and addressing the conclusions.

Dependencies
---
for databases:
```gherkin=
import psycopg2
```
for data manipulation
```gherkin=
import numpy as np
import pandas as pd
```
for statistics
```gherkin=
from scipy import stats
```
for visualization
```gherkin=

import plotly.graph_objs as go
import plotly.plotly as py
import cufflinks
from plotly.offline import iplot
cufflinks.go_offline()
cufflinks.set_config_file(world_readable=True, theme='ggplot')
```
for functions
```gherkin=
from functions import *
```

Hypothesis 1: Is there a statistical difference between the ratings of two different music genres?
---


| $H_{0}$    | $H_{1}$     |
| ------------- |:-------------:|
| we state the null hypothesis as electronic music is same as the country music ($\mu1=\mu2$)   | we state the alternative hypothesis as electronic music is different from the country music ($\mu1\neq\mu2$) |


Hypothesis 2: Is there a statistical difference between the ratings of country music and all other music?
---


| $H_{0}$    | $H_{1}$     |
| ------------- |:-------------:|
| we state the null hypothesis as the country music is same as the other music ($\mu1=\mu2$)  | we state the alternative hypothesis as the country music is different from the other music ($\mu1\neq\mu2$) |


Hypothesis 3: Is there a statistical difference between the music labelled "touch and go" and all other music?
---


| $H_{0}$    | $H_{1}$     |
| ------------- |:-------------:|
| we state the null hypothesis as the music labelled "touch and go" is same as the other music ($\mu1=\mu2$) | we state the alternative hypothesis as the music labelled "touch and go" is different from the other music ($\mu1\neq\mu2$) |





## Results

:::info
Hypothesis 1: Based on the p value we've calculated(1.1083354234386888e-09) and the alpha value we'e set(0.05), we can reject the null hypothesis and accept the alternative hypothesis
:::

:::info
Hypothesis 2: Based on the p value we've calculated(1.7227856290435994e-05) and the alpha value we'e set(0.05), we can reject the null hypothesis and accept the alternative hypothesis
:::

:::info
Hypothesis 3: Based on the p value we've calculated(0.52698691073891) and the alpha value we'e set(0.05), we cannot reject the null hypothesis
:::

###### tags: `Documentation`

