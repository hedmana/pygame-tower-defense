# Tower Defense Game – PyGame & PyQt6

## Overview
This repository contains a tower defense game developed 
in **PyGame** as a final project for a Python 
course at Aalto University.The game includes three 
main states: **Main Menu**, **Level Editor**, and 
**Game Window**.

### Main Menu
The starting screen lets players navigate between the 
level editor and the game.

![Main Menu](assets/main_menu.png)

### Level Editor
Design custom maps on a **12×8 grid** by toggling tiles 
between **road**, **grass**, **start**, and **finish**. 
Each map must include one start and one finish tile at 
the grid’s edge. Invalid maps revert to a default 
layout.

![Level Editor](assets/level_editor.png)

### Game Window
Defend your base by placing towers to stop enemies.   
Towers can be bought, placed, and sold. The player
 starts 
with **3 lives**—each enemy that reaches the base costs 
one life.  Towers can be bought, placed, and sold.
 Survive 
**5 waves** to win.

**Towers**
- **Basic:** Deals direct damage.  
- **Ice:** Freezes enemies briefly.  
- **Poison:** Deals damage over time.  

**Enemies**
- **Basic:** Affected by all towers.  
- **Stealth:** Immune to poison.  
- **Boss:** Immune to freezing; spawns a Basic and a 
Stealth enemy on death.

![Game Window](assets/game.png)

## How to Run (bash)
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install pygame

# Run the game
python3 src/main.py
```
