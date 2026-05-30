from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ("Rain", "Traffic"),
    ("Accident", "Traffic")
])

cpd_rain = TabularCPD(
    variable="Rain",
    variable_card=2,
    values=[[0.7], [0.3]]
)

cpd_accident = TabularCPD(
    variable="Accident",
    variable_card=2,
    values=[[0.8], [0.2]]
)

cpd_traffic = TabularCPD(
    variable="Traffic",
    variable_card=2,
    values=[
        [0.95, 0.6, 0.7, 0.1],
        [0.05, 0.4, 0.3, 0.9]
    ],
    evidence=["Rain", "Accident"],
    evidence_card=[2,2]
)

model.add_cpds(
    cpd_rain,
    cpd_accident,
    cpd_traffic
)

model.check_model()

infer = VariableElimination(model)

result = infer.query(
    variables=["Traffic"],
    evidence={"Rain":1}
)

print(result)
