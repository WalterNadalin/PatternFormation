Consider the non-linear system

$$
\begin{cases}
\dot u(t)=au(t)+bu(t)v(t)\\
\dot v(t)=cv(t)+du(t)v(t)
\end{cases}
$$

along with the initial conditions $u(0)=u_0$ and $v(0)=v_0$. With proper coefficents we can consider $u(t)$ and $v(t)$ respectively number of preys and predators in the same enviromnent at time $t$.

Now, let

$$
\mathbf x(t)=
\begin{bmatrix}
u(t)\\
v(t)
\end{bmatrix},\quad
\mathbf F(\mathbf x, t)=
\begin{bmatrix}
au(t)+bu(t)v(t)\\
cv(t)+du(t)v(t)
\end{bmatrix}
$$

the the forward Euler method to solve numerically this system can be written as

$$
\frac{\mathbf x_{n+1}-\mathbf x_{n}}{h}=\mathbf{F}(t_n, \mathbf x_n)
$$

which is a simple system of equations.
