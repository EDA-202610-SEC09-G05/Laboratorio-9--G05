from DataStructures.Priority_queue import pq_entry as pqe
from DataStructures.List import array_list as al

def default_compare_higher_value(father_node, child_node):
    """
    Función de comparación por defecto para heap orientado a mayor
    """
    if pqe.get_priority(father_node) >= pqe.get_priority(child_node):
        return True
    return False

def default_compare_lower_value(father_node, child_node):
    """
    Función de comparación por defecto para heap orientado a menor
    """
    if pqe.get_priority(father_node) <= pqe.get_priority(child_node):
        return True
    return False

def new_heap(is_min_pq=True):
    """
    Crea una cola de prioridad indexada orientada a menor o mayor
    """
    heap = {
        "elements": al.new_list(),
        "size": 0,
        "cmp_function": None
    }

    al.add_last(heap["elements"], None)

    if is_min_pq:
        heap["cmp_function"] = default_compare_lower_value
    else:
        heap["cmp_function"] = default_compare_higher_value

    return heap

def exchange(my_heap, i, j):
    """
    Intercambia dos elementos del heap
    """
    elements = my_heap["elements"]

    temp = al.get_element(elements, i)
    al.change_info(elements, i, al.get_element(elements, j))
    al.change_info(elements, j, temp)
    
    
def priority(my_heap, parent, child):
    """
    Indica si parent tiene mayor prioridad que child
    """
    return my_heap["cmp_function"](parent, child)

def size(my_heap):
    """
    Retorna el número de elementos del heap
    """
    return my_heap["size"]

def is_empty(my_heap):
    """
    Retorna True si el heap está vacío
    """
    return size(my_heap) == 0

def swim(my_heap, pos):
    """
    Reorganiza el heap hacia arriba
    """
    while pos > 1:
        parent = pos // 2

        current = al.get_element(my_heap["elements"], pos)
        parent_node = al.get_element(my_heap["elements"], parent)

        if priority(my_heap, parent_node, current):
            break

        exchange(my_heap, parent, pos)
        pos = parent
        
def insert(my_heap, priority_value, value):
    """
    Inserta un nuevo elemento en el heap
    """
    entry = pqe.new_pq_entry(priority_value, value)

    al.add_last(my_heap["elements"], entry)
    my_heap["size"] += 1

    swim(my_heap, my_heap["size"])

    return my_heap

