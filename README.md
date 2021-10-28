# Abbreviation data

This repository provides labeled data for training abbreviation expansion
models, as described in:

Gorman, K., Kirov, C., Roark, B., and Sproat, R. In press. Structured
abbreviation in context. In *Findings of EMNLP*, to appear.

If you use this data in a publication, we would appreciate it if you cite this
paper.

## Annotation

Sentences were extracted from English Wikipedia articles, then filtered as
described in the paper. Annotators were then asked to introduce abbreviations to
the sentences.

## Organization

The data, with the original 80%/10%/10% split, can be found in the
[`data`](data/) directory. The data are text-format [Protocol
Buffers](https://developers.google.com/protocol-buffers) using the protocol
described in [`abbreviation.proto`](abbreviation.proto). To load this data
into Python, install the Protocol Buffers compiler `protoc`, then:

```bash
pip install -r requirements.txt
make
```

Then, see [`textproto.py`](textproto.py).

## Authors

This data was collected by [Kyle Gorman](mailto:kbg@google.com) with help from
the annotators and Brian Roark, Richard Sproat, Olivia Redfield, Catherine
Golner, and Katherine Wang.

## License

See [`LICENSE`](LICENSE).

## Contributing

See [`CONTRIBUTING`](CONTRIBUTING).

## Mandatory disclaimer

This is not an official Google product.
