from linkised_list import Linked_List


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [Linked_List() for _ in range(size)]

    def put(self, key, value):
        index = hash(key) % len(self.buckets)
        bucket = self.buckets[index]
        current = bucket.head
        while current:
            if current.value[0] == key:
                current.value = (key, value)
                return
            current = current.next
        bucket.append((key, value))

    def get(self, key):
        index = hash(key) % len(self.buckets)
        bucket = self.buckets[index]
        current = bucket.head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next
        return None

    def delete(self, key):
        index = hash(key) % len(self.buckets)
        bucket = self.buckets[index]
        
        current = bucket.head
        prev = None
        while current:
            if current.value[0] == key:
                if prev is None:
                    bucket.head = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False  



ht = HashTable()
ht.put("fruit", "apple")
ht.put("vegitable", "tomato")
print(ht.get("fruit",))
print(ht.get("vegitable"))
ht.delete("fruit")
print(ht.get("fruit"))  
