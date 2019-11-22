from blockchain.blocks import *

import blockchain
import time

block_book = blockchain.BlockBook('book.json')

b = Block(0, 'Root', BlockTypes.genesis_block, '', time.time(), 0, '')
# for i in range(3):
#     block_book.append_new_block(b)
# block_book.close()
a = Block.from_json(b.to_json())
print(a.to_json())
print()