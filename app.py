from flask import Flask, json, jsonify, render_template, url_for
import copy
from operator import itemgetter

import dynamic2
import metaheuristique
import metaheuristique2
import polynomial
import dynamic

app = Flask(__name__)



"""
**********************************************************************************************************************
                                                    Home
**********************************************************************************************************************
"""


@app.route("/")
def index():
    return render_template('index.html')



"""
**********************************************************************************************************************
                                                Main Problme
**********************************************************************************************************************
"""


@app.route("/problem1Algo")
def problem1Algo():
    return render_template("/indexx.html")


@app.route("/problem2Algo")
def problem2Algo():
    return render_template("/indexx2.html")


"""
**********************************************************************************************************************
                                Polynomial Algorithm for Problem 1 with different data
**********************************************************************************************************************
"""
"""
Plynomial algorithm for 10 tasks 
"""

@app.route("/runProb1PolyData10")
def poly10():
    data = polynomial.polyFor("P1_n10.txt")
    return data
app.jinja_env.globals.update(poly10=poly10)

"""
Plynomial algorithm for 50 tasks 
"""


@app.route("/runProb1PolyData50")
def poly50():
    data = polynomial.polyFor("P1_n50.txt")
    return data

app.jinja_env.globals.update(poly50=poly50)


"""
Plynomial algorithm for 200 tasks 
"""


@app.route("/runProb1PolyData200")
def poly200():
    data = polynomial.polyFor("P1_n200.txt")
    return data

app.jinja_env.globals.update(poly200=poly200)


"""
Plynomial algorithm for 500 tasks 
"""


@app.route("/runProb1PolyData500")
def poly500():
    data = polynomial.polyFor("P1_n500.txt")
    return data

app.jinja_env.globals.update(poly500=poly500)


"""
**********************************************************************************************************************
                                Meta-Heuristic Algorithm for Problem 1 with different data
**********************************************************************************************************************
"""
"""
Meta-heuristic algorithm for 10 tasks 
"""


@app.route("/runProb1MataData10")
def meta10():
    data = metaheuristique.VNS("P1_n10.txt")
    return data

app.jinja_env.globals.update(meta10=meta10)


"""
Meta-heuristic algorithm for 50 tasks 
"""


@app.route("/runProb1MataData50")
def meta50():
    data = metaheuristique.VNS("P1_n50.txt")
    return data

app.jinja_env.globals.update(meta50=meta50)


"""
Meta-heuristic algorithm for 200 tasks 
"""


@app.route("/runProb1MataData200")
def meta200():
    data = metaheuristique.VNS("P1_n200.txt")
    return data

app.jinja_env.globals.update(meta200=meta200)


"""
Meta-heuristic algorithm for 500 tasks 
"""


@app.route("/runProb1MataData500")
def meta500():
    data = metaheuristique.VNS("P1_n500.txt")
    return data

app.jinja_env.globals.update(meta500=meta500)


"""
**********************************************************************************************************************
                                Dynamic Algorithm for Problem 1 with different data
**********************************************************************************************************************
"""

@app.route("/runProb1DynamicData10")
def dynamic10():
    data = dynamic.main_function()
    return data

app.jinja_env.globals.update(dynamic10=dynamic10)

"""
**********************************************************************************************************************
                                Meta-Heuristic Algorithm for Problem 1 with different data
**********************************************************************************************************************
"""
"""
Meta-heuristic algorithm for 10 tasks 
"""


@app.route("/runProb2MataData10")
def meta2_10():
    data = metaheuristique2.VNS("P2_n10.txt")
    return data

app.jinja_env.globals.update(meta2_10=meta2_10)


"""
Meta-heuristic algorithm for 50 tasks 
"""


@app.route("/runProb2MataData100")
def meta2_100():
    data = metaheuristique2.VNS("P2_n100.txt")
    return data

app.jinja_env.globals.update(meta2_100=meta2_100)

"""
Meta-heuristic algorithm for 200 tasks 
"""


@app.route("/runProb2MataData200")
def meta2_200():
    data = metaheuristique2.VNS("P2_n200.txt")
    return data

app.jinja_env.globals.update(meta2_200=meta2_200)
"""
Meta-heuristic algorithm for 500 tasks 
"""
@app.route("/runProb2MataData500")
def meta2_500():
    data = metaheuristique2.VNS("P2_n500.txt")
    return data

app.jinja_env.globals.update(meta2_500=meta2_500)

"""
**********************************************************************************************************************
                                Dynamic Algorithm for Problem 2 with different data
**********************************************************************************************************************
"""

@app.route("/runProb2DynamicData10")
def dynamic2_10():
    data = dynamic2.main_function()
    return data

app.jinja_env.globals.update(dynamic2_10=dynamic2_10)
"""
**********************************************************************************************************************
                                        Entry Data for Problem 1
**********************************************************************************************************************
"""


@app.route("/enterDatapoly1")
def enterDatapoly():
    return render_template("polynomialResult.html")


@app.route("/enterDatameta1")
def enterDatameta1():
    return render_template("/metaheuristicResult1.html")


@app.route("/enterDatadyn1")
def enterDatadyn1():
    return render_template("/dynamicResult1.html")


"""
**********************************************************************************************************************
                                        Entry Data for Problem 2
**********************************************************************************************************************
"""


@app.route("/enterDatameta2")
def enterDatameta2():
    return render_template("/metaheuristicResult2.html")


@app.route("/enterDatadyn2")
def enterDatadyn2():
    return render_template("/dynamicResult2.html")


"""
**********************************************************************************************************************
                                                Main function
**********************************************************************************************************************
"""
if __name__ == "__main__":
    app.run()
