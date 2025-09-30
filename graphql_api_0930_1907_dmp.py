# 代码生成时间: 2025-09-30 19:07:17
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from graphql import graphql_sync
from graphql.type import GraphQLSchema, GraphQLObjectType, GraphQLField, GraphQLInt, GraphQLString, GraphQLList


# Define the root schema for the GraphQL API
class QueryType(GraphQLObjectType):
    """Root query type for the GraphQL API"""
    hello = GraphQLField(GraphQLString, description="A simple type for getting started!")
    def resolve_hello(self, info):
        """Resolve the 'hello' field"""
        return "Hello, World!"

    add = GraphQLField(GraphQLInt, args={'a': GraphQLInt, 'b': GraphQLInt}, description="Adds two numbers")
    def resolve_add(self, info, **args):
        "