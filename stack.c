#include "stack.h"
#include <stdlib.h>
#include <stdio.h>


Stack *stack_init()
{
  /* Aqui agrega tu código */
  Stack* stk = malloc(sizeof(Stack));

  // Stack vacío
  stk -> x = 0;
  stk -> y = 0;
  stk -> count = 0;
  stk -> first = NULL;
  stk -> last = NULL;

  // Retorna el puntero
  return stk;
}

Node* node_init(int value)
{
  // Creo el nodo
  Node* node = malloc(sizeof(Node));

  // Le agrego el valor y le pongo next = NULL
  node -> color = value;
  node -> next = NULL;

  // Retorno el nodo
  return node;
}

void push(Stack* stack, int color)
{
  /* Aqui agrega tu código */
  // Creo el nodo a agregar
  Node* node = node_init(color);

  // Si la lista esta vacia
  if (stack -> count == 0)
  {
    // Hago que sea el primer nodo
    stack -> first = node;
  }
  // Sino,
  else
  {
    // Hago que sea el siguiente del ultimo
    stack -> last -> next = node;
  }

  // Ahora este nodo es el ultimo
  stack -> last = node;
  stack -> last -> next = NULL;

  // Agrego 1 a la cuenta
  stack -> count++;
}

/*int pop(Stack* stack){
  Node* tmp = stack -> first;
  while (tmp -> next != NULL){
    printf("%d", tmp -> color);
    tmp = tmp -> next;
  }
  printf("%s", "-----");
  return 0;
}*/


/*int linkedlist_delete(Stack* stack)
{
  // Variable a retornar
  int value;

  // Si me piden eliminar el primero
  if (stack -> count == 1)
  {
    // Obtengo el valor a retornar
    value = stack -> first -> color;

    // Guardo el primero
    Node* first = stack -> first;

    // Elimino el anterior
    free(first);
  }else if (stack -> count == 0){
    value = 7;
  }
  // En cuelquier otro caso
  else
  {
    // Busco el nodo anterior al que voy a eliminar
    Node* last = list -> first;
    for (int i = 1; i < position; i++)
    {
      last = last -> next;
    }

    // Obtengo el nodo a eliminar
    Node* actual = last -> next;

    // Obtengo el valor a retornar
    value = actual -> value;

    // Cambio el link del anterior al siguiente
    last -> next = actual -> next;

    // Libero la memoria del nodo eliminado
    free(actual);

    // Si elimine el ultimo, actualizo cual es la posicion final de la lista
    if (position == list -> count - 1)
    {
      list -> last = last;
    }
  }

  // Disminullo en 1 el count
  list -> count--;

  // retorno el valor eliminado
  return value;
}*/


/*void destroy(Stack *stack)
{
  // Libero todos los nodos del stack
  //recursive_destroy(stack-> first);

  // Libero el stack
  free(stack);
}*/


/* A continuación puedes crear cualquier función adicional que ayude en la
  implementación de tu programa */
/*void recursive_destroy(Node* node)
{
  // Si tiene sucesor, llama recursivamente
  if (node -> next)
  {
    recursive_destroy(node -> next);
  }

  // Libero al nodo
  free(node);
}*/

void printList(Stack *stack) {
  int i = 0;
  Node ptr;
  stack -> first = &ptr;
  while(i < stack -> count) {
    printf("%d ",ptr.color);
    ptr = *ptr.next;
    i++;
  }
}

   //printf(" [null]\n");
