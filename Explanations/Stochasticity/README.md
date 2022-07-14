In order to study the stochastic phenomena, we use the following model with $u=u(t,x)$, $v=v(t,x)$ and random perturbations:

$$
\begin{cases}
  \partial_t u=f(u,v)+D_u\partial_x^2u+\gamma_u\xi(t,x)\\
  \partial_t u=g(u,v)+D_v\partial_x^2u+\gamma_v\eta(t,x)
\end{cases}
$$

and the same boundary conditions as the problem with no stochasticity and diffusion, i. e. the zero-flux boundary conditions. Here, $\xi(t,x)$ and $\eta(t,x)$ are uncorrelated Gaussian noise with intensities $\gamma_u$ and $\gamma_v$ respectively. They are s. t.:

$$
\langle\xi(t,x)\rangle=0, \quad 
\langle\xi(t,x)\xi(s, y)\rangle=\delta(s-t)\delta(y-x)
$$

and the same holds for $\eta(t,x)$, with $\delta$ Dirac delta.

We achieve the simulation of this stochastic component by adding a linear random term, distributed normally, to the couple of numerical equations given in the example without stochasticity. Since the random terms have to be indipendent both in space and in time we have to generate a sample for each single iteration of the algorithm. This could be very costly.
