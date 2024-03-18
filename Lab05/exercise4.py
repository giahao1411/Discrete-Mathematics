p = "Phong has Visa"
q = "Phong can fly"
r = "Phong can speak English"
t = "Phong goes to america"

s1 = "s1 = q implies t"
s2 = "s2 = p implies t"
s3 = "s3 = r implies t"

print("", "p =", p, "\n", "q =", q, "\n", "r =", r, "\n", "t =", t)
print("\n", s1, "\n", s2, "\n", s3, "\n")

p = "An wake up late"
q = "the traffic is flowing smooth"
not_q = "the traffic is heavy"
r = "school day"
s = "An have go to school"
v = "An is late for school"

s1 = "s1 = ~q"
s2 = "s2 = p implies (v and r)"
s3 = "s3 = s and r"
s4 = "s4 = ~s implies ~v"

print(
    "",
    "p =",
    p,
    "\n",
    "q =",
    q,
    "\n",
    "¬q =",
    not_q,
    "\n",
    "r =",
    r,
    "\n",
    "s =",
    s,
    "\n",
    "v =",
    v,
)
print("\n", s1, "\n", s2, "\n", s3, "\n", s4)
