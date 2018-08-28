#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "trie.h"

// Esta linea permite usar MAX_LENGTH como una constante en el programa
// Uso 101 para considerar el caracter que indica el fin de un string
#define MAX_LENGTH 101

typedef struct TrieNode
{
	char c;
	struct TrieNode *parent;
	struct TrieNode **children;
	bool is_word;
	int freq;
} TrieNode;


// is_word nos marca el fin de la frase o palabra
// el trienode recibe el caracter que va a guardar y el nodo padre
// solicitamos memoria para el nodo y su hijo
struct TrieNode *create_trienode(char c, struct TrieNode *parent)
{
	struct TrieNode *node = malloc(sizeof(struct TrieNode));
	node->c = c;
	node->parent = parent;
	node->children = malloc(26*sizeof(struct TrieNode));
	node->is_word=false;
	node->freq=NULL;
	return node;
}

//destroy_trienode(struct TrieNode *node);
int main(int argc, char *argv[])
{
	if (argc != 4)
	{
		printf("Modo de uso: ./solver [database.txt] [queries.txt] [output.txt]\n");
		return 0;
	}
	FILE *database = fopen(argv[1], "r");
	FILE *queries  = fopen(argv[2], "r");
	FILE *output   = fopen(argv[3], "w");

	if (!database || !queries || !output)
	{
		printf("¡Error abriendo los archivos!");
		return 2;
	}





	//// Ejemplo de lectura de strings:

	// Leo el numero de entradas en la base de datos
	int n;
	fscanf(database, "%d", &n);

	// http://kposkaitis.net/blog/2013/03/09/prefix-tree-implementation-in-c/
	//struct TrieNode *create_tree(){
	// creamos el trie
	struct TrieNode *root = create_trienode(' ', NULL);
	struct TrieNode *ptr = root;
	int character;
	int converted;
	int buffer;

	// Para cada entrada:
	for (int i = 0; i < n; i++)
	{
		// Obtengo la frecuencia y el largo
		int freq, length;
		// Ojo que incluyo un espacio en el formato para que no lo considere como parte del string
		fscanf(database, "%d %d ", &freq, &length);
		printf("freq = %d, length = %d\n", freq, length);

		// Leo el string aprovechando que se el largo maximo
		char chars[MAX_LENGTH];
		fgets(chars, MAX_LENGTH, database); // lee el caracter hasta que encuentra un salto de linea
		printf("%s\n", chars);
		for (int j = 0; j <  length; j++) {
			//printf("%c ", chars[j]);
			character = chars[j];

			// si el caracter es una letra o espacio lo va a guardar
			if(isalpha(character) || character == ' ')
			{
					converted = character - 97;
					if(ptr->children[converted] == NULL)
					{
							ptr->children[converted] = create_trienode(character, ptr);
					}
					// ahora el puntero va a estar en el hijo
					ptr = ptr->children[converted];
					printf("este es el valor guardado: %c\n", ptr -> c);
			}

			if(ptr != root && (!isalpha(character) || buffer == "\n"))
			{
					ptr->is_word = true;
					ptr = root;
			}

			character = buffer;
			buffer = chars[j + 1];

		}
		// cuando se acabe la frase guardamos su frecuencia
		ptr->freq = freq;
		printf("la frecuencia de la palabra es: %d\n", ptr -> freq);
		printf("\n");
	}

	fclose(database);
	fclose(queries);
	fclose(output);
	return 0;
}

void destroy_trienode(struct TrieNode *node)
{
  int i;

  if(node==NULL)
  {
      return;
  }

  for(i=0; i<26; i++)
  {
      destroy_trienode(node->children[i]);
  }

  free(node->children);
  free(node);
  return;
}
