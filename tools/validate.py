"""Validate an OKM export: JSON Schema (structure) + SHACL (graph rules).

Usage: python tools/validate.py examples/lv-csp.okm.json [more files]
Needs: pip install jsonschema rdflib pyshacl
Declared extension classes are materialised as their core class before SHACL runs.
"""
import json, pathlib, sys

import jsonschema, pyshacl, rdflib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OKM = rdflib.Namespace("https://okm-orgknowledgemodel.github.io/okm/ns#")
SCHEMA = json.loads((ROOT / "schema/okm-graph.schema.json").read_text())
CONTEXT = json.loads((ROOT / "context/okm.context.jsonld").read_text())["@context"]
SHAPES = rdflib.Graph().parse(ROOT / "shapes/okm-core.shacl.ttl")


def validate(path):
    doc = json.loads(pathlib.Path(path).read_text())
    errors = [f"schema: {e.json_path}: {e.message}" for e in jsonschema.Draft202012Validator(SCHEMA).iter_errors(doc)]
    ext = doc.pop("extensions", {}) or {}
    doc["@context"] = CONTEXT  # local copy of the context
    g = rdflib.Graph().parse(data=json.dumps(doc), format="json-ld")
    for c in ext.get("classes", []):
        for s in list(g.subjects(rdflib.RDF.type, OKM[c["name"]])):
            g.add((s, rdflib.RDF.type, OKM[c["subClassOf"]]))
    for r in ext.get("relations", []):
        for s in list(g.subjects(rdflib.RDF.predicate, OKM[r["name"]])):
            g.add((s, rdflib.RDF.predicate, OKM[r["subPropertyOf"]]))
    ok, _, report = pyshacl.validate(g, shacl_graph=SHAPES)
    if not ok:
        errors.append("shacl:\n" + report)
    return errors


if __name__ == "__main__":
    bad = 0
    for f in sys.argv[1:]:
        errs = validate(f)
        print(f"{f}: {'OK' if not errs else 'FAILED'}")
        for e in errs:
            print("  " + e)
        bad += bool(errs)
    sys.exit(1 if bad else 0)
