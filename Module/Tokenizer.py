import json
import re
from collections import Counter


class Tokenizer(object):
    def __init__(self, args):
        self.ann_path = args.ann_path
        self.threshold = args.threshold
        self.ann = json.loads(open(self.ann_path, 'r').read())
        self.token2idx, self.idx2token = self.create_vocabulary()

    def create_vocabulary(self):
        total_tokens = []
        for example in self.ann['train']:
            tokens = self.clean_report(example['report']).split()
            for token in tokens:
                total_tokens.append(token)

        counter = Counter(total_tokens)
        vocab = [k for k, v in counter.items() if v >= self.threshold] + ['<unk>']
        vocab.sort()
        token2idx, idx2token = {}, {}
        for idx, token in enumerate(vocab):
            token2idx[token] = idx + 1
            idx2token[idx + 1] = token

        return token2idx, idx2token

    @staticmethod
    def clean_report(report):
        report = re.sub(r'\.{2,}', '.', report)
        report = re.sub(r'\s?\d+\.\s?', '. ', report)
        report = re.sub(r'[.,?;*!%^&_+():-\[\]{}]', '',
                        report.replace('"', '').replace('/', '').replace('\\', '').replace("'", '').strip().lower())
        tokens = re.split(r'\. |\s|-', report)
        tokens = [token for token in tokens if token]
        # cleaned_report = ' . '.join(tokens) + ' .'
        cleaned_report = ' '.join(tokens)
        return cleaned_report

    def get_vocab_size(self):
        return len(self.token2idx)

    def get_token_by_id(self, id):
        return self.idx2token[id]

    def get_idx_by_token(self, token):
        if token not in self.token2idx:
            return self.token2idx['<unk>']
        return self.token2idx[token]

    def decoder(self, ids):
        txt_tokens = [
            self.idx2token[idx] if idx > 0 and idx in self.idx2token
            else self.idx2token[self.token2idx['<unk>']]
            for idx in ids
        ]
        txt = ' '.join(txt_tokens)
        return txt
