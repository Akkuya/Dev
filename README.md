# Dev

My personal monorepo. Contains projects, coursework, and self-study across quant finance, AI, systems programming, and mobile dev.

> CS Co-op @ UTSC — Software Engineering Specialist + Statistics Minor

---

## Structure

```bash
Dev/
    AI_Terminal/          # Local Python LLM assistant (Ollama + LLaMA 3)
    CanvasYoink/          # Submodule — canvas scraper tool
    CompetitiveProgramming/  # Leetcode, contest problems
    GDGUTSC/              # Google Developer Group UTSC work
    Misc/                 # One-offs and experiments
    QuantProjects/        # Quant finance projects
        PuzzleSolver/     # Probability puzzle solver (interview prep)
    School/               # Course assignments and notes
        CSCA48/           # Data Structures in C
        MATA22/           # Linear Algebra
        MATA37/           # Calculus
    flutter_projects/
        gym_app/          # Flutter gym tracking app
    learncpp/             # C++ self-study
    papers-we-love/       # Submodule — CS/math research papers
```

---

## Projects

### PuzzleSolver

Quant finance probability puzzle library. Each problem implements `solve()` (analytical), `simulate()` (Monte Carlo), and `verify()` (checks they agree). Built for interview prep — problems sourced from Brainstellar and Xinfeng Zhou's green book.

### AI Terminal

Local terminal assistant powered by LLaMA 3 via Ollama. CLI interface with memory and tool routing. Built from scratch — no LangChain, no frameworks, core logic designed manually.

### Gym App

Flutter app for tracking workouts. In planning/early development.

### CanvasYoink

Separate repo linked as a submodule.

---

## School

Assignments and notes from UTSC CS Co-op coursework:

| Course | Topic |
| --- | --- |
| CSCA48 | Data Structures & Abstraction (C) |
| MATA22 | Linear Algebra |
| MATA37 | Calculus for Mathematical Sciences |
| MGTA02 | Intro to Marketing |

---

## Languages

Primarily Python, with C for systems/coursework, C++ for self-study, and Dart for Flutter.

---

## Submodules

This repo uses git submodules. After cloning, run:

```bash
git submodule update --init --recursive
```

Note: `papers-we-love` is a large repo (~10GB). Clone with `--depth 1` if you only want the latest:

```bash
git submodule update --init --depth 1 papers-we-love
```
