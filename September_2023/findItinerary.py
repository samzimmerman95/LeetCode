"""
332. Reconstruct Itinerary

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # Create a graph representation of this data. Cities are nodes, flights are edges.
        # We can represent that in a dictionary. Nodes a keys, and edges as values. 
        # Want all cities as keys, even if they do not have edges. Hence the set first, then filling in the edges
        nodes = {j for i in tickets for j in i}
        graph = {}
        for n in nodes:
            graph[n] = []
        for t in tickets:
            graph[t[0]].append(t[1])

        # As there is the possibility for mutliple solutions, and we have to return the itinerary with smallest lexical order
        # we sort the list of edges in reverse order so smallest lexical order comes last.
        
        for node in graph:
            graph[node] = sorted(graph[node],reverse=True)

        print(graph)
        visited = []

        # This type of graph is a Euler Path, which means you can use every edge once.
        # Traverse this in a DFS style manner, but the order of returning the nodes is slightly different than standard DFS (I think).
        # We know that a node that has no outward path (or less outward than inward) must be at the end of the path.
        # If the node has an edge, we follow it. We also remove that edge from the graph so it can not be followed again.
        # We continue to recursively follow edges until there is not one to follow, we append that node to the visited array.
        # The recursion backtracks, and continues following edges until the path runs out, and appending when it does. 

        def findPath(departure):
            while graph[departure]:
                findPath(graph[departure].pop())
            visited.append(departure)
        
        # Start at JFK
        findPath("JFK")

        # Return the array in reverse order because the starting airport is added last.
        return visited[::-1]