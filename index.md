---
layout: page
title: Home
nav_order: 1
description: A week-to-week description of the content covered in the course.
---

<link rel="stylesheet" href="css/index.css">

# Data Engineering
{: .mb-2 }
UC Berkeley, Spring 2021
{: .mb-0 .fs-6 .text-grey-dk-000 }

<div>

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
<div class="role">
  {% for staffer in instructors %}
  {{ staffer }}
  {% endfor %}

</div>

The schedule and dates listed below are tentative and may be subject to change. Check out the syllabus for course information.

</div>

<br>

| Week | Date | Lecture | Assignment |
| :--: | :--: | :--: | :--: |
| 1 | Tu 1/19 | 1. [Introduction & Data Science Lifecycle](https://drive.google.com/file/d/1YHhrSqMEV7LfRF5NVyaXcdcB58aJ01af/view?usp=sharing)| |
| | Th 1/21 | 2. [Logistics and Relational model & algebra](https://drive.google.com/file/d/1Czg4TDaerduUrDLbfOCnnv_8xyp_yeh6/view?usp=sharing) | |
| 2 | Tu 1/26 | 3. [Relational alg. contd. SQL intro](https://drive.google.com/file/d/1nojuIcgyd-npbLUp-65Mz0eW5PXPrgn_/view?usp=sharing) | |
|  | Th 1/28 | 4. [SQL intro, Views](https://drive.google.com/file/d/1IIewYULvLtaLxFAHwgdnwYLwZ29YAM11/view?usp=sharing) | |
| 3 | Tu 2/2 | 5.  [SQL subqueries and aggregation](https://drive.google.com/file/d/1qUHLUSmANCWrkdjAC45bNho1rXf1Kt_J/view?usp=sharing)| |
|  | Th 2/4 | 6. [More SQL: window functions, sampling, string manipulation](https://drive.google.com/file/d/1E1R8rmtNGVGXaLYwxk46EEvrMu6RHoMG/view?usp=sharing)| [Project 1](https://cs194.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/cal-data-eng/sp21&subPath=proj/proj1/) (due 2/19) |
| 4 | Tu 2/9 | 7. [SQL updates, DDL, referential integrity, constraints](https://drive.google.com/file/d/1jSe4xsLHDEpquAa7tWC9Z3joWnmyPDtQ/view?usp=sharing) | |
|  | Th 2/11 | 8. [Index selection and performance tuning](https://drive.google.com/file/d/1yNaI5k5qzynklUl6ddGeCCSaNaHaJFHF/view?usp=sharing) | |
| 5 | Tu 2/16 | 9. [Index selection and performance tuning (II)](https://drive.google.com/file/d/18WwVTzw7nQekUIcffr2d2x1iLFw1qAbc/view?usp=sharing) | |
|  | Th 2/18 | 10. [Index selection and performance tuning (III)](https://drive.google.com/file/d/1k3VU43F1o-Oz5xfzqKyh3fctEWyJJ9Os/view?usp=sharing); 11. [Three Data Models: Relations, Tensors and Dataframes](https://drive.google.com/file/d/1E0EW7vEVEi79thdH986ZHvmKGsp6tVym/view?usp=sharing) | [Multivitamin 1](https://www.gradescope.com/courses/234388/assignments/1009641/) (due 3/4) |
| 6 | Tu 2/23 | 11. Relations, Tensors and Dataframes, Cont.. | |
|  | Th 2/25 | 12. Data Preparation [Full notebook](https://github.com/cal-data-eng/sp21/tree/gh-pages/resources/assets/notebooks/11-data-prep-1/11-dataprep-full.ipynb) and [Slide-oriented notebook](https://github.com/cal-data-eng/sp21/tree/gh-pages/resources/assets/notebooks/11-data-prep-1/11-dataprep-slides.ipynb)  | [Project 2](https://cs194.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/cal-data-eng/sp21&subPath=proj/proj2/) (due 3/12) |
| 7 | Tu 3/2 | 12b. Data Preparation [Slide-oriented notebook](https://github.com/cal-data-eng/sp21/tree/gh-pages/resources/assets/notebooks/12-data-prep-2/12-dataprep2-slides.ipynb) | |
|  | Th 3/4 | 12b. Data Preparation, cont. | |
| 8 | Tu 3/9 | 13. Data Cleaning [Slide-oriented notebook](https://github.com/cal-data-eng/sp21/tree/gh-pages/resources/assets/notebooks/13-DataCleaning-slides.ipynb)| [Multivitamin 2](https://www.gradescope.com/courses/234388/assignments/1084373/) (due 3/17) |
|  | Th 3/11 |  Contd. | |
| 9 | Tu 3/16 | 14. [Normalization and ER](https://drive.google.com/file/d/1Gt1Aaaz-j3JdHaNjL82q7O_6a5aTBJRG/view?usp=sharing)   | |
|  | Th 3/18 | 15. [Semistructured Data](https://drive.google.com/file/d/1veUSZfWotpfZG9mnJac1pYDUcDjAjp36/view?usp=sharing) | [Multivitamin 3](https://www.gradescope.com/courses/234388/assignments/1097711/) (due 3/31) |
| | Tu 3/23 | **Spring Break** | |
| | Th 3/25 | **Spring Break** | |
| 10 | Tu 3/30 | 16. [Querying semistructured data](https://drive.google.com/file/d/1B4HbHjQag7iYp2aO32ecOlpXjHaaEJov/view?usp=sharing) | [Project 3](https://cs194.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/cal-data-eng/sp21&subPath=proj/proj3/) (due 4/15) |
|  | Th 4/1 | Contd.    | |
| 11 | Tu 4/6 | 17. [Spreadsheets](https://drive.google.com/file/d/1PzrqNVsYWdYZi5jPmnl-SdeXpbocQtnv/view?usp=sharing)  | |
|  | Th 4/8 | 18. [Graph data: Property graph models, triples/RDF](https://drive.google.com/file/d/1n4sVrOscesHiGJQ4VfppmwQExz4bmSKf/view?usp=sharing)   19. [BI: OLAP, summarization, and visualization](https://drive.google.com/file/d/1yZJ73e1R2IBpdW6OpkFxNHrst2YmvI_E/view?usp=sharing) | [Multivitamin 4](https://www.gradescope.com/courses/234388/assignments/1160303) (due 4/19) |
| 12 | Tu 4/13 | 20. [Transactions](https://drive.google.com/file/d/1yqCbOibXzcWTkrTFn6AG_FM1wqOBcCqc/view?usp=sharing)   | |
|  | Th 4/15 | 21. [Data Pipelines](https://drive.google.com/file/d/1pYEWweq1jp4tgSuJjsiO7jFKBh7PJ2Po/view?usp=sharing) | |
| 13 | Tu 4/20 | 22. [Approximation: sampling and sketching](https://github.com/cal-data-eng/sp21/tree/gh-pages/resources/assets/notebooks/22-ApproximationSamplingSketching-slides.ipynb)  | [Project 4](https://cs194.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/cal-data-eng/sp21&subPath=proj/proj4/) (due 5/4) |
|  | Th 4/22 | 23. [Storage: Column vs. row, Compression, Exchange formats](https://drive.google.com/file/d/11KfHo_AC5fGd21fpkXsv23eF1qwZTgNB/view?usp=sharing) | |
| 14 | Tu 4/27 | 24. [Parallelization: Map-Reduce, Spark, Parallel DBMS, Dask/Modin](https://drive.google.com/file/d/1P4g6Zz3SmAjFRCA8l6JnnGFg_CaUe8kf/view?usp=sharing) | [Multivitamin 5](https://www.gradescope.com/courses/234388/assignments/1209415) (due 5/3 at 10 AM) |
|  | Th 4/29 | 25. [Security and Privacy](https://drive.google.com/file/d/189k8fP5Cg05M3vCl9h7wL4UK8cD0FggH/view?usp=sharing). 26. [Reflections](https://drive.google.com/file/d/1CWS0YVfDWiMe7x7kP7stcskB-fBksvL6/view?usp=sharing) | [Project 5](https://docs.google.com/document/d/1VRShTbKBQxX0ayVic4HsejPi58cQxPLx8tlQm6_j6zU/edit?usp=sharing) (due 5/14) |
| 15 | Tu 5/4 | **RRR Week** | |
|  | Th 5/6 | **RRR Week** | |
