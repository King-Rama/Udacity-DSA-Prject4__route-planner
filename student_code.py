from math import sqrt



class Q:

    def __init__(self, element=None, score=None):
        self.element = element
        self.score = score


class MinQ:

    def __init__(self):
        self.queue = []

    def en_q(self, element, score):
        new_element = Q(element, score)

        if len(self.queue) == 0:
            self.queue.append(new_element)

        else:
            added = False
            for num, item in enumerate(self.queue):
                if new_element.score < item.score:
                    self.queue.insert(num, new_element)
                    added = True
                    break
            if not added:
                self.queue.append(new_element)

    def dequeue(self):
        return self.queue.pop(0)


def distance(x1_y1, x2_y2):
    """

    Args:
        x1_y1: [x1, y1]
        x2_y2: [x2, y2]

    Returns:    distance from those set of points

    """
    return sqrt(((x2_y2[0] - x1_y1[0])**2) + ((x2_y2[-1] - x1_y1[-1])**2))


def shortest_path(given_map, begin, target):
    node_points = MinQ()
    node_points.en_q(begin, 0)

    visited_nodes = {}
    visited_nodes[begin] = None

    recent_cost = {}
    recent_cost[begin] = 0

    while not len(node_points.queue) == 0:
        pop_lower = node_points.dequeue()
        neighbor, lower_score = pop_lower.element, pop_lower.score

        if neighbor == target:
            short_path = []
            while neighbor != begin:
                short_path.append(neighbor)
                neighbor = visited_nodes[neighbor]
            short_path.append(begin)
            return short_path[::-1]

        for neighbor_road in given_map.roads[neighbor]:
            g = recent_cost[neighbor] + distance(given_map.intersections[neighbor], given_map.intersections[neighbor_road])
            if neighbor_road not in recent_cost or g < recent_cost[neighbor_road]:
                recent_cost[neighbor_road] = g
                f = g + distance(given_map.intersections[neighbor_road], given_map.intersections[target])
                node_points.en_q(neighbor_road, f)
                visited_nodes[neighbor_road] = neighbor
    return None

