# MassieVFX Toolkit Installation Guide

## Overview

The MassieVFX Toolkit is a collection of tools designed to enhance your workflow in Foundry Nuke. This guide will walk you through the installation process.

## Installation Steps

1. **Download the Toolkit:** 
   - Obtain the MassieVFX Toolkit folder.

2. **Move the Toolkit:**
   - Drag and drop the MassieVFXToolkit folder into your `.nuke` folder.

3. **Update `init.py`:**
   - Open your `.nuke` folder.
   - Locate or create the `init.py` file.
   - Add the following line to `init.py`:
     ```python
     nuke.pluginAddPath('MassieVFX-NukeToolkit')
     ```
   - Save the `init.py` file.

   **Note:** If there is no `init.py` file or if it doesn't contain the line `nuke.pluginAddPath('MassieVFX-NukeToolkit')`, Nuke won't detect the MassieVFX directories.

## Final Steps

After completing the above steps, restart Nuke for the changes to take effect.

## Version Information

MassieVFX Toolkit for Foundry Nuke v0.1a - January 2024
