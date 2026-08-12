# TF-IDF — Term Frequency–Inverse Document Frequency

> TF-IDF is a text vectorization technique used in NLP to convert text into numerical vectors based on the importance of words in a collection of documents.

---

## 1. What is TF-IDF?

**TF-IDF = Term Frequency × Inverse Document Frequency**

TF-IDF gives a numerical score to each word based on:

* How frequently the word appears in a document
* How rare or common the word is across all documents

### Main idea

A word gets a **high TF-IDF score** when:

* It appears frequently in the current document
* It does not appear in many other documents

A word gets a **low TF-IDF score** when:

* It appears rarely in the document
* Or it appears in almost every document

---

# 2. Why Do We Need TF-IDF?

Machine Learning models cannot directly understand raw text.

For example:

```
"I love machine learning"
```

We need to convert it into numbers.

TF-IDF can represent the sentence as a numerical vector:

```
[0.0, 0.57, 0.57, 0.0, ...]
```

These vectors can then be given to Machine Learning algorithms.

---

# 3. Basic Intuition

Consider three documents:

```
D1 = "I love machine learning"

D2 = "I love deep learning"

D3 = "Machine learning is powerful"
```

The word:

```
"learning"
```

appears in all documents.

Therefore, it is not very useful for distinguishing one document from another.

But:

```
"machine"
```

appears in fewer documents.

So it can receive a higher importance score.

---

# 4. TF — Term Frequency

TF tells us:

> How frequently does a term occur in a document?

A simple formula is:

```
TF(t,d) =
Number of times term t appears in document d
------------------------------------------------
Total number of terms in document d
```

Where:

```
t = term
d = document
```

---

# 5. TF Example

Document:

```
"machine learning is fun"
```

Suppose we want TF of:

```
"learning"
```

"learning" appears:

```
1 time
```

Total words:

```
4
```

Therefore:

```
TF = 1 / 4

TF = 0.25
```

---

# 6. Another TF Example

Document:

```
"machine learning learning"
```

For:

```
"learning"
```

Count:

```
2
```

Total words:

```
3
```

Therefore:

```
TF = 2 / 3

TF ≈ 0.667
```

So the word "learning" has a higher TF because it appears more frequently in that document.

---

# 7. IDF — Inverse Document Frequency

TF alone is not enough.

A word may occur frequently in one document but also occur in almost every document.

IDF measures how rare a word is across the entire collection of documents.

Basic formula:

```
IDF(t) =
log(
    Number of documents
    -------------------
    Number of documents containing term t
)
```

Where:

```
t = term
```

---

# 8. IDF Intuition

Suppose we have:

```
100 documents
```

Word:

```
"the"
```

appears in:

```
100 documents
```

Then:

```
IDF = log(100 / 100)

IDF = log(1)

IDF = 0
```

Therefore, "the" gets very little importance.

---

# 9. Rare Word Example

Suppose:

```
Total documents = 100
```

Word:

```
"tensorflow"
```

appears in:

```
5 documents
```

Then:

```
IDF = log(100 / 5)

IDF = log(20)
```

The value is relatively high.

Therefore:

```
Rare word → Higher IDF
Common word → Lower IDF
```

---

# 10. TF-IDF Formula

The basic formula is:

```
TF-IDF(t,d) = TF(t,d) × IDF(t)
```

So:

```
TF-IDF
   ↓
Term Frequency
   ×
Inverse Document Frequency
```

---

# 11. Complete Example

Suppose we have:

```
D1 = "cat dog dog"
```

Total documents:

```
3
```

The word:

```
"dog"
```

appears twice in D1.

### Step 1 — TF

Total words:

```
3
```

Frequency of dog:

```
2
```

Therefore:

```
TF = 2 / 3
```

---

Suppose "dog" appears in:

```
2 documents
```

Then:

```
IDF = log(3 / 2)
```

---

Therefore:

```
TF-IDF = (2/3) × log(3/2)
```

The final value represents the importance of "dog" in D1.

---

# 12. Important Intuition

TF answers:

> How important is this word inside this document?

IDF answers:

> How rare is this word across all documents?

TF-IDF answers:

> How important is this word to this document compared with the entire collection?

---

# 13. TF-IDF vs Bag of Words

## Bag of Words

BoW mainly represents:

```
Word Frequency
```

Example:

```
"cat cat dog"
```

could become:

```
cat = 2
dog = 1
```

It does not consider how common a word is across the entire corpus.

---

## TF-IDF

TF-IDF considers:

```
Word Frequency
       +
Word Rarity
```

Therefore:

```
BoW
  ↓
Frequency

TF-IDF
  ↓
Frequency × Rarity
```

---

# 14. TF-IDF vs BoW Example

Suppose:

```
D1 = "machine learning is useful"

D2 = "machine learning is powerful"
```

Words like:

```
machine
learning
is
```

appear across documents.

TF-IDF reduces the importance of words that are common across many documents.

Words that are more specific to a document can receive higher scores.

---

# 15. Why TF-IDF is Useful

TF-IDF can be used for:

* Text classification
* Spam detection
* Sentiment analysis
* Document similarity
* Search engines
* Information retrieval
* Keyword extraction
* Recommendation systems
* Text clustering
* Machine Learning pipelines

---

# 16. TF-IDF Does Not Understand Meaning

Important:

TF-IDF is a statistical representation.

It does NOT understand:

* Meaning
* Context
* Grammar
* Word relationships
* Semantic similarity

For example:

```
"king"
"queen"
```

TF-IDF does not inherently know that these words are semantically related.

---

# 17. TF-IDF and Word Order

TF-IDF generally does not understand word order.

For example:

```
"dog bites man"
```

and:

```
"man bites dog"
```

can contain the same words and therefore have similar TF-IDF representations.

This is one limitation of traditional bag-of-words-based representations.

---

# 18. Vocabulary

Before generating vectors, TF-IDF creates a vocabulary from the corpus.

Example:

```
D1 = "I love Python"

D2 = "I love machine learning"
```

Vocabulary might contain:

```
I
love
Python
machine
learning
```

Each vocabulary term corresponds to a feature/column.

---

# 19. TF-IDF Matrix

Suppose vocabulary:

```
["python", "machine", "learning"]
```

Documents:

```
D1 = "python learning"

D2 = "machine learning"
```

The resulting TF-IDF representation can look conceptually like:

```
| Document | python | machine | learning |
|----------|--------|---------|----------|
| D1       | 0.7    | 0.0     | 0.4      |
| D2       | 0.0    | 0.7     | 0.4      |
```

The exact values depend on the TF-IDF formula and normalization used.

---

# 20. TF-IDF in Scikit-Learn

Scikit-learn provides:

```
TfidfVectorizer
```

Import:

```
from sklearn.feature_extraction.text import TfidfVectorizer
```

---

# 21. Basic Example

```
from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "I love machine learning",
    "I love deep learning",
    "Machine learning is powerful"
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(
    documents
)

print(X)
```

---

# 22. fit_transform()

This is one of the most important concepts.

```
vectorizer.fit_transform(documents)
```

It performs two operations:

```
fit
  ↓
Learn vocabulary and IDF values

transform
  ↓
Convert documents into TF-IDF vectors
```

---

# 23. Vocabulary

Get feature names:

```
feature_names = vectorizer.get_feature_names_out()

print(feature_names)
```

Example output may look like:

```
['deep' 'is' 'learning' 'love' 'machine' 'powerful']
```

---

# 24. Convert to Array

The result of:

```
fit_transform()
```

is usually a sparse matrix.

To inspect it:

```
print(X.toarray())
```

Example:

```
[[0.0, 0.0, 0.5, 0.7, 0.5, 0.0],
 [0.6, 0.0, 0.4, 0.6, 0.0, 0.0],
 [0.0, 0.6, 0.4, 0.0, 0.5, 0.6]]
```

The exact numbers depend on the corpus and vectorizer settings.

---

# 25. Why Sparse Matrix?

Text datasets often have a very large vocabulary.

Suppose:

```
10,000 documents
```

and:

```
50,000 unique words
```

The matrix could have:

```
10,000 × 50,000
```

potential values.

But each document usually contains only a small portion of those words.

Therefore, most values are zero.

This is called:

```
Sparse Data
```

Scikit-learn uses sparse matrices to store this efficiently.

---

# 26. Sparse vs Dense

Dense matrix:

```
[0.2, 0.0, 0.4, 0.0, 0.0, 0.7]
```

Sparse representation stores mainly the non-zero values.

This saves memory for large text datasets.

---

# 27. Convert TF-IDF to DataFrame

For small datasets:

```
import pandas as pd

df = pd.DataFrame(
    X.toarray(),
    columns=vectorizer.get_feature_names_out()
)

print(df)
```

This makes the TF-IDF matrix easier to inspect.

For large datasets, avoid unnecessarily converting sparse matrices to dense arrays.

---

# 28. Transform New Text

After fitting the vectorizer:

```
new_text = [
    "I love machine learning"
]

new_vector = vectorizer.transform(
    new_text
)
```

Important:

Use:

```
transform()
```

for new/unseen data.

Do NOT call:

```
fit_transform()
```

on test or new data.

---

# 29. fit vs transform

## fit()

Learns information from training data.

For TF-IDF, this includes:

* Vocabulary
* IDF values

---

## transform()

Uses the already learned vocabulary and IDF values to convert text into vectors.

---

## fit_transform()

Equivalent conceptually to:

```
fit()
+
transform()
```

---

# 30. Train/Test Split and TF-IDF

This is extremely important.

Suppose:

```
Raw Text
   ↓
Train/Test Split
   ↓
TF-IDF
```

The vectorizer should be fitted ONLY on training text.

Correct:

```
X_train
   ↓
TF-IDF fit_transform()

X_test
   ↓
TF-IDF transform()
```

---

# 31. Why?

Because fitting TF-IDF on the entire dataset before splitting can cause information from the test set to influence the feature transformation.

This is a form of data leakage.

Correct:

```
X_train_text
      ↓
vectorizer.fit_transform()
      ↓
X_train_tfidf

X_test_text
      ↓
vectorizer.transform()
      ↓
X_test_tfidf
```

---

# 32. Complete Classification Workflow

```
Raw Text
   ↓
Text Cleaning
   ↓
Train/Test Split
   ↓
TF-IDF
   ↓
ML Model
   ↓
Evaluation
```

Example:

```
X_train_text, X_test_text, y_train, y_test

vectorizer = TfidfVectorizer()

X_train = vectorizer.fit_transform(
    X_train_text
)

X_test = vectorizer.transform(
    X_test_text
)
```

---

# 33. TF-IDF + Machine Learning

Example:

```
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

documents = [
    "I love this movie",
    "This movie is amazing",
    "I hate this movie",
    "This movie is terrible"
]

labels = [
    1,
    1,
    0,
    0
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(
    documents
)

model = LogisticRegression()

model.fit(
    X,
    labels
)
```

---

# 34. Better Practice — Train/Test Split

```
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

X_train_text, X_test_text, y_train, y_test = train_test_split(
    documents,
    labels,
    test_size=0.2,
    random_state=42
)

vectorizer = TfidfVectorizer()

X_train = vectorizer.fit_transform(
    X_train_text
)

X_test = vectorizer.transform(
    X_test_text
)

model = LogisticRegression()

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)
```

---

# 35. TF-IDF with Pipeline

A cleaner approach is to use a Pipeline.

```
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer()
    ),
    (
        "classifier",
        LogisticRegression()
    )
])

model.fit(
    X_train_text,
    y_train
)

predictions = model.predict(
    X_test_text
)
```

The pipeline helps ensure the transformation is applied correctly during training and prediction.

---

# 36. Important TfidfVectorizer Parameters

Common parameters:

```
TfidfVectorizer(
    lowercase=True,
    stop_words=None,
    max_features=None,
    ngram_range=(1, 1),
    min_df=1,
    max_df=1.0,
    sublinear_tf=False
)
```

---

# 37. lowercase

Default:

```
lowercase=True
```

Example:

```
"Python"
"python"
```

can be normalized to:

```
"python"
```

---

# 38. stop_words

You can remove common words.

Example:

```
vectorizer = TfidfVectorizer(
    stop_words="english"
)
```

This removes common English stopwords using scikit-learn's built-in list.

For a serious NLP project, choose preprocessing based on the dataset and task rather than automatically removing every stopword.

---

# 39. max_features

Limits the vocabulary size.

Example:

```
vectorizer = TfidfVectorizer(
    max_features=5000
)
```

Only up to 5000 selected features are retained according to the vectorizer's feature-selection rules.

Useful when the vocabulary is very large.

---

# 40. ngram_range

Controls which n-grams are generated.

Unigram:

```
ngram_range=(1,1)
```

Bigram:

```
ngram_range=(2,2)
```

Unigram + Bigram:

```
ngram_range=(1,2)
```

Example:

```
"machine learning is useful"
```

Unigrams:

```
machine
learning
is
useful
```

Bigrams:

```
machine learning
learning is
is useful
```

---

# 41. min_df

Controls the minimum document frequency.

Example:

```
TfidfVectorizer(
    min_df=2
)
```

A term must appear in at least 2 documents to be included.

Useful for removing extremely rare terms.

---

# 42. max_df

Controls the maximum document frequency.

Example:

```
TfidfVectorizer(
    max_df=0.8
)
```

Terms appearing in more than 80% of documents can be ignored.

Useful for removing extremely common terms.

---

# 43. sublinear_tf

Example:

```
TfidfVectorizer(
    sublinear_tf=True
)
```

This applies logarithmic scaling to term frequency.

Instead of using raw TF directly, the term frequency is transformed roughly as:

```
1 + log(tf)
```

This can reduce the impact of extremely frequent terms.

---

# 44. TF-IDF Normalization

Scikit-learn's `TfidfVectorizer` uses L2 normalization by default.

Default:

```
norm="l2"
```

Other option:

```
norm="l1"
```

Or:

```
norm=None
```

Normalization affects the scale of the resulting vectors.

---

# 45. Cosine Similarity

TF-IDF is often used with cosine similarity to compare documents.

Concept:

```
Document A
    ↓
TF-IDF Vector

Document B
    ↓
TF-IDF Vector
```

Then:

```
Cosine Similarity
      ↓
Similarity Score
```

---

# 46. Cosine Similarity Example

```
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(
    X
)

print(similarity)
```

The result is a similarity matrix.

Values closer to:

```
1
```

indicate stronger similarity in vector direction.

Values closer to:

```
0
```

indicate little similarity.

---

# 47. Document Similarity Example

Documents:

```
D1 = "Python machine learning"

D2 = "Python machine learning"

D3 = "football cricket"
```

TF-IDF converts them into vectors.

Then cosine similarity can determine that:

```
D1 ≈ D2
```

while:

```
D1 ≠ D3
```

---

# 48. TF-IDF for Search

A simple search system can work like:

```
Documents
   ↓
TF-IDF
   ↓
Document Vectors
```

User Query:

```
"machine learning"

   ↓
TF-IDF
   ↓
Query Vector

   ↓
Cosine Similarity

   ↓
Rank Documents
```

---

# 49. TF-IDF for Keyword Extraction

TF-IDF scores can help identify words that are particularly important to a document.

High score:

```
More important/specific term
```

Low score:

```
Common or less informative term
```

However, keyword extraction quality depends on preprocessing and the dataset.

---

# 50. Advantages of TF-IDF

* Simple
* Fast
* Easy to understand
* Strong baseline for text classification
* Works well with many traditional ML models
* Handles large vocabularies reasonably well using sparse matrices
* Reduces the impact of extremely common words
* Easy to implement with Scikit-Learn

---

# 51. Limitations of TF-IDF

TF-IDF does not inherently understand:

* Word meaning
* Context
* Semantic relationships
* Word order
* Synonyms
* Polysemy

For example:

```
"car"
```

and:

```
"automobile"
```

are treated as different terms.

TF-IDF does not automatically know they have similar meanings.

---

# 52. TF-IDF vs Word Embeddings

TF-IDF:

```
Statistical representation
↓
Word importance
```

Word Embeddings:

```
Semantic representation
↓
Meaning / relationships
```

Examples of embeddings:

```
Word2Vec
GloVe
FastText
Transformer embeddings
```

---

# 53. TF-IDF vs Word2Vec

## TF-IDF

Represents:

```
Document → Vector
```

Focus:

```
Importance of words in documents
```

---

## Word2Vec

Represents:

```
Word → Vector
```

Focus:

```
Semantic relationships between words
```

---

# 54. Important NLP Pipeline

A traditional NLP classification pipeline can be:

```
Raw Text
   ↓
Cleaning
   ↓
Tokenization
   ↓
Normalization
   ↓
Train/Test Split
   ↓
TF-IDF
   ↓
Machine Learning
   ↓
Evaluation
```

---

# 55. Important Data Leakage Rule

Never do:

```
Complete Dataset
     ↓
TF-IDF fit_transform()
     ↓
Train/Test Split
```

Instead:

```
Complete Dataset
     ↓
Train/Test Split
     ↓
Training Text
     ↓
fit_transform()

Test Text
     ↓
transform()
```

Remember:

> Fit only on training data.

---

# 56. TF-IDF Quick Cheat Sheet

Formula:

```
TF-IDF = TF × IDF
```

TF:

```
TF =
Term Count in Document
----------------------
Total Terms in Document
```

IDF:

```
IDF =
log(
    Number of Documents
    -------------------
    Documents Containing Term
)
```

Scikit-Learn:

```
from sklearn.feature_extraction.text import TfidfVectorizer
```

Create:

```
vectorizer = TfidfVectorizer()
```

Train:

```
X_train = vectorizer.fit_transform(
    X_train_text
)
```

Test:

```
X_test = vectorizer.transform(
    X_test_text
)
```

Vocabulary:

```
vectorizer.get_feature_names_out()
```

---

# 57. Most Important Things to Remember

```
TF
↓
Frequency inside a document

IDF
↓
Rarity across documents

TF-IDF
↓
Frequency × Rarity

fit_transform()
↓
Training data

transform()
↓
Test/New data

TfidfVectorizer
↓
Scikit-Learn implementation

Sparse Matrix
↓
Efficient representation of mostly-zero text vectors
```

---

# 58. Final Mental Model

Think of TF-IDF like this:

```
"How important is this word
 for THIS document,
 compared with ALL documents?"

Frequent in current document
          +
Rare across corpus
          ↓
   HIGH TF-IDF

Rare in current document
          OR
Common across corpus
          ↓
    LOW TF-IDF
```

---

# 🚀 TF-IDF → Machine Learning

The complete practical flow:

```
Text Dataset
     ↓
Clean Text
     ↓
Train/Test Split
     ↓
TfidfVectorizer
     ↓
fit_transform(X_train)
     ↓
transform(X_test)
     ↓
ML Model
     ↓
Predictions
     ↓
Evaluation
```

This is one of the most important traditional NLP pipelines to understand before moving toward word embeddings and Transformer-based NLP.
