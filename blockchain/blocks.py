import hashlib as hasher
import json
import datetime as date


class BlockTypes:
    genesis_block = 0
    chat_block = 1
    replay_block = 2
    comment_block = 3


class GenesisTypes:
    private_chat = 0
    group_chat = 1
    page = 2


class Block():
    def __init__(self, index, creator, block_type, data, timestamp, genesis_index, previous_hash):
        self.index = index
        self.creator = creator
        self.block_type = block_type
        self.data = data
        self.genesis_index = genesis_index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) +
                    str(self.creator) +
                    str(self.block_type) +
                    str(self.data) +
                    str(self.genesis_index) +
                    str(self.timestamp) +
                    str(self.previous_hash)).encode())
        return sha.hexdigest()

    def to_json(self):
        return {"index": self.index, "creator": self.creator, "block_type": self.block_type,
                "data": self.data, "timestamp": str(self.timestamp), "genesis_index": self.genesis_index,
                "previous_hash": self.previous_hash, "hash": self.hash}

    @staticmethod
    def from_json(block_json: json):
        return Block(block_json['index'], block_json['creator'], block_json['block_type'], block_json['data'],
                     block_json['timestamp'], block_json['genesis_index'], block_json['previous_hash'])

# def create_genesis_block():
#     # Manually construct a block with
#     # index zero and arbitrary previous hash
#     return Block(0, "CryptoGram Genesis Block",,, str(date.datetime.now()), "0", "0", "0")
#
#     def create_vertical_genesis_block(chat_name, previous_horizontal_hash):
#         return Block(0, chat_name,,, str(date.datetime.now()), "0", previous_horizontal_hash, "0")
