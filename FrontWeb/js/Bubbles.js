const container = document.getElementById('bubble-container');

        function createBubble() {

            const bubble = document.createElement('div');

            bubble.className = 'bubble';

            // TAMANHO ALEATÓRIO
            const size = Math.floor(Math.random() * 20) + 10;

            bubble.style.width = size + 'px';
            bubble.style.height = size + 'px';

            // POSIÇÃO HORIZONTAL ALEATÓRIA
            bubble.style.left = Math.random() * 100 + 'vw';

            // DURAÇÃO ALEATÓRIA
            const duration = Math.random() * 4 + 4;

            bubble.style.animationDuration = duration + 's';

            // ADICIONA AO HTML
            container.appendChild(bubble);

            // REMOVE APÓS ANIMAÇÃO
            setTimeout(() => {

                bubble.remove();

            }, duration * 1000);

        }

setInterval(createBubble, 300);
const formulario = document.getElementById('loginform');
const telaLogin = document.getElementById('tela-login');
const telaRestrita = document.getElementById('tela-restrita');

