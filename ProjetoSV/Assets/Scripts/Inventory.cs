using System.Collections.Generic;
using UnityEngine;

// Classe que representa um item
[System.Serializable]
public class Item
{
    public int itemID;
    public string itemName;
    public bool isStackable;
    public int stackSize = 1;
    public Sprite icon;

}

public class Inventory : MonoBehaviour
{
    public List<Item> items = new List<Item>(); // Lista de itens no inventário
    public int maxSlots = 10; // Limite de itens no inventário

    // Adiciona um item ao inventário
    public bool AddItem(Item newItem)
    {
        if (items.Count >= maxSlots)
        {
            Debug.Log("Inventário cheio!");
            return false;
        }

        // Verifica se o item é empilhável e já existe no inventário
        if (newItem.isStackable)
        {
            Item existingItem = items.Find(i => i.itemID == newItem.itemID);
            if (existingItem != null)
            {
                existingItem.stackSize++;
                Debug.Log($"Item {newItem.itemName} empilhado. Quantidade: {existingItem.stackSize}");
                return true;
            }
        }

        // Se não for empilhável ou não existir, adiciona como novo item
        items.Add(newItem);
        Debug.Log($"Item {newItem.itemName} adicionado ao inventário.");
        return true;
    }

    // Remove um item do inventário
    public void RemoveItem(Item itemToRemove)
    {
        Item existingItem = items.Find(i => i.itemID == itemToRemove.itemID);
        if (existingItem != null)
        {
            if (existingItem.isStackable && existingItem.stackSize > 1)
            {
                existingItem.stackSize--;
                Debug.Log($"Item {existingItem.itemName} reduzido. Restam {existingItem.stackSize}");
            }
            else
            {
                items.Remove(existingItem);
                Debug.Log($"Item {existingItem.itemName} removido do inventário.");
            }
        }
        else
        {
            Debug.Log("O item não está no inventário.");
        }
    }

    // Verifica se o inventário contém um item
    public bool HasItem(Item item)
    {
        return items.Exists(i => i.itemID == item.itemID);
    }

    // Exibe os itens no console (para debug)
    public void ShowInventory()
    {
        Debug.Log("Inventário Atual:");
        foreach (Item item in items)
        {
            Debug.Log($"- {item.itemName} (x{item.stackSize})");
        }
    }
}
