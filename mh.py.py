import ast
import operator as op


OPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}

def safe_eval(expr: str) -> float:
    node = ast.parse(expr, mode="eval").body

    def _eval(n):
        
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return float(n.value)

       
        if isinstance(n, ast.UnaryOp) and type(n.op) in OPS:
            return OPS[type(n.op)](_eval(n.operand))

        
        if isinstance(n, ast.BinOp) and type(n.op) in OPS:
            left = _eval(n.left)
            right = _eval(n.right)
            if isinstance(n.op, ast.Div) and right == 0:
                raise ZeroDivisionError
            return OPS[type(n.op)](left, right)

        
        raise ValueError("Invalid expression")

    return _eval(node)

while True:
    expr = input("benevis chikar konam? :").strip()
    if expr.lower() == "q":
        print("bye bye sisi")
        break

    try:
        result = safe_eval(expr)
        
        if result.is_integer():
            print(f"Result: {int(result)}\n")
        else:
            print(f"Result: {result}\n")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.\n")
    except Exception:
        print("Error: Invalid expression. Use only numbers and + - * / ( ).\n")
