using UnityEngine;
using UnityEngine.UI;

public class InventoryUI : MonoBehaviour
{
    public Transform inventoryPanel;
    public GameObject itemSlotPrefab;
    private Inventory inventory;

    void Start()
    {
        inventory = new Inventory(); // Inicializa o inventário
        UpdateInventoryUI();
    }

    public void UpdateInventoryUI()
    {
        // Limpa a UI de inventário
        foreach (Transform child in inventoryPanel)
        {
            Destroy(child.gameObject);
        }

        // Cria um slot para cada item no inventário
        foreach (Item item in inventory.items)
        {
            GameObject slot = Instantiate(itemSlotPrefab, inventoryPanel);
            slot.transform.GetChild(0).GetComponent<Image>().sprite = item.icon;
            slot.transform.GetChild(1).GetComponent<Text>().text = item.stackSize > 1 ? item.stackSize.ToString() : "";
        }
    }
}
