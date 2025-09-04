#!/usr/bin/env bash
# Usage:
#   ./fix_units.sh                  # fix all *.lyx recursively
#   ./fix_units.sh file1.lyx ...    # or specific files
#
# Notes:
# - Only edits between \begin_inset Formula ... \end_inset
# - Wraps units in \text{...} and fixes spacing/casing
# - Makes a .bak backup of each file

set -euo pipefail

# Ensure UTF-8 so the × and − characters match
export LC_ALL=en_US.UTF-8 || true
export LANG=${LANG:-en_US.UTF-8}

if [ "$#" -gt 0 ]; then
  files=("$@")
else
  mapfile -t files < <(find . -type f -name "*.lyx")
fi

if [ "${#files[@]}" -eq 0 ]; then
  echo "No .lyx files found." >&2
  exit 1
fi

for f in "${files[@]}"; do
  [ -f "$f" ] || continue
  echo "Fixing units in: $f"
  cp -p "$f" "$f.bak"

  # POSIX ERE only (no \s, no (?: )), use [[:space:]] and plain ()
  sed -E -i '
/\\begin_inset Formula/,/\\end_inset/{

  # -------- Deduplicate accidental repeats --------
  s/kHzkHz/kHz/g
  s/HzHz/Hz/g
  s/dBdB/dB/g

  # -------- Velocity (m/s) after a number --------
  # 50m/s, 50 m/s, 1.2×10−3m/s -> 50 \text{m/s}
  s/([0-9]+([.][0-9]+)?(([x×]10([-−])?[0-9]+))?)[[:space:]]*m\/s/\1 \\text{m\/s}/g

  # -------- kHz (handle before Hz) --------
  # 17kHz, 17 Khz, 1.7×10^4khz -> 17 \text{kHz}
  s/([0-9]+([.][0-9]+)?(([x×]10([-−])?[0-9]+))?)[[:space:]]*[kK][hH][zZ]/\1 \\text{kHz}/g

  # -------- Hz --------
  # 200Hz, 200 hz -> 200 \text{Hz}
  s/([0-9]+([.][0-9]+)?(([x×]10([-−])?[0-9]+))?)[[:space:]]*[hH][zZ]/\1 \\text{Hz}/g

  # -------- dB --------
  # 75dB, 75 DB -> 75 \text{dB}
  s/([0-9]+([.][0-9]+)?)[[:space:]]*[dD][bB]/\1 \\text{dB}/g

  # -------- Pascal --------
  # 101325Pa, 0.5 pa, 1×10−3Pa -> ... \text{Pa}
  s/([0-9]+([.][0-9]+)?(([x×]10([-−])?[0-9]+))?)[[:space:]]*[pP][aA]/\1 \\text{Pa}/g

  # -------- Seconds --------
  # 0.005s, 3×10−6s -> ... \text{s}
  s/([0-9]+([.][0-9]+)?(([x×]10([-−])?[0-9]+))?)s/\1 \\text{s}/g

  # -------- Meters --------
  # 0.001m, 1m, 1×10−3m -> ... \text{m}
  s/([0-9]+([.][0-9]+)?(([x×]10([-−])?[0-9]+))?)m/\1 \\text{m}/g

  # -------- Micro-Pascal reference --------
  # \mu Pa -> \mu \text{Pa}
  s/\\mu[[:space:]]*Pa/\\mu \\text{Pa}/g
}
' "$f"

done

echo "Done. Backups saved as *.bak"

