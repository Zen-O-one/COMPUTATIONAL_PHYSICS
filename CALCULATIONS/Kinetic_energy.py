from __future__ import annotations

def kinetic_energy(mass: float,  velocity: float) -> float:
    """Return the kinetic energy(J), takes the mass(kg) and velocity(m/s)"""
    """Raises an error if user input negative mass"""
    if mass < 0:
        raise ValueError("Mass must not be Negative")
    if velocity < 0:
        """Since Velocity can be negative"""
        pass

    return 0.5*mass*(velocity**2)

def prompt_user(prompt: str) ->float:
    """Prompts the user until we get a wanted Value"""
    while True:
        try:
            value = float(input(prompt).strip())
        except ValueError:
            print('Please enter Numerical value')
        if value < 0:
            print('Enter a non_negatie Value')
        break
    return value

def main() -> None:
    mass = prompt_user("Input the mass of the body in Kilogram(kg): ")
    velocity = prompt_user('Input the mass of the body in metre per sec (m/s): ')

    ke = kinetic_energy(mass,velocity)

    print(f'A body of mass {mass:.2f}kg and {velocity:.2f}m/s possess kinetic Energy of {ke:.2f}Joules')


if __name__ == "__main__":
    main()