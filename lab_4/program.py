class SemanticNetwork:
    def __init__(self):
        self.nodes = set()  # Множина всіх вузлів
        self.relationships = []  # Список відносин (зв'язків)

    def add_node(self, node):
        self.nodes.add(node)

    def add_relationship(self, subject, predicate, object_):
        relationship = (subject, predicate, object_)
        self.relationships.append(relationship)

    def get_related_nodes(self, node, predicate):
        related_nodes = set()
        for relationship in self.relationships:
            subject, pred, object_ = relationship
            if subject == node and pred == predicate:
                related_nodes.add(object_)
        return related_nodes

    def query(self, subject, predicate, object_):
        # Запит до семантичної мережі
        if subject and predicate and object_:
            return (subject, predicate, object_) in self.relationships
        elif subject and predicate:
            return self.get_related_nodes(subject, predicate)
        elif predicate and object_:
            related_nodes = set()
            for node in self.nodes:
                if (node, predicate, object_) in self.relationships:
                    related_nodes.add(node)
            return related_nodes
        else:
            return None


# Створення семантичної мережі
network = SemanticNetwork()

# Додавання вузлів (Магазини, Постачальники, Товари)
network.add_node("Магазин1")
network.add_node("Магазин2")
network.add_node("Магазин3")
network.add_node("Постачальник1")
network.add_node("Постачальник2")
network.add_node("Постачальник3")
network.add_node("Товар1")
network.add_node("Товар2")
network.add_node("Товар3")

# Додавання відносин
network.add_relationship("Магазин1", "замовляє", "Товар1")
network.add_relationship("Магазин2", "замовляє", "Товар2")
network.add_relationship("Магазин2", "замовляє", "Товар2")
network.add_relationship("Магазин3", "замовляє", "Товар3")
network.add_relationship("Магазин3", "замовляє", "Товар3")
network.add_relationship("Магазин1", "замовляє", "Товар2")  # Приклад конфлікту
network.add_relationship("Постачальник2", "постачає", "Магазин2")

# Запити до бази знань
print("Магазини, які замовляють Товар2:")
print(network.query(None, "замовляє", "Товар2"))

print("Магазин2 замовляє Товар2:")
print(network.query("Магазин2", "замовляє", "Товар2"))

print("Постачальники, які постачають товари в Магазин2:")
print(network.query(None, "постачає", "Магазин2"))

print("Всі товари, які замовляють в усіх магазинах:")
print(network.query(None, "замовляє", None))
