# Memetic Algorithm for Rastrigin Function Minimization

This repository contains a Python implementation of a **Memetic Algorithm** for minimizing the **Rastrigin function**.

The Rastrigin function is a well-known benchmark function in optimization. Because it has many local minima, it is commonly used to evaluate the performance of optimization algorithms. The objective of this project is to find a solution close to the global minimum of the function.

## Objective

The main objective of this project is to use a memetic algorithm to minimize the Rastrigin function and find its best solution.

The global minimum of the Rastrigin function is located at:

```text
x = [0, 0, ..., 0]
f(x) = 0
```

## About the Algorithm

A memetic algorithm is a hybrid optimization technique that combines evolutionary search with local search improvement.

In this project, the algorithm starts with an initial population of candidate solutions and improves them through selection, crossover, mutation, and local search. During the optimization process, the best solution is updated until the stopping condition is reached.

## Features

* Python implementation of a memetic algorithm
* Minimization of the Rastrigin benchmark function
* Population initialization
* Fitness evaluation
* Selection operation
* Crossover operation
* Mutation operation
* Local search improvement
* Best solution tracking
* 3D visualization of the Rastrigin function
* Display of the best point on a three-dimensional plot
* Configurable algorithm parameters

## Project Structure

```text
memetic-algorithm-rastrigin/
│
├── memetic_algorithm.py
├── requirements.txt
└── README.md
```

## File Description

* `memetic_algorithm.py`: Main Python file containing the Rastrigin function definition, memetic algorithm implementation, and 3D visualization.
* `requirements.txt`: List of required Python packages.
* `README.md`: Project description and usage instructions.

## Requirements

This project requires Python 3.

Required Python packages:

```text
numpy
matplotlib
```

You can install the required packages using:

```bash
pip install -r requirements.txt
```

## How to Run

After downloading or cloning the repository, run the main Python file:

```bash
python memetic_algorithm.py
```

or, on Windows:

```bash
py memetic_algorithm.py
```

## Output

The program provides:

* The best solution found by the memetic algorithm
* The minimum value of the Rastrigin function
* A 3D plot of the Rastrigin function
* A visual indication of the best point on the 3D surface

Example:

```text
first population : 
[[ 5.93030153  5.21436283]
 [-4.54794512  1.36131812]
 [ 5.36781333 -1.03656665]
 [ 0.84429715 -5.76372251]
 [ 5.31405022  1.96000849]
 [-3.26227283 -0.03224051]
 [-0.31659475  4.37698988]
 [ 1.79711424 -0.17959326]
 [ 5.55759514  5.36723667]
 [ 0.85929336 -0.48081421]]
---------------------------------------------
Best individual: [-0.00279482  0.0004551 ]
Best value: 0.001590689829200187
```

The exact result may vary from run to run because the algorithm uses random initialization and stochastic search operators.

## Visualization

In addition to the numerical output, the program also generates a **three-dimensional plot** of the Rastrigin function and marks the best solution found by the algorithm on the graph. This visualization helps illustrate where the optimal point lies on the function surface.

## Applications

This project can be useful for learning and testing optimization algorithms, especially for problems with many local minima.

Possible applications include:

* Function minimization
* Evolutionary computation
* Global optimization
* Benchmark testing
* Hybrid optimization methods
* Educational and research purposes

## Author

Reza Darabpour

## License

This project is provided for educational and research purposes.

