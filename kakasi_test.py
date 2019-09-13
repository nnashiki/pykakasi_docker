import argparse

from pykakasi import kakasi

if __name__ == '__main__':
    kakasi = kakasi()
    kakasi.setMode('H', 'a')  # Hiragana to ascii, default: no conversion
    kakasi.setMode('K', 'a')  # Katakana to ascii, default: no conversion
    kakasi.setMode('J', 'a')  # Japanese to ascii, default: no conversion
    conv = kakasi.getConverter()

    parser = argparse.ArgumentParser()
    parser.add_argument('args', type=str, nargs='*')
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()

    for text in args.args:
        if args.verbose:
            print(text)
        print(conv.do(text))
