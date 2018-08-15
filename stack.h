#pragma once


typedef struct stack Stack; //NOmbre simple de la lista ligada Stack

typedef struct node Node; //Nombre simple para node


struct node
{
  /* Aqui agrega tu código */
  int color;
  struct node *next;
};

struct stack
{
  /* Aqui agrega tu código */
  /** Primer nodo */
  Node* first;
  /** Ultimo nodo */
  Node* last;
  /** Cantidad de nodos */
  int count;
  int x;
  int y;
};


Stack *stack_init();

void push(Stack* stack, int color);

int pop(Stack* stack);

void destroy(Stack *stack);
