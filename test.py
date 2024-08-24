import os

import matplotlib.pyplot as plt
import numpy as np


def hoge(x: int) -> None:
    print(x)


def main() -> None:
    print(os.path.__file__)
    x = np.linspace(0, 4 * np.pi, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    main()
