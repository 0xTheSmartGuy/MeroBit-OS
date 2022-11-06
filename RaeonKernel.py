from importlib.abc import MetaPathFinder
import secrets, sys, base64
def gentable(addrspace): # Address space generator
   global a
   a = {"0x"+secrets.token_hex(addrspace//8) for i in range(addrspace//8)}
def attrib():
   l = False
   while l == False:
       w=random.choice(a.keys())
       if a[w] is not None:
        if len(w) == a.index(w):
         return "Error: No more space!"
        else:
             continue
       else:
            a[w]==__file__
            l=True
def proc_rdmem_kspace():
   woot = 0
   m = []
   for i in a:
      m.append(a[list(a.keys())[woot]])
      woot += 1
   return m # No address space isolation
def proc_rdmem_uspace():
   woot = 0
   for i in a:
       if a[list(a.keys())[woot]] == __file__:
        return "Used"
       else:
            return "Nani" # Address space isolation
       woot += 1
if "# Allowed to rdmem_kspace" in open(__file__).read(): 
 pass
else:
     def proc_rdmem_kspace():
        return None # Brick the unauthorized rdp systems!
if __name__ == "__main__":
  exec(base64.b64decode(b"cHJpbnQoIkJsZWl0dWcgcDFzcyIp").decode())
else:
     pass
