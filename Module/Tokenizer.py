import json
import re
from collections import Counter


class Tokenizer(object):
    def __init__(self, args):
        self.ann_path = args.ann_path

        self.ann = json.loads(open(self.ann_path, 'r').read())

    def create_vocabulary(self):
        total_token = []
        for example in self.ann['train']:
            tokens = self.clean_report(example['report']).split()
            for token in tokens:
                total_token.append(token)

        print(total_token)

    @staticmethod
    def clean_report(report):
        report = re.sub(r'\.{2,}', '.', report)
        report = re.sub(r'\s?\d+\.\s?', '. ', report)
        report = re.sub(r'[.,?;*!%^&_+():-\[\]{}]', '',report.replace('"', '').replace('/', '').replace('\\', '').replace("'", '').strip().lower())
        tokens = re.split(r'\. ', report)
        tokens = [token for token in tokens if token]
        cleaned_report = ' . '.join(tokens) + ' .'
        return cleaned_report

