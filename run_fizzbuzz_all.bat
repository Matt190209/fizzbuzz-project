@echo off
echo 🧩 Ejecutando FizzBuzz en Python
python FizzBuzz.py
python FizzBuzz_Alternative.py

echo 🧩 Ejecutando test C
gcc -pthread fizzbuzz_threads.c FizzBuzzGameTest.c -o FizzBuzzGameTest.exe
FizzBuzzGameTest.exe

echo 🧩 Ejecutando FizzBuzz en Java
javac FizzBuzzGame.java
java FizzBuzzGame
pause
