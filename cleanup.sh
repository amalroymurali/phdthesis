# from the repo root
# 1) Untrack everything (keeps files on disk!)
git rm -r --cached .

# 2) Re-add only what you want to keep in Git
git add recent_files.txt

# 3) Commit the change
git commit -m "Cleanup commit"

