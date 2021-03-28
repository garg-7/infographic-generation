from typing import ValuesView
import sys

class Task:
    def __init__(self, name):
        self.name = name
        self.properties = [] # list of PropertyDescriptor obejects

class PropertyDescriptor:
    def __init__(self, prop_name):
        self.prop_name = prop_name
        self.values = [] # list of PropertyValue objects

class PropertyValue:
    def __init__(self, value, label: str, index: int):
        self.value = value
        self.label = label
        self.index = index

def main():

    results_file = open('raw_text_result.txt', 'r').readlines()
    input_file = list(open('raw_text.txt', 'r').readlines())

    country_node = PropertyDescriptor('Country')
    indicator_node = PropertyDescriptor('Indicator')
    value_node = PropertyDescriptor('Value')
    time_node = PropertyDescriptor('Time')
    placeholder_node = PropertyDescriptor('Placeholders')

    task = Task('Indicator Change Representation')
    task.properties.append(country_node)
    task.properties.append(value_node)
    task.properties.append(indicator_node)
    task.properties.append(time_node)
    task.properties.append(placeholder_node)


    for j, line in enumerate(results_file):
        labels = line.strip().split(' ')[1:-1] # remove the CLS and SEP token labels.
        text_tokens = input_file[j].strip().split(' ')
        
        assert len(labels) == len(text_tokens)
        
        for i, l in enumerate(labels):
            if l.endswith('-C'):
                country_node.values.append(PropertyValue(text_tokens[i], l, i))
            elif l.endswith('-T'):
                time_node.values.append(PropertyValue(text_tokens[i], l, i))
            elif l.endswith('-V'):
                value_node.values.append(PropertyValue(text_tokens[i], l, i))
            elif l.endswith('-P'):
                indicator_node.values.append(PropertyValue(text_tokens[i], l, i))
            elif l=='O':
                placeholder_node.values.append(PropertyValue(text_tokens[i], l, i))
            else:
                print(f'Invalid character on results line {j}. Exiting...')
                sys.exit()

        print('Country: ', end='')
        for i in country_node.values:
            print(i.value, end=' ')
        
        print('\nIndicator: ', end='')
        for i in indicator_node.values:
            print(i.value, end=' ')

        print('\nValue: ', end='')
        for i in value_node.values[:-1]:
            print(i.value, end='')
        print(' '+value_node.values[-1].value)

        print('Time: ', end='')
        for i in time_node.values:
            print(i.value, end=' ')
        
        print('\nPlaceholder tokens: ', end='')
        for i in placeholder_node.values:
            print(i.value, end=' ')

        print('\n')

if __name__=='__main__':
    main()