#!/usr/bin/env python

import os
import numpy as np

from util import *

if __name__ == "__main__":
    vertices, edge_ids, edges, edges_covariance = get_data(os.path.join(os.path.dirname(__file__), '../FRH_P_toro.graph'))

    draw_data_graph(vertices, edge_ids, edges, edges_covariance)
