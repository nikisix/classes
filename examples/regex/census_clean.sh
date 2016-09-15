sed -r -e 's/[\d,]+[\+-]/N/g' $1\
| sed -r -e 's/[\d\.]+[\+-]/N/g' \
| sed -r -e 's/,\s*,\s*,\s*,/,N,N,N,/g' \
| sed -r -e 's/,\s*,\s*,/,N,N,/g' \
| sed -r -e 's/,\s*,/,N,/g'\
| sed -r -e 's/,-,/,N,/g'\
| sed -r -e 's/\(X\)/N/g'\
| sed -r -e 's/\*\*\*\*\*/N/g'\
| sed -r -e 's/\*\*\*/N/g'\
| sed -r -e 's/\*\*/N/g'\
| sed -r -e 's/,\s*$/,N/g'\
| sed -r -e 's/^\s*,/N,/g'
