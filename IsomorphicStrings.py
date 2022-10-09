def isIsomorphic(s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

g = isIsomorphic("badc", "baba")
h = isIsomorphic("egg", "add")
i = isIsomorphic("foo", "bar")
j = isIsomorphic("aaeaa","uuxyy")

print(g,h,i,j)