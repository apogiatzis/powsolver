from powsolver import PoWSolver

pow_solver = PoWSolver(parallel=True)
pow_solver.parse(
    "Please submit a printable string X, such that {alg}(X)[{start:d}:] = {target} and len(X) = {len}",
    "Please submit a printable string X, such that sha256(X)[-6:] = 86d113 and len(X) = 11"
)
sol = pow_solver.solve()
print(sol)