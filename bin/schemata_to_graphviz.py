from graphviz import Digraph
from gdcdatamodel import edge_avsc_object, node_avsc_object

dot = Digraph(comment="High level graph representation of GDC data model",
              format='pdf')
dot.graph_attr['rankdir'] = 'RL'
dot.node_attr['fillcolor'] = 'lightblue'
dot.node_attr['style'] = 'filled'

node_schema = node_avsc_object.to_json()

for node in node_schema:
    dot.node(node['name'], node['name'])
    print node['name']

edge_schema = edge_avsc_object.to_json()

for edge in edge_schema:
    for field in edge['fields']:
        if field['name'] == 'node_labels':
            for node_label in field['type']:
                src_label, dst_label = node_label['name'].split(':')
                dot.edge(src_label, dst_label, edge['name'])

dot.render('docs/viz/gdc_data_model.gv')
