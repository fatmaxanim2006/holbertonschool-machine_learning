# NLP Metrics

This project implements NLP evaluation metrics, starting with BLEU score.

# 1. Repo-nu clone et
git clone https://github.com/fatmaxanim2006/holbertonschool-machine_learning.git
cd holbertonschool-machine_learning

# 2. Qovluğu yarat və içinə keç
mkdir -p supervised_learning/nlp_metrics
cd supervised_learning/nlp_metrics

# 3. README.md yarat
cat > README.md << 'EOF'
# NLP Metrics

This project implements NLP evaluation metrics, starting with BLEU score.

## Files

### 0-uni_bleu.py
Contains the function `uni_bleu(references, sentence)` that calculates
the unigram BLEU score for a sentence.

- `references` is a list of reference translations, each a list of words
- `sentence` is a list containing the model proposed sentence
- Returns the unigram BLEU score

The score combines:
1. **Modified unigram precision** — counts of matching words, clipped by
   the maximum count found in any single reference
2. **Brevity penalty (BP)** — penalizes sentences shorter than the
   closest-length reference

## Requirements
- Python 3.6+
- numpy

## Usage
```python
uni_bleu = __import__('0-uni_bleu').uni_bleu

references = [["the", "cat", "is", "on", "the", "mat"],
              ["there", "is", "a", "cat", "on", "the", "mat"]]
sentence = ["there", "is", "a", "cat", "here"]

print(uni_bleu(references, sentence))
# 0.6549846024623855
```
