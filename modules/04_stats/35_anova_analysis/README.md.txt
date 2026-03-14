# Lesson 35: ANOVA - Analysis of Variance

### 📗 Beyond the T-Test
ANOVA compares the means of three or more groups by analyzing the ratio of variance *between* groups to the variance *within* groups (The **F-statistic**).

- **Null Hypothesis ($H_0$):** All group means are equal ($\mu_1 = \mu_2 = \mu_3$).
- **Alternative Hypothesis ($H_a$):** At least one group mean is different.

### 📝 The F-Distribution Decision
We use the F-distribution to find our p-value. If the variance between groups is significantly larger than the internal noise of the groups, we reject the null.

---

### 💻 Computational Approach: The Unified Dashboard
Our unified script performs two distinct, yet perfectly mirrored, visual tasks:
1. **2D Perspective:** A combination of "Box Plot" and "Swarm Plot" to visualize raw data points and distribution differences simultaneously.
2. **3D Perspective:** A spatial probability density landscape of the F-distribution, where the rejection "plateau" and the observed F-statistic are clearly marked.

### 📊 Visual Evidence

#### I. 2D Multi-Group Comparison
Note how the raw data points (dots) cluster. ANOVA calculates if the "gap" between their centers (box medians) is significant compared to their "spread."
![ANOVA 2D Comparison](../../../assets/35_anova_2d.png)

#### II. 3D F-Distribution Landscape
A spatial representation of the F-test. The steep "cliff" marks the rejection region, and the "flag" is where our test result stands.
![ANOVA 3D Landscape](../../../assets/35_anova_3d.png)

**Files:**
* `anova_master.py`: Unified engine for multi-group testing, dashboard, and asset generation.