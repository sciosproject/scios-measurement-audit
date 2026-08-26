# Sources — and how to verify them without us shipping them

None of the five papers audited is redistributed here, and neither is our
extracted text of them. They are not ours to give away.

That is not a gap in the evidence. It is a stronger form of it: **you do not have
to trust our copy.** Fetch your own from the URL below, confirm its SHA-256 matches
ours, run our extractor on it, and confirm the extraction matches too. If both
match, you are reading the exact bytes we read.

```
python pdftext.py <your-copy.pdf> out.txt
```

| Paper | Source | PDF SHA-256 | Extracted-text SHA-256 |
|---|---|---|---|
| BLEU (Papineni et al., 2002) | <https://aclanthology.org/P02-1040.pdf> | `c0ee6aedcb674da2…` | `7e9282f809127dd2adf9b31d8cfa5f2e01b778b972c056972eddf2d5ada91a5b` |
| Microsoft COCO (Lin et al., 2014) | <https://arxiv.org/abs/1405.0312> | `6aae2fd953d0e833…` | `1fd28cb1964eabcccfa4b5ea088a6b2bc4908156ea4f45558fe817065cac9e6c` |
| ILSVRC (Russakovsky et al., 2015) | <https://arxiv.org/abs/1409.0575> | `b8643541df1b287c…` | `1e51f6a2f5df23a4e269ab55edc036114315c648f48f1570fd199752d2584027` |
| PASCAL VOC (Everingham et al., 2010) | <https://link.springer.com/article/10.1007/s11263-009-0275-4> | `bda24d6d51d58815…` | `0be4973f1cf93dc9ce9659ed20a723aba5f337ef4f68cf314a88152555127054` |
| Cityscapes (Cordts et al., 2016) | <https://arxiv.org/abs/1604.01685> | `56fab90a6cf66d7f…` | `97317a9281170b60030bd99d82da9ab18f5caf33caea8fec65d236aef89b24a4` |

The extractor itself is in this repository (`pdftext.py`), with its own
hash recorded in `MANIFEST.json`. A different extractor will produce different
bytes and a different hash; that is expected, and `quotecheck.py` is tolerant of
the four ways we have seen extraction mangle text (ligatures, per-character
spacing, line-break hyphenation, and decimal points rendered as colons).
