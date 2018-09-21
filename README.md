# baby kangaroo

If you aren't good with big words, just run this script against your document, collect oneself, and
let this script do the drudgery.
## Getting Started

Clone this repo

### Prerequisites

Things you will need to sound smarter

```
import docx
import argparse
from enchant import Dict
from nltk.corpus import wordnet
```


## Running

Output file is a .docx placed in the same directory as your original with 'bk_' prefacing the file name.

```
usage: python3 babykangaroo.py [-h] docx_file

Sound smarter, immediately.

positional arguments:
  docx_file   Document to babykangaroo-ify

optional arguments:
  -h, --help  show this help message and exit

```

### Happy Thesaurusing