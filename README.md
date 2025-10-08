# FizzBuzz Multilenguaje

Este proyecto implementa el juego **FizzBuzz** usando distintos lenguajes y paradigmas: Python (hilos y asincronía), C y Java. Además incluye tests y un script para ejecutar todo automáticamente.

---

## 📂 Estructura del proyecto

prueba-tecnica/
│
├─ FizzBuzz.py # Implementación en Python usando hilos
├─ FizzBuzz_Alternative.py # Implementación en Python usando asyncio
├─ FizzBuzzGame.java # Implementación en Java usando threads
├─ FizzBuzzGameTest.c # Test unitario en C
├─ fizzbuzz_threads.c # Implementación de hilos en C
├─ test_fizzbuzz_threads.py # Test de FizzBuzz con hilos en Python
├─ test_fizzbuzz-async.py # Test de FizzBuzz asincrónico en Python
├─ run_fizzbuzz_all.bat # Script para ejecutar todo en Windows
└─ README.md # Documentación del proyecto

yaml
Copiar código

---

## 💻 Tecnologías usadas

- **Python 3.12**: programación concurrente con `threading` y `asyncio`.  
- **C**: programación con hilos usando `pthread`.  
- **Java 21**: hilos con `Thread` y sincronización.  
- **Git**: control de versiones.  
- **GitHub**: repositorio remoto.  
- **Windows / WSL**: entorno de desarrollo.  

---

## 🚀 Cómo ejecutar el proyecto

### Windows (con `.bat`)

```bat
.\run_fizzbuzz_all.bat
Esto ejecutará:

FizzBuzz en Python (threads y asyncio)

Test unitario en C

FizzBuzz en Java

WSL / Linux
Instalar compilador C y Java:

bash
Copiar código
sudo apt update
sudo apt install gcc openjdk-21-jdk
Ejecutar Python:

bash
Copiar código
python3 FizzBuzz.py
python3 FizzBuzz_Alternative.py
Compilar y ejecutar C:

bash
Copiar código
gcc -pthread fizzbuzz_threads.c FizzBuzzGameTest.c -o FizzBuzzGameTest
./FizzBuzzGameTest
Compilar y ejecutar Java:

bash
Copiar código
javac FizzBuzzGame.java
java FizzBuzzGame
🧪 Tests
Python threading: test_fizzbuzz_threads.py

Python async: test_fizzbuzz-async.py

Ejecutar con:

bash
Copiar código
pytest -s test_fizzbuzz_threads.py
pytest -s test_fizzbuzz-async.py
C: compilando FizzBuzzGameTest.c con fizzbuzz_threads.c

Java: las pruebas están incluidas en la ejecución de FizzBuzzGame.java.

📌 Descripción de la lógica
Los jugadores se turnan para decir números del 1 al max_number.

Si un número es divisible por fizzDiv, dicen "¡fizz!".

Si es divisible por buzzDiv, dicen "¡buzz!".

Si es divisible por ambos, dicen "¡fizzbuzz!".

La ejecución es concurrente: hilos o async según el lenguaje.

🎯 Objetivos del proyecto
Practicar programación concurrente en distintos lenguajes.

Validar la lógica FizzBuzz mediante tests unitarios e integrados.

Automatizar la ejecución de todos los códigos con un script de Windows.

Documentar un proyecto multilenguaje listo para producción o presentación
