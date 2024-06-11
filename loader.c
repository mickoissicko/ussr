#include <stdlib.h>
#include <stdio.h>

int main()
{
    printf("Loading...\n");

    #ifdef _WIN32
        system("launcher.bat");
    #else
        system("chmod +x launcher.sh");
        system("./launcher.sh");
    #endif
}

