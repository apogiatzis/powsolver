import hashlib
import logging
import string
import pathos.multiprocessing as mp

from functools import partial
from itertools import product
from parse import parse

logger = logging.getLogger(__name__)

class PoWSolver:
    def __init__(self, parallel=False, charset=string.ascii_letters + string.digits, processes=8):
        self.charset = charset
        self.parallel = parallel
        self.processes = processes

    def parse(self, fmt, pow_str):
        """
        Uses a string format to parse parameters of the PoW puzzle
        """
        parsed = parse(fmt, pow_str)

        self.alg = getattr(hashlib, parsed["alg"])
        self.target = parsed["target"]
        self.len = int(parsed.named.get("len", 4))
        self.slice = slice(
            parsed.named.get("start", None),
            parsed.named.get("end", None),
            parsed.named.get("step", None),
        )

    def solve(self):
        """
        Solves the given proof of work puzzle
        """
        return self.solve_parallel() if self.parallel else self.solve_sequential()
        

    def solve_sequential(self):
        """
        Solves the given proof of work puzzle in a sequential manner
        """
        for proof in product(self.charset, repeat=self.len):
            proof = "".join(proof).encode()
            if self.valid_proof(proof):
                return proof
        return None

    def solve_parallel(self):
        """
        Solves the given proof of work puzzle in a parallel manner
        """
        pool = mp.Pool(self.processes)

        def test(x):
            return (x, self.valid_proof(x))

        gen = map(lambda s:''.join(s).encode(), product(self.charset, repeat=self.len))
        proofs = pool.imap_unordered(test, gen, chunksize=10000)
        pool.close()
        for proof, valid in proofs:
            if valid:
                pool.terminate()
                break
        pool.join()
        return proof if valid else None

    def valid_proof(self, proof):
        """Verifies that the proof matches the target"""
        h = self.alg(proof).hexdigest()[self.slice]
        return h == self.target
