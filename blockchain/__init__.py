import blockchain.blocks
import json


class BlockBook:
    def __init__(self, block_chain_data_base_path):
        self.block_chain_data_base_path = block_chain_data_base_path
        file = open(block_chain_data_base_path, 'w+')
        lines = file.readlines()
        # print(type(lines[0]))
        if lines.__len__() == 0:
            self.latest_blocks = list()
            json.dump('{"Book": []}', file)
        elif lines.__len__() < 1000:
            self.latest_blocks = [json.load(block) for block in lines[::-1][-lines.__len__():-1]]
        else:
            self.latest_blocks = [json.load(block) for block in lines[::-1][-1000:-1]]

        # file.close()

    def append_new_block(self, block: blocks.Block):
        with open(self.block_chain_data_base_path,'a+') as file:
            json.dump(block.to_json(), file)
            # file.writelines([str(block.to_json())+'\n'])
            self.latest_blocks.append(block.to_json())
        file.close()
