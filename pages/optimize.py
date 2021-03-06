from optlang import Model, Variable, Constraint, Objective
from .models import Option


def fact(meta, plazo, DD, Gm, F):
    # All the (symbolic) variables are declared, with a name and optionally a lower and/or upper bound.
    a = Variable('%ahorro', lb=0, ub=1)
    g = Variable('%otrosgastos', lb=0, ub=1)
    f = Variable('%fondoemergencia', lb=0, ub=1)

    # A constraint is constructed from an expression of variables and a lower and/or upper bound (lb and ub).
    c1 = Constraint(a + g + f, lb=1 ,ub=1)
    c2 = Constraint(g * DD, lb=Gm)
    #El % de ahorro * dinero disponible * el plazo debe ser estrictamente igual a la meta
    c3 = Constraint(a * DD * plazo, lb=meta ,ub=meta)
    c4 = Constraint(f * DD, lb=F, ub=F)

    # An objective can be formulated
    obj = Objective(a * DD * plazo, direction='max')

    # Variables, constraints and objective are combined in a Model object, which can subsequently be optimized.
    model = Model(name='Simple model')
    model.objective = obj
    model.add([c1, c2, c3, c4])

    status = model.optimize()
    #print("status:", model.status)
    #print("objective value:", model.objective.value)
    #print("----------")
    resultados = {'%ahorro':0, '%otrosgastos':0, '%fondoemergencia':0, 'status': status, 'months':plazo}
    for var_name, var in model.variables.iteritems():
        resultados[var_name] = round(var.primal*DD)
    if model.status == 'optimal':  
        print('Opcion 1:')
        print('Ahorrando mensual',resultados['%ahorro'],', lograras ahorrar',resultados['%ahorro']*plazo)
        print('Para otros gastos tendrías disponible mensual',resultados['%otrosgastos'])
        print('En',plazo,'meses')
    else:
        print('La meta no es factible con las condiciones dadas:')
        print('Con',DD,'disponible, ahorrar',meta,'en',plazo,'meses, con',Gm,'mínimo para otros gastos.')
    resultados['saving'] = resultados['%ahorro']
    resultados['other'] = resultados['%otrosgastos']
    resultados['emergency'] = resultados['%fondoemergencia']
    resultados['total'] = resultados['%ahorro'] * plazo
    resultados['msg'] = "Ahorrando mensual $ " + '{:,}'.format(resultados['saving']).replace(",",".") \
        + " , lograrás ahorrar $ " + '{:,}'.format(resultados['total']).replace(",",".") \
        + ". Para otros gastos tendrías disponible mensual $ " \
        + '{:,}'.format(resultados['other']).replace(",",".") + " en "+str(resultados['months']) + " meses."
    return resultados

def tiempo(meta, DD, Gm, F):
    plazo = 0
    while plazo <= 60:
        a = Variable('%ahorro', lb=0, ub=1)
        g = Variable('%otrosgastos', lb=0, ub=1)
        f = Variable('%fondoemergencia', lb=0, ub=1)

    # A constraint is constructed from an expression of variables and a lower and/or upper bound (lb and ub).
        c1 = Constraint(a + g + f, lb=1 ,ub=1)
        c2 = Constraint(g * DD, lb=Gm)
    #El % de ahorro * dinero disponible * el plazo debe ser estrictamente igual a la meta
        c3 = Constraint(a * DD * plazo, lb=meta, ub=meta)
        c4 = Constraint(f * DD, lb=F, ub=F)
    # An objective can be formulated
        obj = Objective(a * DD * plazo, direction='max')
    # Variables, constraints and objective are combined in a Model object, which can subsequently be optimized.
        model = Model(name='Simple model')
        model.objective = obj
        model.add([c1, c2, c3, c4])
        resultados = dict()
        status = model.optimize()
        for var_name, var in model.variables.iteritems():
            #print(var_name, "=", round(var.primal * DD))
            resultados[var_name] = round(var.primal*DD)
        if model.status == 'optimal':
            print('Opción 2:')
            print('Ahorrando mensual',resultados['%ahorro'],', lograras ahorrar',resultados['%ahorro']*plazo)
            print('Para otros gastos tendrías disponible mensual',resultados['%otrosgastos'])
            print('En',plazo,'meses')
            break
        plazo +=1
    if plazo > 60:
        status = 'overtime'
    resultados.update({'status': status, 'months': plazo})
    resultados['months'] = plazo
    resultados['saving'] = resultados['%ahorro']
    resultados['other'] = resultados['%otrosgastos']
    resultados['emergency'] = resultados['%fondoemergencia']
    resultados['total'] = resultados['%ahorro'] * plazo
    resultados['msg'] = "Ahorrando mensual $ " + '{:,}'.format(resultados['saving']).replace(",",".") \
        + " , lograrás ahorrar $ " + '{:,}'.format(resultados['total']).replace(",",".") \
        + ". Para otros gastos tendrías disponible mensual $ " \
        + '{:,}'.format(resultados['other']).replace(",",".") + " en "+str(resultados['months']) + " meses."
    return resultados


def costos(meta, plazo, DD, Gm, F):
    a = Variable('%ahorro', lb=0, ub=1)
    g = Variable('%otrosgastos', lb=0, ub=1)
    f = Variable('%fondoemergencia', lb=0, ub=1)

    # A constraint is constructed from an expression of variables and a lower and/or upper bound (lb and ub).
    c1 = Constraint(a + g + f, lb=1 ,ub=1)
    c2 = Constraint(g * DD, lb=Gm, ub=Gm)
  #El % de ahorro * dinero disponible * el plazo debe ser estrictamente igual a la meta
    c3 = Constraint(a * DD * plazo, lb=meta)
    c4 = Constraint(f * DD, lb=F, ub=F)

  # An objective can be formulated
    obj = Objective(a * DD * plazo, direction='max')

  # Variables, constraints and objective are combined in a Model object, which can subsequently be optimized.
    model = Model(name='Simple model')
    model.objective = obj
    model.add([c1, c2, c3, c4])

    status = model.optimize()
    resultados = {'status': status, 'months': plazo}

    for var_name, var in model.variables.iteritems():
        #print(var_name, "=", round(var.primal * DD))
        resultados[var_name] = round(var.primal*DD)
    if model.status == 'optimal': 
        print('Opcion 3:')
        print('Ahorrando mensual',resultados['%ahorro'],', lograras ahorrar',resultados['%ahorro']*plazo)
        print('Para otros gastos tendrías disponible mensual',resultados['%otrosgastos'])
        print('En',plazo,'meses')
    else:
        print('La meta no es factible con las condiciones dadas:')
        print('Con',DD,'disponible, ahorrar',meta,'en',plazo,'meses, con',Gm,'mínimo para otros gastos.')
    resultados['saving'] = resultados['%ahorro']
    resultados['other'] = resultados['%otrosgastos']
    resultados['emergency'] = resultados['%fondoemergencia']
    resultados['total'] = resultados['%ahorro'] * plazo
    resultados['msg'] = "Ahorrando mensual $ " + '{:,}'.format(resultados['saving']).replace(",",".") \
        + " , lograrás ahorrar $ " + '{:,}'.format(resultados['total']).replace(",",".") \
        + ". Para otros gastos tendrías disponible mensual $ " \
        + '{:,}'.format(resultados['other']).replace(",",".") + " en "+str(resultados['months']) + " meses."
    return resultados

# solver
def solve(meta, plazo, DD, Gm, F):
    res_1 = fact(meta, plazo, DD, Gm, F)
    res_2 = tiempo(meta, DD, Gm, F)
    res_3 = costos(meta, plazo, DD, Gm, F)

    return {'res_1': res_1, 'res_2': res_2,'res_3': res_3}