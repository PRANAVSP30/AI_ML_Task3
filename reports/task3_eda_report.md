#  Task 3 – EDA Report (Netflix Dataset)
## By: Pranav S P

### 1. Objective

The goal of this task is to apply Exploratory Data Analysis (EDA) on the Netflix dataset to understand data         patterns, content types, ratings distribution, trends over years, outliers, and correlations.


### 2. Key Analyses Performed

- Dataset shape, structure, and null value inspection

- Countplots for:

    Content type (Movies vs TV Shows)

    Ratings distribution

- Created a numerical feature “title_length” for deeper analysis

- Histogram for title length distribution

- Boxplot for outlier detection

- Correlation heatmap (release_year vs title_length)


### 3. Key Insights

- Type Analysis

    Netflix has more Movies than TV Shows.
    - Movies dominate Netflix’s content library.

- Ratings Distribution

    TV-MA is the most common rating.
    - Netflix produces/publishes a lot of mature content.

- Title Length

    Most titles are between 5 and 20 characters.
    - Netflix titles are short and concise.

- Outliers

    Some titles are extremely long → visible in the boxplot.
    - These are uncommon and could be promotional content or documentaries.

- Correlation Analysis

    No strong correlation between title length and release year.
    - Title naming style does not depend on the year.


### 4. Conclusion

- The dataset shows strong patterns in content type and age rating.
- EDA reveals that Netflix focuses heavily on movie content and on TV-MA-rated shows.

This EDA helps in understanding trends, planning ML tasks (like genre classification or content recommendation), and identifying important variables for modeling.