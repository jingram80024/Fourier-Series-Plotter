import numpy as np
import matplotlib.pyplot as plt

async def graph(composite_sinusoids: int, step: int, *plots: tuple[int, ...]):

    composite_sinusoids += 1
    a_0 = ((np.exp(2*np.pi)-1)/(np.pi))
    a_n = []
    b_n = []
 
    for n in range(composite_sinusoids):
        a_x = ((np.exp(2*np.pi))-1)/((np.pi*((n+1)**2))+np.pi)
        a_n.append(a_x)
        b_x = ((n+1)-((n+1)*np.exp(2*np.pi)))/((np.pi*((n+1)**2))+np.pi)
        b_n.append(b_x)

    w_t = np.arange(0,(4*np.pi),(np.pi/step))

    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12,5))
    ax.set_xlabel('wt')
    ax.set_ylabel('f(wt)')
    ax.set_title("Fourier Series of exp^(wt)")

    n = 0
    #f_x = a_0/2
    f_x = np.full(w_t.size,(a_0/2))
    for n in range(composite_sinusoids):
        if (n) in plots:
            ax.plot(w_t, f_x, label=n)
        f_x = f_x + a_n[n]*np.cos((n+1)*w_t)
        f_x = f_x + b_n[n]*np.sin((n+1)*w_t)
    ax.legend()
    ax.legend(title="Composite Sinusoids")
    return fig