import streamlit as st
import numpy as np
import plotly.graph_objects as go
from sympy import symbols, sympify, lambdify, diff, solve, integrate, simplify

# Page configuration
st.set_page_config(page_title="Equation Visualizer", layout="wide")

st.title("📈 Equation Visualizer")
mode = st.radio(
    "Select Mode",
    ["2D Graph", "3D Surface"]
)

st.write(
    """
    Enter a mathematical expression in terms of x.

    Examples:
    - x**2
    - sin(x)
    - cos(x)
    - exp(x)
    - log(x)
    """
)

# User input
if mode == "2D Graph":
    equation = st.text_input(
        "Enter equation",
        value="x**2"
    )
else:
    equation = st.text_input(
        "Enter z = f(x,y)",
        value="x**2 + y**2"
    )

# Range selection
x_min = st.number_input("X min", value=-10.0)
x_max = st.number_input("X max", value=10.0)
show_derivative = st.checkbox("Show Derivative")
show_critical_points = st.checkbox("Show Critical Points")
show_roots = st.checkbox("Show Roots")
show_integral = st.checkbox("Show Integral")



if st.button("Plot Graph"):
    if mode == "3D Surface":

        try:

            x, y = symbols("x y")

            expr = sympify(equation)

            surface_func = lambdify(
                (x, y),
                expr,
                modules=["numpy"]
            )

            x_vals = np.linspace(-10, 10, 100)
            y_vals = np.linspace(-10, 10, 100)

            X, Y = np.meshgrid(
                x_vals,
                y_vals
            )

            Z = surface_func(X, Y)

            fig = go.Figure(
                data=[
                    go.Surface(
                        x=X,
                        y=Y,
                        z=Z
                    )
                ]
            )

            fig.update_layout(
                title=f"z = {expr}",
                scene=dict(
                    xaxis_title="X",
                    yaxis_title="Y",
                    zaxis_title="Z"
                ),
                height=800
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.stop()

        except Exception as e:

            st.error(f"3D Error: {e}")

            st.stop()

    try:
        # Define symbolic variable
        x, y = symbols("x y")
        

        # Convert string to symbolic expression
        expr = sympify(equation)
        
        if show_derivative:
            derivative_expr = diff(expr, x)
            
        critical_points = []

        if show_critical_points:

            derivative_expr = diff(expr, x)

            critical_x = solve(derivative_expr, x)

            for point in critical_x:
                try:
                    x_val = float(point)

                    y_val = float(expr.subs(x, point))

                    critical_points.append((x_val, y_val))

                except:
                    pass
        roots = []
        if show_roots:

            root_values = solve(expr, x)

            for root in root_values:
                try:
                    x_root = float(root)

                    roots.append(x_root)

                except:
                    pass
        if show_integral:
            a = st.number_input("Lower Bound", value=0.0)
            b = st.number_input("Upper Bound", value=3.0)      
        integral_expr = None
        area_value = None

        if show_integral:

            integral_expr = integrate(expr, x)

            area_value = integrate(expr, (x, a, b))
        # Create numerical function
        f = lambdify(x, expr, modules=["numpy"])

        # Generate x values
        x_vals = np.linspace(x_min, x_max, 1000)

        # Compute y values
        y_vals = f(x_vals)

        # Create graph
        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=x_vals,
                y=y_vals,
                mode="lines",
                name=str(expr)
            )
        )
        if show_derivative:

            derivative_func = lambdify(
                x,
                derivative_expr,
                modules=["numpy"]
            )

            derivative_y = derivative_func(x_vals)

        fig.add_trace(
            go.Scatter(
                x=x_vals,
                y=derivative_y,
                mode="lines",
                name=f"Derivative: {derivative_expr}"
        )
    )
        fig.update_layout(
            title=f"y = {expr}",
            xaxis_title="x",
            yaxis_title="y",
            hovermode="x unified"
        )
        fig.update_layout(
            xaxis=dict(
                zeroline=True,
                zerolinewidth=2,
                zerolinecolor="white",
                showgrid=True
            ),
            yaxis=dict(
                zeroline=True,
                zerolinewidth=2,
                zerolinecolor="white",
                showgrid=True
            )
        )
        if show_critical_points and critical_points:
            critical_x, critical_y = zip(*critical_points)
            fig.add_trace(
                go.Scatter(
                    x=critical_x,
                    y=critical_y,
                    mode="markers",
                    name="Critical Points",
                    marker=dict(color="red", size=10)
                )
            )
        if roots:

            fig.add_trace(
                go.Scatter(
                    x=roots,
                    y=[0] * len(roots),
                    mode="markers",
                    marker=dict(
                        size=12,
                        color="green"
                    ),
                    name="Roots"
                )
            )
            
        if show_integral:

            x_fill = np.linspace(a, b, 500)
            y_fill = f(x_fill)

            fig.add_trace(
                go.Scatter(
                    x=np.concatenate([x_fill, x_fill[::-1]]),
                    y=np.concatenate([y_fill, np.zeros_like(y_fill)]),
                    fill="toself",
                    mode="lines",
                    name="Area Under Curve"
                )
            )
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Parsed Expression")
        st.code(str(expr))
                
        if critical_points:

            st.subheader("Critical Points")

            for x_c, y_c in critical_points:

                st.write(
                    f"x = {x_c:.4f}, y = {y_c:.4f}"
        )
        if roots:

            st.subheader("Roots")

            for root in roots:

                st.write(f"x = {root:.4f}")
    except Exception as e:
        st.error(f"Error: {e}")
        
        if show_derivative:
            st.subheader("Derivative")
            st.code(str(derivative_expr))
        if show_integral:

            st.subheader("Indefinite Integral")

            st.code(str(integral_expr))

            st.subheader("Definite Integral")

            st.write(f"Integral from {a} to {b} = {float(area_value):.6f}")