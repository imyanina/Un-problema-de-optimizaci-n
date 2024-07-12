import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.markdown(
    "<h1 style='font-family: Cambria Math, serif; color: #276E90; text-align: center;'>Un problema de optimización</h1>",
    unsafe_allow_html=True
)

st.markdown('''
Se tiene una hoja rectangular de dimensiones **$𝐿$**(largo) y 
**$𝑊$**(ancho). El objetivo es maximizar el volumen de una caja sin tapa que se puede formar cortando cuadrados idénticos de lado $𝑥$ en cada esquina de la hoja y doblando los bordes para formar las paredes de la caja.
''')
st.image("https://imyanina.github.io/proyecto/cubo.png", width=650)

with st.container(border=True):
    st.markdown("**Dígite las medidas de su hoja:**")

    col1, col2 = st.columns(2)

    with col1:
        b = float(st.number_input("largo:", min_value=0.0, value=1.0, step=0.1))
    
    with col2:
        c = float(st.number_input("ancho:", min_value=0.0, value=1.0, step=0.1))

    if b==0 or c==0:
        st.error("Las dimensiones de la hoja deben ser mayores a cero. Por favor, digite las medidas de su hoja.")
    else:
        st.markdown("Las dimensiones de la hoja son:")

        colu1, colu2, colu3 = st.columns(3)

        with colu2:
            if b==c:
                st.image("https://imyanina.github.io/proyecto/imagetwo.png", width=400, use_column_width=True)
                st.markdown(f"<div style='text-align: center; font-size: 24px; margin-top: -20px'>{b:.1f}</div>", unsafe_allow_html=True)
            else:
                st.image("https://imyanina.github.io/proyecto/imageone.png", width=500, use_column_width=True)
                if b>c:
                    st.markdown(f"<div style='text-align: center; font-size: 24px; margin-top: -20px;'>{b:.1f}</div>", unsafe_allow_html=True)  
                else:
                    st.markdown(f"<div style='text-align: center; font-size: 24px; margin-top: -20px;'>{c:.1f}</div>", unsafe_allow_html=True)
        with colu3:
            if b==c:
                st.write()
            elif b>c:
                st.markdown(f"<div style='font-size: 24px; margin-top: 60px;'>{c:.1f}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='font-size: 24px; margin-top: 60px;'>{b:.1f}</div>", unsafe_allow_html=True)

st.divider()
if b!=0 and c!=0:
    st.header(":blue[Volumen de la caja]")

    st.markdown('''
    El volumen de una caja se determina multiplicando sus dimensiones:
    $$
    V=L\\times W\\times H 
    $$
    - $L$ es el largo
    - $W$ es el ancho
    - $H$ es el alto
    ''')

    with st.container(border=True):
        st.markdown('''
        Las dimensiones de su caja están dadas por:
        ''')
        if b==c:
            st.markdown(f'''
            - $L={b:.1f}-2x$
            - $W={c:.1f}-2x$
            - $H=x$
            ''')
        elif b>c:
            st.markdown(f'''
            - $L={b:.1f}-2x$
            - $W={c:.1f}-2x$
            - $H=x$
            ''')
        else:
            st.markdown(f'''
            - $L={c:.1f}-2x$
            - $W={b:.1f}-2x$
            - $H=x$
            ''')

    x = sp.symbols('x')
    p = b - 2*x
    a = c - 2*x
    v = p*a*x
    simpli = sp.expand(v)

    st.markdown(f'''
    El volumen de la caja es:
    $$
    V=({sp.latex(p)})({sp.latex(a)})x
    $$
    ''')

    st.markdown(f'''
    Al operar, obtenemos:
    $$
    V={sp.latex(simpli)}
    $$
    ''')


    st.divider()
    #aqui voy

    st.header(":blue[Derivada para encontrar máximos]")

    st.markdown('''
    La derivada de una función nos proporciona información crucial sobre su comportamiento. Para encontrar los máximos (y mínimos) de una función, seguimos estos pasos:
    1. Calculamos la primera derivada de la función, $f'(x)$.
    2. Encontramos los puntos críticos, solucionamos la ecuación $f'(x)=0$. Los puntos que satisfacen esta ecuación son donde la pendiente de la recta tangente a la curva es cero.
    3. Usaremos la segunda derivada de la función $f''(x)$ para determinar si los puntos son mínimos, máximos o puntos de inflexión. Si $f''(x)<0$ en un punto crítico ese punto es un máximo local.
    ''')

    derivada = sp.diff(simpli, x)
    puncriti = sp.solve(derivada, x)

    st.markdown(f'''
    En nuestro caso, la primera derivada es:
    $$
    V'={sp.latex(derivada)}
    $$
    y si resolvemos ${sp.latex(derivada)} = 0$, obtenemos:
    $$
    x_1={puncriti[0]:.2f}
    $$
    $$
    x_2={puncriti[1]:.2f}
    $$
    ''')

    segderivada = sp.diff(derivada, x)

    st.markdown(f'''
    La segunda derivada de la función es:
    $$
    V''={sp.latex(segderivada)}
    $$
    ''')

    reemplaza1 = segderivada.subs(x, puncriti[0])
    reemplaza2 = segderivada.subs(x, puncriti[1])

    st.markdown(f'''
    Al reemplazar $x_1$ y $x_2$ en $V''(x)$, obtenemos:
    $$
    V''({puncriti[0]:.2f})={reemplaza1:.2f}
    $$
    $$
    V''({puncriti[1]:.2f})={reemplaza2:.2f}
    $$
    ''')

    if reemplaza1<0:
        st.markdown(f'''
        Como ${reemplaza1:.2f}<0$, el punto $x_1$ es un máximo local. Es decir, el máximo volumen se obtiene cuando $x={puncriti[0]:.2f}$
        ''')
    elif reemplaza2<0:
        st.markdown(f'''
        Como ${reemplaza2:.2f}<0$, el punto $x_2$ es un máximo local. Es decir, el máximo volumen se obtiene cuando $x={puncriti[1]:.2f}$
        ''')

    #Gráfica
    maximo = min(puncriti)
    minimo = max(puncriti)
    volmax = v.subs(x, maximo)
    volmin = v.subs(x, minimo)

    vol1=float(f"{volmax:.2f}")
    vol2=float(f"{volmin:.2f}")

    x1=float(f"{puncriti[0]:.2f}")
    x2=float(f"{puncriti[1]:.2f}")

    st.divider()
    st.header(":blue[Gráfica de la función del volumen y su derivada]")

    simpli_num = sp.lambdify(x, simpli, 'numpy')
    simpli_prime_num = sp.lambdify(x, derivada, 'numpy')

    x_vals = np.linspace(x1-5,x2+5, 100)

    y_vals = simpli_num(x_vals)
    y_prime_vals = simpli_prime_num(x_vals)
    fig,ax=plt.subplots()

    ax.plot(x_vals, y_vals, label="volumen")
    ax.plot(x_vals, y_prime_vals, label="derivada", linestyle='--')
    ax.set_ylim([vol2-5,vol1+5])
    ax.axhline(0, color='gray', linewidth=0.8)
    ax.axvline(0, color='gray', linewidth=0.8)
    ax.legend()

    st.pyplot(fig)
