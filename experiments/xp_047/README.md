# XP\#047

semafor on FN 1.7 FT with NLP4J + BMST

### Test scores
| P | R | F1 |
| --- | --- | --- |
| 64.8 | 55.7 | 59.9 |

### Splits generation
```
pyfn convert \
  --from fnxml \
  --to semafor \
  --source /path/to/fndata-1.7-with-dev \
  --target /path/to/experiments/xp_047/data \
  --splits train \
  --output_sentences
```

### Data preparation
```
./prepare.sh -x 047 -p semafor -s test -f /path/to/fndata-1.7-with-dev
```

### Preprocessing
```
./preprocess.sh -x 047 -t nlp4j -d bmst -p semafor
```

### Training
```
./semafor.sh -m train -x 047
```

### Decoding
```
./semafor.sh -m decode -x 047 -s test
```

### Scoring
```
./score.sh -x 047 -p semafor -s test -f gold
```
