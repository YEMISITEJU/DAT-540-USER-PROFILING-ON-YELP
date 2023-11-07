from mrjob.job import MRJob
import re
from mrjob.protocol import TextValueProtocol

class MRCountSum(MRJob):
    OUTPUT_PROTOCOL = TextValueProtocol
    def mapper(self, _, line):
        line = line.strip() # remove leading and trailing whitespace
        line = re.sub('[{}"]','', line)
        fields = line.split(',')
        new_fields = list(filter(lambda x: x.__contains__(':'), fields))
        other_friends = list(filter(lambda x: not x.count(':'), fields))

        def parseKeyValues(pairs):
            newData = {}
            for pair in pairs:
                data = pair.split(':')
                newData[data[0]] = int(data[1]) if data[1].isdigit() else data[>
            return newData
        dict = parseKeyValues(new_fields)
        dict['friends'] = (0 if dict['friends'] == '' else 1) + len(other_frien>
        values = list(dict.values())
        strValues = ','.join(str(value) for value in values)
        yield '', strValues

if __name__ == '__main__':
    MRCountSum.run()