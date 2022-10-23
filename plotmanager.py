from js import document, console, File
from pyodide.ffi import create_proxy
import FourierPlotter
import asyncio

def setup():
    getParams_proxy = create_proxy(getParams)
    e = document.getElementById("btn")
    e.addEventListener("click", getParams_proxy)

async def getParams(event):
    sinusoid_count = document.getElementById("sinusoid-count").value
    step_size = document.getElementById("x-axis-step-size").value
    selected_plots = document.getElementById("selected-plots").value

    # Sanitize sinusoid count and step size user input
    if (not sinusoid_count.isnumeric()) or (not step_size.isnumeric()):
        err = "Number of sinusoids and/or number of plot points must be an integer"
        console.log(err)
        Element("mpl").write(err)
        return
    err = "Sinusoid limit: 1000, Plot points limit: 500"
    if (len(sinusoid_count) > 4) or (len(step_size) > 4):
        console.log(err)
        Element("mpl").write(err)
        return
    sinusoidz = int(sinusoid_count)
    stepz = int(step_size)
    if (sinusoidz > 1000) or (stepz > 500):
        console.log(err)
        Element("mpl").write(err)
        return
    stepz = stepz * 2 # user puts in number of points per cycle, but plotting module takes in points per 2 cycles
    
    # Sanitize plot requests
    err = "please follow the example convention for entering plots you want to show"
    valid_chars = "01234567890, "
    for char in selected_plots:
        if not char in valid_chars:
            console.log(err)
            Element("mpl").write(err)
            return
    if len(selected_plots) > 30:
        err = "Too many plots selected"
        console.log(error)
        Element("mpl").write(err)
        return
    split_plotz = selected_plots.split(",")
    for plot in split_plotz:
        # check for comma errors (whitespace between numbers in split strings)
        try:
            int(plot)
        except:
            err = "Plots list has a syntax error. Check for commas."
            console.log(err)
            Element("mpl").write(err)
            return
    plotz = tuple(map(int, split_plotz))
    for plot in plotz:
        if plot > sinusoidz:
            err = "Plot #" + str(plot) + " is greater than number of composite sinusoids requested"
            console.log(err)
            Element("mpl").write(err)
            return

    fig = await FourierPlotter.graph(sinusoidz, stepz, *plotz)
    Element("mpl").write(fig)


setup()