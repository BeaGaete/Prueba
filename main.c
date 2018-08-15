#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "stack.h"
#include "stack.c"
#include "string.h"

typedef struct Point {
  int x;
  int y;
  struct stack* prt;
}Point;

int pop(Stack* stack);

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
  FILE *input_file = fopen("../../tests/test_01.txt", "r");

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

  Point*** points = malloc(sizeof(Point**)*n);
  for (int t = 0; t < n; t++){
    points[t] = malloc(sizeof(Point*)*m);
    for (int z = 0; z < m; z++){
      points[t][z] = malloc(sizeof(Point));
      points[t][z] -> prt = stack_init();
    }
  }




  // declaro un areglo de colores
  //char *colores[30] = {"verde", "rojo", "azul", "amarillo", "morado", "vacio"};
  // hacemos la matriz

	for (i = 0; i < l; i++) // recorremos las lineas del texto
	{
		/* Definimos las variables del problema */
		int o; int r; int c; int k;

		/* Leemos cada linea del archivo */
		fscanf(input_file, "%d %d %d %d", &o, &r, &c, &k);
    printf("%d %d %d %d\n", o, r, c, k);

		//////////////// Aqui agrega tu código ///////////////////
    /*Point *(points[n][m]);
    if (points[r][c] -> stk == NULL){
      points[r][c] = (Point *)malloc(sizeof(Point));
      points[r][c] -> stk = stack_init();
      if(o == 0){
        push(points[r][c] -> stk, k);
        printf("Primera bola en posicion %d %d de color %d\n", r, c, points[r][c] -> stk -> first -> color);
        printf("Ultima bola en posicion %d %d de color %d\n", r, c, points[r][c] -> stk -> last -> color);
        printf("Numero de bolas del stack %d\n", points[r][c] -> stk -> count);
      }else{
        //pop(record[r][c]);
        printf("todavía no implementado\n");
      }
    }else{
      if(o == 0){
        push(points[r][c] -> stk, k);
        printf("Primera bola en posicion %d %d de color %d\n", r, c, points[r][c] -> stk -> first -> color);
        printf("Ultima bola en posicion %d %d de color %d\n", r, c, points[r][c] -> stk -> last -> color);
        printf("Numero de bolas del stack %d\n", points[r][c] -> stk -> count);
      }else{
        //pop(record[r][c]);
        printf("todavía no implementado\n");
      }
    }
    free(points[r][c]);*/


    if(o == 0){
      //printf("linea %d\n", i + 1);
      push(points[r][c] -> prt, k);
      //push(points[r][c] -> prt, 6);
      printf("Primera bola en posición %d %d de color %d\n", r, c, points[r][c] -> prt -> first -> color);
      printf("Ultima bola en posición %d %d de color %d\n", r, c, points[r][c] -> prt -> last -> color);
      printf("Numero de bolas del stack %d\n", points[r][c] -> prt -> count);
      printf("------------------------------\n");
      /*Node * tmp = points[r][c] -> prt -> first;
      while (tmp != NULL) {
          printf("%d\n", tmp->color);
          tmp = tmp->next;
      }
      free(tmp);
      printf("------------------------------\n");*/
    }else{
      //printf("linea %d\n", i + 1);
      if (points[r][c] -> prt -> count > 0){
        printf("se debería sacar una bola\n");
        bola_sale = pop(points[r][c] -> prt);
        printf("Se sacó bola %d de la posición %d %d\n", bola_sale, r, c);
        printf("Numero de bolas del stack %d\n", points[r][c] -> prt -> count);
      }
    }

    /*struct stack *record[t][z];
    for (t = 0; t < n; t++){
      for (z = 0; z < m; z++){
        if(t == r && z == c){
          if(o == 0){
            points[t][z] -> x = r;
            points[t][z] -> y = c;

            push(points[t][z], k);
            printf("Primera bola en posicion %d %d de color %d\n", r, c, points[t][z] -> first -> color);
            printf("Ultima bola en posicion %d %d de color %d\n", r, c, points[t][z] -> last -> color);
            printf("Numero de bolas del stack %d\n", points[t][z] -> count);
            if (A[t][z] == 0){
              struct stack *p = stack_init();

              record[t][z] = p;
              push(record[t][z], k);
              printf("Primera bola en posicion %d %d de color %d\n", r, c, record[t][z] -> first -> color);
              printf("Ultima bola en posicion %d %d de color %d\n", r, c, record[t][z] -> last -> color);
              printf("Numero de bolas del stack %d\n", record[t][z] -> count);
              A[t][z] = 1;
            }else{
              push(record[t][z], k);
              printf("Primera bola en posicion %d %d de color %d\n", r, c, record[t][z] -> first -> color);
              printf("Ultima bola en posicion %d %d de color %d\n", r, c, record[t][z] -> last -> color);
              printf("Numero de bolas del stack %d\n", record[t][z] -> count);
            }
          }else{
            //pop(record[r][c]);
            printf("todavía no implementado\n");
          }
        }
      }
    }*/
    //leer_matriz(A, n, m, r, c);
    //printf("%d\n", A[r][c] -> count);
    //push(A[r][c], k);
    // para ocupar menos memoria lo ponemos aquí
    /*if (o == 0){
      push(record[r][c], k);
      //push(record[k][j], k);
      //push(record[k][j], 6);
      printf("Primera bola en posicion %d %d de color %d\n", r, c, record[r][c] -> first -> color);
      printf("Ultima bola en posicion %d %d de color %d\n", r, c, record[r][c] -> last -> color);
      printf("Numero de bolas del stack %d\n", record[r][c] -> count);
    }else{
      //pop(record[r][c]);
      printf("todavía no implementado\n");
    }*/

    /*record[r][c] -> x = r;
    record[r][c] -> y = c;
    if (o == 0){
      // printf("bola???? %d\n", record[r][c] -> first -> color);

      //push(record[r][c], 2);
      //push(record[r][c], 6);
      printf("Primera bola en posicion %d %d de color %d\n", r, c, record[r][c] -> first -> color);
      printf("Ultima bola en posicion %d %d de color %d\n", r, c, record[r][c] -> first -> color);
      printf("Numero de bolas del stack %d\n", record[r][c] -> count);
      //printList(record[r][c]);
    }else{
      //printf("Se sacó una bola %d\n", pop(record[r][c] -> first, 1));

    }*/
    /*for (k = 0; k < m; k++){
      for (j = 0; j < m; j++){
        //record[i][j] = p;
        //record[i][j] -> x = i;
        //record[i][j] -> y = j;
        //printf("la i y la j %d %d\n", i, j);
        //printf("la r y la c %d %d\n", r, c);
        if (k == r && j == c){
          // printf("cuando hay match %d %d\n", k, j);
          if (o == 0){
            push(record[k][j], k);
            push(record[k][j], k);
            push(record[k][j], 6);
            printf("Primera bola en posicion %d %d de color %d\n", r, c, record[k][j] -> first -> color);
            printf("Ultima bola en posicion %d %d de color %d\n", r, c, record[k][j] -> last -> color);
            printf("Numero de bolas del stack %d\n", record[k][j] -> count);
          }else{
            printf("todavía no implementado\n");
          }
        }
      }
    }*/
  }

  // liberamos la memoria
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



int pop(Stack* stack){
  int value;
  Node * temp = stack -> first;
  Node * previousToTail;
  if (stack -> last == NULL){
    free(temp);
    return 7;
  }
  else {
    if (temp == stack -> last) {
          value = temp -> color;
          free(stack -> last);
    } else {
          previousToTail = temp;
          while (previousToTail -> next != stack -> last){
               previousToTail = previousToTail -> next;
          }
          value = previousToTail -> next -> color;
          stack -> last = previousToTail;
          free(stack -> last -> next);
    }
    stack -> count--;
    return value;
  }
}
