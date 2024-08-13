class Item:
    def __init__(self, itemName, price):
        self.itemName = itemName
        self.price = price
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, item):
        if not isinstance(item, Item):
            raise ValueError("Only objects of Item class can be added to the list.")
        
        if self.head is None:
            self.head = item
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = item

    def display(self):
        items = []
        current = self.head
        while current:
            items.append(f"{current.itemName}: {current.price}")
            current = current.next
        return " -> ".join(items)

# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(Item("Item1", 10.0))
    ll.append(Item("Item2", 15.0))
    ll.append(Item("Item3", 20.0))
    print(ll.display())
