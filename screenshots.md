**SCREENSHOT 1: MAIN MENU**
──────────────────────────────────────────────────────────────────
           THERMODYNAMIC PROPERTIES CALCULATOR
──────────────────────────────────────────────────────────────────
  OPTIONS
  ─────────────────────────────────────────
  1. Calculate properties for a preset reaction
  2. Calculate properties for all preset reactions
  3. Enter a custom reaction
  4. View molecule data
  5. List all supported molecules
  6. Exit
  ─────────────────────────────────────────
  Enter your choice (1-6): _

**SCREENSHOT 2: LIST OF SUPPORTED MOLECULES**
──────────────────────────────────────────────────────────────────
                    SUPPORTED MOLECULES
──────────────────────────────────────────────────────────────────

  Diatomic:
    H2         Hydrogen                     ΔHf° =   0.0 kJ/mol
    O2         Oxygen                       ΔHf° =   0.0 kJ/mol
    N2         Nitrogen                     ΔHf° =   0.0 kJ/mol
    F2         Fluorine                     ΔHf° =   0.0 kJ/mol
    Cl2        Chlorine                     ΔHf° =   0.0 kJ/mol
    Br2        Bromine                      ΔHf° =   0.0 kJ/mol
    HF         Hydrogen Fluoride            ΔHf° = -271.1 kJ/mol
    HCl        Hydrogen Chloride            ΔHf° =  -92.3 kJ/mol
    HBr        Hydrogen Bromide             ΔHf° =  -36.3 kJ/mol
    NO         Nitric Oxide                 ΔHf° =  +90.3 kJ/mol
    CO         Carbon Monoxide              ΔHf° = -110.5 kJ/mol

  Polyatomic:
    H2O        Water                        ΔHf° = -285.8 kJ/mol
    H2O_g      Water (gas)                  ΔHf° = -241.8 kJ/mol
    CO2        Carbon Dioxide               ΔHf° = -393.5 kJ/mol
    NH3        Ammonia                      ΔHf° =  -46.1 kJ/mol
    SO2        Sulfur Dioxide               ΔHf° = -296.8 kJ/mol
    SO3        Sulfur Trioxide              ΔHf° = -395.7 kJ/mol
    NO2        Nitrogen Dioxide             ΔHf° =  +33.2 kJ/mol
    N2O4       Dinitrogen Tetroxide         ΔHf° =   +9.2 kJ/mol
    CH4        Methane                      ΔHf° =  -74.8 kJ/mol
    C2H6       Ethane                       ΔHf° =  -84.7 kJ/mol
    C2H4       Ethylene                     ΔHf° =  +52.3 kJ/mol
    C2H2       Acetylene                    ΔHf° = +226.7 kJ/mol
    C6H6       Benzene                      ΔHf° =  +49.0 kJ/mol
    CH3OH      Methanol                     ΔHf° = -238.7 kJ/mol
    C2H5OH     Ethanol                      ΔHf° = -277.7 kJ/mol

  Total Molecules Supported: 26
──────────────────────────────────────────────────────────────────

**SCREENSHOT 3: PRESET REACTION SELECTION**
──────────────────────────────────────────────────────────────────
  PRESET REACTIONS
  1. Combustion of Hydrogen
  2. Haber Process (Ammonia Synthesis)
  3. Combustion of Methane
  4. Combustion of Ethanol
  5. Formation of Sulfur Trioxide
  6. Decomposition of Dinitrogen Tetroxide

  Select reaction number: 3
  Valid selection → Running thermodynamic analysis...

**SCREENSHOT 4: THERMODYNAMIC RESULTS OUTPUT (COMBUSTION OF METHANE)**
──────────────────────────────────────────────────────────────────
  REACTION : Combustion of Methane
──────────────────────────────────────────────────────────────────
  ΔH°_rxn  = -890.30  kJ/mol
  ΔS°_rxn  = -242.80  J/mol·K
  ΔG°_rxn  = -817.90  kJ/mol  (from ΔGf° values)
  ΔG (T=298.15 K) = -817.87  kJ/mol  (from ΔG = ΔH − TΔS)

  Enthalpy  : Exothermic (ΔH < 0) — Heat Released
  Spontaneity: Spontaneous (ΔG < 0)
──────────────────────────────────────────────────────────────────

**SCREENSHOT 5: MOLECULE DATA VIEW**
──────────────────────────────────────────────────────────────────
  MOLECULE : Ammonia  (NH3)   [polyatomic]
──────────────────────────────────────────────────────────────────
  Phase              : g
  ΔHf° (kJ/mol)      : -46.10
  ΔGf° (kJ/mol)      : -16.50
  S°   (J/mol·K)     : 192.80
──────────────────────────────────────────────────────────────────

**SCREENSHOT 6: ALL REACTIONS BATCH LOG**
──────────────────────────────────────────────────────────────────
   GENERATING THERMODYNAMIC DATA FOR ALL PRESET REACTIONS
──────────────────────────────────────────────────────────────────

  REACTION : Combustion of Hydrogen
  ΔH° = -571.60 kJ/mol  |  ΔS° = -326.80 J/mol·K  |  ΔG° = -474.20 kJ/mol
  → Exothermic | Spontaneous

  REACTION : Haber Process (Ammonia Synthesis)
  ΔH° = -92.20 kJ/mol   |  ΔS° = -198.20 J/mol·K  |  ΔG° = -33.00 kJ/mol
  → Exothermic | Spontaneous

  REACTION : Combustion of Methane
  ΔH° = -890.30 kJ/mol  |  ΔS° = -242.80 J/mol·K  |  ΔG° = -817.90 kJ/mol
  → Exothermic | Spontaneous

  REACTION : Combustion of Ethanol
  ΔH° = -1366.70 kJ/mol |  ΔS° = -138.80 J/mol·K  |  ΔG° = -1325.40 kJ/mol
  → Exothermic | Spontaneous

  REACTION : Formation of Sulfur Trioxide
  ΔH° = -197.80 kJ/mol  |  ΔS° = -188.40 J/mol·K  |  ΔG° = -141.80 kJ/mol
  → Exothermic | Spontaneous

  REACTION : Decomposition of Dinitrogen Tetroxide
  ΔH° = +57.20 kJ/mol   |  ΔS° = +175.80 J/mol·K  |  ΔG° = +4.70 kJ/mol
  → Endothermic | Non-Spontaneous at 298 K

  [✔] All reactions processed.
──────────────────────────────────────────────────────────────────
