class BinaryTree:
    
    
    def __init__(self):
        """Konstructor"""
        self.root = None
        self.size = 0
        
    def remove(self, key):
        if self.root is None:
            pass
        else:
            self._remove(key, self.root)
            self.size -= 1 
            


    def _remove(self, key, c_node):
        
        if self.root.key == key: 
            if self.root.left_child is None and self.root.right_child is None:
                self.root = None
            elif self.root.left_child and self.root.right_child is None:
                self.root = self.root.left_child
            elif self.root.left_child is None and self.root.right_child:
                self.root = self.root.right_child
            elif self.root.left_child and self.root.right_child:
                delete_node_parents = self.root
                delete_node = self.root.left_child
                
                while delete_node.right_child:
                    delete_node_parents = delete_node
                    delete_node = delete_node.right_child
                
                self.root.key = delete_node.key
                self.root.value = delete_node.value
                if delete_node.left_child: 
                    if delete_node_parents.key < delete_node.key:
                        delete_node_parents.right_child = delete_node.left_child
                    elif den_node_parents.key > delete_node.key:
                        den_node_parents.right_child = delete_node.right_child
                        
                else:
                    if delete_node.key > delete_node_parents.key:
                        delete_node_parents.right_child = None
                    else:
                        delete_node_parents.left_child = None
        
        
        elif c_node.key < key:
            
            if c_node.right_child.key == key:
                
                if c_node.right_child.right_child is None and c_node.right_child.left_child is None:
                    c_node.right_child = None
                
                elif c_node.right_child.left_child and c_node.right_child.right_child is None:
                    c_node.right_child = c_node.right_child.left_child
                
                elif c_node.right_child.left_child is None and c_node.right_child.right_child:
                    c_node.right_child = c_node.right_child.right_child
                
                else:
                    delete_node_parents = c_node.right_child
                    delete_node = c_node.right_child.left_child
                    
                    while delete_node.right_child:
                        delete_node_parents = delete_node
                        delete_node = delete_node.right_child
                    
                    self._remove(delete_node.key, delete_node_parents)
                    c_node.right_child.key = delete_node.key
                    c_node.right_child.value = delete_node.value
        
            else:
                return self._remove(key, c_node.right_child)
            
        else:
            if c_node.left_child.key == key:
                if c_node.left_child.right_child is None and c_node.left_child.left_child is None:
                    c_node.left_child = None
                elif c_node.left_child.left_child and c_node.left_child.right_child is None:
                    c_node.left_child = c_node.left_child.left_child
                elif c_node.left_child.left_child is None and c_node.left_child.right_child:
                    c_node.left_child = c_node.left_child.right_child
                else:
                    delete_node_parents = c_node.left_child
                    delete_node = c_node.left_child.left_child
                    
                    while delete_node.right_child:
                        delete_node_parents = del_node
                        delete_node = del_node.right_child
                    
                    self._remove(delete_node.key, delete_node_parents)
                    c_node.right_child.key = delete_node.key
                    c_node.right_child.value = delete_node.value
            else: 
                return self._remove(key, c_node.left_child)