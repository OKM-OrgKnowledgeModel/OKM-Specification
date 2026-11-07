# Organisation Knowledge Model (OKM)

An open specification for **organisation knowledge bases**: versioned, machine-readable models of an organisation that AI agents and people can query with evidence for every answer.

OKM works at every scale — a team, a company, a public institution, a whole country — with the same classes, relations, identifiers and agent operations.

> **Status:** 0.1.0 working draft, 7 November 2026. Open for comment through GitHub issues.

## What problem it solves

Organisations are putting AI agents to work on their documents and data. Agents can find text, but they cannot reliably answer *who is responsible for X, on what basis, since when, and how do you know?* — because that knowledge is spread across org charts, statutes, policies, process maps, system inventories and budgets, each in its own format.

OKM defines one model for that knowledge:

- **20 core classes** — Organisation, Unit, Role, Function, Task, Rule, Document, Service, Process, System, Dataset, Goal, Indicator, BudgetLine, Term and others;
- **25 core relations** — partOf, responsibleFor, performs, establishes, realises, uses, funds and others;
- **evidence on every relation** — source, legal or policy basis, method, and a status: `source`, `derived`, `proposed`, `confirmed` or `rejected`;
- **time on every statement** — valid from/to, and as-of queries;
- **permanent, resolvable identifiers** with aliases and date-pinned versions;
- **five agent operations** — `resolve`, `neighbours`, `path`, `explain`, `search` — for example as MCP tools.

Technically, OKM is a small **core ontology** with rules for evidence, time and identifiers, plus an AI agent interface. Every term maps to existing open standards: W3C ORG (The Organization Ontology), the EU SEMIC Core Vocabularies, ArchiMate, BPMN, SKOS, DCAT, PROV-O and ELI.

## Contents

| Path | What it is |
|---|---|
| [SPECIFICATION.md](SPECIFICATION.md) | The specification |
| [context/okm.context.jsonld](context/okm.context.jsonld) | JSON-LD context for exports |
| [schema/okm-graph.schema.json](schema/okm-graph.schema.json) | JSON Schema for exports |
| [shapes/okm-core.shacl.ttl](shapes/okm-core.shacl.ttl) | SHACL shapes for graph rules |
| [tools/validate.py](tools/validate.py) | Validator (JSON Schema + SHACL) |
| [examples/lv-csp.okm.json](examples/lv-csp.okm.json) | Country profile: a Latvian state institution, from public data |
| [examples/company.okm.json](examples/company.okm.json) | Company profile: a fictional company with an AI agent in a role |

## Validate an export

```sh
pip install jsonschema rdflib pyshacl
python tools/validate.py examples/lv-csp.okm.json examples/company.okm.json
```

## Implementations

| Implementation | Profile | By |
|---|---|---|
| VZB — Valsts Zināšanu Bāze (in VDZP) | country (Latvia), public sources | PPP Asociācija (PPPA) |
| Neksus Core | company, private | Neksus AI |

OKM is independent of both. Anyone may implement it; conformance levels are defined in section 11 of the specification.

## Related open specifications

- [UAPF](https://github.com/uapformat/uapf-spec) — Unified Algorithmic Process Format, for processes referenced by OKM `Process` and `Step`.

## Contributing

Open an issue for questions, gaps and proposed changes. Changes to classes, relations or evidence rules are decided in issues before a pull request.

## Licence

Specification text: CC BY 4.0. Schemas, shapes, context and tools: Apache License 2.0. See [LICENSE.md](LICENSE.md).
