# Thermodynamic-Properties-Calculator

                          THERMODYNAMICS ↓
                               |
              Reactants        |        Products
           [H₂ + O₂ + ...]    |    [H₂O + CO₂ + ...]
                  \            |           /
                   \    ΔH°rxn = Σ(ΔHf° products)    /
                    \        − Σ(ΔHf° reactants)    /
                     \           |           /
                      \          |          /
                  ΔS°rxn      ΔG°rxn      TΔS
                   (entropy)  (Gibbs)   (T-correction)
                               |
              ← SPONTANEOUS  ΔG < 0  |  ΔG > 0  NON-SPONTANEOUS →

**A computational chemistry project for calculating ΔH, ΔG, ΔS,
predicting spontaneity, and visualizing thermodynamic behavior.**


## Project Overview

The **Thermodynamic Properties Calculator** is a computational chemistry project designed to
calculate and visualize standard thermodynamic properties of chemical reactions involving
both diatomic and polyatomic molecules. Using a curated database of standard enthalpies of
formation (ΔHf°), standard Gibbs free energies of formation (ΔGf°), and standard molar
entropies (S°), the program applies Hess's Law to compute reaction-level ΔH, ΔG, and ΔS
values at 298 K — and extends ΔG analysis across a temperature range using the
relationship ΔG = ΔH − TΔS.

The tool supports:

* Calculating thermodynamic properties for a **specific preset reaction**.
* Calculating thermodynamic properties for **all preset reactions**.
* Analyzing a **custom user-defined reaction** by entering formulas and stoichiometry.
* Inspecting **individual molecule data** from the thermodynamic database.

The system correctly handles both diatomic (H₂, N₂, CO, HCl, etc.) and
polyatomic (H₂O, NH₃, CH₄, C₂H₅OH, etc.) molecules, with clean Matplotlib
visualizations including bar charts and ΔG vs Temperature curves.

---

## Features

* Calculate standard thermodynamic properties for supported diatomic and polyatomic molecules
* Hess's Law-based computation of:

  * Standard Enthalpy Change (ΔH°_rxn) in kJ/mol
  * Standard Entropy Change (ΔS°_rxn) in J/mol·K
  * Standard Gibbs Free Energy Change (ΔG°_rxn) in kJ/mol
* ΔG at any temperature via ΔG = ΔH − TΔS
* Automatic classification of reactions as:

  * Exothermic / Endothermic (from ΔH)
  * Spontaneous / Non-Spontaneous / At Equilibrium (from ΔG)
* Preset reaction library (combustion, synthesis, decomposition)
* Custom reaction input via formula:stoichiometry notation
* Batch-generation mode for all preset reactions
* Matplotlib bar chart of ΔH, ΔG, ΔS per reaction
* ΔG vs Temperature plot with spontaneity regions highlighted
* User-friendly CLI with a numbered main menu

---

## Technologies / Tools Used

* Python 3.x
* Matplotlib
* NumPy
* Object-Oriented Programming
* Computational Chemistry Concepts (Hess's Law, Gibbs Free Energy, Entropy, MOT)

---

## Steps to Install and Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Thermodynamic-Properties-Calculator.git
cd Thermodynamic-Properties-Calculator
```

### 2. Install Dependencies

```bash
pip install matplotlib numpy
```

### 3. Run the Program

```bash
python main.py
```

### 4. Choose an Option Inside the Program

* Select a preset reaction (e.g., Combustion of Methane, Haber Process)
* OR enter a custom reaction using formula:stoichiometry pairs
* OR generate thermodynamic data for all preset reactions at once

---

## Instructions for Testing

1. Run the script using `python main.py`.
2. When prompted, choose any option from the main menu.
3. The program will:

   * Compute ΔH°, ΔS°, and ΔG° for the selected reaction
   * Predict spontaneity and classify enthalpy type
   * Display a bar chart of thermodynamic values
   * Plot ΔG vs Temperature from 100 K to 1500 K
   * Optionally save plots as PNG files
4. Ensure that:

   * Combustion of Hydrogen shows **ΔH < 0** (exothermic)
   * Haber Process shows **ΔG < 0** (spontaneous at 298 K)
   * Decomposition of N₂O₄ shows **ΔH > 0** (endothermic)
   * ΔG vs T plot correctly shows spontaneity crossover temperature
