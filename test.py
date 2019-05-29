d = len(sigma)
P = matrix(sigma)
q = matrix(np.zeros(d, float))
A = matrix([
    np.ones(d, float).tolist(), r_i.tolist()
    ]).trans()
b = matrix([1.0, float(rho)])
##########################################################
# Se define la restricción para cuando las ventas en corto
# están permitidas
##########################################################
diagonal = np.zeros((d, d), float)
np.fill_diagonal(diagonal, -1.0)

G = matrix(diagonal)
h = matrix(np.zeros(d, float))
##########################################################
# Se revisa la condición de Ventas en corto para asignar
# valores a G y h
##########################################################
if Ventas_en_corto == True:
    G = None
    h = None
else:
    G = G
    h = h
