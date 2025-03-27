# Teatris Game

Teatris es una implementación del clásico juego de Tetris en Python. Este proyecto está diseñado para ser una experiencia divertida y educativa, permitiendo a los jugadores disfrutar del juego mientras se exploran conceptos de programación y diseño de juegos.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
teatris-game/
├── src/
│   ├── main.py               # Punto de entrada del juego
│   ├── game/                  # Lógica del juego
│   │   ├── __init__.py       # Inicializa el paquete del juego
│   │   ├── board.py          # Clase que gestiona el estado del tablero
│   │   ├── tetromino.py      # Clase que representa las piezas del juego
│   │   └── game_logic.py     # Lógica del juego y detección de colisiones
│   ├── assets/                # Recursos del juego
│   │   ├── fonts/            # Fuentes utilizadas en el juego
│   │   └── sounds/           # Efectos de sonido y música
│   └── utils/                 # Funciones auxiliares
│       ├── __init__.py       # Inicializa el paquete de utilidades
│       └── helpers.py        # Funciones auxiliares
├── tests/                     # Pruebas unitarias
│   ├── __init__.py           # Inicializa el paquete de pruebas
│   ├── test_board.py         # Pruebas para la clase Board
│   ├── test_tetromino.py     # Pruebas para la clase Tetromino
│   └── test_game_logic.py    # Pruebas para la lógica del juego
├── requirements.txt           # Dependencias del proyecto
├── .gitignore                 # Archivos y directorios a ignorar
└── README.md                  # Documentación del proyecto
```

## Instalación

Para instalar las dependencias necesarias, ejecuta el siguiente comando:

```
pip install -r requirements.txt
```

## Uso

Para iniciar el juego, ejecuta el archivo `main.py`:

```
python src/main.py
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.