# CSV Search Script

Este script Python procura por GTINs específicos em arquivos CSV dentro de uma pasta e grava os resultados em um arquivo CSV de saída.

## Pré-requisitos

- Python 3.x instalado
- Biblioteca `csv` (já incluída na instalação padrão do Python)

## Instalação do Python

1. Baixe e instale o Python a partir do [site oficial](https://www.python.org/).
2. Durante a instalação, certifique-se de marcar a opção "Add Python to PATH".

## Verificar Instalação do Python

Abra o terminal integrado no Visual Studio Code e execute o comando abaixo para verificar a versão do Python instalada:

```bash
python --version

# Se o comando acima não funcionar tente:

py --version

```

## Configurar o Python no Visual Studio Code

- No Visual Studio Code, pressione Ctrl+Shift+P para abrir a paleta de comandos.
- Digite Python: Select Interpreter e selecione a versão do Python instalada.

# Executar o Script

- Abra o terminal integrado no Visual Studio Code.
- Navegue até o diretório onde o script csvSearch.py está localizado. Use o comando cd para isso. Por exemplo:
```bash
cd C:\\seu\\diretorio\\com\\o\\arquivo\\csvSearch.py
```
-Execute o script usando o comando python seguido do nome do arquivo. Por exemplo:
```bash
python csvSearch.py
```

## Configuração do Script
- O script está configurado para procurar os seguintes GTINs:
```bash
gtins = [
    '123', '1234', '12345'
]
```


## Contribuição
- Sinta-se à vontade para contribuir com melhorias para este script. Envie um pull request ou abra uma issue para discutir as mudanças que gostaria de fazer.