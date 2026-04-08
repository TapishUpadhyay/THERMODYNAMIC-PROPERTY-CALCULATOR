import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


class Molecule:
    """Represents a molecule with its thermodynamic data."""

    def __init__(self, name, formula, delta_hf, delta_gf, entropy, phase, mol_type):
        self.name       = name        # Full chemical name
        self.formula    = formula     # Chemical formula string
        self.delta_hf   = delta_hf   # Standard enthalpy of formation (kJ/mol)
        self.delta_gf   = delta_gf   # Standard Gibbs free energy of formation (kJ/mol)
        self.entropy    = entropy     # Standard molar entropy (J/mol·K)
        self.phase      = phase       # 'g', 'l', 'aq', 's'
        self.mol_type   = mol_type   # 'diatomic' or 'polyatomic'


class ReactionData:
    """Represents a chemical reaction and its computed thermodynamic results."""

    def __init__(self, reactants, products, delta_h, delta_g, delta_s):
        self.reactants = reactants   # List of (formula, stoichiometry) tuples
        self.products  = products    # List of (formula, stoichiometry) tuples
        self.delta_h   = delta_h    # ΔH_rxn in kJ/mol
        self.delta_g   = delta_g    # ΔG_rxn in kJ/mol
        self.delta_s   = delta_s    # ΔS_rxn in J/mol·K


class ThermodynamicCalculator:
    """Main class to calculate and visualize thermodynamic properties."""

    def __init__(self):
        # Database of molecules with standard thermodynamic data at 298 K
        # Sources: NIST WebBook / Standard Chemistry References
        self.molecule_db = {

            # ————— Diatomic Molecules —————
            'H2':  Molecule('Hydrogen',          'H2',  0.0,    0.0,    130.7,  'g', 'diatomic'),
            'O2':  Molecule('Oxygen',            'O2',  0.0,    0.0,    205.2,  'g', 'diatomic'),
            'N2':  Molecule('Nitrogen',          'N2',  0.0,    0.0,    191.6,  'g', 'diatomic'),
            'F2':  Molecule('Fluorine',          'F2',  0.0,    0.0,    202.8,  'g', 'diatomic'),
            'Cl2': Molecule('Chlorine',          'Cl2', 0.0,    0.0,    223.1,  'g', 'diatomic'),
            'Br2': Molecule('Bromine',           'Br2', 0.0,    0.0,    152.2,  'l', 'diatomic'),
            'HF':  Molecule('Hydrogen Fluoride', 'HF',  -271.1, -273.2, 173.8,  'g', 'diatomic'),
            'HCl': Molecule('Hydrogen Chloride', 'HCl', -92.3,  -95.3,  186.9,  'g', 'diatomic'),
            'HBr': Molecule('Hydrogen Bromide',  'HBr', -36.3,  -53.4,  198.7,  'g', 'diatomic'),
            'NO':  Molecule('Nitric Oxide',      'NO',  90.3,   86.6,   210.8,  'g', 'diatomic'),
            'CO':  Molecule('Carbon Monoxide',   'CO',  -110.5, -137.2, 197.7,  'g', 'diatomic'),

            # ————— Polyatomic Molecules —————
            'H2O':  Molecule('Water',              'H2O',  -285.8, -237.1, 69.9,   'l', 'polyatomic'),
            'H2O_g':Molecule('Water (gas)',         'H2O_g',-241.8, -228.6, 188.7,  'g', 'polyatomic'),
            'CO2':  Molecule('Carbon Dioxide',     'CO2',  -393.5, -394.4, 213.8,  'g', 'polyatomic'),
            'NH3':  Molecule('Ammonia',            'NH3',  -46.1,  -16.5,  192.8,  'g', 'polyatomic'),
            'SO2':  Molecule('Sulfur Dioxide',     'SO2',  -296.8, -300.2, 248.2,  'g', 'polyatomic'),
            'SO3':  Molecule('Sulfur Trioxide',    'SO3',  -395.7, -371.1, 256.8,  'g', 'polyatomic'),
            'NO2':  Molecule('Nitrogen Dioxide',   'NO2',  33.2,   51.3,   240.1,  'g', 'polyatomic'),
            'N2O4': Molecule('Dinitrogen Tetroxide','N2O4', 9.2,    97.9,   304.4,  'g', 'polyatomic'),
            'CH4':  Molecule('Methane',            'CH4',  -74.8,  -50.7,  186.3,  'g', 'polyatomic'),
            'C2H6': Molecule('Ethane',             'C2H6', -84.7,  -32.8,  229.6,  'g', 'polyatomic'),
            'C2H4': Molecule('Ethylene',           'C2H4', 52.3,   68.2,   219.6,  'g', 'polyatomic'),
            'C2H2': Molecule('Acetylene',          'C2H2', 226.7,  209.2,  200.9,  'g', 'polyatomic'),
            'C6H6': Molecule('Benzene',            'C6H6', 49.0,   124.5,  173.4,  'l', 'polyatomic'),
            'CH3OH':Molecule('Methanol',           'CH3OH',-238.7, -166.3, 126.8,  'l', 'polyatomic'),
            'C2H5OH':Molecule('Ethanol',           'C2H5OH',-277.7,-174.8, 160.7,  'l', 'polyatomic'),
        }

        # Preset reactions for batch generation and quick demo
        self.preset_reactions = [
            {
                'name':      'Combustion of Hydrogen',
                'reactants': [('H2', 2), ('O2', 1)],
                'products':  [('H2O', 2)],
            },
            {
                'name':      'Haber Process (Ammonia Synthesis)',
                'reactants': [('N2', 1), ('H2', 3)],
                'products':  [('NH3', 2)],
            },
            {
                'name':      'Combustion of Methane',
                'reactants': [('CH4', 1), ('O2', 2)],
                'products':  [('CO2', 1), ('H2O', 2)],
            },
            {
                'name':      'Combustion of Ethanol',
                'reactants': [('C2H5OH', 1), ('O2', 3)],
                'products':  [('CO2', 2), ('H2O', 3)],
            },
            {
                'name':      'Formation of Sulfur Trioxide',
                'reactants': [('SO2', 2), ('O2', 1)],
                'products':  [('SO3', 2)],
            },
            {
                'name':      'Decomposition of Dinitrogen Tetroxide',
                'reactants': [('N2O4', 1)],
                'products':  [('NO2', 2)],
            },
        ]

    # ===================================================================
    #  CORE THERMODYNAMIC CALCULATIONS
    # ===================================================================

    def calculate_delta_h(self, reactants, products):
        """Calculate ΔH_rxn = Σ(n × ΔHf° products) − Σ(n × ΔHf° reactants)."""
        h_products  = sum(n * self.molecule_db[f].delta_hf for f, n in products)
        h_reactants = sum(n * self.molecule_db[f].delta_hf for f, n in reactants)
        return round(h_products - h_reactants, 2)

    def calculate_delta_s(self, reactants, products):
        """Calculate ΔS_rxn = Σ(n × S° products) − Σ(n × S° reactants) in J/mol·K."""
        s_products  = sum(n * self.molecule_db[f].entropy for f, n in products)
        s_reactants = sum(n * self.molecule_db[f].entropy for f, n in reactants)
        return round(s_products - s_reactants, 2)

    def calculate_delta_g_hess(self, reactants, products):
        """Calculate ΔG_rxn = Σ(n × ΔGf° products) − Σ(n × ΔGf° reactants)."""
        g_products  = sum(n * self.molecule_db[f].delta_gf for f, n in products)
        g_reactants = sum(n * self.molecule_db[f].delta_gf for f, n in reactants)
        return round(g_products - g_reactants, 2)

    def calculate_delta_g_equation(self, delta_h, delta_s, T=298.15):
        """Calculate ΔG using ΔG = ΔH − TΔS at a given temperature T (K)."""
        # ΔS is in J/mol·K → convert to kJ/mol·K
        return round(delta_h - T * (delta_s / 1000), 2)

    def predict_spontaneity(self, delta_g):
        """Predict spontaneity from sign of ΔG."""
        if delta_g < 0:
            return "Spontaneous (ΔG < 0)"
        elif delta_g == 0:
            return "At Equilibrium (ΔG = 0)"
        else:
            return "Non-Spontaneous (ΔG > 0)"

    def predict_enthalpy_type(self, delta_h):
        """Predict whether reaction is exothermic or endothermic."""
        if delta_h < 0:
            return "Exothermic (ΔH < 0) — Heat Released"
        elif delta_h == 0:
            return "Thermoneutral (ΔH = 0)"
        else:
            return "Endothermic (ΔH > 0) — Heat Absorbed"

    def run_full_calculation(self, reactants, products, T=298.15):
        """Run complete thermodynamic analysis and return ReactionData."""
        delta_h = self.calculate_delta_h(reactants, products)
        delta_s = self.calculate_delta_s(reactants, products)
        delta_g = self.calculate_delta_g_hess(reactants, products)
        return ReactionData(reactants, products, delta_h, delta_g, delta_s)

    # ===================================================================
    #  PRINTING HELPERS
    # ===================================================================

    def format_reaction_string(self, reactants, products):
        """Return a human-readable reaction equation string."""
        def side(pairs):
            return ' + '.join(
                (f"{n}" if n > 1 else '') + f for f, n in pairs
            )
        return f"{side(reactants)}  →  {side(products)}"

    def print_results(self, reaction_name, rd, T=298.15):
        """Print a formatted thermodynamic result block."""
        print("\n" + "─" * 62)
        print(f"  REACTION : {reaction_name}")
        print("─" * 62)
        print(f"  ΔH°_rxn  = {rd.delta_h:+.2f}  kJ/mol")
        print(f"  ΔS°_rxn  = {rd.delta_s:+.2f}  J/mol·K")
        print(f"  ΔG°_rxn  = {rd.delta_g:+.2f}  kJ/mol  (from ΔGf° values)")
        dg_ts = self.calculate_delta_g_equation(rd.delta_h, rd.delta_s, T)
        print(f"  ΔG (T={T} K) = {dg_ts:+.2f}  kJ/mol  (from ΔG = ΔH − TΔS)")
        print(f"\n  Enthalpy  : {self.predict_enthalpy_type(rd.delta_h)}")
        print(f"  Spontaneity: {self.predict_spontaneity(rd.delta_g)}")
        print("─" * 62)

    # ===================================================================
    #  VISUALIZATION
    # ===================================================================

    def plot_thermodynamic_bar(self, reaction_name, rd, save_path=None):
        """Generate a bar chart of ΔH, ΔG, and ΔS for the reaction."""

        labels  = ['ΔH° (kJ/mol)', 'ΔG° (kJ/mol)', 'ΔS° (J/mol·K)']
        values  = [rd.delta_h, rd.delta_g, rd.delta_s]
        colors  = ['#e74c3c' if v >= 0 else '#2ecc71' for v in values]

        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        fig.suptitle(f'Thermodynamic Properties\n{reaction_name}', fontsize=14, fontweight='bold')

        # ── Left panel: bar chart ─────────────────────────────────────
        ax = axes[0]
        bars = ax.bar(labels, values, color=colors, width=0.4, edgecolor='black', linewidth=0.8)

        # Value labels on bars
        for bar, val in zip(bars, values):
            ypos = bar.get_height() + (max(abs(v) for v in values) * 0.02) if val >= 0 \
                   else bar.get_height() - (max(abs(v) for v in values) * 0.06)
            ax.text(bar.get_x() + bar.get_width() / 2, ypos,
                    f'{val:+.2f}', ha='center', va='bottom', fontsize=11, fontweight='bold')

        ax.axhline(0, color='black', linewidth=1.2)
        ax.set_ylabel('Value', fontsize=12)
        ax.set_title('Property Values at 298 K', fontsize=11)
        ax.tick_params(axis='x', labelsize=10)

        # Legend patches
        legend_handles = [
            mpatches.Patch(color='#e74c3c', label='Positive (endothermic / non-spont.)'),
            mpatches.Patch(color='#2ecc71', label='Negative (exothermic / spontaneous)')
        ]
        ax.legend(handles=legend_handles, labels=[h.get_label() for h in legend_handles], fontsize=9, loc='upper right')

        for spine in ['top', 'right']:
            ax.spines[spine].set_visible(False)

        # ── Right panel: ΔG vs Temperature ───────────────────────────
        ax2 = axes[1]
        temps = np.linspace(100, 1500, 300)
        dg_values = [self.calculate_delta_g_equation(rd.delta_h, rd.delta_s, t) for t in temps]

        ax2.plot(temps, dg_values, color='#3498db', linewidth=2.5, label='ΔG = ΔH − TΔS')
        ax2.axhline(0, color='black', linewidth=1.0, linestyle='--', alpha=0.5, label='ΔG = 0 (Equilibrium)')
        ax2.fill_between(temps, dg_values, 0,
                         where=[v < 0 for v in dg_values],
                         alpha=0.15, color='#2ecc71', label='Spontaneous Region (ΔG < 0)')
        ax2.fill_between(temps, dg_values, 0,
                         where=[v > 0 for v in dg_values],
                         alpha=0.15, color='#e74c3c', label='Non-Spontaneous (ΔG > 0)')

        ax2.axvline(298.15, color='gray', linewidth=1.2, linestyle=':', label='T = 298 K')
        ax2.set_xlabel('Temperature (K)', fontsize=12)
        ax2.set_ylabel('ΔG (kJ/mol)', fontsize=12)
        ax2.set_title('ΔG vs Temperature', fontsize=11)
        ax2.legend(fontsize=9)

        for spine in ['top', 'right']:
            ax2.spines[spine].set_visible(False)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"  Plot saved → {save_path}")

        plt.show()

    # ===================================================================
    #  MOLECULE INFO
    # ===================================================================

    def display_molecule_info(self, formula):
        """Display all stored thermodynamic data for a single molecule."""
        if formula not in self.molecule_db:
            print(f"  Molecule '{formula}' not found in database.")
            return

        m = self.molecule_db[formula]
        print("\n" + "─" * 62)
        print(f"  MOLECULE : {m.name}  ({m.formula})   [{m.mol_type}]")
        print("─" * 62)
        print(f"  Phase              : {m.phase}")
        print(f"  ΔHf° (kJ/mol)      : {m.delta_hf:+.2f}")
        print(f"  ΔGf° (kJ/mol)      : {m.delta_gf:+.2f}")
        print(f"  S°   (J/mol·K)     : {m.entropy:.2f}")
        print("─" * 62)


# =======================================================================
#  CLI ENTRY POINT
# =======================================================================

def main():
    """Interactive command-line interface."""

    print("=" * 62)
    print("       THERMODYNAMIC PROPERTIES CALCULATOR")
    print("=" * 62)

    calc = ThermodynamicCalculator()

    while True:
        print("\n  OPTIONS")
        print("  ─────────────────────────────────────────")
        print("  1. Calculate properties for a preset reaction")
        print("  2. Calculate properties for all preset reactions")
        print("  3. Enter a custom reaction")
        print("  4. View molecule data")
        print("  5. List all supported molecules")
        print("  6. Exit")
        print("  ─────────────────────────────────────────")

        choice = input("\n  Enter your choice (1-6): ").strip()

        # ── Option 1: Single preset reaction ─────────────────────────
        if choice == '1':
            print("\n  PRESET REACTIONS")
            for i, rxn in enumerate(calc.preset_reactions, 1):
                print(f"  {i}. {rxn['name']}")

            sel = input("\n  Select reaction number: ").strip()
            try:
                rxn = calc.preset_reactions[int(sel) - 1]
                rd = calc.run_full_calculation(rxn['reactants'], rxn['products'])
                calc.print_results(rxn['name'], rd)

                save = input("\n  Generate and save plot? (y/n): ").strip().lower()
                save_path = f"{rxn['name'].replace(' ', '_')}_thermo.png" if save == 'y' else None
                calc.plot_thermodynamic_bar(rxn['name'], rd, save_path)

            except (IndexError, ValueError):
                print("  Invalid selection.")

        # ── Option 2: All preset reactions ───────────────────────────
        elif choice == '2':
            print("\n" + "=" * 62)
            print("   GENERATING THERMODYNAMIC DATA FOR ALL PRESET REACTIONS")
            print("=" * 62)
            for rxn in calc.preset_reactions:
                rd = calc.run_full_calculation(rxn['reactants'], rxn['products'])
                calc.print_results(rxn['name'], rd)
                save_path = f"{rxn['name'].replace(' ', '_')}_thermo.png"
                calc.plot_thermodynamic_bar(rxn['name'], rd, save_path)
            print("\n  [✔] All reactions processed.")

        # ── Option 3: Custom reaction ─────────────────────────────────
        elif choice == '3':
            print("\n  CUSTOM REACTION")
            print("  Enter reactants and products as formula:stoichiometry pairs.")
            print("  Example: H2:2 O2:1  →  H2O:2")
            print("\n  Supported formulas:", ', '.join(sorted(calc.molecule_db.keys())))

            try:
                r_input = input("\n  Reactants (e.g. H2:2 O2:1): ").strip().split()
                p_input = input("  Products  (e.g. H2O:2):      ").strip().split()

                reactants = [(pair.split(':')[0], int(pair.split(':')[1])) for pair in r_input]
                products  = [(pair.split(':')[0], int(pair.split(':')[1])) for pair in p_input]

                # Validate formulas
                all_formulas = [f for f, _ in reactants + products]
                missing = [f for f in all_formulas if f not in calc.molecule_db]
                if missing:
                    print(f"  Unknown molecules: {missing}. Please use supported formulas.")
                else:
                    reaction_name = calc.format_reaction_string(reactants, products)
                    rd = calc.run_full_calculation(reactants, products)
                    calc.print_results(reaction_name, rd)

                    save = input("\n  Generate and save plot? (y/n): ").strip().lower()
                    save_path = "custom_reaction_thermo.png" if save == 'y' else None
                    calc.plot_thermodynamic_bar(reaction_name, rd, save_path)

            except Exception as e:
                print(f"  Input error: {e}. Please follow the format exactly.")

        # ── Option 4: View molecule data ─────────────────────────────
        elif choice == '4':
            formula = input("\n  Enter molecule formula (e.g. H2O, CO2, NH3): ").strip()
            calc.display_molecule_info(formula)

        # ── Option 5: List supported molecules ───────────────────────
        elif choice == '5':
            print("\n" + "─" * 62)
            print("           SUPPORTED MOLECULES")
            print("─" * 62)
            diatomic  = [(f, m) for f, m in calc.molecule_db.items() if m.mol_type == 'diatomic']
            polyatomic = [(f, m) for f, m in calc.molecule_db.items() if m.mol_type == 'polyatomic']

            print("\n  Diatomic:")
            for f, m in diatomic:
                print(f"    {f:<10} {m.name:<28} ΔHf° = {m.delta_hf:+.1f} kJ/mol")

            print("\n  Polyatomic:")
            for f, m in polyatomic:
                print(f"    {f:<10} {m.name:<28} ΔHf° = {m.delta_hf:+.1f} kJ/mol")

            print(f"\n  Total Molecules Supported: {len(calc.molecule_db)}")
            print("─" * 62)

        # ── Option 6: Exit ────────────────────────────────────────────
        elif choice == '6':
            print("\n  Thank you for using the Thermodynamic Properties Calculator!")
            break

        else:
            print("  Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
