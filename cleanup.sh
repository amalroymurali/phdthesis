# from the repo root
# 1) Untrack everything (keeps files on disk!)
git rm -r --cached .

# 2) Re-add only what you want to keep in Git
xargs -d '\n' -a recent_files.txt git add

# 3) Commit the change
git commit -m "Thesis Approved."

