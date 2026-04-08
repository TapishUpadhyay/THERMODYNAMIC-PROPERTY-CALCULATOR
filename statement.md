# Thermodynamic Properties Calculator

## Problem Statement
Understanding thermodynamic properties of chemical reactions is a fundamental part of chemistry
education, yet manually applying Hess's Law, computing Gibbs free energy changes, and predicting
spontaneity is tedious, error-prone, and difficult for beginners to visualize. Students and
researchers frequently struggle to connect raw thermodynamic data (ΔHf°, ΔGf°, S°) to
meaningful conclusions about reaction behavior. There is a need for an automated, interactive
tool that can instantly compute ΔH, ΔG, and ΔS for chemical reactions, predict their
spontaneity across temperature ranges, and display the results through clear, interpretable
visualizations — reducing manual calculation effort and deepening conceptual understanding.

## Scope of the Project
The Thermodynamic Properties Calculator aims to simplify the calculation and visualization of
thermodynamic quantities for educational and research purposes. The project covers:
- Computation of ΔH°_rxn, ΔS°_rxn, and ΔG°_rxn for diatomic and polyatomic molecule reactions.
- Temperature-dependent ΔG analysis using the relation ΔG = ΔH − TΔS.
- Automatic prediction of spontaneity and reaction type (exothermic/endothermic).
- A curated database of standard thermodynamic data for 26 common molecules.
- Support for preset reactions as well as custom user-defined reactions.
- Visual output including bar charts of property values and ΔG vs Temperature plots.
- Exporting and saving diagrams as PNG files for study and presentations.



## Features
The Thermodynamic Properties Calculator includes the following key features:
1. **User-Friendly Interface:** 
2. **Molecule Database:**
3. **Preset Reaction Library:** 
4. **Custom Reaction Input:** 
5. **Thermodynamic Computation Engine:** Applies Hess's Law to compute ΔH°, ΔS°, and ΔG°;
   also evaluates ΔG at any temperature using ΔG = ΔH − TΔS.
6. **Spontaneity & Enthalpy Prediction:** Automatically classifies each reaction as
   exothermic/endothermic and spontaneous/non-spontaneous based on computed values.
7. **Visualization:** Generates a dual-panel Matplotlib figure — a bar chart of ΔH, ΔG, ΔS
   and a ΔG vs Temperature curve with spontaneity regions highlighted.
