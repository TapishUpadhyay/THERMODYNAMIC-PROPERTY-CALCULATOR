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

## Target Users
The primary target users of this project are:
- **Students** studying physical chemistry or chemical thermodynamics at the undergraduate level.
- **Teachers and educators** who need a quick, clear demonstration of Hess's Law and Gibbs energy.
- **Researchers** and chemistry enthusiasts who require rapid thermodynamic screening of reactions.

## High-Level Features
The Thermodynamic Properties Calculator includes the following key features:
1. **User-Friendly Interface:** A numbered main menu with clear navigation for all operations.
2. **Molecule Database:** A built-in thermodynamic database of 26 diatomic and polyatomic
   molecules with ΔHf°, ΔGf°, and S° values sourced from standard references (NIST WebBook).
3. **Preset Reaction Library:** Six common reactions (combustion, synthesis, decomposition)
   available for instant calculation without manual input.
4. **Custom Reaction Input:** Users can define any reaction using formula:stoichiometry notation
   (e.g., CH4:1 O2:2 → CO2:1 H2O:2) for flexible analysis.
5. **Thermodynamic Computation Engine:** Applies Hess's Law to compute ΔH°, ΔS°, and ΔG°;
   also evaluates ΔG at any temperature using ΔG = ΔH − TΔS.
6. **Spontaneity & Enthalpy Prediction:** Automatically classifies each reaction as
   exothermic/endothermic and spontaneous/non-spontaneous based on computed values.
7. **Visualization:** Generates a dual-panel Matplotlib figure — a bar chart of ΔH, ΔG, ΔS
   and a ΔG vs Temperature curve with spontaneity regions highlighted.
8. **Export and Save Options:** All plots can be saved as high-resolution PNG files for
   assignments, reports, or presentations.
9. **Batch Mode:** Calculates and plots thermodynamic data for all preset reactions in one run.
10. **Educational Aid:** Helps users understand reaction feasibility, temperature dependence of
    spontaneity, and the interplay between enthalpy and entropy through visual output.
