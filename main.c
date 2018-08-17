#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "stack.h"
#include "stack.c"
#include "string.h"

typedef struct Point {
  struct stack* prt;
}Point;

int pop(Stack* stack);
// void pop_recursive(Stack* stack, int k, FILE *output_file);
//int main(int argc, char *argv[])
int main()

{

	/*if (argc != 2)
	{
		printf("Modo de uso: ./solver test.txt\n");
		return 0;
	}*/

	/* Abrimos el archivo input en modo de lectura */
	//FILE *input_file = fopen(argv[1], "r");
  FILE *input_file = fopen("../../tests/test_02.txt", "r");

	/* Abrimos el archivo output en modo de escritura */
	FILE *output_file = fopen("output.txt", "w");

	/* Revisa que el archivo fue abierto correctamente */
	if (!input_file)
	{
		printf("¡El archivo %s no existe!\n", "../tests/test_00.txt");
		return 2;
	}

	/* Definimos y asignamos las constantes del problema */
	int n; int m; int l; int i; int k; int t; int z; int bola_sale;
	fscanf(input_file, "%d %d %d", &n, &m, &l);

  // creo la matriz de nxm y le asigno memoria
  /*Point *(points[n][m]);
  for (int t = 0; t < n; t++) {
    for (int z = 0; z < m; z++){
      points[t][z] = (Point *)malloc(sizeof(Point));
      points[t][z] -> prt = stack_init();
    }
  }*/

  // confeccionamos la matriz nxm, solictamos memoria e iniciamos los stacks
  Point*** points = malloc(sizeof(Point**)*n);
  for (int t = 0; t < n; t++){
    points[t] = malloc(sizeof(Point*)*m);
    for (int z = 0; z < m; z++){
      points[t][z] = malloc(sizeof(Point));
      points[t][z] -> prt = stack_init();
    }
  }

	for (i = 0; i < l; i++) // recorremos las lineas del texto
	{
		/* Definimos las variables del problema */
		int o; int r; int c; int k;

		/* Leemos cada linea del archivo */
		fscanf(input_file, "%d %d %d %d", &o, &r, &c, &k);
    printf("%d %d %d %d\n", o, r, c, k);

		//////////////// Aqui agrega tu código ///////////////////


    if(o == 0){
      push(points[r][c] -> prt, k);
      printf("Primera bola en posición %d %d de color %d\n", r, c, k);
      printf("Ultima bola en posición %d %d de color %d\n", r, c, k);
      printf("Numero de bolas del stack %d\n", points[r][c] -> prt -> count);
      printf("------------------------------\n");
    }else{
      if (points[r][c] -> prt -> count == 0){
        //fprintf(output_file, "%s en posicion %d %d\n", "vacio", r, c);
        fprintf(output_file, "%s\n", "vacio");
      }else{
        // hay una o más bolas en el satck
        bola_sale = pop(points[r][c] -> prt); // sscamos una
        //fprintf(output_file, "%d en posicion %d %d\n", bola_sale, r, c);
        fprintf(output_file, "%d\n", bola_sale);
        if (points[r][c] -> prt -> count == 0){
          if(bola_sale != k){
            fprintf(output_file, "%s\n", "vacio");
          }
        }else{
          if (bola_sale != k){
            while(points[r][c] -> prt -> count >= 1){
              bola_sale = pop(points[r][c] -> prt);
              fprintf(output_file, "%d\n", bola_sale);
              if(bola_sale == k){
                break;
              }
            }
            if(bola_sale != k){
              fprintf(output_file, "%s\n", "vacio");
            }
          }
        }
      }
    }
      printf("Se sacó bola %d de la posición %d %d\n", bola_sale, r, c);
      printf("Numero de bolas del stack %d\n", points[r][c] -> prt -> count);
  }

  // liberamos la memoria de los stack
  for (t = 0; t < n; t++){
    for (z = 0; z < m; z++){
      destroy(points[t][z] -> prt);
      free(points[t][z]);
    }
  }


  // liberamos la memoria de la matriz
  for (int t = 0; t < n; t++){
    free(points[t]);
  }
  free(points);

	/* Cerramos los archivos correctamente */
	fclose(input_file);
	fclose(output_file);


	///////////////// Recuerda que antes de acabar tu programa debes liberar toda la memoria reservada ///////////////////


	/* Esta linea indica que el programa termino sin errores */
	return 0;
}


void destroy(Stack *stack){
  free(stack);
}
/*void destroy(Stack *stack)
{
  int i = 0;
  Node *tmp = node_init(7);
  while(i < stack -> count - 1 ){
    tmp = stack -> first;
    tmp -> next = stack -> first -> next;
    free(stack -> first);
    tmp = tmp -> next;
    i++;
  }
  //free(stack -> last);
  free(tmp);
  free(stack);
}*/

int pop(Stack* stack){
  int value;
  Node * temp = node_init(7);
  temp = stack -> first;
  Node * previousToTail = node_init(7);
  // si el stack esta vacío
  if (stack -> last == NULL){
    free(temp);
    return 7;
  }
  else {
    if (temp == stack -> last) {
          value = temp -> color;
          free(stack -> last);
          //free(temp);
    } else {
          previousToTail = temp;
          while (previousToTail -> next != stack -> last){
               previousToTail = previousToTail -> next;
          }
          value = previousToTail -> next -> color;
          stack -> last = previousToTail;
          free(stack -> last -> next);
          //free(previousToTail);
    }
    stack -> count--;
    //free(temp);
    return value;
  }
}

/*void pop_recursive(Stack * stack, int k, FILE *output_file){
  int bola_sale;
  bola_sale = pop(stack);
  if (stack -> count == 0){
    if (bola_sale == k){
      fprintf(output_file, "%d\n", k);
    }else{
      fprintf(output_file, "%s\n", "vacio");
    }
  }
  else{
    if (bola_sale == k){
      fprintf(output_file, "%d\n", k);
    }else{
      pop_recursive(stack, k, output_file);
    }
  }
}*/
