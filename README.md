```markdown
# Velocity Calculator with Maqueen & BBC micro:bit

## Overview

The Velocity Calculator with Maqueen & BBC micro:bit is a project that calculates the velocity of a Maqueen robot. It uses two micro:bits: one attached to the Maqueen robot and another for user interaction. The velocity is computed based on the distance the robot travels in a specified time interval.

## Features

- **Distance Measurement**: Measures the initial and final distances from an obstacle.
- **Time Interval**: Calculates velocity over a specified time period.
- **Error Handling**: Alerts if the robot is too close to the wall.

## Requirements

- BBC micro:bit (2 units)
- Maqueen robot
- `mbrobot_plusV2` library

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/velocity-calculator-maqueen.git
   ```
2. Navigate to the project directory:
   ```sh
   cd velocity-calculator-maqueen
   ```
3. Ensure the `mbrobot_plusV2` library is installed on your micro:bits.

## Usage

### Micro:bit 1 (User Interface)

1. Flash the following code onto the first micro:bit:
    ```python
    from mbrobot_plusV2 import *
    from microbit import *
    import radio

    radio.on()
    radio.config(channel=7, group=123)

    def get():
        message = radio.receive()
        while message is None:
            message = radio.receive()
        return message

    while True:
        if button_a.is_pressed():
            display.show(Image.HAPPY)
            radio.send("start")
            message = get()
            if message == "ERROR":
                print("Roboter ist zu nah an der Wand!")
            else:
                print("Geschwindigkeit = {}".format(message))
        sleep(10)
    ```

2. When button A is pressed, the micro:bit sends a "start" signal to the second micro:bit.

### Micro:bit 2 (Maqueen Robot Controller)

1. Flash the following code onto the second micro:bit:
    ```python
    from mbrobot_plusV2 import *
    from microbit import *
    import radio

    radio.on()
    radio.config(channel=7, group=123)

    while True:
        message = radio.receive()
        if message == "start":
            d_0 = getDistance()
            if d_0 < 10:
                radio.send("ERROR")
            else:
                t = 3  # Time in seconds the robot will drive forward
                forward()
                delay(t * 1000)
                stop()
                d_end = getDistance()
                v = (0.01 * (d_0 - d_end)) / t  # Convert cm to meters
                radio.send(str(v))
        sleep(10)
    ```

2. This micro:bit controls the Maqueen robot, measuring initial and final distances, and calculates the velocity.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## Contact

For any questions or suggestions, please contact [yourname@example.com](mailto:yourname@example.com).
```
