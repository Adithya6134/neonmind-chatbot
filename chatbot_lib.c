#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// A simple C function to calculate string similarity (Levenshtein Distance)
int levenshtein(const char *s1, const char *s2) {
    int len1 = strlen(s1);
    int len2 = strlen(s2);
    int matrix[len1 + 1][len2 + 1];

    for (int i = 0; i <= len1; i++) matrix[i][0] = i;
    for (int j = 0; j <= len2; j++) matrix[0][j] = j;

    for (int i = 1; i <= len1; i++) {
        for (int j = 1; j <= len2; j++) {
            int cost = (s1[i - 1] == s2[j - 1]) ? 0 : 1;
            int delete_op = matrix[i - 1][j] + 1;
            int insert_op = matrix[i][j - 1] + 1;
            int sub_op = matrix[i - 1][j - 1] + cost;
            
            int min = delete_op;
            if (insert_op < min) min = insert_op;
            if (sub_op < min) min = sub_op;
            
            matrix[i][j] = min;
        }
    }
    return matrix[len1][len2];
}

// Wrapper to return a "similarity score" (0 to 100)
// Lower distance = Higher score
int get_similarity_score(const char *s1, const char *s2) {
    int dist = levenshtein(s1, s2);
    int max_len = strlen(s1) > strlen(s2) ? strlen(s1) : strlen(s2);
    if (max_len == 0) return 100;
    
    return (int)((1.0 - (double)dist / max_len) * 100);
}