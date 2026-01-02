# Kinetic Energy (CALCULATIONS) ⚛️

**Overview**

Small utility that computes the kinetic energy of a body using mass (kg) and velocity (m/s). The main script is `Kinetic_energy.py` and includes a reusable function and a simple CLI.

---

## Usage ▶️

Run from the `CALCULATIONS` folder or project root:

```bash
python3 Kinetic_energy.py
# or from project root:
# python3 CALCULATIONS/Kinetic_energy.py
```

Follow the prompts to enter mass (kg) and velocity (m/s).

---

## Functions 🔧

- `kinetic_energy(mass: float, velocity: float) -> float` — returns kinetic energy in Joules (0.5 * m * v**2).
- `prompt_user(prompt: str) -> float` — basic input helper for numeric input.
- `main()` — CLI entry point.

---

## Example

```
Input the mass of the body in Kilogram(kg): 10
Input the mass of the body in metre per sec (m/s): 3
A body of mass 10.00kg and 3.00m/s possess kinetic Energy of 45.00Joules
```

---

