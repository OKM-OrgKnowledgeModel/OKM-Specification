# Organisation Knowledge Model (OKM) — Specification

Version 0.1.0 (draft) · 7 November 2026 · Status: working draft, open for comment

The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY are to be read as described in RFC 2119.

## 1. Definition

An **organisation knowledge base** is a versioned, machine-readable model of an organisation that records:

- what exists (entities),
- what each thing is called everywhere (identifiers),
- how things relate (relations),
- what may and must happen (rules and processes),
- what was true when (time),
- and what each statement rests on (evidence),

linked to the original texts and data, and queried by people and AI agents through stable operations.

OKM is the specification of that model. Technically, OKM is a small **core ontology** — a fixed set of classes and relations with definitions, published in RDF (JSON-LD) and validated with SHACL — together with the rules for identifiers, evidence and time, and an interface for AI agents. It extends existing ontologies rather than replacing them (section 12). It applies at every scale: a team, a company, a group of companies, a public institution, a whole country. A country is modelled as an organisation of organisations, using the same classes and relations.

A document store, a vector index or a data lakehouse is not an organisation knowledge base on its own. Those are inputs to it and indexes over it. The test of an OKM knowledge base is that it can answer *"who is responsible for X, on what basis, since when, and how do you know?"* with evidence for every part of the answer.

## 2. Scope

OKM specifies:

1. the core classes and relations (section 4–5),
2. identifier rules (section 6),
3. evidence and time on every statement (section 7–8),
4. an exchange format and validation (section 9),
5. a query interface for AI agents (section 10),
6. conformance levels (section 11),
7. mappings to existing standards (section 12).

OKM does not specify storage technology, user interfaces, how data is extracted from source systems, or the content of any particular organisation. Implementations MAY use a relational database, a graph database or an RDF store.

## 3. Principles

1. **Model, not product.** The model (classes, relations, mappings, validation rules) is kept as files under version control. Any database is rebuilt from those files and from the sources.
2. **Evidence on every statement.** A relation without a basis or a source is a hypothesis and MUST be marked as such.
3. **Time on every statement.** Organisations change. Every entity and relation carries its validity period.
4. **Identifiers are permanent.** An identifier, once published, is never reused for something else.
5. **Data, text and graph are separate, linked by identifier.** Numbers stay in the data platform, wording stays in the text store, meaning lives in the graph. Each can be replaced without breaking the others.
6. **Standards first.** Every core term maps to an existing open vocabulary where one exists (section 12). OKM adds only what those vocabularies lack: evidence statuses, validity on relations, and the agent interface.
7. **Same model, different policy.** Public bodies MAY publish their knowledge base openly; companies keep theirs private. The model is identical; access control is outside this specification.

## 4. Core classes

Every entity (node) has exactly one core class. Implementations MAY define subclasses (for example `Ministry` as a subclass of `Organisation`) and MUST declare them with `okm:subClassOf` pointing to a core class.

| Class | Definition | Country example | Company example |
|---|---|---|---|
| `Organisation` | A legal or administrative body that can hold responsibilities. | ministry, agency, municipality | company, subsidiary |
| `Unit` | A part of an organisation without separate legal standing. | department of a ministry | sales department |
| `Role` | A position or responsibility that an agent can hold within a unit or organisation. | head of agency | finance controller |
| `Agent` | A person or software agent (including an AI agent) that holds a role. Optional; see 4.1. | — | AI invoice agent |
| `Function` | An enduring area of responsibility. | official statistics | accounts payable |
| `Task` | A concrete duty within a function. | collect and process statistical data | approve supplier invoices |
| `Competence` | A power or right to act. | issue binding rulings | sign contracts up to a limit |
| `Rule` | A normative unit: an article, paragraph or point of a law, regulation, policy, contract or standard. | article 16(5) of a law | clause 4.2 of the travel policy |
| `Document` | A text that contains rules or records: an act, statute, policy, contract, report. | institution statute | employee handbook |
| `Service` | Something provided to a customer, citizen or another unit. | public service | product or internal service |
| `Process` | An ordered set of steps that realises a function or service. Expressed in BPMN or UAPF. | vehicle registration process | order-to-cash |
| `Step` | One activity, event or decision in a process. | check the application | issue the invoice |
| `System` | An information system, application or technical component. | state information system | ERP |
| `Dataset` | A collection of data held or published. | register, open dataset | customer master data |
| `Goal` | An intended outcome. | government declaration task | strategic objective |
| `Measure` | An action or initiative intended to reach a goal. | action plan measure | project |
| `Indicator` | A quantity that measures a goal, measure or service. | NAP indicator | KPI |
| `BudgetLine` | An allocation of money. | budget programme | cost centre budget |
| `Term` | A defined concept or classifier value. | legal definition, COFOG code | glossary term, product code |
| `Place` | A geographic or administrative area. | municipality (ATVK) | site, region |

### 4.1 Natural persons

`Agent` nodes that represent natural persons are OPTIONAL and outside the public profile. A public knowledge base SHOULD model roles, not people. Where persons are modelled, the implementation is responsible for lawful processing (for example GDPR); OKM adds no personal attributes beyond a label.

## 5. Core relations

A relation (edge) has a subject, a predicate from this table, and an object. Domain and range are the classes allowed on each side. Implementations MAY define sub-properties and MUST declare them with `okm:subPropertyOf`.

| Relation | Subject → Object | Meaning |
|---|---|---|
| `partOf` | Organisation, Unit → Organisation, Unit | structural hierarchy |
| `supervisedBy` | Organisation → Organisation | subordination or supervision without being part of |
| `roleIn` | Role → Organisation, Unit | where a role sits |
| `holds` | Agent → Role | who or what holds a role |
| `responsibleFor` | Organisation, Unit, Role → Function, Service, Process, Goal, Measure, Dataset, System | accountability |
| `performs` | Organisation, Unit, Role, Agent, System → Task, Step | who or what carries out the work |
| `hasCompetence` | Organisation, Unit, Role → Competence | powers held |
| `partOfFunction` | Task → Function | a task belongs to a function |
| `establishes` | Rule → any class | the rule creates, requires or governs the object (legal or normative basis) |
| `contains` | Document → Rule | the rule is a unit of the document |
| `amends` | Rule, Document → Rule, Document | changes the object |
| `supersedes` | any → same class | replaces the object |
| `implements` | Rule → Rule | national or internal rule implementing a higher rule (for example transposition of a directive) |
| `realises` | Process → Function, Service | the process delivers the function or service |
| `hasStep` | Process → Step | process composition |
| `invokes` | Step → Process | a step calls another process |
| `uses` | Process, Step, Service, System → System, Dataset | dependency |
| `produces` | Process, Step, System → Dataset, Document | output |
| `contributesTo` | Measure, Function → Goal | intended effect |
| `measures` | Indicator → Goal, Measure, Service, Process | what an indicator tracks |
| `funds` | BudgetLine → Function, Measure, Service, Organisation, Unit | financing |
| `defines` | Rule, Document → Term | where a term is defined |
| `classifiedAs` | any → Term | classification by a classifier value |
| `broader` | Term → Term | classifier hierarchy (SKOS) |
| `locatedIn` | Organisation, Unit, Service, System → Place | location or territorial scope |

## 6. Identifiers

1. Every node MUST have one **canonical identifier**: an absolute IRI.
2. A canonical identifier MUST NOT be reused for a different thing, including after the thing ceases to exist.
3. Canonical identifiers SHOULD be **resolvable**: an HTTP GET returns a human-readable page for browsers and JSON-LD for `Accept: application/ld+json`.
4. A node MAY carry any number of **aliases**: identifiers from other schemes, each with its scheme name (for example a company registration number, LEI, a national institution code, CELEX, ELI, an internal system ID).
5. An identifier MAY be **version-pinned** by appending `@YYYY-MM-DD`, meaning "this thing as it applied from that date". The date is the date the version applies from, not the date of publication or loading. An unpinned identifier means the current version.
6. Identifiers of parts SHOULD extend the identifier of the whole (for example `…statute.p4.3` for point 4.3 of a statute), so that a unit can be traced to its document without a lookup.

## 7. Evidence

Every relation MUST carry evidence:

| Field | Required | Meaning |
|---|---|---|
| `status` | yes | one of the five statuses below |
| `basis` | if `status` is `source` or `confirmed` and a rule exists | identifier of the `Rule` the statement rests on |
| `source` | yes | IRI of the record or document the statement was taken from (the system of record) |
| `method` | yes | how the statement was made: `extracted`, `rule`, `model`, `manual` |
| `recordedAt` | yes | when the statement entered the knowledge base |
| `confidence` | if `status` is `proposed` | 0–1, as given by the proposing model or rule |
| `reviewedBy`, `reviewedAt` | if `status` is `confirmed` or `rejected` | who decided, and when; MAY be a role rather than a person |

**Statuses**

| Status | Meaning | May an agent state it as fact? |
|---|---|---|
| `source` | stated in the system of record | yes, citing `source` |
| `derived` | computed by a published rule from `source` statements | yes, naming the rule |
| `proposed` | suggested by a model or a person, not yet reviewed | no — must be presented as a suggestion |
| `confirmed` | proposed and then accepted by a responsible reviewer | yes, citing the reviewer and source |
| `rejected` | proposed and rejected; kept so it is not proposed again | no |

Nodes carry `source` and `recordedAt` in the same way. Statements are never silently corrected: when a source changes, the old statement gets a `validTo`, and a new statement is added.

## 8. Time

1. Every node and relation MAY carry `validFrom` and `validTo` (ISO 8601 dates). Absent `validFrom` means "from an unknown date"; absent `validTo` means "still valid".
2. `validFrom`/`validTo` describe when the statement is true in the world (valid time). `recordedAt` describes when the knowledge base learnt it (transaction time).
3. Every query operation in section 10 MUST accept an `asOf` date and return only statements valid on that date.

## 9. Exchange format and validation

An OKM export is a JSON-LD document using the OKM context (`context/okm.context.jsonld`):

```json
{
  "@context": "https://okm-orgknowledgemodel.github.io/okm/context/okm.context.jsonld",
  "okmVersion": "0.1.0",
  "publisher": "…",
  "generatedAt": "2026-11-07T20:00:00Z",
  "nodes": [ { "id": "…", "class": "Organisation", "label": "…", "aliases": [], "validFrom": "…", "source": "…", "recordedAt": "…" } ],
  "edges": [ { "id": "…", "subject": "…", "predicate": "responsibleFor", "object": "…", "status": "source", "basis": "…", "source": "…", "method": "extracted", "validFrom": "…", "recordedAt": "…" } ]
}
```

- The structure is validated by `schema/okm-graph.schema.json` (JSON Schema 2020-12).
- Graph rules (class of subject and object per relation, required evidence per status) are validated by `shapes/okm-core.shacl.ttl` (SHACL), or by an equivalent check in the implementation.
- Large exports MAY be split into JSON Lines files (`nodes.jsonl`, `edges.jsonl`) with the same objects.

## 10. Agent interface

An implementation at level 4 exposes these operations, for example as MCP tools. Every operation accepts `asOf` (default: today) and `minStatus` (default: `derived`, meaning `source`, `derived` and `confirmed`; set `proposed` to include suggestions).

| Operation | Input | Output |
|---|---|---|
| `resolve` | `id` (canonical or alias, optionally version-pinned) | the node, its aliases and its validity |
| `neighbours` | `id`, optional `predicate`, `direction` (`out`, `in`, `both`) | relations with their evidence |
| `path` | `from`, `to`, optional `predicates`, `maxHops` (default 4) | the shortest chains of relations, each with evidence |
| `explain` | an edge `id`, or `subject` + `predicate` + `object` | full evidence: basis text reference, source, method, status, review |
| `search` | `text`, optional `class` | matching nodes, ranked, with the text unit that matched |

Every response MUST include, for each relation returned, its `status`, `source` and, where present, `basis`. An agent using OKM MUST NOT present a `proposed` relation as fact.

## 11. Conformance levels

| Level | Name | Requirement |
|---|---|---|
| 1 | Model | Exports validate against the JSON Schema; every node has one core class (or a declared subclass). |
| 2 | Evidence | Every relation carries the evidence fields of section 7; SHACL validation passes. |
| 3 | Resolvable | Canonical identifiers resolve over HTTP as in section 6. |
| 4 | Agent | The operations of section 10 are available, with `asOf` and `minStatus`. |

An implementation states its level as, for example, "OKM 0.1 Level 2".

## 12. Mappings to existing standards

| OKM | W3C ORG (The Organization Ontology) | SEMIC Core Vocabularies | ArchiMate | Other |
|---|---|---|---|---|
| `Organisation` | `org:Organization`, `org:FormalOrganization` | `cpov:PublicOrganisation` (public sector) | Business Actor | schema.org `Organization` |
| `Unit` | `org:OrganizationalUnit` | — | Business Actor | |
| `Role` | `org:Role`, `org:Post` | — | Business Role | |
| `Agent` | `foaf:Agent` | — | Business Actor | `prov:Agent` |
| `Function` | — | — | Business Function | |
| `Task` | — | — | Business Function / Business Process (fine-grained) | |
| `Competence` | — | — | — | |
| `Rule` | — | — | Constraint / Requirement | ELI `eli:LegalResource` (subdivision) |
| `Document` | — | — | Business Object / Contract | ELI `eli:LegalResource`, `foaf:Document` |
| `Service` | — | `cpsv:PublicService` (CPSV-AP) | Business Service | |
| `Process` | — | — | Business Process | BPMN `process`, UAPF package |
| `Step` | — | — | Business Process / Event | BPMN flow node |
| `System` | — | — | Application Component | |
| `Dataset` | — | — | Data Object | DCAT `dcat:Dataset` |
| `Goal` | — | — | Goal / Outcome | |
| `Measure` | — | — | Work Package / Course of Action | |
| `Indicator` | — | — | Assessment / Meaning | |
| `BudgetLine` | — | — | — | |
| `Term` | — | — | — | SKOS `skos:Concept` |
| `Place` | `org:Site` | `locn:Location` | Location | |
| `partOf` | `org:subOrganizationOf`, `org:unitOf` | | Composition | |
| `roleIn` / `holds` | `org:Membership` | | Assignment | |
| `realises` | — | | Realization | |
| `uses` | — | | Serving / Access | |
| `broader` | — | | | `skos:broader` |
| evidence | — | | | PROV-O `prov:wasDerivedFrom`, `prov:wasAttributedTo` |
| validity | `org:memberDuring` | | | OWL-Time |

## 13. Open questions for 0.2

1. Permanent namespace IRI for OKM terms (w3id.org redirect or own domain).
2. Whether `Task` and `Competence` should become subclasses of `Function` rather than separate classes.
3. A minimal profile for executable rules (decision tables), aligned with UAPF and DMN.
4. Mapping of `Indicator` values (time series) to the data platform: by reference only, or a small value model.
5. A second agent operation set for writing: `propose` and `review`.

## 14. Normative and informative references

| Short name | Title | Publisher | Link |
|---|---|---|---|
| W3C ORG | The Organization Ontology, W3C Recommendation, 16 January 2014 (namespace `http://www.w3.org/ns/org#`) | W3C | https://www.w3.org/TR/vocab-org/ |
| PROV-O | PROV-O: The PROV Ontology | W3C | https://www.w3.org/TR/prov-o/ |
| OWL-Time | Time Ontology in OWL | W3C | https://www.w3.org/TR/owl-time/ |
| SKOS | Simple Knowledge Organization System | W3C | https://www.w3.org/TR/skos-reference/ |
| SHACL | Shapes Constraint Language | W3C | https://www.w3.org/TR/shacl/ |
| JSON-LD 1.1 | JSON-LD 1.1 | W3C | https://www.w3.org/TR/json-ld11/ |
| DCAT | Data Catalog Vocabulary | W3C | https://www.w3.org/TR/vocab-dcat/ |
| SEMIC Core Vocabularies | Core Public Organisation (CPOV), Core Public Service (CPSV-AP), Core Business, Core Location and others | European Commission, SEMIC | https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/solution/core-vocabularies |
| ELI | European Legislation Identifier | EU Publications Office | https://op.europa.eu/en/web/eu-vocabularies/eli |
| ArchiMate | ArchiMate Specification | The Open Group | https://www.opengroup.org/archimate-forum/archimate-overview |
| BPMN | Business Process Model and Notation 2.0 | OMG | https://www.omg.org/spec/BPMN/2.0/ |
| UAPF | Unified Algorithmic Process Format | UAPF | https://github.com/uapformat/uapf-spec |
| RFC 2119 | Key words for use in RFCs to Indicate Requirement Levels | IETF | https://www.rfc-editor.org/rfc/rfc2119 |

## 15. Reference implementations

- **VZB (Valsts Zināšanu Bāze)** in VDZP — country profile for Latvia, built from public sources; PPPA (PPP Asociācija).
- **Neksus Core** — company profile; Neksus AI.

Both implementations are independent of this specification; this specification belongs to neither.
