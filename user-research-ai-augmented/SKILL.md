---
name: user-research-ai-augmented
description: Use when conducting AI-augmented user experience research, helps structure prompts and automate routine analysis
---

# AI-Augmented User Research (REFINE + Three-Zone Framework)

## Overview

Integrate AI into user research without losing the human touch. Provides structured frameworks for prompt engineering and defines clear boundaries between automation and human judgment.

## When to Use

- Starting a new user research project
- Processing large amounts of interview/survey data
- Synthesizing qualitative insights
- Need to scale research without increasing headcount proportionally

## Core Framework 1: REFINE Prompt Engineering

Source: UX Reactor, 2025

Structure every AI prompt using this six-component framework:

| Letter | Component | What to do | Example |
|--------|-----------|------------|---------|
| **R** | **Role** | Assign AI a clear role | `You are a senior UX researcher with 10 years experience in consumer product interviews` |
| **E** | **Expectations** | State what output you expect | `I need you to identify the top 5 pain points from these interview transcripts` |
| **F** | **Format** | Specify output format | `Output as markdown table with Pain Point / Frequency / Quote Example` |
| **I** | **Iterate** | Plan for iteration, don't expect perfection | `We'll refine these themes in a second pass after I review` |
| **N** | **Nuance** | Provide context and nuance | `Users are primarily college students aged 18-24 using mobile-first social apps` |
| **E** | **Example** | (Optional but recommended) Give an example output | `For example, the output should look like this: ...` |

### REFINE Example Prompt

```
R = You are a senior UX researcher analyzing user interviews for a productivity app
E = Extract the main user pain points around onboarding
F = Markdown table: Pain Point | # of Mentions | Representative Quote
I = We'll prioritize and validate these in a second pass
N = All users are new signups who completed onboarding in the last 7 days
E =

| Pain Point | # of Mentions | Representative Quote |
|------------|---------------|-----------------------|
| Can't find export feature | 8 | "I looked everywhere couldn't figure out how to export my data" |
```

## Core Framework 2: Three-Zone Automation Boundaries

Source: Medium, "AI-Assisted User Research: A Practical Framework"

Divide your research process into three zones based on how much AI to use:

### 🟢 Green Zone — Full Automation

**What it is:** Tasks that can be safely 100% automated

**When to use:**
- Transcription of interviews
- Initial thematic coding (theme identification)
- Sentiment analysis across responses
- Summary of key takeaways from transcripts
- Counting frequency of topics
- Generating initial affinity diagram groups
- First draft of user persona descriptions

**How:** Use REFINE prompts to structure the output, then use directly

### 🟡 Yellow Zone — Human-AI Collaboration

**What it is:** AI does the heavy lifting, human makes the judgments

**When to use:**
- Affinity diagram mapping (AI groups, human adjusts and names groups)
- Journey map drafting (AI creates first pass, human adds insights)
- Thematic synthesis (AI identifies themes, human validates and connects)
- Persona refinement (AI generates draft, human adds depth and nuance)

**How:**
1. AI generates the first pass output
2. You review, move things around, rename, merge/split
3. Result is better than either could do alone

### 🔴 Red Zone — Human Primacy, AI as Helper

**What it is:** Humans lead, AI can offer alternative perspectives but doesn't decide

**When to use:**
- Strategic insight generation (what does this all mean for product strategy?)
- Empathetic connection and emotional sense-making
- Priority setting (which pain points are most important to fix?)
- Ethical assessment (does this research cause any harm?)
- Validating with stakeholders

**How:**
- AI can suggest alternative hypotheses to consider
- AI can surface disconfirming evidence you might have missed
- But the final insight/priority/judgment must be human

## 6-Step AI Synthesis Pipeline

Source: Great Question, 2025

```
1. Raw Data → AI Transcription
   Output: Clean text transcripts

2. Transcripts → AI Open Coding
   Output: Initial code labels and themes

3. Open Codes → AI Affinity Grouping
   Output: Clustered themes with supporting quotes

4. AI Clusters → Human Affinity Mapping
   Output: Finalized theme structure

5. Final Themes → AI Insight Synthesis
   Output: Draft insights with evidence

6. Draft Insights → Human Strategy Interpretation
   Output: Actionable recommendations for product
```

## Recommended Toolchain

| Tool Type | Examples |
|-----------|----------|
| **AI-assisted Qualitative Analysis** | Looppanel, NVivo (with AI), ATLAS.ti (with AI) |
| **Integrated User Research Platform** | Outset.ai, Maze, UserTesting AI |
| **Transcription** | Otter.ai, Descript |
| **DIY with LLMs** | Claude with REFINE prompts |

## Best Practices

1. **Always retain human oversight** — AI is for scaling your work, not replacing your judgment
2. **Start small** — automate the routine stuff first, free up time for high-value human work
3. **Validate with users** — AI patterns are hypotheses until you confirm them with real users
4. **Keep track of what works** — document which prompts/approaches give good results for your team
5. **Don't throw away the quotes** — AI can summarize, but direct user quotes keep insights grounded

## Boundaries to Respect

❌ AI should NOT:
- Make product priority decisions
- Replace talking to real users
- Tell you what to build
- Add emotional empathy that only a human researcher can provide

✅ AI SHOULD:
- Save you hours on transcription and initial coding
- Surface patterns you might have missed
- Help you process more data than you could manually
- Free you up to do the high-value strategic work

## References

- Original REFINE framework: https://uxreactor.com/ai-for-ux-user-research-prompt-best-practices-and-framework/
- Three-Zone framework: https://medium.com/design-bootcamp/ai-assisted-user-research-a-practical-framework-afefd54c882f
- 6-Step Pipeline: https://greatquestion.co/ux-research/ai-analysis-synthesis
- Top AI thematic tools: https://www.looppanel.com/blog/ai-thematic-analysis
- 2026 complete guide: https://www.parallelhq.com/blog/ai-user-research
