# Apply EAODS v17.3 Volume 9

From the root of the local `EAODS-v3` repository:

```bash
git checkout main
git pull --ff-only
git checkout -b docs/add-v17.3-volume-09
cp -R ~/Downloads/EAODS-v3-volume-09-pr/. .
python scripts/validate_front_matter.py
mkdocs build --strict
git add .
git commit -m "docs(v17.3): add infrastructure resilience architecture"
git push -u origin docs/add-v17.3-volume-09
```

Then create a pull request from `docs/add-v17.3-volume-09` into `main`.
