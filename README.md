# Bot de Pesca e Ataque Automático - Pokémon  

Este projeto é um bot automatizado desenvolvido com Python para auxiliar nas tarefas de pesca e ataque em um jogo de Pokémon. Ele utiliza as bibliotecas **pyautogui** e módulos personalizados para realizar ações automaticamente, como detectar bolhas, jogar o minigame de pesca e executar sequências de ataques.  

## 🎯 Funcionalidades  
- **Pesca Automática:**  
  - Posiciona a vara de pescar em locais pré-definidos.  
  - Detecta bolhas de pesca na tela e ativa automaticamente a pesca.  
  - Joga o minigame de pesca identificando a posição do peixe e controlando a barra.  

- **Ataques Automáticos:**  
  - Executa uma sequência predefinida de ataques utilizando teclas configuradas.  

## ⚙️ Requisitos  
- Python 3.x  
- Bibliotecas Python:  
  - `pyautogui`  
  - `keyboard`  
- Arquivos de imagem:  
  - `bubble.png`  
  - `fish.jpg`  
  - `barra.jpg`  

## 🛠️ Como Configurar  
1. Certifique-se de ter o **Python 3.x** instalado.  
2. Instale as dependências necessárias:  
   ```bash
   pip install pyautogui keyboard

   Certifique-se de que os arquivos de imagem (bubble.png, fish.jpg, barra.jpg) estejam na mesma pasta do script.
📂 Estrutura do Código

├── main.py             # Script principal do bot  
├── myKeyboard.py       # Módulo para simulação de teclas (personalizado)  
├── reapet_atack.py     # Módulo para repetir sequências de ataque  
├── bubble.png          # Imagem da bolha de pesca  
├── fish.jpg            # Imagem do peixe no minigame  
├── barra.jpg           # Imagem da barra do minigame  
└── README.md           # Documentação do projeto  
🖥️ Como Usar
Execute o script principal:
bash
python main.py

Pressione a tecla H para iniciar o bot.
O bot começará a realizar as ações automaticamente:
Escolherá um local de pesca.
Detectará as bolhas para iniciar a pesca.
Jogará o minigame de pesca automaticamente.
Executará ataques ao final de cada ciclo de pesca.
📋 Observações
Certifique-se de que o jogo esteja rodando em modo janela para que o bot possa identificar as imagens corretamente.
Ajuste as regiões e coordenadas no código se necessário, dependendo da resolução do seu monitor.
🛠️ Melhorias Futuras
Implementar suporte para resolução dinâmica.
Adicionar logs para monitorar o desempenho do bot.
Personalizar os ataques com base em condições do jogo.
📜 Licença
Este projeto foi desenvolvido para fins educacionais e está sob os direitos autorais de Andre Amorim Liberatto.


