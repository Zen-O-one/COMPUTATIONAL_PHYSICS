from __future__ import annotations

def kinetic_energy(mass: float,  velocity: float) -> float:
    """ Returns the kinetic energy in joules.

    Args:
        mass: mass in kilograms (cannot be negative)
        velocity: velocity in metres per second. """

    if mass < 0:
        raise ValueError("Mass must not be Negative")
    return 0.5*mass*(velocity**2)


def prompt_non_negative_float(prompt: str) ->float:
    """Prompts the user until we get a non-negative float """
    while True:
        try:
            value = float(input(prompt).strip())
        except ValueError:
            print('Please enter Numerical value')
            continue

        if value < 0:
            print('Enter a non_negative Value')
            continue
        return value


def main() -> None:
    # try:
    #     mass = prompt_non_negative_float("Input the mass of the body in Kilogram(kg): ")
    #     velocity = prompt_non_negative_float('Input the velocity of the body in metre per sec (m/s): ')
    # except KeyboardInterrupt:
    #     print("Aborted!!!")
    mass = prompt_non_negative_float(\
        'Input the mass of the body in kilogram: ')

    velocity = prompt_non_negative_float(\
        'Input the velocity of the body in m/s: ')

    ke = kinetic_energy(mass, velocity)
    print(f'A body of mass {mass:.2f}kg and {velocity:.2f}m/s possess kinetic Energy of {ke:.2f}Joules')


if __name__ == "__main__":
    main()