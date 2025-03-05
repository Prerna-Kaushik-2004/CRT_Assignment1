'''Ques-3: Use list comprehension to generate all Pythagorean triplets (a, b, c)
where a² + b² = c² and a, b, c ≤ 50.'''
l = [(a, b, c) for a in range(1, 51) for b in range(1, 51) for c in range(1, 51) if a**2 + b**2 == c**2]
print("Pythagoras triplets: " ,l)