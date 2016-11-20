#!/bin/bash


# awk '{d[$1]++}END{for(w in d) print w, d[w]}' RS=" |\n" words.txt | sort -k 2 -nr
awk '{for (i = 1; i <= NF; ++i) ++s[$i]}END{
  for (i in s) print i, s[i]
}' words.txt | sort -k 2 -nr
