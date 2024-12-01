# Semantic Search Basics

Welcome to **Semantic Search Basics**, a repository designed to help you explore the applications of various embedding techniques for semantic search and to compare their results against traditional lexical search methods.

## 🧠 What is Semantic Search?

Semantic search aims to enhance traditional lexical search by interpreting the intent behind a user's query. While lexical search relies on exact word matches, semantic search focuses on the contextual and intentional meaning of the input. This makes it particularly useful when there are diverse ways to phrase a query that might not lexically match the target text. Instead, semantic search uses embeddings to capture the deeper meaning of the input, serving as a more robust key to find the most relevant results.

## 🔍 Project Overview

This repository includes Jupyter notebooks demonstrating how to:

- Implement and compare various embedding methods for semantic search.
- Benchmark semantic search results against lexical search results.
- Evaluate the performance of these methods using real-world queries.

### Dataset

The project uses the **arXiv dataset** (available on [Kaggle](https://www.kaggle.com/datasets/Cornell-University/arxiv/data)) to simulate real-world queries. We focus on human-generated queries in the STEM domain to find research papers on specific topics.

### Methodology

- **Input Data**: Real queries from users looking for STEM-related papers.
- **Comparison Metrics**:
  - **Semantic Search**: Using embeddings to find results based on intent and context.
  - **Lexical Search**: Using exact word matches.
  - **Ground Truth**: Evaluating against known correct results.

## 🚀 How to Get Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/semantic-search-basics.git

