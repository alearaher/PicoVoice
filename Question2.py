from collections.abc import Sequence

#usiing basic dictionary for now
word_to_phonemes = {
        "THEIR": ["DH", "EH", "R"],
        "THERE": ["DH", "EH", "R"],
    }


#creating tree data struct
class TreeNode:
    def __init__(self, word=None, start=0, end=0):
        self.word = word 
        self.start = start  
        self.end = end 
        self.children = []  


def build_tree(phoneme_sequence, word_to_phonemes):
    root = TreeNode()

    def grow_tree(node):
        # If we’ve reached the end of the sequence, stop growing
        if node.end == len(phoneme_sequence):
            return

        # Try matching words that start from current position
        for word, phonemes in word_to_phonemes.items():
            length = len(phonemes)
            chunk = phoneme_sequence[node.end:node.end + length]

            if chunk == phonemes:
                child = TreeNode(word, node.end, node.end + length)
                node.children.append(child)
                grow_tree(child)

    grow_tree(root)
    return root


def collect_paths(node, current_path, all_paths, phoneme_sequence_length):
    if node.word:
        current_path.append(node.word)

    # Valid path: no children, and used entire sequence
    if not node.children and node.end == phoneme_sequence_length:
        all_paths.append(current_path[:])
    else:
        for child in node.children:
            collect_paths(child, current_path, all_paths, phoneme_sequence_length)

    if node.word:
        current_path.pop()


 


def find_word_combos_with_pronunciation(phonemes: Sequence[str]) -> Sequence[Sequence[str]]:
    print("Finding words combinations...")
    root = build_tree(phonemes, word_to_phonemes)
    results = []
    #Aproaching this through trees:   
    collect_paths(root, [], results, len(phonemes))
    return results



phoneme_sequence = ["DH", "EH", "R", "DH", "EH", "R"]
combinations = find_word_combos_with_pronunciation(phoneme_sequence)

for combo in combinations:
    print(combo)




