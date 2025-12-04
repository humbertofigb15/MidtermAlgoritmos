# Midterm 2 – Algorithmic Improvement Project  
**Predicción de tendencia USD/MXN usando Dynamic Programming y un modelo Greedy**

Autores:  
- Humberto Figueroa Bouttier  
- Rodrigo González de la Garza  
- Diego Gaitán Sánchez  
- Enrique Antonio Pires Rodríguez  

---

## 1. Descripción General del Problema

El proyecto analiza si es posible predecir la tendencia diaria del tipo de cambio USD/MXN utilizando un modelo determinista basado en algoritmos.  
El mercado cambiario es volátil y difícil de predecir, pero algunas señales de corto plazo pueden detectarse mediante análisis de ventanas móviles y técnicas de optimización.

**Pregunta central:**  
¿Un enfoque algorítmico simple, eficiente y determinista puede igualar o superar el desempeño de un método financiero clásico como el promedio móvil?

---

## 2. Objetivos del Proyecto

- Construir un modelo de predicción basado únicamente en técnicas algorítmicas.  
- Optimizar el cálculo de ventanas mediante programación dinámica.  
- Comparar su rendimiento contra un enfoque tradicional.  
- Utilizar datos reales del Banco de México para validar el experimento.  
- Evaluar tanto la precisión del modelo como su eficiencia computacional.

---

## 3. Enfoque Metodológico

El proyecto integra dos componentes principales:

### 3.1 Optimización de Ventanas
Se utiliza un esquema de programación dinámica basado en sumas acumuladas para acelerar los cálculos sobre ventanas deslizantes.  
Este mecanismo permite hacer consultas rápidas y reduce significativamente el tiempo de cómputo.

### 3.2 Modelo de Tendencia (DP + Greedy)
El modelo observa el comportamiento reciente del tipo de cambio en una ventana corta y decide si el siguiente día la moneda tenderá a subir o bajar.

### 3.3 Método de Comparación: Promedio Móvil
El promedio móvil es una técnica clásica en análisis financiero.  
Sirve como línea base para determinar si nuestro modelo algorítmico realmente aporta valor.

---

## 4. Arquitectura del Sistema

El proyecto está organizado en módulos independientes:

- **Cliente Banxico:** descarga series oficiales del tipo de cambio.  
- **Motor DP:** acelera cálculos de ventana mediante sumas acumuladas.  
- **Predictores:** implementan tanto el modelo propuesto como el baseline.  
- **Evaluación:** calcula precisión, conteos y métricas.  
- **Benchmark:** compara el tiempo del modelo optimizado contra la versión ingenua.  
- **Experimentos:** ejecutan todo el flujo con datos reales.  
- **main.py:** archivo principal que ejecuta el benchmark y las pruebas.

Esta organización permite extender o reemplazar componentes sin modificar todo el sistema.

---

## 5. Complejidad y Escalabilidad

El uso de programación dinámica reduce drásticamente el costo del cómputo sobre ventanas.  
Mientras que un enfoque tradicional requiere operaciones proporcionales al tamaño de la ventana, la técnica utilizada permite obtener resultados casi instantáneamente.  

Esto mejora la escalabilidad y habilita el uso de ventanas más grandes o series más extensas sin comprometer velocidad.

---

## 6. Resultados de Rendimiento

Una parte esencial del proyecto consistió en comparar el rendimiento entre:

1. **Cálculo de ventana ingenuo (lento)**
2. **Cálculo con programación dinámica (rápido)**

En pruebas con 50,000 datos y ventanas de tamaño 30, el modelo optimizado alcanzó una aceleración de aproximadamente **6 veces** frente al enfoque tradicional.

Esto confirma que el diseño algorítmico implementado no solo funciona, sino que es sustancialmente más eficiente.

---

## 7. Resultados con Datos Reales del Banco de México

Se utilizaron alrededor de 730 días de datos reales del tipo de cambio USD/MXN.  
Con una ventana de 5 días, los resultados fueron:

- **Modelo DP + Greedy:** 0.510 de precisión  
- **Promedio Móvil:** 0.509 de precisión  

Aunque las diferencias son pequeñas —lo cual es normal en series financieras— el modelo propuesto logra igualar e incluso superar ligeramente al método tradicional.

Esto demuestra que un enfoque determinista, simple y eficiente puede competir con técnicas ampliamente utilizadas en análisis financiero.

---

## 8. Cómo Ejecutarlo

1. Instalar dependencias:  
   `pip install -r requirements.txt`

2. Establecer tu token del Banco de México:  
   `export BANXICO_TOKEN="TU_TOKEN_AQUI"`

3. Ejecutar la experiencia completa:  
   `python main.py`

Esto correrá tanto las pruebas de rendimiento como el experimento con datos reales.

---

## 10. Referencias

- Banco de México – API SIE.  

