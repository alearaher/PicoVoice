#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_WORDS 10000
#define WORD_LEN 50

typedef struct {
    char word[WORD_LEN];
    int freq;
} Word_freq;

// Check if the word already exists in the table
bool word_in_table(Word_freq arr[], int len, const char *wrd) {
    for (int i = 0; i < len; i++) {
        if (strcmp(arr[i].word, wrd) == 0) {
            return true;
        }
    }
    return false;
}

void edit_word_arr(Word_freq arr[], int len, const char *wrd) {
    for (int i = 0; i < len; i++) {
        if (strcmp(arr[i].word, wrd) == 0) {
            arr[i].freq++;
            return;
        }
    }
}

void swap(Word_freq *a, Word_freq *b) {
    Word_freq temp = *a;
    *a = *b;
    *b = temp;
}

// Find and print the n most frequent words
void find_frequent_words(const char *path, int n) {
    FILE *f = fopen(path, "r");
    if (f == NULL) {
        perror("Error opening file");
        return;
    }

    Word_freq freq_table[MAX_WORDS];
    int word_count = 0;
    char buffer[256];
    const char *delim = " \t\n.,!?;:\"()[]{}";

    while (fgets(buffer, sizeof(buffer), f)) {
        char *token = strtok(buffer, delim);
        while (token != NULL) {
            if (!word_in_table(freq_table, word_count, token)) {
                if (word_count < MAX_WORDS) {
                    strncpy(freq_table[word_count].word, token, WORD_LEN - 1);
                    freq_table[word_count].word[WORD_LEN - 1] = '\0';
                    freq_table[word_count].freq = 1;
                    word_count++;
                }
            } else {
                edit_word_arr(freq_table, word_count, token);
            }

            token = strtok(NULL, delim);
        }
    }
    fclose(f);

    // bubble sort by freq
    for (int i = 0; i < word_count - 1; i++) {
        for (int j = i + 1; j < word_count; j++) {
            if (freq_table[j].freq > freq_table[i].freq) {
                swap(&freq_table[i], &freq_table[j]);
            }
        }
    }

    printf("\nTop %d most frequent word(s):\n", n);
    for (int i = 0; i < n && i < word_count; i++) {
        printf("%-20s : %d\n", freq_table[i].word, freq_table[i].freq);
    }
}

// Main function
int main() {
    const char *filename = "input.txt";
    int top_n;

    printf("Enter how many top frequent words to show: ");
    scanf("%d", &top_n);

    find_frequent_words(filename, top_n);

    return 0;
}
