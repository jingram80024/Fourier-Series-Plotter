# Fourier-Series-Plotter

## NOTE: Pyscript was very new at the time of writing and this likely won't work anymore :)

 Python module plots the fourier series of a repeating exponential function for any user defined number of composite sinusoids.

 Check out my GitHub Pages deployment to test this python function using pyscript:

 https://jingram80024.github.io/Fourier-Series-Plotter

The function used for the Fourier Series is a repeating exponential defined from 0 to $2\pi$.

$$
f(x) = e^{x}
$$

Solutions:
The Fourier Series of the exponential repeating every $2\pi$ is shown below.

$$
f(x) = \frac{1}{2}a_o +\sum_{n=1}^N a_n \cos nx+\sum_{n=1}^N b_n \sin nx
$$

where

$$
a_o=\frac{1}{\pi}(e^{2\pi}-1),
$$

$$
a_n=\frac{e^{2\pi}-1}{\pi n^2+\pi},
$$

and

$$
b_n=\frac{n-ne^{2\pi}}{\pi n^2+\pi}
$$

>## Sample Plot

Below is a sample plot created by the script for 1, 4, 7, and 100000 composite sinusoids.

With more composite sinusoids, the fourier series looks nearly identical to $f(x)=e^x$, repeating every $2\pi$.

![figure 1](https://github.com/jingram80024/Fourier-Series-Plotter/blob/main/Sample_Plot.png)

>## Derivations

>### Solving for $a_o$

$$
a_o = \frac{1}{\pi}\int_0^{2\pi} f(x)dx
$$

$$
a_o = \frac{1}{\pi}\int_0^{2\pi} e^xdx
$$

$$
a_o = \frac{1}{\pi}e^x\bigg|_0^{2\pi}
$$

$$
a_o = \frac{1}{\pi}e^{2\pi} - \frac{1}{\pi}e^{0}
$$

$$
a_o = \frac{1}{\pi}(e^{2\pi}-1)
$$

>### Solving for $a_n$

$$
a_n = \frac{1}{\pi}\int_0^{2\pi} f(x)\cos nxdx
$$

$$
a_n = \frac{1}{\pi}\int_0^{2\pi} e^x\cos nxdx
$$

|let||
|-|-|
| $u=e^x$ | $du=e^x$ |
| $dv=\cos nxdx$ | $v=\frac{1}{n}\sin nx$ |

$$
I = \frac{1}{\pi}\bigg(e^x \frac{1}{n}\sin nx-\frac{1}{n}\int_0^{2\pi}\sin nxe^xdx\bigg)
$$

|let||
|-|-|
| $u=e^x$ | $du=e^x$ |
| $dv=\sin nxdx$ | $v=-\frac{1}{n}\cos nx$ |

$$
I = \frac{1}{\pi}\bigg(e^x \frac{1}{n}\sin nx-\frac{1}{n}\bigg(e^x\frac{-1}{n}\cos nx-\int_0^{2\pi}\frac{-1}{n}\cos nxe^xdx\bigg)\bigg)
$$

$$
I = \frac{1}{\pi n}e^x \sin nx+\frac{1}{\pi n^2}e^x\cos nx-\frac{1}{\pi n^2}\int_0^{2\pi}e^x\cos nxdx
$$

but,

$$
I = \frac{1}{\pi}\int_0^{2\pi} e^x\cos nxdx
$$

then,

$$
\bigg(1+\frac{1}{n^2}\bigg)I = \frac{1}{\pi n}e^x \sin nx+\frac{1}{\pi n^2}e^x\cos nx
$$

$$
I = \frac{e^x(n\sin nx+\cos nx)}{\pi n^2+\pi}\bigg|_0^{2\pi}
$$

$$
I = \frac{e^{2\pi}(n\sin 2\pi n+\cos 2\pi n)}{\pi n^2+\pi}-\frac{e^{0}(n\sin 0+\cos 0)}{\pi n^2+\pi}
$$

$$
I = \frac{e^{2\pi}}{\pi n^2+\pi}-\frac{1}{\pi n^2+\pi}
$$

$$
a_n = I = \frac{e^{2\pi}-1}{\pi n^2+\pi}
$$

>### Solving for $b_n$

$$
b_n = \frac{1}{\pi}\int_0^{2\pi} f(x)\sin nxdx
$$

$$
b_n = \frac{1}{\pi}\int_0^{2\pi} e^x\sin nxdx
$$

|let||
|-|-|
| $u=e^x$ | $du=e^x$ |
| $dv=\sin nxdx$ | $v=-\frac{1}{n}\cos nx$ |

$$
I = \frac{1}{\pi}\bigg(e^x\frac{-1}{n}\cos nx-\int_0^{2\pi}e^x\frac{-1}{n}\cos nxdx\bigg)
$$

$$
I = \frac{1}{\pi}\bigg(-\frac{1}{n}e^x\cos nx+\frac{1}{n}\int_0^{2\pi}e^x\cos nxdx\bigg)
$$

|let||
|-|-|
| $u=e^x$ | $du=e^x$ |
| $dv=\cos nxdx$ | $v=\frac{1}{n}\sin nx$ |

$$
I = \frac{1}{\pi}\bigg(-\frac{1}{n}e^x\cos nx+\frac{1}{n}\bigg(e^x\frac{1}{n}\sin nx - \int_0^{2\pi}\frac{1}{n}\sin nxe^xdx\bigg)\bigg)
$$

$$
I = -\frac{1}{\pi n}e^x\cos nx + \frac{1}{\pi n^2}e^x\sin nx-\frac{1}{\pi n^2}\int_0^{2\pi}e^x\sin nxdx
$$

but,

$$
I = \frac{1}{\pi}\int_0^{2\pi} e^x\sin nxdx
$$

then,

$$
\bigg(1+\frac{1}{n^2}\bigg)I = -\frac{1}{\pi n}e^x\cos nx + \frac{1}{\pi n^2}e^x\sin nx
$$

$$
I = \frac{e^x(\sin nx-n\cos nx)}{\pi n^2+\pi}\bigg|_0^{2\pi}
$$

$$
I = \frac{e^{2\pi}(\sin 2\pi n-n\cos 2\pi n)}{\pi n^2+\pi}-\frac{e^{0}(\sin 0-n\cos 0)}{\pi n^2+\pi}
$$

$$
I = \frac{e^{2\pi}(-n)}{\pi n^2+\pi}-\frac{-n}{\pi n^2+\pi}
$$

$$
b_n = I = \frac{n-ne^{2\pi}}{\pi n^2+\pi}
$$
