from __future__ import annotations

def kinetic_energy(mass: float,  velocity: float) -> float:
    """Return the kinetic energy in joules.
    Args:
        mass: mass in kilograms (cannot be negative)
        velocity: velocity in metres per second.
        Raises: ValueError if mass is negative """

    if mass < 0:
        raise ValueError("Mass must not be negative")
    return 0.5 * mass * (velocity**2)


def prompt_non_negative_float(prompt: str) -> float:
    """Prompts the user until we get a non-negative float """
    while True:
        try:
            value = float(input(prompt).strip())
        except ValueError:
            print('Please enter numeric value')
            continue

        if value < 0:
            print('Enter a non-negative value')
            continue
        return value


def main() -> None:
    try:
        mass = prompt_non_negative_float(
            "Input the mass of the body in Kilogram(kg): "
        )
        velocity = prompt_non_negative_float(
            'Input the velocity of the body in metre per sec (m/s): '
            )
    except KeyboardInterrupt:
        print("Aborted!!!")

    ke = kinetic_energy(mass, velocity)
    print(f'kinetic energy: {ke:.2f}J')


if __name__ == "__main__":
    main()