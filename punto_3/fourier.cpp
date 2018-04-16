#include <iostream> 
#include <fstream> 
#include <string>
#include <stdio.h>
#include <math.h>

using namespace std;

//Declaramos la funcion que saca el numero de filas de los datos que entran por parametro. los datos seran datos.txt

void dimension_fila(char* archivo, int& filas);
void dimension_fila(char* archivo, int& filas){
  ifstream datos(archivo);
  //numero de filas
  string numero;
  filas = 0;
  while( !datos.eof() ){
    getline(datos, numero);
    filas +=1;
  }

}

//Declaramos la funcion que saca el numero de filas de los datos que entran por parametro. los datos seran datos.txt
void dimension_columna(char* archivo, int& columnas);
void dimension_columna(char* archivo, int& columnas){
  //numero de columnas
  ifstream datos(archivo);
  string linea1;
  getline(datos, linea1);
  columnas = 0;
  int i;
  int M = linea1.size();
    for(i = 0; i<M; i++){
     columnas  += ( linea1[i] != ' ' )? 1 : 0;
    }
}

//Funciones para inicializar una matriz y borrarla, entra por parametro  el numero de espacio que queremos que tenga de ancho.   
double** inicializa( int ancho);
double** inicializa( int ancho){
    double **datos;
    datos = new double*[ancho];
    for(int i=0; i < ancho; i++)
        datos[i] = new double[ancho];
    return datos;
}
void borra(double** arreglo, int filas );
void borra(double** arreglo, int filas ){
    for(int i = 0; i < filas; i++)
        delete[] arreglo[i];
    delete[] arreglo;
}


//Funcion para cargar archivo
void cargar( char* nombre_archivo, double **datos, int columnas, int filas );
void cargar( char* nombre_archivo, double **datos, int columnas, int filas ){
    ifstream archivo(nombre_archivo);
    double x[columnas*filas];
    for( int i = 0; i < filas*columnas; i++){
        archivo >> x[i];
    }
    
    for( int i = 0; i < filas; i++){
       for( int j = 0; j < columnas; j++){
	 datos[i][j] = x[i*columnas +j];
	      }
    }
  
}
// Esta funcion imprimer las dos columnas del archivo txt
void llena( char* nombre_archivo, double **datos, int columnas, int filas);
void llena( char* nombre_archivo, double **datos, int columnas, int filas){
  datos = inicializa(filas);
  cargar(nombre_archivo, datos, columnas, filas);
  for(int i = 0; i<filas-1; i++){
    for(int j =0; j<columnas; j++){
      cout<<datos[i][j]<< " " ;
    }
    cout<<endl;
  }
  borra(datos, filas);
  
}

//Funcion para hacer un linspace
double* linspace(double*line, int a, int b, int N){
    double delta =(b-a)/(N-1.0);
    for (int i=0; i<N; i++){
            line[i] = (i*delta);
    }
    return line;
}

// Funcion para la interpolacionde lagragne

double* lagrange( double*col1, double* col2, double *x_mod, double* y_mod, int filas ){
  for (int k =0; k<filas; k++){
      double numero = 1.0;
      for (int i= 0; i<filas; i++){
	  double v = col2[i];
	  for (int j=0; j<filas; j++){
	    if (i != j){
		  v = v*(x_mod[k] - col1[j])/(col1[i] - col1[j]);
		  numero += v;
		}
	    }
	}
      y_mod[k] = numero -1.0;
    }
  return y_mod;
}
		  
		 
// Funcion para la transformada de Fourier separando real de iamginario 

double * fourier(double* real, double* imaginaria, double* x_nuevo, double*y_nuevo, int filas){
  for (int i = 0; i<filas;i++){
    double numero_real = 0.0;
    double numero_imaginario = 0.0;
    for (int j =0; j< filas;j++){
      numero_real += y_nuevo[j] * cos((-2*3.14159*i*j)/filas);
      numero_imaginario += y_nuevo[j] * sin((-2*3.14159*i*j)/filas);
      real[j]= numero_real;
      imaginaria[j]= numero_imaginario;
      cout<<real[j]<<"  " << " " << imaginaria[j] <<endl;
	}
    
    }
  return real, imaginaria;
}

		  
double* frecuencias_f(double*frecuencias, double*real, double*imaginaria, int filas){
  for(int i=0; i<filas;i++){
      double raiz  = (real[i] * real[i]) + ( imaginaria[i] *  imaginaria[i]);
      double norma = pow(raiz,0.5);
      frecuencias[i] = norma;
      cout<<imaginaria[i]<<" "<<endl;
    }
  return frecuencias;
}
					  
int main(int argc, char * argv[] ){
    int m=0, n=0;
    dimension_fila(argv[1],n);
    dimension_columna(argv[1],m);
    double **datos;
    //llena(argv[1], datos, m, n);
    datos = inicializa(n);
    cargar(argv[1],datos,m,n);
    //Vamos a pasar cada columna a un array

    double x[n];
    double y[n];
    for (int i = 0; i<n-1; i++){
      x[i] = datos[i][0];
      y[i] = datos[i][1];
    }
    int filas = n-1;
    double a = x[0];
    double b = x[filas-1];
    double x_mod[n];
    linspace(x_mod, a, b, filas);
    double y_mod[n];
    lagrange( x, y, x_mod, y_mod, filas );
    double real[filas];
    double imaginaria[filas];
    double frecuencias[filas];
    cout<< "Real" << "  " << "Imaginaria"<<endl; 
    fourier(real,imaginaria, x_mod, y_mod, filas);
    cout<< "Frecuencias"<<endl;
    frecuencias_f(frecuencias, real, imaginaria, filas);

 }


