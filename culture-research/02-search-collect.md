# Phase 2: Search Design & Paper Collection

**Purpose:** Design systematic search strategy, execute parallel region searches, acquire papers.

## 2a. Search Strategy Design

Before any search, produce a written protocol:

- **Discipline search templates** — tailored query terms per discipline (anthropology: "cultural practices everyday life"; sociology: "daily routines social structure"; psychology: "habit routine behavior"; urban studies: "urban daily mobility activity space")
- **Inclusion/exclusion criteria** — author type (professor-affiliated), study type (empirical, systematic review), population (general), date range, language
- **Source list per region** — Google Scholar, Semantic Scholar, ResearchGate, institutional repositories, region-specific academic databases, regional journals

## 2b. Region-Parallel Search

Run searches organized by geographic region, **each as a parallel sub-agent**:

| Region | Typical Search Focus |
|--------|---------------------|
| East Asia | China, Japan, South Korea, Taiwan — collectivism, work culture, filial piety |
| South & Southeast Asia | India, Indonesia, Thailand, Vietnam — family structure, rural/urban divide |
| Europe | UK, Germany, France, Nordic, Eastern — welfare state, individualism, work-life |
| Americas | US, Canada, Brazil, Mexico — immigration, diversity, inequality |
| Middle East & Africa | Egypt, Nigeria, South Africa, Turkey, Iran — religion, community, tradition |
| Oceania & Pacific | Australia, New Zealand, Pacific Islands — indigenous practices, island life |

**Per-region sub-agent task:** search, identify candidates, return list with title, author, affiliation, year, URL, abstract, and the search query that found it.

## 2c. Collation & Deduplication

- Merge all region results into a unified candidate list
- Deduplicate (same paper found by multiple region agents)
- Prioritize by relevance to research question, professor affiliation, and source type

## 2d. Paper Acquisition

- Download accessible PDFs/reports to `papers/raw/`
- Create metadata JSON for each paper: title, full author list, institutional affiliation(s), year, source URL, search query, abstract, DOI
- Rename and organize: `papers/{region}/{FirstAuthor}_{Year}_{ShortTitle}.pdf`
- Classify each paper: discipline, methodology type, population sampled, sample size

## 2e. Coverage Report

Produce `papers/coverage-report.md`:

- Papers per region, discipline, decade, methodology, population type
- **Explicit coverage gaps flagged** — regions, disciplines, or behavior domains with zero hits
- Language bias note — what languages were searched vs what exists
