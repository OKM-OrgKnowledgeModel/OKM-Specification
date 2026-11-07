# Proposal 0001 — relation `references`

- **Status:** proposed for 0.2
- **Date:** 8 November 2026
- **Raised by:** VZB reference implementation (country profile, Latvia)

## Problem

A unit of one document often mentions another rule or document without being based on it, amending it or implementing it. Examples:

- a point of an institution statute: "the bureau … performs the tasks set in article 37 of the State Civil Service Law";
- a clause of a company policy: "expenses are approved as described in section 4 of the travel policy";
- a contract clause: "personal data are processed under the data processing agreement".

OKM 0.1 has no relation for this. The closest relations are wrong for it:

| Relation | Why it does not fit |
|---|---|
| `establishes` | Says the subject is the legal or normative basis of the object. A mention is often not a basis. |
| `implements` | Says the subject implements a higher rule (for example, transposition). |
| `amends` | Says the subject changes the object. |

In the Latvian country profile, about 270 statute points mention a law in this way. Without a relation they cannot be linked, so an agent cannot answer "which institutions' tasks rely on article 37 of the State Civil Service Law?".

## Proposal

Add a core relation:

| Relation | Domain → range | Meaning |
|---|---|---|
| `references` | Rule, Document → Rule, Document | the subject mentions the object; no claim that the object is its basis, that it implements or changes it |

Rules:

1. `references` is the weakest normative relation. When a stronger relation (`establishes`, `implements`, `amends`) can be stated, it SHOULD be used instead, and `references` SHOULD NOT be added for the same pair.
2. Evidence is required as for every relation. A mention found by text parsing has status `derived` and method `rule`; one suggested by a model has status `proposed`.
3. `basis` is not used: the subject itself is where the mention is made.

Mappings: ELI `eli:cites`; Akoma Ntoso `<ref>`; Dublin Core `dcterms:references`.

## Changes

- SPECIFICATION.md, section 5: add the row; section 12: add the mappings.
- schema/okm-graph.schema.json: add `references` to the `subPropertyOf` enum of extension relations.
- shapes/okm-core.shacl.ttl: add a shape restricting subject and object to `Rule` or `Document`.

## Discussion

Comment in a GitHub issue that links to this file, or in a pull request against it.
