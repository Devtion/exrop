from Exrop import Exrop

rop = Exrop("/bin/ls")
rop.find_gadgets(cache=True)
#chain = rop.set_regs({'rdi':0x41414141, 'rsi': 0x42424242, 'rdx':0x43434343, 'rax':0x44444444})
chain = rop.set_writes({0x41414141: 0xdeadbeefff, 0x43434343: 0x00110011})
chain.dump()