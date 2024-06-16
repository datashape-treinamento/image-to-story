
# ImageToStory

ImageToStory é um projeto Python que transforma imagens em histórias curtas e as converte em áudio. Utilizando modelos de inteligência artificial da Hugging Face, OpenAI e gTTS, este projeto demonstra como integrar várias tecnologias de IA para criar conteúdo narrativo a partir de imagens.

## Funcionalidades
- Extrai texto descritivo de imagens.
- Gera histórias curtas e intrigantes a partir do texto extraído.
- Converte a história gerada em áudio.

## Tecnologias Utilizadas
- Python
- Hugging Face Transformers
- OpenAI API
- gTTS (Google Text-to-Speech)
- dotenv (para gerenciamento de variáveis de ambiente)
- PyTorch (para modelagem de visão computacional)

## Requisitos
- Python instalado na máquina.
- PyTorch configurado e instalado de acordo com o seu sistema.

## Como Usar
1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/ImageToStory.git
    ```
2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3. Instale o PyTorch conforme as instruções do [site oficial](https://pytorch.org/get-started/locally/). Por exemplo, para um sistema Mac sem CUDA, use:
    ```bash
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
    ```
4. Configure sua chave de API da OpenAI em um arquivo `.env`:
    ```text
    OPENAI_API_KEY=your_openai_api_key
    ```
5. Execute o script principal:
    ```bash
    python main.py
    ```

## Recursos Adicionais
- Veja o vídeo tutorial no YouTube: [Transforme Imagens em Histórias com IA](https://youtu.be/vrrvRj87k7g)
- Leia o artigo completo no nosso site: [Transforme Imagens em Histórias com IA](https://amauryeuzebio.com.br/transforme-imagens-em-historias-com-ia/)

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença
Este projeto está licenciado sob a Licença MIT.
