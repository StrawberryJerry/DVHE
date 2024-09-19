import torch
import torch.nn as nn
import torch.nn.functional as F
from model.graph_encoder import truncated_normal  # Ensure this import matches your project structure

class HNHNLayer(nn.Module):
    def __init__(self, in_dim, out_dim, act=None):
        super(HNHNLayer, self).__init__()
        self.in_dim = in_dim
        self.out_dim = out_dim
        self.act = act
        self.W_v2e = nn.Parameter(torch.zeros(in_dim, out_dim))
        self.W_e2v = nn.Parameter(torch.zeros(out_dim, in_dim))
        self.W_v2e.data = truncated_normal(self.W_v2e.data, std=0.02)
        self.W_e2v.data = truncated_normal(self.W_e2v.data, std=0.02)
        self.b_v = nn.Parameter(torch.zeros(out_dim))
        self.b_e = nn.Parameter(torch.zeros(out_dim))

    def forward(self, vertices_repr):
        # Compute the transformation of vertices to edges
        vertices_to_edges = torch.matmul(vertices_repr, self.W_v2e) + self.b_v
        if self.act is not None:
            vertices_to_edges = self.act(vertices_to_edges)

        # Compute the transformation of edges to vertices
        edges_to_vertices = torch.matmul(vertices_to_edges, self.W_e2v) + self.b_e
        if self.act is not None:
            edges_to_vertices = self.act(edges_to_vertices)

        return edges_to_vertices
