import unittest
from app import Item, LinkedList

class TestLinkedList(unittest.TestCase):
    
    def test_append_item(self):
        ll = LinkedList()
        item = Item("Item1", 10.0)
        ll.append(item)
        self.assertEqual(ll.head.itemName, "Item1")
        self.assertEqual(ll.head.price, 10.0)

    def test_append_multiple_items(self):
        ll = LinkedList()
        item1 = Item("Item1", 10.0)
        item2 = Item("Item2", 15.0)
        ll.append(item1)
        ll.append(item2)
        self.assertEqual(ll.head.next.itemName, "Item2")
        self.assertEqual(ll.head.next.price, 15.0)

    def test_display(self):
        ll = LinkedList()
        item1 = Item("Item1", 10.0)
        item2 = Item("Item2", 15.0)
        ll.append(item1)
        ll.append(item2)
        self.assertEqual(ll.display(), "Item1: 10.0 -> Item2: 15.0")

    def test_append_non_item(self):
        ll = LinkedList()
        with self.assertRaises(ValueError):
            ll.append("Not an Item")

if __name__ == "__main__":
    unittest.main()
