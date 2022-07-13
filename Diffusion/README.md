Given $u=u(x,y)$ and $v(x,t)$ consider the following the system of equations:

$$
\begin{cases}
\partial_t u = f(u, v) + \alpha \partial_x^2 u\\
\partial_t v = g(u, v) + \beta \partial_x^2 v
\end{cases}
$$

for $t\in [0,T]$ and $x\in[a,b]$. 

Now consider the central finite difference discretization of the second order partial derivative:

$$
D^2_{x_i} u(t)=\frac{u_{i+1}(t)-2u_i(t)+u_{i-1}(t)}{h_x^2}
$$

where $u_i(t)=u(x_i, t)$ and $v_i(t)=v(x_i, t)$ supposing we homogeneously discretize the domain $[a,b]$ with discretization step $h_x$. Analogously we define $D^2_{x_i} v(t)$.

We can thus write for all $x_i$:

$$
\begin{cases}
\dot u_i(t) = f(u_i(t), v_i(t)) + \alpha D_{x_i}^2 u(t)=f_i(t)+\alpha D_{x_i}^2 u(t)\\
\dot v_i(t) = g(u_i(t), v_i(t)) + \beta D_{x_i}^2 v(t)=g_i(t)+\beta D_{x_i}^2 u(t)
\end{cases}
$$

that can be solved using a forward Euler method as before.

We can generalize by definining:

$$
\mathbf{x}=
\begin{bmatrix}
x_0(t) \\
x_1(t) \\
\vdots \\
x_k(t)
\end{bmatrix},\quad
\mathbf{u}(t)=u(\mathbf{x}, t)=
\begin{bmatrix}
u_0(t) \\
u_1(t) \\
\vdots \\
u_k(t)
\end{bmatrix},\quad
\mathbf{v}(t)=v(\mathbf{x}, t)=
\begin{bmatrix}
v_0(t) \\
v_1(t) \\
\vdots \\
v_k(t)
\end{bmatrix}$$

and:

$$
\mathbf{f}(t)=f(\mathbf u(t), \mathbf v(t))= 
\begin{bmatrix}
f_0(t) \\
f_1(t) \\
\vdots \\
f_k(t)
\end{bmatrix},\quad \mathbf{g}(t)=g(\mathbf u(t), \mathbf v(t))= 
\begin{bmatrix}
g_0(t) \\
g_1(t) \\
\vdots \\
g_k(t)
\end{bmatrix}
$$

where $k=\lfloor (b - a) / h_x \rfloor$, we can write:

$$
\begin{cases}
\dot{\mathbf{u}}(t) = \mathbf{f}(t) + \alpha D_{\mathbf{x}}^2 \mathbf u(t)\\
\dot{\mathbf{v}}(t) = \mathbf{g}(t) + \beta D_{\mathbf{x}}^2 \mathbf  v(t)
\end{cases}
$$

and then use the forward Euler method as in the example without diffusion:

$$
\begin{cases}
\mathbf{u}(t_{j+1}) = (I_k+\alpha h_t A)\mathbf{u}(t_j) + h_t\mathbf f(t_j)\\
\mathbf{v}(t_{j+1}) = (I_k+\beta h_t A)\mathbf{u}(t_j) + h_t\mathbf g(t_j)
\end{cases}
$$

where $A$ is the matrix associated the the finite difference method used above above and $h_t$ is the discretization step used to discretize the time.
