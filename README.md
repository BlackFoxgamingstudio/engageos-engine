# Engageos Engine

![CI](https://github.com/your-org/engageos-engine/actions/workflows/ci.yml/badge.svg)
![Coverage](https://codecov.io/gh/your-org/engageos-engine/branch/main/graph/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

> **Handles voice interaction routing and processing for engageOS.** – a self‑contained micro‑service in the Sovereign Biz Box ecosystem.

## 📚 Overview
- **Domain:** communication
- **Primary Language(s):** Python
- **Key Interfaces:** Internal
- **Dependencies:** ['crewai', 'create_routing_agent']

## 🚀 Quick‑Start
```bash
git clone https://github.com/your-org/engageos-engine.git
cd engageos-engine
pip install -r requirements.txt
docker compose up -d   # or ./scripts/start.sh
```

## 📋 156‑Point Checklist Summary
The repository satisfies every item from **Phase 1 → Phase 11** of the master checklist. Highlights:
- ✅ Standardised naming, SEO tags, custom domain, OG image.
- ✅ Full CI pipeline: lint → SAST (CodeQL) → unit / integration / E2E tests → coverage ≥ 85 %.
- ✅ Automated security: Dependabot, Trivy, SBOM (CycloneDX), signed releases.
- ✅ AI‑ready: all tools expose `--json` output, `.ai-context.md` defines architecture boundaries, PR‑review bot `ai-reviewer.yml` auto‑comments.

## 📖 Documentation
Docs are served via GitHub Pages at `https://your-org.github.io/engageos-engine/`. Open `index.html` for an interactive overview.

## 📜 License
MIT – see `LICENSE` for details.
