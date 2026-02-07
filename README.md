# Ichi-kara
``` Learn anything, from first principles.```

- 'ichi-kara' is a personal learning platform that curates high-quality knowledge from across the internet and transforms it into structured, beginner-friendly learning experiences.

- Given a topic, the system discovers relevant educational content, extracts the core ideas, and presents them in two complementary formats:

> 1. Mode A — 📘 AI-Curated Notes
- Structured explanations
- Examples, analogies
- Key ideas distilled from multiple sources Beginner → intermediate flow
- Based on real references, not hallucination

> 2. Mode B — 🎥 AI-Generated Guided Video
- Same knowledge
- Converted into:
    narration
    visuals / slides / diagrams
    Designed for quick learning
- Feels like a short, focused lecture
- The guided video is programmatically generated from the same curated knowledge base using AI narration and visual synthesis.

Same knowledge core.
Two different cognitive entry points.

- The goal of ichi-kara is not just to summarize information, but to support deep understanding across domains — programming, data science, design, humanities, or any subject the learner wants to explore.

- The project is built as a modular system combining web crawling, content extraction, natural language processing, and AI-assisted explanation, with a focus on usability and human-centered learning design.

- This repository documents the ongoing development of ichi-kara as both:

    > a practical learning tool for everyday use, and

    > an applied exploration of Python, AI systems, and human–computer interaction.


## System Architecture

```
ichi-kara/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── crawler/
│   │   ├── nlp/
│   │   ├── ai/
│   │   └── db/
│   ├── requirements.txt
│   └── README.md
├── frontend/
│   ├── src/
│   └── README.md
├── docs/
│   ├── architecture.md
│   └── design.md
├── .gitignore
├── README.md
└── LICENSE
```

## Process Architecture

```
User Topic
   ↓
Search + Crawl
   ↓
Clean & Extract
   ↓
Knowledge Store (text + embeddings)
   ↓
AI Explanation Engine
   ├── Text Notes (read mode)
   └── Teaching Script
          ↓
      Video Generator
          ↓
      Guided Learning Video
```

``` Project Status: Early development (v0.1). Core crawling and text-generation pipelines are under active development. Video generation is planned for a later milestone. ```