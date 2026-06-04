const container = document.getElementById('bubble2-container');

function createBubble() {
    // Segurança: Se o container não existir na página, o código não roda (evita erros)
    if (!container) return; 

    const bubble = document.createElement('div');
    bubble.className = 'bubble2';

    // TAMANHO ALEATÓRIO (Entre 10px e 30px)
    const size = Math.floor(Math.random() * 20) + 10;
    bubble.style.width = size + 'px';
    bubble.style.height = size + 'px';

    // POSIÇÃO HORIZONTAL ALEATÓRIA (De 0% a 100% da largura da tela)
    bubble.style.left = Math.random() * 100 + 'vw';

    // DURAÇÃO ALEATÓRIA DA QUEDA (Entre 4 e 8 segundos)
    const duration = Math.random() * 4 + 4;
    bubble.style.animationDuration = duration + 's';

    // ADICIONA A BOLHA DENTRO DO CONTAINER
    container.appendChild(bubble); /* CORRIGIDO: Antes estava 'bubble' sem estar declarado */

    // REMOVE A BOLHA APÓS A ANIMAÇÃO TERMINAR (Evita que o PC do usuário trave com milhares de bolhas invisíveis)
    setTimeout(() => {
        bubble.remove();
    }, duration * 1000);
}

// Cria uma bolha a cada 300 milissegundos
setInterval(createBubble, 300);