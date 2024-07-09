# CREATE KIM MIN JAE'S PASS and HEAT MAP IN THE BAYER LEVERKUSEN MATCH


**This project is a pass and heat map of a soccer player in a match. The statsbombpy package in Python and the mplsoccer library were used for this project. 
Specific variables were selected and worked on this dataset.**

---
## Start
 Python libraries are imported because the required methods will not work without them.

```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mplsoccer import Pitch, Sbopen, VerticalPitch
from statsbombpy import sb
```
---

---
## Choose Matches
Since there is a lot of match information, the relevant season and league ID is selected. (Bayern Munih-Bayer Leverkusen match id is 9 and 2023-2024 season id is 281.)

```python
df_match = parser.match(competition_id = 9, season_id = 281)
```

---

---
## Create Pitch
Football field graphic is created using the mplsoccer library.

```python
pitch = Pitch(pitch_color="grass",
              line_color="white",
              stripe=True)
fig, ax = pitch.draw(figsize=(16, 11),
                     constrained_layout=False,
                     tight_layout = True)
fig.set_facecolor("#FFFFFF")
```
---

---
## Create Heatmap
A heat map is created showing the football player's performance during the match.

```python
pitch.kdeplot(
    x=df_pass["x"],
    y=df_pass["y"],
    shade=True,
    shade_lowest=False,
    alpha=0.5,
    n_levels=10,
    cmap="plasma",
    ax=ax)
```
---




