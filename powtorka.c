#include <stdio.h>
#include <stdlib.h>

struct element
{
    int i;
    struct element * next;
};

void wyczysc(struct element * Lista)
{
    struct element * wsk=Lista->next;
    struct element * wsk2=Lista;
    Lista=wsk;
    while(Lista!=NULL)
    {
        Lista=Lista->next;
        free(wsk);
        wsk=Lista;
    }
    wsk2->next=NULL;
}

void wyswietlListeZGlowa(struct element*Lista)
{
    struct element*temp=Lista->next;
    if(temp==NULL)
    {
        printf("Lista jest pusta\n");
    }
    while(temp!=NULL)
    {
        printf("%d\n",temp->i);
        temp=temp->next;
    }
    printf("----\n");
}


int main()
{
    struct element* l1=malloc(sizeof(struct element));
    l1->next=malloc(sizeof(struct element));
    l1->next->i=5;
    l1->next->next=malloc(sizeof(struct element));
    l1->next->next->i=7;
    l1->next->next->next=malloc(sizeof(struct element));
    l1->next->next->next->i=-2;
    l1->next->next->next->next=NULL;
    wyswietlListeZGlowa(l1);
    wyczysc(l1);
    wyswietlListeZGlowa(l1);
    return 0;
}
//////////////////////////////////////////////////////////////////////
#include <stdio.h>
#include <stdlib.h>

struct element
{
    int i;
    struct element * next;
};

struct element * utworz()
{
    return NULL;
};

struct element* wyczysc(struct element *Lista)
{
    struct element * wsk=Lista;
    while(Lista!=NULL)
    {
        Lista=Lista->next;
        free(wsk);
        wsk=Lista;
    }
    return NULL;
}

void wyswietlListeBezGlowy(struct element*Lista)
{
    struct element*temp=Lista;
    if(temp==NULL)
    {
        printf("Lista jest pusta\n");
    }
    while(temp!=NULL)
    {
        printf("%d\n",temp->i);
        temp=temp->next;
    }
    printf("----\n");
}

int main()
{
    struct element* example = utworz();
    example=wyczysc(example);
    wyswietlListeBezGlowy(example);
    struct element * lista1 = malloc(sizeof(struct element));
    lista1->i=7;
    lista1->next=malloc(sizeof(struct element));
    lista1->next->i=-3;
    lista1->next->next=malloc(sizeof(struct element));
    lista1->next->next->i=8;
    lista1->next->next->next=NULL;
    wyswietlListeBezGlowy(lista1);
    lista1=wyczysc(lista1);
    wyswietlListeBezGlowy(lista1);
    return 0;
}
//////////////////////////////////////////////////////////////////////
#include <stdio.h>
#include <stdlib.h>

struct element
{
    int i;
    struct element * next;
};

void dodaj(struct element**Lista, int a)
{
    struct element * wsk = malloc(sizeof(struct element));
    wsk->i=a;
    wsk->next=*Lista;
    *Lista= wsk;
};

struct element * utworz()
{
    return NULL;
};

int main()
{
    struct element* l1 = utworz();
    dodaj(&l1,2);
    dodaj(&l1,4);
    dodaj(&l1,7);
    dodaj(&l1,-2);
    struct element * wsk = l1;
    while(wsk!=NULL)
    {
        printf("%d\n",wsk->i);
        wsk=wsk->next;
    }
    return 0;
}
//////////////////////////////////////////////////////////////////////
