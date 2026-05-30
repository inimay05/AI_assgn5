# AI Assignment 5
---

# Repository Structure

```text
AI_assgn5
│
├── Assignment-1-Search-Algorithms
│   ├── minimax.py
│   ├── alpha_beta.py
│   ├── heuristic_alpha_beta.py
│   ├── mcts.py
│   ├── test_cases.py
│   
│
├── Assignment-2-AI-Travel-Planner
│   ├── app.py
│   ├── knowledge_base.json
│  
│
├── Assignment-3-Knowledge-Graphs
│   ├── knowledge_graph.py
│   ├── graph.ttl
│  
│
└── Assignment-4-Bayesian-Networks
    ├── bayesian_network.py
    
```

---

# Assignment 1

# Search Algorithms

## Objective

Implement and compare classical AI search algorithms used in adversarial decision making.

### Algorithms Implemented

1. Minimax Search
2. Alpha-Beta Pruning
3. Heuristic Alpha-Beta Search
4. Monte Carlo Tree Search (MCTS)

---

## Minimax Search

Minimax is a recursive decision-making algorithm used in two-player games. It assumes both players play optimally.

### Features

* Complete search of game tree
* Optimal move selection
* Suitable for deterministic games

---

## Alpha-Beta Pruning

Alpha-Beta Pruning improves Minimax by removing branches that cannot influence the final decision.

### Advantages

* Reduces search space
* Faster execution
* Produces same result as Minimax

---

## Heuristic Alpha-Beta Search

Uses evaluation functions to estimate node values when full tree exploration is expensive.

### Advantages

* Faster than complete search
* Suitable for large game trees
* Commonly used in Chess and Checkers

---

## Monte Carlo Tree Search

MCTS uses random simulations and statistical sampling to determine promising moves.

### Phases

1. Selection
2. Expansion
3. Simulation
4. Backpropagation

### Applications

* AlphaGo
* Game AI
* Planning Systems

---

## Test Cases

### Test Case 1

Input:

```text
[3,5,6,9,1,2,0,-1]
```

Expected Output:

```text
Optimal Value = 5
```

---

### Test Case 2

Alpha-Beta Search

Expected Output:

```text
Optimal Value = 5
```

---

### Test Case 3

Heuristic Alpha-Beta

Expected Output:

```text
Best Heuristic Value = 7
```

---

### Test Case 4

Monte Carlo Tree Search

Expected Output:

```text
Visits distributed among explored nodes
```

---

# Assignment 2

# AI-Based Travel Planner

## Objective

Design an AI-based Travel Planner that reuses existing knowledge bases such as tourist attractions, food recommendations, activities, and budget assessment.

---

## Knowledge Base

The planner stores information regarding:

* Tourist destinations
* Budget categories
* Food preferences
* Activities
* Travel recommendations

---

## AI Approach

A rule-based recommendation engine was implemented.

### Inputs

* Budget
* Preferred Activity

### Outputs

* Recommended Tourist Destination

---

## Example

Input:

```text
Budget = medium
Activity = beach
```

Output:

```text
Goa
```

---

## Features

* Knowledge-based reasoning
* Personalized recommendation
* Budget-aware planning
* Activity matching

---

## Future Enhancements

* Hotel Recommendation
* Flight Cost Estimation
* Weather Prediction
* Personalized Itinerary Generation
* Integration with Tourism APIs

---

# Assignment 3

# Knowledge Graphs

## Objective

Study Knowledge Graphs and explore tools used for graph-based knowledge representation.

---

## What is a Knowledge Graph?

A Knowledge Graph represents entities and relationships as nodes and edges.

Knowledge is represented as triples:

```text
Subject → Predicate → Object
```

Example:

```text
Goa → hasActivity → Beach
```

---

## Implementation

A simple RDF graph was implemented using RDFLib.

### Triple Added

```text
(Goa, hasActivity, Beach)
```

The graph is exported in Turtle (.ttl) format.

---

## Tools Explored

### RDFLib

Python library for RDF processing.

### Neo4j

Graph database platform.

### Apache Jena

Java framework for semantic web applications.

### Protégé

Ontology editor for knowledge modeling.

### GraphDB

Enterprise knowledge graph database.

---

## Output

```text
Triples in Graph:

http://example.org/Goa
http://example.org/hasActivity
http://example.org/Beach
```

---

# Assignment 4

# Bayesian Networks

## Objective

Explore Bayesian Networks for probabilistic reasoning and inference.

---

## Problem Chosen

Traffic Prediction based on:

* Rain
* Accident

---

## Bayesian Network Structure

```text
Rain ------\
            \
             -> Traffic
            /
Accident ---/
```

---

## Concepts Used

### Conditional Probability

Represents uncertainty using probability distributions.

### Bayesian Inference

Updates beliefs based on evidence.

### Variable Elimination

Inference algorithm used to compute posterior probabilities.

---

## Tools Explored

### pgmpy

Python library for Bayesian Networks.

### GeNIe

Graphical Bayesian Network tool.

### Netica

Probabilistic reasoning software.

### BayesiaLab

Industrial Bayesian modeling platform.

---

## Example Query

```text
P(Traffic | Rain = True)
```

Output:

Probability distribution for traffic conditions given rainfall.

---

# Software Requirements

## Common Requirements

* Python 3.x
* Git
* GitHub

---

## Assignment 1

No external libraries required.

---

## Assignment 2

No external libraries required.

---

## Assignment 3

Library:

```bash
pip install rdflib --break-system-packages
```

---

## Assignment 4

Library:

```bash
pip install pgmpy --break-system-packages
```

---

# Execution Instructions

## Assignment 1

```bash
python3 minimax.py
python3 alpha_beta.py
python3 heuristic_alpha_beta.py
python3 mcts.py
```

---

## Assignment 2

```bash
python3 app.py
```

---

## Assignment 3

```bash
python3 knowledge_graph.py
```

---

## Assignment 4

```bash
python3 bayesian_network.py
```

---

# Learning Outcomes

Through this assignment the following AI concepts were studied and implemented:

* Adversarial Search
* Game Tree Optimization
* Monte Carlo Methods
* Knowledge-Based Systems
* AI Travel Recommendation
* Knowledge Graphs
* RDF Representation
* Bayesian Networks
* Probabilistic Reasoning
* Inference Algorithms

---

# Conclusion

This assignment demonstrates the implementation of important Artificial Intelligence techniques including search algorithms, recommendation systems, knowledge representation, semantic knowledge graphs, and probabilistic reasoning. The developed solutions provide practical exposure to fundamental AI methodologies and their real-world applications.
