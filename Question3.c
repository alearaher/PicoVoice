#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h> 

#define WORD_LEN 50

typedef struct {
    char* word[WORD_LEN];
    int freq;
 }Word_freq;


// Check if the word already exists in the table
bool word_in_table(Word_freq arr[], const char *wrd){
    int ln =  sizeof arr/sizeof arr[0];
    for (int i = 0; i < ln ; i++){
        if (strcmp(arr[i].word, wrd) == 0){
            return true;
        }
    }
    return false;
}

void edit_word_arr(Word_freq arr[], const char *wrd){
    int ln =  sizeof arr/sizeof arr[0];
        for (int i = 0; i < ln ; i++){
            if (strcmp(arr[i].word, wrd) == 0){
                arr[i].freq++;
            }
        }

}

//First we must import and read the file
char **find_frequent_words(const char *path, int n) {
    //using path to get .txt file

    FILE *f = fopen(path, "r");

    //check if valid file ommited for now

    const char delim[] = "\t\n";
    Word_freq freq_table[10000];

    const unsigned MAX_LENGTH = 256;
    char buffer[MAX_LENGTH];



 


    while (fgets(buffer, MAX_LENGTH, f)){

        //iterate through words per line to read them
        char *token = strtok(buffer, delim);
        int indx = 0;
        Word_freq top_word = (Word_freq){" ", 0};
        //first, check if word exists already in table
        while(token != NULL){
            if(!word_in_table(freq_table, token)){
                //if its not on the table, add it and intialize it with count of 1
                freq_table[indx] = (Word_freq) {token, 1};
            }else{
                //using linear search, needs optimzation
                edit_word_arr(freq_table, token);

                //check if this is bigger than the current most frequent word
                if(freq_table[indx].freq > top_word.freq){
                    top_word = (Word_freq){freq_table[indx].word, freq_table[indx].freq};
                }

            }
            indx++;
        }

         fclose(f);

         printf("\n Word with most frequency: ");
        printf("%-20s : %d\n", top_word.word,top_word.freq);

    }

}