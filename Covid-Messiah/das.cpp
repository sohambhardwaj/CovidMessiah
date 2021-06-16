#define _WIN32_WINNT 0x0500
#include "windows.h"

MEMORYSTATUSEX memInfo;
memInfo.dwLength = sizeof(MEMORYSTATUSEX);
GlobalMemoryStatusEx(&memInfo);
DWORDLONG totalVirtualMem = memInfo.ullTotalPageFile;