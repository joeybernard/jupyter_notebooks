#include <math.h>
#include <stdio.h>
#include <sys/time.h>

int main() {
  printf("Start\n");
  struct timeval start,stop;
  float start_time, stop_time;
  gettimeofday(&start, NULL);
  int size = 100000;
  float array[size];
  float ans[size];
  printf("Here\n");
  for (int i=0; i<size; i++) {
    ans[i] = tan(array[i]);
  }
  gettimeofday(&stop, NULL);
  start_time = (start.tv_sec * 1000000) + (start.tv_usec);
  stop_time = (stop.tv_sec * 1000000) + (stop.tv_usec);
  printf("time: %f\n", (stop_time - start_time));
  printf("End\n");
}
