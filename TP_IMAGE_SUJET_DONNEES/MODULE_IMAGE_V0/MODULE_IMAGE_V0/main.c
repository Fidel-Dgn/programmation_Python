#include <stdio.h>
#include <stdlib.h>

#include "ferrane_module_image.h"

/* AUTEUR : ISABELLE FERRANE                       */
/* DATE CREATION : 11/10/2018                      */
/*-------------------------------------------------*/

/* PROGRAMME DE TEST de FERRANE_MODULE_IMAGE */

int main(void)
{
	/* séquence de test des fonction de FERRANE_MODULE_IMAGE */
	printf("DEBUT DE TEST MODULE \n");

	test_prog();
	
	printf("DEBUT DE TEST MODULE \n");
	
	return EXIT_SUCCESS;   /*-- valeur de retour = succès exécution défini dans stdlib.h */
	
}


#include <stdio.h>
#include <stdlib.h>


void afficher_image_codee(int n)
{
        int p, t, w, h;
        int sueil = 255/n;

		if(scanf("%d",&n)!=1 ){
                
                return -1;
        }
        if(n<1 || n>=256){
                return -1;
        }
        if((n&(n-1))!=0){
                
                return 0;
        }

        int sueil = 255/n;//seuil de quantification
        if(scanf("%d %d",&w,&h)!=2 || w<=0 || h<=0){
                fprintf(stderr,"Erreur: Entete fichier image incorrecte\n");
                return 1;
        }
        printf("%d       %d\n",w,h);

        for (int y = 0; y < h*w; y++){

                if (scanf("%d",&p)!=1 || p<0 || p>255) {

                if (scanf("%d",&p)!=1 || p<0 || p>255) {
                fprintf(stderr,"Erreur: Valeur de pixel incorrecte\n");
                return 1;
            }
                return 1;
            }
        for (int y = 0; y < h*w; y++){
                if (scanf("%d",&p)!=1 || p<0 || p>255) {
                        fprintf(stderr,"Erreur: Valeur de pixel incorrecte\n");
                        return;
                }
                for(int i=1;i<=n;i++){
                        if(p<i*sueil){
                                p=i-1;
                                break;
                        }
                }

                printf("%d",p);
                t=y+1;
                if(t%(w)==0){
                        printf("\n");
                }else{
                        if(p<9){
                                printf("       ");
                        }

                        if(p>9 && p<100){
                                 printf("      ");
                        }

                        if(p>99 && p<=256){
                                 printf("     ");
                        }
                }


        }
}

void afficher_image_codee(int n)
{
        int w,h,p,t;
        if(n<1 || n>256){
                return -1;
        }
        if((n&(n-1))!=0){
                return 0;
        }

        int sueil = 255/n;//seuil de quantification
        if(scanf("%d %d",&w,&h)!=2 || w<=0 || h<=0){
                return -1;
        }
        printf("%d       %d\n",w,h);

        for (int y = 0; y < h*w; y++){

               
                if (scanf("%d",&p)!=1 || p<0 || p>255) {
                return -1;
            }
                for(int i=1;i<=n;i++){
                        if(p<i*sueil){
                                p=i-1;
                                break;
                        }
                }

                printf("%d",p);
                t=y+1;
                if(t%(w)==0){
                        printf("\n");

                }else{
                        if(p<9){
                                printf("       ");
                        }

                        if(p>9 && p<100){
                                 printf("      ");
                        }

                        if(p>99 && p<=256){
                                 printf("     ");
                        }
                }


        }

}					

int lire_image(int ligne, int colonne){
        int pixel; 
        for(int i=0;i<ligne;i++){
                for(int j=0;j<colonne;j++){
                        if(scanf("%d",&pixel)!=1 || pixel<0 || pixel>255){
                                fprintf(stderr,"Erreur: Valeur de pixel incorrecte ou fichier image corrompu\n");
                                return 0;
                        }
                        IMAGE[i][j]=pixel;
                        return 1;
                }
        }
}

for(int i=0;i<ligne;i++){
                for(int j=0;j<colonne;j++){
                        
                        p=IMAGE[i][j];
                        printf("%d",p);
                        t=y+1;
                        if(t%(w)==0){
                                printf("\n");

                        }else{
                                if(p<9){
                                        printf("       ");
                                }

                                if(p>9 && p<100){
                                        printf("      ");
                                }

                                if(p>99 && p<=256){
                                        printf("     ");
                                }
                        }
                }
}

void  afficher_image_codee_bis(int n, int ligne, int colonne){
        int p,i,j,k;

        int sueil = 255/n;//seuil de quantification
        printf("%d       %d\n",ligne,colonne);

        for (i = 0; i < ligne; i++){
                for(j=0;j<colonne;j++){

                        p=IMAGE[i][j];
                        for(k=1;k<=n;k++){
                                if(p<k*sueil){
                                        p=k-1;
                                        break;
                                }
                        }

                        printf("%d",p);

                        if(j==colonne-1){
                                printf("\n");

                        }else{
                                if(p<9){
                                        printf("       ");
                                }

                                if(p>9 && p<100){
                                        printf("      ");
                                }

                                if(p>99 && p<=256){
                                        printf("     ");
                                }
                        }
                }
        }


}

void image_miroir(int ligne,int colonne)
{
        int i, j,p;

        printf("%d       %d\n",ligne,colonne);
        for (i = 0; i < ligne; i++) {
                for (j = colonne - 1; j >= 0; j--) {
                        p=IMAGE[i][j];
                        
                        printf("%d",p);

                        if(j==colonne-1){
                                printf("\n");

                        }else{
                                if(p<9){
                                        printf("       ");
                                        }

                                if(p>9 && p<100){
                                        printf("      ");
                                }

                                if(p>99 && p<=256){
                                        printf("     ");
                                }
                        }
                }
 
        }
}




void rotation_image(int angle,int colonne,int ligne)
{
    int i, j,p;

    if (angle == 90) {
        /* nouvelle image : */
        for (j = 0; j < colonne; j++) {
            for (i = ligne - 1; i >= 0; i--) {
                p=IMAGE[i][j];
                printf("%d", p);

                if(i==0){
                                printf("\n");

                        }else{
                                if(p<9){
                                        printf("       ");
                                        }

                                if(p>9 && p<100){
                                        printf("      ");
                                }

                                if(p>99 && p<=256){
                                        printf("     ");
                                }
                        }
            }
        
        }
    }
    else if (angle == 180) {
        for (i = ligne - 1; i >= 0; i--) {
            for (j = colonne - 1; j >= 0; j--) {
                p=IMAGE[i][j];
                printf("%d", p);
                if(j==0){
                                printf("\n");

                        }else{
                                if(p<9){
                                        printf("       ");
                                        }

                                if(p>9 && p<100){
                                        printf("      ");
                                }

                                if(p>99 && p<=256){
                                        printf("     ");
                                }
                        }
            }
            
        }
    }
    else {
        printf("Angle non supporte : %d (utiliser 90 ou 180)\n", angle);
    }
}



void histogramme(int ligne, int colonne,int niv)
{
        int i, j, niveau;
        int *effectif;
        int total;
        total = ligne * colonne;

        effectif = (int *)calloc(niv, sizeof(int));
        if (effectif == NULL) {
                printf("Erreur d'allocation memoire\n");
                return;
        }

        for (i = 0; i < ligne; i++) {
                for (j = 0; j < colonne; j++) {
                        niveau = IMAGE[i][j];

                        effectif[niveau]++;

                }
        }

        printf("Niveau | Frequence (%%)\n");
        for (niveau = 0; niveau < niv; niveau++) {
                if (effectif[niveau] > 0) {   /* n'affiche que les niveaux présents dans l'image */
                printf("%6d | %6.2f\n", niveau, 100.0 * effectif[niveau]/total);
                }
        }
}


        ligne = 4;
        colonne = 5;
        niv = 256;

        printf("=== Image originale ===\n");
        for (i = 0; i < ligne; i++) {
                for (j = 0; j < colonne; j++) {
                printf("%-8d", IMAGE[i][j]);
                }
                printf("\n");
        }

        printf("\n=== 38) image_miroir ===\n");
        image_miroir(ligne, colonne);

        printf("\n=== 39) rotation_image 90 ===\n");
        rotation_image(90, colonne, ligne);

        printf("\n=== 39) rotation_image 180 ===\n");
        rotation_image(180, colonne, ligne);

        printf("\n=== 39) rotation_image 45 (cas d'erreur) ===\n");
        rotation_image(45, colonne, ligne);

        printf("\n=== 40) histogramme ===\n");
        histogramme(ligne, colonne, niv);