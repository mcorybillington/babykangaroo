# babykangaroo

If you aren't good with big words, just run this script against your document, sit back, and let babykangaroo do the hard work.

babykangaroo-ified:

>If you aren't respectable with self-aggrandizing words, precisely outpouring this handwriting against your document, baby-sit back, and countenance babykangaroo practice the intemperately work.
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
usage: babykangaroo.py [-h] [-c] docx_file

Sound smarter, immediately.

positional arguments:
  docx_file        Document to babykangaroo-ify

optional arguments:
  -h, --help       show this help message and exit
  -c, --corporate  Corporate syntax
```

Corporate syntax adds common corporate lingo/buzzwords to your docx file. It is still a bit shaky, but I'm trying to improve it.

### Happy Thesaurusing