# Machine Learning Model Development & Deployment with Ray AIR 

© 2019-2022, Anyscale. All Rights Reserved

<img src ="images/ray-serve.png" width="80%" height="40%">

Divided into three modules, each module will take about an hour, combined with lecture and followed by 
hands-on 👩‍💻 exercises in class.

This is a two-part tutorial. The first part will focus on [Ray Serve](https://docs.ray.io/en/latest/serve/index.html), which is a framework-agnostic and Python-first machine learning model serving library built on Ray. This tutorial will cover how Ray Serve makes it easy to deploy, operate, and scale a machine learning model using Ray Serve APIs. 

The second part is an introduction to [Ray AI Runtime](https://docs.ray.io/en/master/ray-air/getting-started.html). As part of Ray 2.0, Ray AI Runtime (AIR) is an open-source toolkit for building end-to-end ML applications. We will discuss the merits of Ray AIR and how its key concepts and components allow to take your simple and scalable use cases and scale it.

### Module 1 
#### Objective: Introduction of concepts, architecture, and Ray Serve APIs and integrations

 * Lecture 20 mins
   * What is Ray Serve & Why
   * Ray Serve Architecture & Components
   * Ray Serve Deployment Design Patterns
   * Ray Serve Integrations (MLflow, FastAPI, W & B)
   * What's new in Ray Serve 2.0
   * Introduction to Ray AIR for Machine Learning (Ray 2.0)
 * Notebooks & Exercises 
    * Ray Serve Model Serving Challenges
    * Ray Serve and MLflow Integration
    * Ray Serve Model Composition
   
### Module 2
#### Objective: Understand Deployment patterns and deployment graph APIs to build inference graphs
 * Notebooks & Exercises 
     * Ray Serve Inference Graphs
     
### Module 3
#### Objective: Introduction to Ray AIR for end-to-end model development and deployment 
 * Notebooks & Exercises 

### In this course, you will learn :

* 👩 Understand Ray Serve architecture, components, and flow of requests across replicas
* 📖 Learn how to use Ray Serve APIs to create, access, and deploy your models and mechanisms to access model deployments via Python APIs and HTTP endpoints
* 🧑‍💻Implement common model deployment patterns for serving ML models using the inference graph API as a directed acyclic graph (DAG)
* 📈 Scale up/down individual components of an inference graph node, utilizing appropriate hardware resources (GPUs/CPUs) and replicas
* 🎛 Inspect load and deployments in a Ray dashboard
* ⚙️  Introduction of Ray AIR for end-to-end machine development/deployment

### 🎓Prerequisite knowledge ###
**Level**: Beginners or intermediate ML/DS/MLOps practitioners
 * Familiarity with Python 3.7+ and basic programming concepts: lists, comprehensions, decorators, functions, dictionaries, classes, loops, exceptional handling, etc
 * Laptop with at least 8-16GB Memory with latest Chrome browser
 * Prior knowledge of Jupyter notebooks helpful
 * Basic knowledge of machine learning concepts
 * Basic understanding of model serving or scoring

Let's have 😜 fun with Ray Serve! To start with this tutorial, go [here](ex_00_tutorial_overview.ipynb).






