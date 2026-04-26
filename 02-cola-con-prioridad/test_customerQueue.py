import pytest
from CustomerQueue import CustomerQueue

# 1. Caso Base: El ejemplo del ejercicio
def test_basic_flow():
    cq = CustomerQueue()
    cq.enqueue("Alice", 3)
    cq.enqueue("Bob", 2)
    cq.enqueue("Charlie", 1)
    cq.enqueue("Dave", 2)
    
    assert cq.dequeue() == "Charlie"
    assert cq.dequeue() == "Bob"
    assert cq.dequeue() == "Dave"
    assert cq.dequeue() == "Alice"

# 2. Cola Vacía: Debe retornar None
def test_empty_queue():
    cq = CustomerQueue()
    assert cq.dequeue() is None

# 3. Solo VIPs: Debe respetar el orden de llegada (FIFO)
def test_only_vips():
    cq = CustomerQueue()
    cq.enqueue("V1", 1)
    cq.enqueue("V2", 1)
    cq.enqueue("V3", 1)
    assert cq.dequeue() == "V1"
    assert cq.dequeue() == "V2"
    assert cq.dequeue() == "V3"

# 4. Prioridad Saltada: Si no hay 1, pasa a la 2
def test_skip_priority_level():
    cq = CustomerQueue()
    cq.enqueue("Regular", 3)
    cq.enqueue("Preferencial", 2)
    # No hay nivel 1
    assert cq.dequeue() == "Preferencial"
    assert cq.dequeue() == "Regular"

# 5. Intercalado: Meter, sacar y volver a meter
def test_interleaved_operations():
    cq = CustomerQueue()
    cq.enqueue("Beto", 2)
    assert cq.dequeue() == "Beto"
    cq.enqueue("Ana", 1)
    assert cq.dequeue() == "Ana"

# 6. Mismos nombres, diferente prioridad
def test_same_names_different_priority():
    cq = CustomerQueue()
    cq.enqueue("Luis", 3)
    cq.enqueue("Luis", 1)
    # El Luis VIP sale primero
    assert cq.dequeue() == "Luis"
    assert cq.dequeue() == "Luis"

# 7. Vaciar y volver a intentar: Debe dar None
def test_dequeue_until_none():
    cq = CustomerQueue()
    cq.enqueue("Solo", 1)
    cq.dequeue()
    assert cq.dequeue() is None

# 8. Carga mayor: Muchos en una sola prioridad
def test_large_single_priority():
    cq = CustomerQueue()
    names = [f"User{i}" for i in range(100)]
    for name in names:
        cq.enqueue(name, 3)
    
    for name in names:
        assert cq.dequeue() == name

# 9. Invasión VIP: Alguien llega al final pero tiene prioridad 1
def test_late_vip_arrival():
    cq = CustomerQueue()
    cq.enqueue("Tarde1", 3)
    cq.enqueue("Tarde2", 3)
    cq.enqueue("VIP", 1) # Llegó último
    assert cq.dequeue() == "VIP" # Pero sale primero

# 10. Prioridad inexistente (Si aplicaste mi consejo de validación)
def test_invalid_priority():
    cq = CustomerQueue()
    # Si intentamos meter prioridad 4 (no definida en el dict)
    # Tu código actual no fallará pero no debería guardarlo si validaste
    cq.enqueue("Fantasma", 4)
    assert cq.dequeue() is None