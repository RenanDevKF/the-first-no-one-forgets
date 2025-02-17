using UnityEngine;

public class InventoryResizer : MonoBehaviour
{
    public RectTransform inventoryPanel;
    public int columns = 4; // Número de colunas desejado
    public int rows = 3; // Número de linhas desejada
    public float cellWidth = 100f; // Largura de cada célula
    public float cellHeight = 100f; // Altura de cada célula
    public float spacing = 10f; // Espaçamento entre os itens

    void Start()
    {
        ResizeInventoryPanel();
    }

    void ResizeInventoryPanel()
    {
        // Calcula o tamanho total necessário para o inventário
        float totalWidth = columns * cellWidth + (columns - 1) * spacing;
        float totalHeight = rows * cellHeight + (rows - 1) * spacing;

        // Ajusta o tamanho do painel
        inventoryPanel.sizeDelta = new Vector2(totalWidth, totalHeight);
    }
}
