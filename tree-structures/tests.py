from data_generator import generate_sequences
from tree_operations import max_key_bst, max_key_hmin, tree_with_balance
from utils import measure_execution_time
import trees as t

def test_all_operations(sequence, sequence_type, iteration):
    bst_time, bst = measure_execution_time(t.create_bst, sequence)
    avl_time, avl = measure_execution_time(t.create_avl, sequence)
    heap_time, heap = measure_execution_time(t.create_heap, sequence)
    
    print(f"\n{sequence_type} sequence #{iteration} results:")
    print("\nTree Creation Times:")
    print(f"BST build time: {bst_time:.6f} ms")
    print(f"AVL build time: {avl_time:.6f} ms")
    print(f"Min Heap build time: {heap_time:.6f} ms")
    
    bst_max_time, _ = measure_execution_time(max_key_bst, bst.root)
    avl_max_time, _ = measure_execution_time(max_key_bst, avl.root)
    heap_max_time, _ = measure_execution_time(max_key_hmin, heap.root)
    
    print("\nMaximum Key Search Times:")
    print(f"BST max search time: {bst_max_time:.6f} ms")
    print(f"AVL max search time: {avl_max_time:.6f} ms")
    print(f"Min Heap max search time: {heap_max_time:.6f} ms")

    balance_time, _ = measure_execution_time(tree_with_balance, sequence)
    print(f"BST balancing time: {balance_time:.6f} ms")
    

def run_all_tests(k=20):
    print("="*50)
    print("Starting tests...")
    print("="*50)
    
    sequences = generate_sequences(k)
    
    print("\nTesting Random Sequences:")
    print("-"*30)
    for i, seq in enumerate(sequences["random"], 1):
        test_all_operations(seq, "Random", i)
        
    print("\nTesting Ascending Sequences:")
    print("-"*30)
    for i, seq in enumerate(sequences["ascending"], 1):
        test_all_operations(seq, "Ascending", i)


if __name__ == "__main__":
    run_all_tests()