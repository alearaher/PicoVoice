from collections.abc import Sequence

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
        # If node ends at the end of the sequence, it's a full path
        if node.end == len(phoneme_sequence):
            return

        # Try every possible word starting from this node's end index
        for word, phonemes in word_to_phonemes.items():
            length = len(phonemes)
            next_chunk = phoneme_sequence[node.end:node.end + length]

            if next_chunk == phonemes:
                child = TreeNode(word, node.end, node.end + length)
                node.children.append(child)
                grow_tree(child)  # recursively grow from this child

    grow_tree(root)
    return root


def find_word_combos_with_pronunciation(phonemes: Sequence[str]) -> Sequence[Sequence[str]]:
    print("Finding words combinations...")
    result = []
    #Aproaching this through trees:

    





