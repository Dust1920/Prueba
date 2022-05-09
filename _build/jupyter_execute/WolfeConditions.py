#!/usr/bin/env python
# coding: utf-8

# # Lema 3.1
# 
# Suponga que $f:\mathbb{R}^n\to\mathbb{R}$ es continua y diferenciable. Sea $p_k$ una dirección de descenso en $x_k$, y asuma que $f$ es acotado por debajo por los rayos $\ell_α=\{x_k+αp_k\mid α>0\}$. Entonces si $0< c_1< c_2 < 1$, entonces existen intervalos de tamaños de paso que satisface las condiciones de Wolf y las condiciones fuertes de Wolf.
# 
# ## Demostración
# 
# Consideremos
# $$ϕ(α)=f(x_k+αp_k)$$
# Como $f$ es acotada $ϕ$ tambien lo es. Definimos 
# $$l(α)=f(x_k)+αc_1∇f(x_k)^Tp_k$$ 
# Como $l(\alpha)$ no esta acotada por debajo necesariamente existe $\alpha^*=\min\{α\mid f(x_k+αp_k)=\phi (α)\}$ tal que 
# 
# $$f(x_k+α^*p_k)=f(x_k)+α^*c_1∇f(x_k)^Tp_k\ \ (⋆)$$ 
# 
# Luego, $ℓ_α$ es un conjunto convexo $∀α>0$, por lo tanto al tomar 
# $α'\in(0,α^*)$ entonces  
# 
# $$f(x_k+α^*p_k)\leq f(x_k)+α^*c_1∇f(x_k)^Tp_k$$
# 
# Teniendo asi la condición de suficiente decrecimiento. Luego, para el segundo criterio usaremos el Teorema del valor medio para funciones multivariables. 
# Entonces, para algun $α^{**}∈(0,α^*)$
# 
# $$f(x_k+α^*p_k)=f(x_k)+\alpha^*∇f(x_k+α^{**}p)p^T (⋆⋆)$$
# 
# Por $(\star)$ tenemos que 
# 
# $$f(x_k+α^*p_k)-f(x_k)=α^*c_1∇f(x_k)^Tp_k$$, 
# 
# De manera similar con $(⋆\star)$, e igualando tenemos que 
# 
# $$\alpha^* ∇f(x_k+α^{*.*}p)p^T=α^*c_1∇f(x_k)^Tp_k$$
# 
# y para algun $1 > c_2 > c_1$ tenemos que 
# 
# $$ ∇f(x_k+α^{**} p)p^T=c_1∇f(x_k)^Tp_k \geq c_2∇f(x_k)^Tp_k$$
# 
# Como ambos son negativos tenemos las condiciones de Wolf, ahora para obtener las fuertes debemos aplicar el valor absoluto a la segunda condicion, por tanto se invertira la desigualdad.Entonces teneemos que 
# 
#  $$|∇f(x_k+α^{**}p)p^T|\leq c_2 |∇f(x_k)^Tp_k|$$
# 
#  Teniendo asi las condiciones fuertes de Wolf.
# 
# ### Teoremas 
# Condiciones de Wolf 
# $$f(x_k+αp_k)\leq f(x_k)+c_1 α_k \nabla f(k_k)^Tp_k$$
# $$\nabla f(x_k+α_kp_k)^Tp_k\geq c_2 \nabla f_(x_k)^Tp_k$$
# Condiciones Fuertes de Wolf 
# 
# $$f(x_k+αp_k)\leq f(x_k)+c_1 α_k ∇f_k^Tp_k$$
# $$|\nabla f(x_k+α_kp_k)^Tp_k|\leq c_2| ∇f_k^Tp_k|$$
# 
# Teorema del valor medio para funciones multivariables. 
# 
# Sea $f:\mathbb{R}^n\to\mathbb{R}$ para cualquier vector $p$ tenemos que 
# $$f(x+p)=f(x)+∇f(x+αp)^Tp$$
# Para algun $α\in (0,1)$
