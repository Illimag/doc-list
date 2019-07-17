# CUDA Programming Model

## This information is all from the Nvidia CUDA Documentation.

CUDA is a parallel programming platform from Nvidia, which runs on Nvidia's GPUs.

GPUs which are Graphic Processing Units, are often used in graphic heavy processes such as 3D and video renderings.

This is because of the architecture of a GPU, which consists of cores similarly to a CPU.

But unlike a CPU which has a few cores that can do complex tasks individually, GPU has many cores that can do simple tasks together.

Looking it from an order of magnitude, a CPU may have around 1-8 cores.

A GPU can have 1000s of cores which means a GPU can be an order of magnitude more efficient in processing than a CPU.

When a GPU is used for General Processing related tasks it is often called GPGPU.

The following code examples are written in C.

## Kernels

### "CUDA C extends C by allowing the programmer to define C functions, called kernels, that, when called, are executed N times in parallel by N different CUDA threads, as opposed to only once like regular C functions." NVIDIA DOCS

Here is an example of what a CUDA thread ID looks like:

    threadIdx.x

Here is an example of how to execute the number of CUDA threads specifically:

    test<<1,N>>

Additionally we use the declaration:

    __global__

To define the Kernel.

Here is an example of code that adds two vectors A and B of size N and stores the result into vector C:

    __global__ 
    void VecAdd(float* A, float* B, float* C){
        int i = threadIdx.x;
        C[i]=A[i]+B[i];
    }
    int main(){
        VecAdd<<1,N>>(A,B,C);
    }

Each N thread of the thread block will run the function VecAdd() in parallel.

## Thread Hierarchy

    threadIdx 

is a 3-component vector.

So this means threads can be using an one-dimensional, two-dimensional, or three-dimensional thread index.

Which will form an oone-dimensional, two-dimensional, or three-dimensional block of threads, called a thread block.

This allows a way to invoke computation across the elements in a domain such as a vector, matrix or volume.

So this means we can have:

    threadIdx.x
    threadIdx.y
    threadIdx.z

