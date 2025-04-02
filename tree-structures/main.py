from tests import run_all_tests
from utils import load_seq_from_file, measure_execution_time
from data_generator import generate_sequences
import trees as t
from tree_operations import bin_tree_height, get_node_bst, get_node_hmin, max_key_bst, lvl_order_iteration, max_key_hmin, min_key_bst, min_key_hmin, pre_order, remove_post_order, reverse_in_order

def menu():
    while True:
        print("\nMenu:")
        print("1. Find min/max key in the tree with search path")
        print("2. Find level with given key and print all keys on that level")
        print("3. Print all tree keys in descending order")
        print("4. Print subtree in pre-order for given root, its height. Delete it (post-order)")
        print("5. Run tests")
        print("6. Exit")

        option = input("Choose option: ")

        if option == "6":
            break
        elif option == "5":
            run_all_tests()

        elif option in ["1", "2", "3", "4"]:
            # operations common for all options 1-4
            input_type = input("Choose data source (1: file, 2: generator): ")
            sequence: list[int] = []

            if input_type == "1":
                filepath = "tree-structures/file.txt"
                sequence = load_seq_from_file(filepath)
            else:
                k = int(input("Enter the upper bound of sequence length. (n: <10,k>): "))
                sequence = generate_sequences(k)["random"][0]
            
            bst_root = t.create_bst(sequence)
            avl_root = t.create_avl(sequence)
            heap_root = t.create_heap(sequence)
            
            # manage options 1-4 for each tree type
            for tree_type, root in [("BST", bst_root.root), ("AVL", avl_root.root), ("MIN HEAP", heap_root.root)]:
                print("-" * 20)
                print(f"Results for {tree_type}:")
                if option == "1":
                    time1, (min, path1) = measure_execution_time(min_key_bst if tree_type == "BST" or tree_type == "AVL" else min_key_hmin, root)
                    time2, (max, path2) = measure_execution_time(max_key_bst if tree_type == "BST" or tree_type == "AVL" else max_key_hmin, root)
                    
                    print(f"Minimum key: {min}\nSearch path: {path1}\nExecution time: {time1} ms")
                    print(f"Maximum key: {max}\nSearch path: {path2}\nExecution time: {time2} ms")
                
                elif option == "2":
                    key = int(input("Enter key to search: "))
                    time, (level, keys_on_level) = measure_execution_time(lvl_order_iteration, root, key)
                    if level != -1:
                        print(f"Level: {level}")
                        print(f"Keys on level {level}: {keys_on_level}")
                        print(f"Execution time: {time} ms")
                    else:
                        print("Key not found")
                
                elif option == "3":
                    print("Elements in descending order:")
                    time, _ = measure_execution_time(reverse_in_order, root)
                    print(f"Execution time: {time} ms")
                
                elif option == "4":
                    key = int(input("Enter subtree root key: "))
                    subtree_root = get_node_bst(root, key) if tree_type == "BST" or tree_type == "AVL" else get_node_hmin(root, key)
                    if subtree_root:
                        print("Pre-order traversal:")
                        time, _ = measure_execution_time(pre_order, subtree_root)
                        print(f"Execution time: {time} ms")

                        height = bin_tree_height(subtree_root)
                        print(f"Subtree height: {height}")
                        
                        time, _ = measure_execution_time(remove_post_order, subtree_root)
                        print(f"Removal time: {time} ms")
                    else:
                        print("Key not found")

        else:
            print("Niewłaściwy wybór. Spróbuj ponownie")


if __name__ == "__main__":
    menu()