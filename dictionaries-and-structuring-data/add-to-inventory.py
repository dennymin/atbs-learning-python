def displayInventory(inventory):
  print("Inventory:")
  item_total = 0
  for k, v in inventory.items():
      # FILL THIS PART IN
      item_total += v
      print(str(v) + ' ' + k)
  print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
  # your code goes here
  for i in range(len(addedItems)):
    if addedItems[i] in inventory.keys():
      inventory[addedItems[i]] += 1
    else:
      inventory.update({addedItems[i]:1})
  return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
