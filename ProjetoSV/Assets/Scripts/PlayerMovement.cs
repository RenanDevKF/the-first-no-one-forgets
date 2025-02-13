using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    public float speed = 5f; // Velocidade do personagem
    private Vector2 movement;
    private Rigidbody2D rb;
    private Animator animator;

    private Vector2 lastDirection = Vector2.down; // Direção inicial (olhando para baixo)

    private void Awake()
    {
        // Obtém o Rigidbody2D do Player
        rb = GetComponent<Rigidbody2D>();
        rb.gravityScale = 0; // Remove a gravidade
        rb.freezeRotation = true; // Evita rotações indesejadas

        // Obtém o Animator do Player
        animator = GetComponent<Animator>();
    }

    private void Update()
    {
        // Captura a entrada do teclado (horizontal e vertical)
        movement.x = Input.GetAxisRaw("Horizontal");
        movement.y = Input.GetAxisRaw("Vertical");

        // Normaliza o movimento para evitar que diagonais sejam mais rápidas
        movement = movement.normalized;

        // Se há movimento, definir a última direção válida
        if (movement.sqrMagnitude > 0)
        {
            // Prioriza horizontal se não estiver pressionando vertical
            if (movement.x != 0 && movement.y == 0)
            {
                lastDirection = new Vector2(movement.x, 0);
            }
            // Prioriza vertical se não estiver pressionando horizontal
            else if (movement.y != 0 && movement.x == 0)
            {
                lastDirection = new Vector2(0, movement.y);
            }
            // Se estiver pressionando ambos (diagonal), mantém a última direção válida (evita rotação)
        }

        // Atualiza os parâmetros do Animator com a última direção registrada
        animator.SetFloat("MoveX", lastDirection.x);
        animator.SetFloat("MoveY", lastDirection.y);
        animator.SetBool("IsMoving", movement.sqrMagnitude > 0);
    }

    private void FixedUpdate()
    {
        // Aplica a velocidade ao Rigidbody2D
        rb.linearVelocity = movement * speed;

        transform.position = new Vector3(
            Mathf.Round(transform.position.x * 16) / 16,
            Mathf.Round(transform.position.y * 16) / 16,
            transform.position.z
        );        
    }
}

