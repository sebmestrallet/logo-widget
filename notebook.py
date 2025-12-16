import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""
    # Anywidget demo

    [anywidget.dev](https://anywidget.dev/)
    """)
    return


@app.cell
def _():
    import anywidget
    import traitlets
    import marimo as mo
    return anywidget, mo, traitlets


@app.cell
def _(mo):
    mo.md(r"""
    Controls (using `marimo.ui.*`)
    """)
    return


@app.cell
def _(mo):
    X_INIT = 400
    Y_INIT = 200
    SIZE_INIT = 1.0
    ROTATION_INIT = 0

    x = mo.ui.number(
        start=0,
        stop=1000,
        value=X_INIT,
        label="x"
    )

    y = mo.ui.number(
        start=0,
        stop=1000,
        value=Y_INIT,
        label="y"
    )

    size = mo.ui.slider(
        start=0.5,
        stop=4.0,
        step=0.1,
        value=SIZE_INIT,
        label="Size"
    )

    rotation = mo.ui.slider(
        start=0,
        stop=360,
        step=1,
        value=ROTATION_INIT,
        label="Rotation"
    )

    mo.callout(mo.vstack([
        x,
        y,
        size,
        rotation
    ]))
    return ROTATION_INIT, SIZE_INIT, X_INIT, Y_INIT, rotation, size, x, y


@app.cell
def _(mo):
    mo.md(r"""
    Widget definition
    """)
    return


@app.cell
def _(ROTATION_INIT, SIZE_INIT, X_INIT, Y_INIT, anywidget, traitlets):
    class Widget(anywidget.AnyWidget):
        _esm = "widget.js"
        x = traitlets.Int(X_INIT).tag(sync=True)
        y = traitlets.Int(Y_INIT).tag(sync=True)
        size = traitlets.Float(SIZE_INIT).tag(sync=True)
        rotation = traitlets.Int(ROTATION_INIT).tag(sync=True)
        count = traitlets.Int(0).tag(sync=True)

    print(Widget)
    return (Widget,)


@app.cell
def _(mo):
    mo.md(r"""
    Widget instantiation
    """)
    return


@app.cell
def _(Widget, mo, rotation, size, x, y):
    widget = mo.ui.anywidget(Widget(
        x=x.value,
        y=y.value,
        size=size.value,
        rotation=rotation.value
    ))
    widget
    return (widget,)


@app.cell
def _(mo):
    mo.md(r"""
    Dictionnary of values synchronized between Python and Javascript:
    """)
    return


@app.cell
def _(widget):
    widget.value
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
