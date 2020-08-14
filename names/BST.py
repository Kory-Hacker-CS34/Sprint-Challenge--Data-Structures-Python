class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # pass
        #if the value being passed is less than the current value, then we need to go left
        if value < self.value:
            if not self.left: #if there is no left value, then wrap our value in the node class
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value: #we could do just and else, but we want our duplicate nodes to go right so we have to make and elif
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            # elif self.left.value == target:
            #     return True
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            # elif self.right.value == target:
            #     return True
            else:
                return self.right.contains(target)
    # def contains(self, target):
    #     # pass

    #     #check to see if target is current value
    #     # if target == self.value:
    #     #     return True
    #     #start checking branches
    #     if target < self.value:
    #         if self.left is None:
    #             #if not, then the target isn't in the tree
    #             return False
    #         elif self.left.value == target:
    #             #otherwise, we've found our target
    #             return True
    #     #checking the right branch
    #     elif target > self.value:
    #         #any more right branches?
    #         if self.right is None:
    #             return False
    #         elif self.right.value == target:
    #             return True

    # Return the maximum value found in the tree
    def get_max(self):
        # pass

        #due to the rules of BST, we really only can check the right branch
        #so, if there is no more right branches, then we've found our max value
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # pass
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # pass

        if self.left:
            self.left.in_order_print(self.left)

        print(self.value)
        if self.right:
            self.right.in_order_print(self.left)

        # print(self.value)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # pass
        #TK said to utilize a queue, so i'm going to add that in.
        from collections import deque
        queue = deque()
        queue.append(self)

        while len(queue) > 0:
            #at the start of each loop, remove the item at the front of the queue
            current = queue.popleft()

            #if there is a left or right value, add it to the queue
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # pass

        stack = []
        stack.append(node)

        while len(stack) > 0:
            current = stack.pop()
            #going through the tree, and adding each node to the stack-list, starting from the given node
            #checking the left branch
            if current.right:
                stack.append(current.right)
            #checking the right branch
            if current.left:
                stack.append(current.left)
            #print the current value, then loop again
            print(current.value)