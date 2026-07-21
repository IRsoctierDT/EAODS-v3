# Repository Upgrade Migration

This patch relocates MkDocs-published framework and governance documents beneath `docs/`, preventing strict-build failures caused by navigation references outside the documentation directory.

## Apply

```bash
cp -R EAODS-v3-repository-upgrade/. /path/to/EAODS-v3/
cd /path/to/EAODS-v3
git add .
git commit -m "chore: harden repository governance and documentation automation"
git push
```

## Remove obsolete duplicate file

After confirming the new site builds, remove:

```bash
git rm frameworks/EAODS-v17.3/volume-08-security-engineering.md
git commit -m "refactor(docs): remove obsolete framework duplicate"
git push
```

The source-of-truth location becomes:

```text
docs/frameworks/EAODS-v17.3/volume-08-security-engineering.md
```
