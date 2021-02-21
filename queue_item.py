class QueueItem:
    def __init__(self, line, block_num):
        line = line.rstrip('\n').strip(' ')
        split_line = line.split(" ")
        self.term = split_line[0] # What is the term
        self.posting_list = line.split(" ")[1:] # Remove first item
        self.block_num = block_num # Tell us what block file this item comes from

    def GetTerm(self):
        return self.term

    def GetPostingList(self):
        return self.posting_list

    def GetBlockNum(self):
        return int(self.block_num)

    # We compare by term values first. If two items have the same term values, then we will
    # compare their block number.
    def __eq__(self, other):
        return ((self.term, int(self.block_num)) == (other.GetTerm(), other.GetBlockNum()))

    def __ne__(self, other):
        return ((self.term, int(self.block_num)) != (other.GetTerm(), other.GetBlockNum()))

    def __lt__(self, other):
        return ((self.term, int(self.block_num)) < (other.GetTerm(), other.GetBlockNum()))

    def __le__(self, other):
        return ((self.term, int(self.block_num)) <= (other.GetTerm(), other.GetBlockNum()))

    def __gt__(self, other):
        return ((self.term, int(self.block_num)) > (other.GetTerm(), other.GetBlockNum()))

    def __ge__(self, other):
        return ((self.term, int(self.block_num)) >= (other.GetTerm(), other.GetBlockNum()))

    def __repr__(self):
        return "%s %s" % (self.term, int(self.block_num))