#!/bin/bash
set -euo pipefail

# Go to repo root
cd "$(git rev-parse --show-toplevel)"

# 1) Build the keep list = only *.lyx that end with _final.lyx (relative paths)
KEEP_LIST=".keep_only_final_lyx.txt"
: > "$KEEP_LIST"
# Use find to locate them; strip leading './'
while IFS= read -r f; do
  printf '%s\n' "${f#./}" >> "$KEEP_LIST"
done < <(find . -type f -name '*_final.lyx')

echo "Keeping these files:"
cat "$KEEP_LIST" || true
echo

# 2) Remove ALL tracked files from the index (not from disk), regardless of shell globbing
git ls-files -z | xargs -0 git rm --cached -r --quiet

# 3) Re-add ONLY the keepers (force in case .gitignore would block)
# If the list is empty, avoid failing
if [[ -s "$KEEP_LIST" ]]; then
  while IFS= read -r p; do
    [[ -z "${p// }" ]] && continue
    git add -f -- "$p"
  done < "$KEEP_LIST"
else
  echo "WARNING: No *_final.lyx files found to keep."
fi

# 4) Commit
# (If there are no changes, this will fail; guard it.)
if ! git diff --cached --quiet; then
  git commit -m "Thesis submitted. Cleanup."
  echo "Done: committed with only the *_final.lyx files tracked."
else
  echo "No staged changes to commit. Did the keep list end up empty?"
fi

