
import argparse

flower_map = {
    'A': 'Rose', 'B': 'Camellia', 'C': 'Magnolia', 'D': 'Poppy', 'E': 'Tulip',
    'F': 'Chrysanthemum', 'G': 'Hyacinth', 'H': 'Violet', 'I': 'Lavender', 'J': 'Heather',
    'K': 'Petunia', 'L': 'Gladiolus', 'M': 'Yarrow', 'N': 'Wisteria', 'O': 'Hibiscus',
    'P': 'Edelweiss', 'Q': 'Iris', 'R': 'Anemone', 'S': 'Kalmia', 'T': 'Zinnia',
    'U': 'Lotus', 'V': 'Oleander', 'W': 'Begonia', 'X': 'Foxglove', 'Y': 'Sunflower',
    'Z': 'Dahlia',
    'a': 'Jasmine', 'b': 'Freesia', 'c': 'Bluebell', 'd': 'Aconite', 'e': 'Orchid',
    'f': 'Azalea', 'g': 'Carnation', 'h': 'Ursinia', 'i': 'Gardenia', 'j': 'Snowdrop',
    'k': 'Marigold', 'l': 'Nerine', 'm': 'Aster', 'n': 'Xeranthemum', 'o': 'Peony',
    'p': 'Daisy', 'q': 'Buttercup', 'r': 'Primula', 's': 'Crocus', 't': 'Verbena',
    'u': 'Snapdragon', 'v': 'Cosmos', 'w': 'Delphinium', 'x': 'Fuchsia', 'y': 'Primrose',
    'z': 'Scabiosa',
    '0': 'Hydrangea', '1': 'Amaranth', '2': 'Clematis', '3': 'Pansy', '4': 'Daffodil',
    '5': 'Lilac', '6': 'Calla', '7': 'Phlox', '8': 'Geranium', '9': 'Amaryllis',
    '{': 'Canna', '}': 'Silene', '_': 'Thistle', '+': 'Lotuswort', '\\': 'Anthurium', "'": 'Viola',
    ' ': 'Cyclamen', ':': 'Ixora'
}

# invert
rev = {v.strip(): k for k, v in flower_map.items()}

def decode(bouquet_str):
    tokens = bouquet_str.split()
    seed = []
    missing = []
    for t in tokens:
        key = rev.get(t.strip())
        if key is None:
            missing.append(t)
            seed.append('?')
        else:
            seed.append(key)
    return ''.join(seed), missing

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--bouquet', '-b', help='paste bouquet string (flowers separated by spaces)')
    p.add_argument('--file', '-f', help='file containing bouquet string')
    args = p.parse_args()

    if not (args.bouquet or args.file):
        p.print_help(); return

    s = args.bouquet
    if args.file:
        with open(args.file, 'r') as fh:
            s = fh.read().strip()

    seed, missing = decode(s)
    print("decoded seed / message:\n", seed)
    if missing:
        print("\nMissing / unknown flower tokens (could be parsing mismatch):")
        print(missing)
    else:
        print("\nNo missing tokens — flag should be visible above (format HCS{...}).")

if __name__ == '__main__':
    main()
