#include <iostream>
#include <windows.h>
#define l  600
//#define w  500
using namespace std;


void* window(void*args){

    HWND h=FindWindow("notepad",NULL);
    SetForegroundWindow(h);

    SetWindowText(h,"zhangwen");

  for(int i=1;i<20;++i){
     int r;
    if( i%2 == 0 )r=0;
    else if( i%2 == 1) r=1;
    //ShowWindow(h,r);
    SetWindowPos(h,NULL,1280/(1+rand()%30),1024/(1+rand()%30),i*20,0,NULL);
    cout<<i<<'\t'<<r<<endl;
    _sleep(300);
    }
}

   void sp(char* s){
      HWND H=FindWindow(NULL,s);
      if(H == 0){
            _sleep(5000);
            HWND H=FindWindow(NULL,s); //GetForegroundWindow();
           // cout<<"---------------"<<s<<endl;
                  }
      SetForegroundWindow(H);
      for (int i=0;i<10;++i){
                //SetWindowPos(GetForegroundWindow(),NULL,l,l/2,l,l-100,NULL);
                SetWindowPos(H,NULL,l,100,500,230,NULL);
                _sleep(l/12);
                //SetWindowPos(GetForegroundWindow(),NULL,l+10,l/2+10,l,l-100,NULL);
                SetWindowPos(H,NULL,l+10,100+10,500,230,NULL);
                _sleep(l/12);
               //SetWindowPos(GetForegroundWindow(),NULL,l,l/2,l,l-100,NULL);
               SetWindowPos(H,NULL,l,100,500,230,NULL);
                            }

   }

int main(int argc,char* argv[])
{
    //ShowWindow(GetForegroundWindow(),1);
    //HWND h=FindWindow(NULL,"dfga");//argv[1]);

    //if (h == 0)return 1;
    //argv[1]="09:34:32"; //×ö²âÊÔÓÃ
    //cout<<argv[1]<<endl;
    sp(argv[1]);

   //cout <<"hello......" << endl;
    return 0;
}
