# Library SCA Benchmark v2 — intentionally vulnerable dependencies

> **For scanner evaluation only.** This repository intentionally declares old, vulnerable open-source dependencies. Do not deploy, install the pinned dependencies into a real application, or run as a public server. All books/users are fictitious.

A tiny library-management demo with package manifests for **Python / npm / Maven**. The goal is to see whether a Software Composition Analysis (SCA) tool recognizes known vulnerabilities in dependency **names and exact versions**. The executable Python sample uses only the standard library; it does **not** need the intentionally old dependencies.

## Scan targets at repository root

| File | Ecosystem | What a scanner should identify |
|---|---|---|
| `requirements.txt` | Python / PyPI | Pinned Python library versions |
| `package.json` and `package-lock.json` | JavaScript / npm | Pinned npm package versions |
| `pom.xml` | Java / Maven | Direct Maven dependency versions |
| `Dockerfile` | Container configuration | Optional Trivy misconfiguration checks **only if enabled** |
| `infra/deployment.yaml` | Kubernetes configuration | Optional Trivy misconfiguration checks **only if enabled** |

**Important**: Dependency alerts are not proof that the example runtime path is exploitable. SCA detects *potential* exposure due to known vulnerable components. A separate SAST/DAST assessment is needed to evaluate flaws in application logic or their reachability.

## GitHub and AutoSCA

1. Create a **test-only** GitHub repository (private if AutoSCA supports it, otherwise public with no secrets).
2. Upload **the contents of this directory**, not this ZIP file. Check that `requirements.txt`, `package-lock.json`, and `pom.xml` are visible on the first GitHub repository page, not buried in an extra outer folder.
3. Enter the GitHub repository URL in AutoSCA and run a new scan.
4. Verify **which manifests and how many packages were recognized**; compare with the separately supplied `library_sca_v2_expected_findings.csv` (not part of this repository).
5. If scanning returns 0 findings, check scan logs, supported ecosystems, directory recursion, scanner CLI flags, and whether the package/OSV vulnerability databases are up to date.

## Optional local offline demo (safe path only)

Do **not** install `requirements.txt` or run `npm install` / Maven builds for this benchmark. To see a tiny sample library API without those dependencies, you can run:

```bash
python src/library_api.py
```

It binds to `127.0.0.1:8765`. Open `http://127.0.0.1:8765/api/books`. The sample database uses a temporary directory and dummy books.

## What this benchmark does NOT test

SCA will generally **not** detect SQL injection, IDOR, XSS from app logic, missing authorization, business-logic races, Python–SQLite dialect mismatches, or front/back response-contract errors merely by scanning dependencies. Those require other analysis techniques.

The test deliberately avoids any real passwords, access tokens, or user data. No exploit payloads are included.
