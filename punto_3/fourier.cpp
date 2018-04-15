#include <iostream> 
#include <fstream> 
#include <string>

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

//Funcion para cargar la primera columna del archivo
void cargar_columna1( char* nombre_archivo, double **datos, int columnas, int filas );
void cargar_columna1( char* nombre_archivo, double **datos, int columnas, int filas ){
    ifstream archivo(nombre_archivo);
    double x[columnas*filas];
    for( int i = 0; i < filas*columnas; i++){
        archivo >> x[i];
    }
    
    for( int i = 0; i < filas; i++){
            datos[i][0] = x[i*columnas];
    }
  
}

//Funcion para llenar la primera columna, por medio de inicializa y cargar
void llena_1( char* nombre_archivo, double **datos, int columnas, int filas);
void llena_1( char* nombre_archivo, double **datos, int columnas, int filas){
  datos = inicializa(filas);
  cargar_columna1( nombre_archivo, datos, columnas, filas);
  for(int i = 0; i < filas-1; i++ ){
     for(int j =0; j< columnas-1; j++){
       
       cout<<datos[i][j]<< " " ;
     }
     cout<<endl;
  }
  borra( datos, filas);
}

//Lo mismo para la columna 2
void cargar_columna2( char* nombre_archivo, double **datos, int columnas, int filas );
void cargar_columna2( char* nombre_archivo, double **datos, int columnas, int filas ){
    ifstream archivo(nombre_archivo);
    double x[columnas*filas];
    for( int i = 0; i < filas*columnas; i++){
        archivo >> x[i];
    }
    
    for( int i = 0; i < filas; i++){
       for( int j = 0; j < columnas; j++){
	 datos[i][0] = x[i*columnas +j];
	      }
    }
  
}

void llena_2( char* nombre_archivo, double **datos, int columnas, int filas);
void llena_2( char* nombre_archivo, double **datos, int columnas, int filas){
  datos = inicializa(filas);
  cargar_columna2( nombre_archivo, datos, columnas, filas);
  for(int i = 0; i<filas-1; i++){
    for(int j =0; j<columnas-1; j++){
      cout<<datos[i][j]<< " " ;
    }
    cout<<endl;
  }
  borra(datos, filas);
  
}

					  
					  
int main(int argc, char * argv[] ){
    int m=0, n=0;
    dimension_fila(argv[1],n);
    dimension_columna(argv[1],m);
    double **data;
    //llena_1(argv[1], data, m, n);
    llena_2(argv[1], data, m, n);
    return 0;

}


