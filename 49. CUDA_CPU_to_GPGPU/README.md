# CUDA CPU to GPGPU

## This information is from Nvidia website, video called "Your First CUDA C Program"

We can still run programs that use CPU with CUDA.

Here is an example of a script that is written to run in the .cu extension while using the CPU.

## Add vectors with CPU

    #include <stdio.h>
    #define SIZE    1024

    void VectorAdd(int *a, int *b, int *c, int n){
        
        int i;

        for(i=0;i<n;++i){
            c[i]=a[i]+b[i];
        }

    }

    int main(){
        int *a, *b, *c;

        a = (int *)malloc(SIZE * sizeof(int));
        b = (int *)malloc(SIZE * sizeof(int));
        c = (int *)malloc(SIZE * sizeof(int));

        for(int i=0;i<SIZE;++i){
            a[i]=i;
            b[i]=i;
            c[i]=0;
        }

        VectorAdd(a, b, c, SIZE);

        for(int i=0;i<10;++i){
            printf("c[%d]=%d\n",i,c[i]);
        }

        free(a);
        free(b);
        free(c);

        return 0;

    }

## CPU to GPGPU conversion

We can convert the code to run on the GPGPU.

STEP1: Make variables accessable from CPU as well as the GPGPU
STEP2: Specify launch configuration of Kernel
STEP3: Make Kernel function able to run on GPGPU

Replace malloc with:

    cudaMallocManaged

Places variables to unified space for both CPU and GPGPU.

Then will return a pointer to access from host and device.

Replace free with:

    cudaFree

Update VectorAdd with:

    <<<1, SIZE>>>

First is the number of thread blocks.

The next is number of threads in thread blocks.

Each instance of the Kernel will launch in individual thread.

To assure that the CPU waits for Kernels to complete:

    cudaDeviceSynchronize()

After Kernel launch.

Parallelize vector add function

    __global__

This tells complier this function is executed from GPGPU.

To identify each thread:

    threadIdx

Remove for loop.

## Add vectors with GPGPU

    #include <stdio.h>
    #define SIZE    1024

    __global__ void VectorAdd(int *a, int *b, int *c, int n){    
        int i = threadIdx.x;

        if (i<n>)
            c[i]=a[i]+b[i];

    }

    int main(){
        int *a, *b, *c;

        cudaMallocManaged(&a, SIZE * sizeof(int));
        cudaMallocManaged(&b, SIZE * sizeof(int));
        cudaMallocManaged(&c, SIZE * sizeof(int));

        for(int i=0;i<SIZE;++i){
            a[i]=i;
            b[i]=i;
            c[i]=0;
        }

        VectorAdd <<<1, SIZE>>> (a, b, c, SIZE);

        cudaDeviceSynchronize();

        for(int i=0;i<10;++i){
            printf("c[%d]=%d\n",i,c[i]);
        }

        cudaFree(a);
        cudaFree(b);
        cudaFree(c);

        return 0;

    }