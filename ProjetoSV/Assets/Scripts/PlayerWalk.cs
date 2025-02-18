using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerWalk : MonoBehaviour
{
    public Animator anim;
    public float speed;

    private Vector3 lastDirection = Vector3.down; // Última direção de movimento

    void Update()
    {
        // Captura a entrada do teclado (movimento horizontal e vertical)
        Vector3 movement = new Vector3(Input.GetAxisRaw("Horizontal"), Input.GetAxisRaw("Vertical"), 0f);

        // Normaliza o movimento para evitar que a diagonal ande mais rápido
        movement = movement.normalized;

        // Atualiza a última direção se houver movimento
        if (movement.magnitude > 0)
        {
            lastDirection = movement;
        }

        // Atualiza o Animator com a direção de movimento (se houver movimento) ou mantém a última direção
        anim.SetFloat("Horizontal", movement.magnitude > 0 ? movement.x : lastDirection.x);
        anim.SetFloat("Vertical", movement.magnitude > 0 ? movement.y : lastDirection.y);
        anim.SetFloat("Speed", movement.magnitude);

        // Move o personagem com base no input
        transform.position += movement * speed * Time.deltaTime;
    }
}
