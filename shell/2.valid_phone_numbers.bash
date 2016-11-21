#!/bin/bash

# awk '$0 ~ /^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/{print}' file.txt
# awk regular expression http://coolshell.cn/articles/9070.html, 一般不能用{3}必须硬写，没有\d等，然后就变成这个画风了
# awk '$0 ~ /^([0-9][0-9][0-9]-|\([0-9][0-9][0-9]\) )[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$/{print}' file.txt
grep -P "^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$" file.txt
