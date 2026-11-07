# Organizācijas zināšanu modelis (OKM) — kopsavilkums latviešu valodā

OKM (Organisation Knowledge Model) ir atvērta specifikācija organizācijas zināšanu bāzei — versionētam, mašīnlasāmam organizācijas modelim, ko var vaicāt gan cilvēki, gan MI aģenti, un katrai atbildei ir pamatojums.

Zināšanu bāze glabā, kas organizācijā pastāv, kā tas tiek identificēts visās sistēmās, kā viss savstarpēji saistīts, kas ir atļauts un obligāts, kas bija spēkā kurā brīdī un uz ko katrs apgalvojums balstās. Tā nav dokumentu krātuve vai vektoru indekss — tie ir zināšanu bāzes avoti un rādītāji.

Modelis ir vienāds visos mērogos: komandai, uzņēmumam, valsts iestādei un visai valstij. Valsts tiek modelēta kā organizāciju organizācija ar tām pašām klasēm un saitēm.

## Galvenās daļas

- **20 pamatklases** — organizācija, struktūrvienība, loma, funkcija, uzdevums, tiesību norma, dokuments, pakalpojums, process, sistēma, datu kopa, mērķis, rādītājs, budžeta pozīcija, termins u. c.
- **25 pamatsaites** — ietilpst, atbild par, izpilda, nosaka, īsteno, izmanto, finansē u. c.
- **Pamatojums katrai saitei** — avots, tiesiskais pamats, metode un statuss: no avota, atvasināta, ieteikta, apstiprināta vai noraidīta. MI aģents ieteiktu saiti nedrīkst pasniegt kā faktu.
- **Laiks katram apgalvojumam** — spēkā no/līdz un vaicājumi uz noteiktu datumu.
- **Pastāvīgi identifikatori** ar sinonīmiem citās sistēmās un versijām pēc datuma.
- **Pieci MI aģentu vaicājumi** — `resolve`, `neighbours`, `path`, `explain`, `search` (piemēram, kā MCP rīki).

Tehniski OKM ir neliela **pamatontoloģija** ar noteikumiem par pamatojumu, laiku un identifikatoriem, kā arī saskarne MI aģentiem. Katrs termins ir sasaistīts ar esošajiem atvērtajiem standartiem: W3C ORG (The Organization Ontology), ES SEMIC pamatvārdnīcām, ArchiMate, BPMN, SKOS, DCAT, PROV-O un ELI.

## Ieviesumi

- **VZB — Valsts Zināšanu Bāze** VDZP platformā: valsts profils Latvijai no publiskiem avotiem (PPP Asociācija).
- **Neksus Core**: uzņēmuma profils (Neksus AI).

Specifikācija nepieder nevienam no tiem. Pilnais teksts angļu valodā — [SPECIFICATION.md](SPECIFICATION.md).

Versija 0.1.0, darba melnraksts, 2026. gada 7. novembris.
