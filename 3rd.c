#include <stdio.h> 
int main() 
{ 
fp = fopen("myfile.txt" , "r"); 
int count,i; 
int c=0; 
while(1) 
{ 
 count = 0; 
 for(i=0;i<10;i++)
 { 
 c = getc(fp); 
 if( c == -1) 
 break; 
 if(c>='0' && c<='9') 
 count++; 
 } 
 if(c == -1) 
 break; 
 if(count==10)
 { 
 char s[10]; 
 fseek(fp,-10,SEEK_CUR);// sets the file position to the given offset 
 fgets(s,11,fp); 
 printf("%s",s); 
 break; 
 } 
} 
if (count!=10) 
{ 
 rewind(fp);//sets the position to the beginning of the file 
 for(i=0;i<10;) 
 { 
 c = getc(fp); 
 if(c>='0' && c<='9') 
 continue; 
 printf("%c",c); 
 i++; 
 } 
}
 return 0; 
}
